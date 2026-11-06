import re, html, sys
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("source")
ap.add_argument("out")
ap.add_argument("--footer", default="יחידה 5.1 – מחרוזות")
ap.add_argument("--subtitle", default="")
ap.add_argument("--emoji", default="🤖")
ap.add_argument("--card", default="", help="a word shown in a card on the title slide")
ap.add_argument("--boxes", default="", help="slides that get the letter boxes, e.g. 7,8")
ap.add_argument("--boxes-word", default="ROBOT")
ap.add_argument("--numbered", default="", help="slides whose bullets are a numbered list, e.g. 19")
args = ap.parse_args()
BOX_SLIDES = [int(x) for x in args.boxes.split(",") if x]
NUM_SLIDES = [int(x) for x in args.numbered.split(",") if x]
src = open(args.source, encoding="utf-8").read().split("\n")
FOOT = args.footer

def inl(t):
    t = html.escape(t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)

# ---- parse ----
slides = []; cur = None; i = 0
while i < len(src):
    l = src[i]
    if l.startswith("### Slide"):
        m = re.match(r"### Slide (\d+) — (.*)", l)
        cur = {"n": int(m.group(1)), "title": m.group(2), "timer": None, "items": []}
        slides.append(cur)
    elif cur is not None:
        if l.startswith("```"):
            lang = l[3:].strip(); i += 1; b = []
            while not src[i].startswith("```"): b.append(src[i]); i += 1
            cur["items"].append(("code", lang, "\n".join(b)))
        elif l.startswith("Timer on the slide"):
            cur["timer"] = re.search(r"\*\*(\d+)", l).group(1)
        elif l.startswith("|"):
            rows = []
            while i < len(src) and src[i].startswith("|"): rows.append(src[i]); i += 1
            i -= 1
            cur["items"].append(("table", [[c.strip() for c in r.strip().strip("|").split("|")] for k, r in enumerate(rows) if k != 1]))
        elif l.startswith("Text:"):
            cur["items"].append(("text", l[5:].strip().strip('"')))
        elif l.startswith("- "):
            cur["items"].append(("bullet", l[2:]))
        elif re.match(r"\d+\. ", l):
            cur["items"].append(("bullet", re.sub(r"^\d+\. ", "", l)))
        elif l.startswith("Picture:"):
            cur["items"].append(("picture", l[8:].strip()))
        elif l.strip() in ("Wrong use:", "Fix:"):
            cur["items"].append(("label", "שימוש שגוי" if l.startswith("Wrong") else "תיקון"))
    i += 1

def boxes(letters, pos, neg):
    cells = "".join(f'<div class="bx"><span class="up">{p}</span><b>{c}</b><span class="dn">{n}</span></div>' for c, p, n in zip(letters, pos, neg))
    return f'<div class="boxes">{cells}</div>'

def render(s):
    n = s["n"]; items = s["items"]
    codes = [x for x in items if x[0] == "code"]
    lines = sum(x[2].count("\n") + 1 for x in codes)
    cls = "big" if lines <= 6 else ("mid" if lines <= 11 else "small")
    h = [f'<section class="slide n{n}">']
    if n == 1:
        h.append(f'<div class="titlebox"><div class="robot">{args.emoji}</div>'
                 f'<h1>{FOOT}</h1><h2>{args.subtitle}</h2>'
                 + (f'<div class="card">{args.card}</div>' if args.card else '') + '</div>')
    else:
        h.append(f'<header><h1>{inl(s["title"])}</h1>' + (f'<div class="timer">⏱ {s["timer"]} דקות</div>' if s["timer"] else "") + "</header>")
        h.append(f'<main class="{cls}">')
        texts = [x for x in items if x[0] == "text"]
        for t in texts: h.append(f'<p class="lead">{inl(t[1])}</p>')
        if n in BOX_SLIDES:
            w = args.boxes_word
            h.append(boxes(w, range(len(w)), range(-len(w), 0)))
        # build rows: label / pair(src,out) / single / table
        rows = []; k = 0
        its = [x for x in items if x[0] in ("label", "code", "table")]
        while k < len(its):
            x = its[k]
            if x[0] == "code" and x[1] != "text" and k + 1 < len(its) and its[k+1][0] == "code" and its[k+1][1] == "text" and max(len(l) for l in x[2].split("\n")) <= (46 if x[2].count("\n") >= 11 else 38 if x[2].count("\n") >= 6 else 34) and max(len(l) for l in its[k+1][2].split("\n")) <= 34:
                rows.append(("pair", x, its[k+1])); k += 2
            elif x[0] == "code" and x[2].count("\n") + 1 > 14:
                ls = x[2].split("\n"); half = (len(ls) + 1) // 2
                rows.append(("pair", (x[0], x[1], "\n".join(ls[:half])), (x[0], x[1], "\n".join(ls[half:])), True)); k += 1
            else:
                rows.append((x[0], x)); k += 1
        def sav(code): return 640 if code.count(chr(10)) >= 11 else 470
        def fs_for(code, avail):
            ml = max(len(l) for l in code.split("\n"))
            return min(38, avail / (0.602 * ml))
        def height(rows, f):
            hh = 0
            for r in rows:
                if r[0] == "pair":
                    hh += max(r[1][2].count("\n") + 1, r[2][2].count("\n") + 1) * min(fs_for(r[1][2], sav(r[1][2])), fs_for(r[2][2], 360 if sav(r[1][2]) > 500 else 470)) * f * 1.3 + 34
                elif r[0] == "code":
                    hh += (r[1][2].count("\n") + 1) * fs_for(r[1][2], 1100) * f * 1.3 + 34
                elif r[0] == "label": hh += 36
                else: hh += 330
            return hh
        nb = len([x for x in items if x[0] == "bullet"]); nt = len(texts)
        budget = 630 - 60 - nt * 50 - nb * 50 - (160 if n in BOX_SLIDES else 0)
        f = 1.0
        while height(rows, f) > budget and f > 0.3: f -= 0.05
        area = []
        for r in rows:
            if r[0] == "label": area.append(f'<div class="lab">{r[1][1]}</div>')
            elif r[0] == "table":
                t = "<table>"
                for kk, rr in enumerate(r[1][1]):
                    tag = "th" if kk == 0 else "td"
                    t += "<tr>" + "".join(f"<{tag}>{inl(c)}</{tag}>" for c in rr) + "</tr>"
                area.append(t + "</table>")
            elif r[0] == "pair":
                fsz = min(fs_for(r[1][2], sav(r[1][2])), fs_for(r[2][2], 360 if sav(r[1][2]) > 500 else 470)) * f
                area.append(f'<div class="pair" style="grid-template-columns:{'1.7fr 1fr' if sav(r[1][2]) > 500 else '1fr 1fr'}"><pre class="{'out' if r[1][1] == 'text' else 'src'}" style="font-size:{fsz:.0f}px">{html.escape(r[1][2])}</pre><pre class="out" style="font-size:{fsz:.0f}px">{html.escape(r[2][2])}</pre></div>')
            else:
                c = r[1]; fsz = fs_for(c[2], 1100) * f
                area.append(f'<pre class="{"out" if c[1] == "text" else "src"}" style="font-size:{fsz:.0f}px">{html.escape(c[2])}</pre>')
        h.append('<div class="area">' + "".join(area) + "</div>")
        bl = [x for x in items if x[0] == "bullet"]
        if bl:
            tg = "ol" if n in NUM_SLIDES else "ul"
            h.append(f"<{tg}>" + "".join(f"<li>{inl(x[1])}</li>" for x in bl) + f"</{tg}>")
        h.append("</main>")
    h.append(f'<footer>{FOOT}<span class="pg">{n}</span></footer></section>')
    return "\n".join(h)

