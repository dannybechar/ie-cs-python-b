"""Build one self-contained HTML slide deck beside every lesson page.

    pip install -r requirements.txt
    python -I build_decks.py            # rebuilds units/*/lessons/L*.html from the matching L*.md
    python -I build_decks.py --check    # exit 1 if any .html is missing or out of date

The Markdown lesson page (the student-facing Hebrew lab brief) is the source of truth; the HTML is generated.
Rules (docs/standards/README.md): one inline file, no external resources, light/dark, phone layout,
one slide per printed page, student-safe (sections headed Solution / Answer key / Teacher are dropped).
"""
import html
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[2]
TEACHER_HEADING = re.compile(r"(?i)(solutions?|answer key|answers? for the teacher|teacher)|פתרון|מפתח תשובות|למורה|הערת מורה")

CSS = """
:root{--bg:#f6f7fb;--card:#fff;--fg:#1d2433;--muted:#5a6478;--accent:#1f5fbf;--line:#d7dcea;--code:#eef1f8;--note:#e8f0ff;--tip:#e6f6ec;--warn:#fff3d6}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#10141c;--card:#171d29;--fg:#e8ecf5;--muted:#9aa5bd;--accent:#7fb0ff;--line:#2a3347;--code:#0e121a;--note:#16233d;--tip:#12301f;--warn:#3a2f10}}
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:var(--bg);color:var(--fg);font:18px/1.6 "Segoe UI",Arial,sans-serif}
.deck{display:flex;flex-direction:column;height:100%}
main{flex:1;min-height:0;display:flex;justify-content:center;padding:16px}
.slide{display:none;width:100%;max-width:980px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 24px;overflow:auto}
.slide.on{display:block}
h1{font-size:2em;margin:.2em 0}h2{font-size:1.45em;margin:.1em 0 .6em;color:var(--accent)}
table{border-collapse:collapse;width:100%;margin:.6em 0}th,td{border:1px solid var(--line);padding:6px 10px;text-align:start;unicode-bidi:plaintext}
th{background:var(--code)}
pre{direction:ltr;text-align:left;background:var(--code);border:1px solid var(--line);border-radius:8px;padding:10px 14px;overflow:auto;font-size:.92em}
code{display:inline-block;direction:ltr;unicode-bidi:isolate;background:var(--code);border-radius:4px;padding:0 4px;font-family:Consolas,"Courier New",monospace}
pre code{background:none;padding:0}
.alert{border-inline-start:5px solid var(--accent);background:var(--note);border-radius:8px;padding:6px 14px;margin:.8em 0}
.alert.tip{background:var(--tip)}.alert.warning,.alert.caution{background:var(--warn)}
.alert .t{font-weight:700;display:block;color:var(--muted);font-size:.8em;letter-spacing:.04em}
nav{display:flex;align-items:center;justify-content:center;gap:14px;padding:10px 16px;border-top:1px solid var(--line);background:var(--card)}
button{font:inherit;padding:8px 18px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--fg);cursor:pointer}
button:hover{border-color:var(--accent)}#pos{min-width:5em;text-align:center;color:var(--muted);direction:ltr;unicode-bidi:isolate}
@media (max-width:600px){body{font-size:16px}.slide{padding:14px}main{padding:8px}}
@media print{html,body{height:auto}body{background:#fff;color:#000;font-size:14pt}nav{display:none}.deck,main{display:block;padding:0}
.slide{display:block!important;max-width:none;border:0;border-radius:0;padding:0;overflow:visible;page-break-after:always;break-after:page}
.slide:last-child{page-break-after:auto}.alert,pre,th,code{background:#fff!important;border:1px solid #999}}
"""

