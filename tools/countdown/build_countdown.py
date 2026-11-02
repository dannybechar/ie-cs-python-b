#!/usr/bin/env python3
"""Build a Hebrew countdown page (timed in-class cases) from a cases JSON file in a unit folder.

The method is borrowed from the IB DP1 "Test Prep Countdown": one case at a time is projected, a big clock runs
(green, amber, red), the room "locks out" at zero, and the reveal screen shows a for-loop solution and a
while-loop solution that use different ideas, and how they differ.

Reads, from the folder of the JSON file:
  - <cases>.json        title, subtitle, footer, the steps to get the file, and per case: function name, Hebrew
                        title and goal, minutes, tools used, test calls, how the two solutions differ
  - the reference .py   <func>_for and <func>_while for every case (shown on the reveal screen)
  - the starter .py     <func> stub for every case (shown on the briefing screen)
It runs every test call on both versions, stops if they disagree, and writes the results as the expected output.

Usage (Python 3, standard library only):
  python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json
"""
import ast
import contextlib
import io
import json
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")


def functions(source):
    """Map function name -> its source text (with the comment lines just above it)."""
    tree = ast.parse(source)
    lines = source.split("\n")
    found = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            start = node.lineno - 1
            while start > 0 and lines[start - 1].startswith("#"):
                start -= 1
            found[node.name] = "\n".join(lines[start:node.end_lineno])
    return found


def write_instructions(meta, cases, path):
    """The students' instructions (Markdown, for tools/md_to_docx.py --worksheet): no solutions."""
    out = ["# " + meta["title"], "", meta["subtitle"], "", '<div dir="rtl">', ""]
    out += ["%d. %s" % (i + 1, step) for i, step in enumerate(meta["steps"])]
    out += ["", "</div>"]
    for c in cases:
        out += ["", "<pagebreak>"] if c["num"] != cases[0]["num"] else []
        out += ["", "## תיק %d (%d דקות): %s" % (c["num"], c["minutes"], c["title"]), "",
                '<div dir="rtl">', "", c["objective"], "", "</div>", "", '<div dir="rtl">', "",
                "הפעולה בקובץ:", "", "</div>", "", "```python", c["starter"][c["starter"].index("def "):], "```", "", '<div dir="rtl">', "",
                "בדיקות – כשהפעולה נכונה, התוצאה שווה לצפוי:", "", "</div>", "", "```python"]
        for line in c["expected"].split("\n"):
            call, result = line.split("  ->  ")
            out += [call, "# expected: " + result]
        out += ["```"]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("wrote %s" % path)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cases_path = os.path.abspath(sys.argv[1])
    folder = os.path.dirname(cases_path)
    meta = json.loads(read(cases_path))
    ref_path = os.path.join(folder, meta["reference"])
    ref_src = read(ref_path)
    ref_funcs = functions(ref_src)
    starter_funcs = functions(read(os.path.join(folder, meta["starter"])))
    with contextlib.redirect_stdout(io.StringIO()):
        module = runpy.run_path(ref_path)

    cases = []
    for c in meta["cases"]:
        name = c["func"]
        lines = []
        for call in c["calls"]:
            results = []
            for version in ("for", "while"):
                args = call[call.index("("):]
                results.append(eval(name + "_" + version + args, dict(module)))
            if results[0] != results[1]:
                sys.exit("case %d: for and while disagree on %s: %r / %r" % (c["n"], call, results[0], results[1]))
            shown = '"%s"' % results[0] if isinstance(results[0], str) else str(results[0])
            lines.append("%s  ->  %s" % (call, shown))
        solutions = {}
        for version in ("for", "while"):
            code = ref_funcs[name + "_" + version]
            code = code[code.index("def "):]  # the reveal shows code only; the contrast text explains it
            solutions[version] = code.replace("def %s_%s(" % (name, version), "def %s(" % name)
        cases.append({
            "num": c["n"], "title": c["title"], "objective": c["objective"], "minutes": c["minutes"],
            "ops": c["ops"], "contrast": c["contrast"], "func": name,
            "calls": "\n".join(c["calls"]), "expected": "\n".join(lines),
            "starter": starter_funcs[name], "for": solutions["for"], "while": solutions["while"],
        })

    data = json.dumps({"title": meta["title"], "subtitle": meta["subtitle"], "footer": meta["footer"],
                       "steps": meta["steps"], "cases": cases}, ensure_ascii=False).replace("</", "<\\/")
    page = read(os.path.join(HERE, "countdown_template.html"))
    page = page.replace("/*__DATA__*/{}", data).replace("__TITLE__", meta["title"])
    out = os.path.join(folder, meta["output"])
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    print("wrote %s (%d cases, %d KB)" % (out, len(cases), len(page) // 1024))
    if meta.get("instructions"):
        write_instructions(meta, cases, os.path.join(folder, meta["instructions"]))
    for c in cases:
        print("  case %d %s:\n    %s" % (c["num"], c["func"], c["expected"].replace("\n", "\n    ")))


if __name__ == "__main__":
    main()
