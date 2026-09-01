# Grade 9 — Python C (Transition Year)

This repository is the source of truth for working examples and teaching
resources for the Grade 9 course. This is a **transition-year** (תשפ"ז)
program: the Ministry of Education's 2026/27 circular permits the old
Python C track as an official Grade 9 alternative this year, alongside the
new programs, until an official "AI + Computer Science Part C" syllabus is
published. Content here is built directly against
[`docs/ministry-source/python-c.pdf`](docs/ministry-source/python-c.pdf).

Because the new Grade 8 program teaches List but not Tuple/Set, Unit 1
includes a small bridge (List review + a compact Tuple/Set introduction)
absorbed into the unit's official 12 hours — see
[`units/u1-data-structures/strategy/unit-strategy.md`](units/u1-data-structures/strategy/unit-strategy.md).

## Current build status

**6 of 30 official double meetings are built** — all of Unit 1 (Data
Structures). See [`course-map.md`](course-map.md) for the full
unit-by-unit breakdown.

- [Unit 1 — Data Structures](units/u1-data-structures) — complete (6/6 meetings)
- [Unit 2 — Classes & OOP](units/u2-classes-and-oop) — not yet started
- [Unit 3 — Mouse Events](units/u3-mouse-events) — not yet started
- [Unit 4 — Keyboard Events, Timer & Animation](units/u4-keyboard-timer-animation) — not yet started
- [Unit 5 — Final Integrated Project](units/u5-final-integrated-project) — not yet started

## Repository layout

```
docs/
  annual-strategy.md        — year-wide pedagogical strategy (transition-year framing, exit profile)
  annual-work-plan-he.docx  — official annual work plan (Hebrew)
  ministry-source/          — the official ministry PDFs this course answers to
units/
  u{N}-{official-unit-slug}/
    strategy/unit-strategy.md   — that unit's official scope + meeting breakdown
    m{K}-{meeting-slug}/
      examples/    — Starter / Reference Python scripts
      teacher/     — Hebrew lesson deck + lesson notes
      student/     — Hebrew lab brief (docx + pdf)
      assessment/  — exit-check image
```

## Repository conventions

- Every `.py` example must compile cleanly before it's committed.
- Code files use `_Starter` / `_Reference` — `_Starter` is the student's
  starting point (may contain an intentional bug, documented in that
  meeting's `teacher/lesson-notes.md`), `_Reference` is the model solution.
- No version suffixes in filenames — git history is the version record.
- Hebrew-facing files (decks, lab briefs, exit checks) keep an explicit
  `-he` suffix since directory names are English.
- Units 3–4's Turtle mouse/keyboard/animation examples need manual
  smoke-testing (open, run, click/press) — they can't be verified headless.
- Generated files (`__pycache__/`, etc.) are not committed.
- Never commit student information, passwords, tokens, or private school data.

## Course workflow

1. Open the meeting folder under `units/`.
2. Read `teacher/lesson-notes.md` for the full 90-minute lesson plan.
3. Run the `examples/` scripts and confirm they behave as documented.
4. Compare against `student/lab-brief-he.docx` and the exit check.
5. Commit only after the example has been verified.