JS = """
(function(){var s=[].slice.call(document.querySelectorAll('.slide')),i=0,pos=document.getElementById('pos');
function show(n){i=Math.max(0,Math.min(s.length-1,n));s.forEach(function(e,k){e.classList.toggle('on',k===i)});s[i].scrollTop=0;
pos.textContent=(i+1)+' / '+s.length;try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
document.getElementById('prev').onclick=function(){show(i-1)};document.getElementById('next').onclick=function(){show(i+1)};
document.addEventListener('keydown',function(e){var k=e.key;
if(k==='ArrowLeft'||k===' '||k==='PageDown'){e.preventDefault();show(i+1)}else if(k==='ArrowRight'||k==='PageUp'){e.preventDefault();show(i-1)}});
var h=parseInt((location.hash||'').slice(1),10);show(h>0?h-1:0)})();
"""


def split_sections(text):
    """Split at '## ' headings, ignoring lines inside code fences. Returns (intro, [(heading, body)])."""
    intro, sections, cur, fence = [], [], None, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            cur = [line[3:].strip(), []]
            sections.append(cur)
            continue
        (cur[1] if cur else intro).append(line)
    return "\n".join(intro), [(h, "\n".join(b)) for h, b in sections]


def alerts_to_html(md_text):
    """Turn each '> [!TYPE]' blockquote group into an explicit alert container (consecutive alerts stay separate)."""
    out, quote, fence = [], [], False

    def flush():
        if not quote:
            return
        groups, cur = [], None
        for ln in quote:
            body = ln[1:][1:] if ln[1:].startswith(" ") else ln[1:]
            m = re.match(r"\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", body, re.I)
            if m:
                cur = [m.group(1).upper(), []]
                groups.append(cur)
            elif cur is None:
                cur = ["", []]
                groups.append(cur)
                cur[1].append(body)
            else:
                cur[1].append(body)
        for kind, lines in groups:
            if kind:
                out.extend(['<div class="alert %s" markdown="1">' % kind.lower(), '<span class="t">%s</span>' % kind, ""] + lines + ["", "</div>", ""])
            else:
                out.extend(["> " + x for x in lines] + [""])
        quote.clear()

    for line in md_text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith(">"):
            quote.append(line)
            continue
        flush()
        out.append(line)
    flush()
    return "\n".join(out)


def render(md_text):
    md_text = alerts_to_html(md_text)
    md_text = re.sub(r'<div dir="rtl">', '<div dir="rtl" markdown="1">', md_text)
    out = markdown.markdown(md_text, extensions=["tables", "fenced_code", "md_in_html", "sane_lists"])
    out = out.replace(' markdown="1"', "")
    return out


def build(md_path):
    text = md_path.read_text(encoding="utf-8")
    intro, sections = split_sections(text)
    m = re.search(r"^# (.+)$", intro, re.M)
    title = m.group(1).strip() if m else md_path.stem
    slides = [render(intro)]
    for heading, body in sections:
        if TEACHER_HEADING.search(heading):
            continue
        slides.append(render("## %s\n\n%s" % (heading, body)))
    body = "\n".join('<section class="slide">\n%s\n</section>' % s for s in slides)
    return (
        '<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n<div class=\"deck\">\n<main>\n%s\n</main>\n"
        '<nav><button id="prev" type="button">הקודם</button><span id="pos"></span>'
        '<button id="next" type="button">הבא</button></nav>\n</div>\n<script>%s</script>\n</body>\n</html>\n'
        % (html.escape(title), CSS, body, JS)
    )


if __name__ == "__main__":
    check = "--check" in sys.argv
    bad = 0
    pages = sorted((ROOT / "units").glob("*/lessons/L*.md"))
    for md_path in pages:
        target = md_path.with_suffix(".html")
        new = build(md_path)
        if check:
            if not target.exists() or target.read_text(encoding="utf-8") != new:
                print("OUT OF DATE:", target.relative_to(ROOT).as_posix())
                bad += 1
        else:
            target.write_text(new, encoding="utf-8", newline="\n")
    print("%d lesson pages, %s" % (len(pages), "%d out of date" % bad if check else "decks written"))
    sys.exit(1 if bad else 0)
