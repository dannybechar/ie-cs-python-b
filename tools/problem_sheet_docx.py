# Build a "problem + writing box" worksheet (.docx) from a small Markdown file.
# Usage: python tools/problem_sheet_docx.py in.md out.docx [rows_per_page=3 | "3,2"] [font_scale=1.0] [writing_box_cm=9.8]
# rows_per_page may be a list ("3,2" = three problems on the first side, two on the second); font_scale enlarges all text.
#
# Layout (A4 portrait): one table row per problem. The problem is in a box on the RIGHT (Hebrew, right-to-left,
# code and expected output in bold Courier New, left-to-right, grey boxes); next to it, on the LEFT, an empty box
# for handwriting the code. Before the first "## " heading: header lines (the first "# " line is the title).
# Each "## " heading starts a problem; its text, ```python and ```text blocks go in the problem box.
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

HEB = re.compile("[֐-׿]")
CODE_FONT = "Courier New"
TEXT_FONT = "Arial"


def set_font(run, name, size=None, bold=None):
    run.font.name = name
    rfonts = run._r.get_or_add_rPr().get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)
    if size:
        run.font.size = Pt(size)
        szcs = OxmlElement("w:szCs")
        szcs.set(qn("w:val"), str(int(size * 2)))
        run._r.get_or_add_rPr().append(szcs)
    if bold is not None:
        run.bold = bold
        if bold:
            run._r.get_or_add_rPr().append(OxmlElement("w:bCs"))  # bold for right-to-left (complex-script) text


def set_bidi(par):
    par._p.get_or_add_pPr().append(OxmlElement("w:bidi"))  # right-to-left; no explicit alignment (Word reads it as the other edge)


def shade(par_or_cell, fill, cell=False):
    el = par_or_cell._tc.get_or_add_tcPr() if cell else par_or_cell._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    el.append(shd)


def para_borders(par, color="808080"):
    ppr = par._p.get_or_add_pPr()
    pb = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single")
        b.set(qn("w:sz"), "6")
        b.set(qn("w:space"), "2")
        b.set(qn("w:color"), color)
        pb.append(b)
    ppr.append(pb)


def spacing(par, before=0, after=0):
    par.paragraph_format.space_before = Pt(before)
    par.paragraph_format.space_after = Pt(after)


def add_text(par, text, size=10.5, rtl=True):
    for chunk in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
        if not chunk:
            continue
        bold = chunk.startswith("**")
        code = chunk.startswith("`")
        chunk = chunk.strip("*") if bold else chunk.strip("`") if code else chunk
        run = par.add_run(chunk)
        if code:
            set_font(run, CODE_FONT, size, True)
        else:
            set_font(run, TEXT_FONT, size, bold)
            if rtl and HEB.search(chunk):
                run._r.get_or_add_rPr().append(OxmlElement("w:rtl"))


def hebrew_par(container, text, size=10.5, bold=False, before=0, after=3):
    par = container.add_paragraph()
    set_bidi(par)
    spacing(par, before, after)
    add_text(par, f"**{text}**" if bold else text, size)
    return par


def code_par(container, lines, size=10):
    """A grey boxed code block: one paragraph per line, left-aligned, left-to-right, bold Courier New."""
    pars = []
    for i, line in enumerate(lines):
        par = container.add_paragraph()
        spacing(par, 0, 0)
        par.paragraph_format.left_indent = Cm(0.15)
        shade(par, "F0F0F0")
        run = par.add_run(line if line else " ")
        set_font(run, CODE_FONT, size, True)
        pars.append(par)
    # a thin box around the whole block (top on first, bottom on last, sides on all)
    for i, par in enumerate(pars):
        ppr = par._p.get_or_add_pPr()
        pb = OxmlElement("w:pBdr")
        for side in ("left", "right") + (("top",) if i == 0 else ()) + (("bottom",) if i == len(pars) - 1 else ()):
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "6")
            b.set(qn("w:space"), "3")
            b.set(qn("w:color"), "808080")
            pb.append(b)
        ppr.append(pb)
    gap = container.add_paragraph()
    spacing(gap, 0, 0)
    gap.paragraph_format.line_spacing = Pt(4)


def set_cell_width(cell, cm):
    cell.width = Cm(cm)
    tcw = cell._tc.get_or_add_tcPr().get_or_add_tcW()
    tcw.set(qn("w:type"), "dxa")
    tcw.set(qn("w:w"), str(int(cm * 567)))


