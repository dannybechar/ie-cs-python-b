# Convert a simple Markdown file (headings, paragraphs, bullets, tables, code blocks) to .docx.
# Hebrew paragraphs and tables become right-to-left; code blocks stay left-to-right.
# Usage: python md_to_docx.py input.md output.docx [extra.py appended as a code block]
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

HEB = re.compile("[\u0590-\u05ff]")


def set_rtl(par):
    ppr = par._p.get_or_add_pPr()
    ppr.append(OxmlElement("w:bidi"))
    par.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def add_runs(par, text, rtl, font=None):
    for i, chunk in enumerate(re.split(r"(\*\*.+?\*\*|`[^`]+`)", text)):
        if not chunk:
            continue
        bold = chunk.startswith("**")
        code = chunk.startswith("`")
        chunk = chunk.strip("*") if bold else chunk.strip("`") if code else chunk
        run = par.add_run(chunk)
        run.bold = bold
        if code or font:
            run.font.name = font or "Consolas"
        if rtl:
            rpr = run._r.get_or_add_rPr()
            rpr.append(OxmlElement("w:rtl"))


def paragraph(doc, text, style=None):
    rtl = bool(HEB.search(text))
    par = doc.add_paragraph(style=style)
    add_runs(par, text, rtl)
    if rtl:
        set_rtl(par)
    return par


def code_block(doc, lines):
    for line in lines:
        par = doc.add_paragraph()
        par.paragraph_format.space_after = Pt(0)
        run = par.add_run(line if line else " ")
        run.font.name = "Consolas"
        run.font.size = Pt(10)
    doc.add_paragraph()


def table(doc, rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-+:?", c) for c in r)]
    tbl = doc.add_table(rows=len(cells), cols=len(cells[0]), style="Table Grid")
    rtl = any(HEB.search(c) for r in cells for c in r)
    if rtl:
        tbl._tbl.tblPr.append(OxmlElement("w:bidiVisual"))
    for i, r in enumerate(cells):
        for j, c in enumerate(r):
            cell = tbl.cell(i, j)
            cell.text = ""
            par = cell.paragraphs[0]
            add_runs(par, c.replace("&nbsp;", " ").replace("\\_", "_"), bool(HEB.search(c)))
            if i == 0:
                for run in par.runs:
                    run.bold = True
    doc.add_paragraph()


def convert(src, dst, extra=None):
    doc = Document()
    doc.styles["Normal"].font.name = "Arial"
    doc.styles["Normal"].font.size = Pt(11)
    lines = open(src, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            code_block(doc, lines[i + 1:j])
            i = j + 1
            continue
        if line.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            table(doc, lines[i:j])
            i = j
            continue
        m = re.match(r"(#+) (.*)", line)
        if m:
            h = doc.add_heading(level=min(len(m.group(1)), 3))
            add_runs(h, m.group(2), bool(HEB.search(m.group(2))))
            if HEB.search(m.group(2)):
                set_rtl(h)
        elif re.match(r"\s*- ", line):
            paragraph(doc, re.sub(r"^\s*- ", "", line), "List Bullet")
        elif re.match(r"\d+\. ", line):
            paragraph(doc, line)
        elif line.strip() in ("", "---") or line.startswith("<"):
            pass
        else:
            paragraph(doc, line)
        i += 1
    if extra:
        doc.add_heading("Model solutions (Python)", level=2)
        code_block(doc, open(extra, encoding="utf-8").read().splitlines())
    doc.save(dst)


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