css = """
@page{size:1280px 720px;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;direction:rtl}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;page-break-after:always;background:#f4f8ff;padding:28px 56px 52px}
header{display:flex;justify-content:space-between;align-items:center;border-bottom:5px solid #2b6cb0;padding-bottom:8px;margin-bottom:14px}
h1{margin:0;font-size:42px;color:#1a365d}
.timer{background:#c53030;color:#fff;font-size:34px;font-weight:bold;padding:6px 20px;border-radius:30px}
main{display:flex;flex-direction:column;gap:12px}
.lead{margin:0;font-size:34px;color:#222;line-height:1.35}
code{font-family:"Courier New",monospace;direction:ltr;unicode-bidi:isolate;display:inline-block;background:#e2e8f0;padding:0 6px;border-radius:5px;font-weight:bold}
pre{font-family:"Courier New",monospace;font-weight:bold;direction:ltr;text-align:left;unicode-bidi:isolate;margin:0;padding:12px 18px;border-radius:10px;white-space:pre-wrap}
.src{background:#fff;border:3px solid #2b6cb0;color:#111}
.out{background:#1a202c;color:#9ae6b4}

.area{display:flex;flex-direction:column;gap:10px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:start;direction:ltr}
.lab{font-size:26px;font-weight:bold;color:#c53030}
.area.two .lab{direction:rtl}
ul,ol{margin:0;padding-right:40px;font-size:32px;line-height:1.4;color:#222}
table{border-collapse:collapse;font-size:34px;width:100%}
td,th{border:2px solid #4a5568;padding:8px 14px}th{background:#bee3f8}td{background:#fff}
.boxes{display:flex;direction:ltr;gap:10px;justify-content:center;margin:6px 0 8px}
.bx{width:110px;height:130px;border:4px solid #2b6cb0;background:#fff;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:4px;font-family:"Courier New",monospace}
.bx b{font-size:56px}.up{color:#2b6cb0;font-size:28px;font-weight:bold}.dn{color:#c05621;font-size:28px;font-weight:bold}
footer{position:absolute;left:0;right:0;bottom:0;height:40px;background:#1a365d;color:#fff;font-size:20px;display:flex;justify-content:center;align-items:center}
.pg{position:absolute;left:20px}
.titlebox{text-align:center;padding-top:50px}
.titlebox h1{font-size:76px;margin:10px 0}.titlebox h2{font-size:44px;color:#2b6cb0;margin:0}
.robot{font-size:130px}.card{display:inline-block;margin-top:24px;background:#fff;border:5px solid #2b6cb0;border-radius:16px;padding:10px 60px;font:bold 60px "Courier New",monospace;direction:ltr}
.n1{background:linear-gradient(#e6f0ff,#fff)}
"""
out = f'<!DOCTYPE html><html lang="he" dir="rtl"><meta charset="utf-8"><title>{FOOT}</title><style>{css}</style><body>' + "\n".join(render(s) for s in slides) + "</body></html>"
open(args.out, "w", encoding="utf-8").write(out)
print(len(slides), "slides")
