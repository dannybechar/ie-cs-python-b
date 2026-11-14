"""Repo consistency check. Usage:  python -I tools/check-repo.py   (run from the repo root)

Errors (exit 1):  a Reference/Solution .py that does not compile; a lesson page without teacher notes or HTML twin;
                  not 30 meetings.
Warnings:         Starter .py that does not compile (some are broken on purpose); a lesson without a NotebookLM slide
                  PDF (new decks are made on request); lesson notes without a Duration line.
Nothing is written to disk (compile() only, no __pycache__).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warnings = [], []


def check_python():
    n = 0
    for f in sorted((ROOT / "units").rglob("*.py")):
        n += 1
        try:
            compile(f.read_text(encoding="utf-8-sig"), str(f), "exec")
        except SyntaxError as e:
            msg = "%s: %s (line %s)" % (f.relative_to(ROOT).as_posix(), e.msg, e.lineno)
            (warnings if "_Starter" in f.name or f.parent.name == "exercises" else errors).append("python: " + msg)
    return n


def check_meetings():
    n = 0
    for unit in sorted((ROOT / "units").glob("u[0-9]*")):
        notes = sorted((unit / "teacher").glob("L*-notes.md"))
        if not notes:
            errors.append("%s: no lesson notes" % unit.name)
        for note in notes:
            n += 1
            stem = note.name[: -len("-notes.md")]
            for need in ("lessons/%s.md" % stem, "lessons/%s.html" % stem):
                if not (unit / need).exists():
                    errors.append("%s: missing %s" % (unit.name, need))
            if not (unit / "lessons" / stem / "slides-he.pdf").exists():
                warnings.append("%s: no slides-he.pdf for %s" % (unit.name, stem))
            if not re.search(r"(?i)duration", note.read_text(encoding="utf-8")):
                warnings.append("%s/%s: no Duration line" % (unit.name, note.name))
        for page in sorted((unit / "lessons").glob("L*.md")):
            if not (unit / "teacher" / (page.stem + "-notes.md")).exists():
                errors.append("%s: lesson page %s has no teacher notes" % (unit.name, page.name))
    return n


if __name__ == "__main__":
    py = check_python()
    meetings = check_meetings()
    if meetings != 30:
        errors.append("expected 30 meetings, found %d" % meetings)
    print("python files: %d | meetings: %d" % (py, meetings))
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)
