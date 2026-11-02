#!/usr/bin/env python3
"""Build a Hebrew countdown page (timed in-class cases) from a cases JSON file in a unit folder.

The method is borrowed from the IB DP1 "Test Prep Countdown": one case at a time is projected, a big clock runs
(green, amber, red), the room "locks out" at zero, and the reveal screen shows a for-loop solution and a
while-loop solution that use different ideas, and how they differ.

Cases are plain statements, no functions (for classes that have not learned def): a variable holds the text,
the student's code works on it and prints the answer.

Reads, from the folder of the JSON file:
  - <cases>.json       title, subtitle, footer, unit, the steps to get the files, and per case: starter file name,
                       English goal (for the starter's comment), Hebrew title and goal, minutes, tools used,
                       test values, how the two solutions differ
  - the reference .py  sections "# === case N for ===" and "# === case N while ===". The first code line of a
                       section is  text = "..."  ; the build replaces it with every test value, runs the section,
                       and stops if the for and while versions print different things
Writes, into the same folder:
  - the page (<output>), the students' instructions (<instructions>, Markdown, no solutions),
    and one starter file per case (<file>)

Usage (Python 3, standard library only):
  python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json
"""
import contextlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = re.compile(r"^# === case (\d+) (for|while) ===$", re.M)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s" % path)


def sections(source):
    """(case number, loop) -> the section's code without its leading comment lines."""
    found = {}
    marks = list(MARK.finditer(source))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(source)
        lines = source[m.end():end].strip("\n").split("\n")
        while lines and lines[0].startswith("#"):
            lines.pop(0)
        found[(int(m.group(1)), m.group(2))] = "\n".join(lines).rstrip() + "\n"
    return found


def quoted(value):
    return '"%s"' % value


def run(code, value):
    first, rest = code.split("\n", 1)
    if not first.startswith("text = "):
        sys.exit("a section must start with: text = ...\n" + code)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        exec("text = %s\n%s" % (quoted(value), rest), {})
    return out.getvalue().rstrip("\n")


def starter(meta, c):
    lines = ["# %s - case %d: %s" % (meta["unit"], c["num"], c["goal_en"]),
             "# Write your code under the text line, with the loop the board shows (for or while).",
             "# Run, compare with the expected output, then change the text to the next value and run again:"]
    for v, e in zip(c["inputs"], c["outputs"]):
        lines.append("#   text = %s    expected: %s" % (quoted(v), e.replace("\n", " / ")))
    lines += ["", "text = %s" % quoted(c["inputs"][0]), "", ""]
    return "\n".join(lines)


def instructions(meta, cases):
    out = ["# " + meta["title"], "", meta["subtitle"], "", '<div dir="rtl">', ""]
    out += ["%d. %s" % (i + 1, step) for i, step in enumerate(meta["steps"])]
    out += ["", "</div>"]
    for c in cases:
        out += ["", "<pagebreak>"] if c["num"] != cases[0]["num"] else []
        out += ["", "## תיק %d (%d דקות): %s" % (c["num"], c["minutes"], c["title"]), "",
                '<div dir="rtl">', "", c["objective"], "", "</div>", "", '<div dir="rtl">', "",
                "פותחים את הקובץ הבא:", "", "</div>", "", "```python", c["file"], "```", "", '<div dir="rtl">', "",
                "בדיקות – בכל פעם משנים את הטקסט ומריצים. כשהקוד נכון, הפלט שווה לצפוי:", "", "</div>", "",
                "```python"]
        for v, e in zip(c["inputs"], c["outputs"]):
            out += ["text = " + quoted(v), "# expected: " + e.replace("\n", " / ")]
        out += ["```"]
    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cases_path = os.path.abspath(sys.argv[1])
    folder = os.path.dirname(cases_path)
    meta = json.loads(read(cases_path))
    code = sections(read(os.path.join(folder, meta["reference"])))

    cases = []
    for c in meta["cases"]:
        n = c["n"]
        outputs = []
        for value in c["inputs"]:
            got = [run(code[(n, loop)], value) for loop in ("for", "while")]
            if got[0] != got[1]:
                sys.exit("case %d: for and while disagree on %r: %r / %r" % (n, value, got[0], got[1]))
            outputs.append(got[0])
        case = dict(c, num=n, outputs=outputs, solution_for=code[(n, "for")], solution_while=code[(n, "while")])
        case["starter"] = starter(meta, case)
        case["expected"] = "\n\n".join("text = %s\n%s" % (quoted(v), e) for v, e in zip(c["inputs"], outputs))
        case["first"] = "\n".join("text = " + quoted(v) for v in c["inputs"])
        cases.append(case)

    page_cases = [{k: c[k] for k in ("num", "file", "title", "objective", "minutes", "ops", "contrast",
                                     "starter", "expected", "first", "solution_for", "solution_while")}
                  for c in cases]
    data = json.dumps({"title": meta["title"], "subtitle": meta["subtitle"], "footer": meta["footer"],
                       "steps": meta["steps"], "cases": page_cases}, ensure_ascii=False).replace("</", "<\\/")
    page = read(os.path.join(HERE, "countdown_template.html"))
    write(os.path.join(folder, meta["output"]),
          page.replace("/*__DATA__*/{}", data).replace("__TITLE__", meta["title"]))
    write(os.path.join(folder, meta["instructions"]), instructions(meta, cases))
    for c in cases:
        write(os.path.join(folder, c["file"]), c["starter"])
    for c in cases:
        print("  case %d: %s" % (c["num"], " | ".join("%s -> %s" % (v, e) for v, e in zip(c["inputs"], c["outputs"]))))


if __name__ == "__main__":
    main()