def row_height(row, cm):
    trpr = row._tr.get_or_add_trPr()
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(cm * 567)))
    h.set(qn("w:hRule"), "exact")
    trpr.append(h)
    cs = OxmlElement("w:cantSplit")
    trpr.append(cs)


def cell_margins(table, cm=0.2):
    tblpr = table._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for side in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{side}")
        e.set(qn("w:w"), str(int(cm * 567)))
        e.set(qn("w:type"), "dxa")
        m.append(e)
    tblpr.append(m)


def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    header, problems, cur, i = [], [], None, 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("## "):
            cur = {"title": l[3:].strip(), "items": []}
            problems.append(cur)
        elif l.startswith("```"):
            lang = l[3:].strip()
            block = []
            i += 1
            while not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            (cur["items"] if cur else header).append(("code", lang, block))
        elif l.strip():
            (cur["items"] if cur else header).append(("text", l.strip()))
        i += 1
    return header, problems


def build(src, dst, rows_per_page=3, scale=1.0, left_cm=9.8):
    header, problems = parse(src)
    pages = rows_per_page if isinstance(rows_per_page, list) else [rows_per_page] * (len(problems) // rows_per_page + 1)
    starts, acc = [], 0
    for cnt in pages:
        starts.append(acc)
        acc += cnt
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(1.2)
    sec.top_margin, sec.bottom_margin = Cm(1.0), Cm(1.0)
    st = doc.styles["Normal"]
    st.font.name = TEXT_FONT
    st.font.size = Pt(10.5)
    first = True
    for n, p in enumerate(problems):
        if n in starts:
            page_rows = pages[starts.index(n)]
            start = len(doc.paragraphs)
            for item in header:
                if item[0] == "text":
                    t = item[1]
                    if t.startswith("# "):
                        hebrew_par(doc, t[2:], 15 * min(scale, 1.2), True, 0, 1)
                    else:
                        hebrew_par(doc, t, 9.5 * scale, False, 0, 1)
                else:
                    code_par(doc, item[2], 9 * scale)
            if n > 0:  # a new side: start on a new page, header repeated
                doc.paragraphs[start].paragraph_format.page_break_before = True
        table = doc.add_table(rows=1, cols=2)
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell_margins(table)
        usable = 21 - 2.4
        left_w, right_w = left_cm, usable - left_cm
        row = table.rows[0]
        height = (29.7 - 2.0 - 2.6 * scale - 0.45 * page_rows) / page_rows
        row_height(row, height)
        left, right = row.cells
        # the table grid must carry the widths too (LibreOffice reads the grid, Word the cell widths)
        # columns of a right-to-left table are listed visually from the left: writing box first
        table.columns[0].width, table.columns[1].width = Cm(left_w), Cm(right_w)
        set_cell_width(left, left_w)
        set_cell_width(right, right_w)
        # left cell: empty writing box with a small label
        lab = left.paragraphs[0]
        set_bidi(lab)
        spacing(lab, 0, 0)
        r = lab.add_run("כתבו כאן את הקוד")
        set_font(r, TEXT_FONT, 8, False)
        r.font.color.rgb = __import__("docx").shared.RGBColor(0x99, 0x99, 0x99)
        r._r.get_or_add_rPr().append(OxmlElement("w:rtl"))
        # right cell: the problem
        title = right.paragraphs[0]
        set_bidi(title)
        spacing(title, 0, 3)
        add_text(title, f"**{p['title']}**", 11.5 * scale)
        for item in p["items"]:
            if item[0] == "text":
                hebrew_par(right, item[1], 10.5 * scale, False, 0, 3)
            elif item[1] == "text":
                hebrew_par(right, "דוגמת פלט:", 9 * scale, True, 2, 1)
                code_par(right, item[2], 9.5 * scale)
            else:
                code_par(right, item[2], 10 * scale)
        gap = doc.add_paragraph()
        spacing(gap, 0, 0)
        gap.paragraph_format.line_spacing = Pt(6)
    doc.save(dst)


if __name__ == "__main__":
    a = sys.argv[1:]
    rows = 3
    if len(a) > 2:
        rows = [int(x) for x in a[2].split(",")] if "," in a[2] else int(a[2])
    build(a[0], a[1], rows, float(a[3]) if len(a) > 3 else 1.0, float(a[4]) if len(a) > 4 else 9.8)
