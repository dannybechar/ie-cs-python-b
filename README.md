# Grade 9 — Python C (Transition Year)

This repository is the source of truth for working examples and teaching
resources for the Grade 9 course. This is a **transition-year** (תשפ"ז)
program: the Ministry of Education's 2026/27 circular permits the old
Python C track as an official Grade 9 alternative this year, alongside the
new programs, until an official "AI + Computer Science Part C" syllabus is
published. Content here is built directly against
[`docs/ministry-source/python-c.pdf`](docs/ministry-source/python-c.pdf).

It follows the structure, conventions and workflow of the Grade 7 Python A course,
[`ie-cs-python-a`](https://github.com/dannybechar/ie-cs-python-a). How meetings are built, reviewed
and approved is described in [`CLAUDE.md`](CLAUDE.md).

## Current build status

**0 of 30 official double meetings are built.** See [`course-map.md`](course-map.md) for the unit-by-unit
breakdown, the schedule and the pace check, and each unit's `unit-strategy.md` for its official scope.

- Unit 1 — Data Structures — not started (0/6 meetings)
- Unit 2 — Classes — not started (0/6 meetings)
- Unit 3 — Mouse Events — not started (0/6 meetings)
- Unit 4 — Keyboard Events and Timer — not started (0/6 meetings)
- Unit 5 — Final Project — not started (0/6 meetings)

## Repository layout

```
CLAUDE.md                   — the build / review / approve workflow
docs/
  annual-strategy.md        — year-wide pedagogical strategy (transition-year framing, exit profile)
  annual-work-plan-he.docx  — official annual work plan (Hebrew)
  ministry-source/          — the official ministry PDFs this course answers to
tools/
  deck-patch-kit/           — scripts for reviewing and patching the NotebookLM slide decks
units/
  u{N}-{official-unit-slug}/
    README.md               — index of the unit's meetings and their files
    unit-strategy.md        — that unit's official scope + meeting breakdown
    m{K}-lesson-notes.md    — teacher: minute-by-minute plan for meeting K
    m{K}-slides-he.pdf      — teacher: Hebrew slide deck (NotebookLM, patched)
    m{K}-lab-brief-he.md    — student: Hebrew lab brief
    *_Starter.py / *_Reference.py — lab code for the unit's meetings
```

## Repository conventions

- **Naming rule:** a meeting is named by its curriculum unit, as
  **Unit {U}.{M} — {unit name}** (e.g. *Unit 2.1 — Classes*);
  in Hebrew, **יחידה {U}.{M} – {שם היחידה}** (e.g. *יחידה 2.1 – מחלקות*).
  Unit names follow the Ministry program (`python-c.pdf`). A lesson's theme
  appears only as a subtitle, never as its name. This applies to headings,
  the course map, lab briefs, slide titles and footers, and NotebookLM
  notebook names.
- Every `.py` example must compile cleanly before it's committed.
- Code files use `_Starter` / `_Reference` — `_Starter` is the student's
  starting point (may contain an intentional bug, documented in that
  meeting's `m{K}-lesson-notes.md`), `_Reference` is the model solution.
- All of a unit's files sit flat in the unit folder; the `m{K}-` prefix
  says which meeting a file belongs to.
- Every lesson's notes state its **Duration** and **Structure**. When a
  meeting is added or retimed, log it in [`course-map.md`](course-map.md)
  and keep each unit's planned minutes within its official minutes
  (1 academic hour = 45 minutes).
- No version suffixes in filenames — git history is the version record.
- Hebrew-facing files (decks, lab briefs, exit checks) keep an explicit
  `-he` suffix since directory names are English.
- Markdown is the source format for lesson notes, lab briefs and plans, so
  everything renders on GitHub. Exceptions: original ministry documents stay
  in their original format, and slide decks are made in NotebookLM and
  committed as `m{K}-slides-he.pdf`.
- Hebrew in Markdown: start every Hebrew line with a Hebrew word (GitHub
  picks each paragraph's direction from its first letter). Put code in
  fenced blocks. Wrap tables and numbered/bulleted lists in
  `<div dir="rtl">` … `</div>` with blank lines inside, since GitHub
  doesn't set their direction automatically.
- Units 3–4's Turtle mouse/keyboard/timer examples need a live run
  (open, run, click/press) — they can't be fully verified headless.
- Generated files (`__pycache__/`, etc.) are not committed.
- Never commit student information, passwords, tokens, or private school data.

## Course workflow

1. Open the unit folder under `units/`; its `README.md` lists each meeting's files.
2. Read `m{K}-lesson-notes.md` for the full 90-minute lesson plan.
3. Run the `_Starter` / `_Reference` scripts and confirm they behave as documented.
4. Compare against `m{K}-lab-brief-he.md` and the exit check.
5. Commit only after the example has been verified.

## Slide decks

Every meeting's deck is made in NotebookLM from its lesson notes and lab brief,
then checked slide by slide against the lesson notes and the `_Reference` code,
patched where needed, and committed as `m{K}-slides-he.pdf`. The tools and the
list of recurring NotebookLM problems are in [`tools/deck-patch-kit/`](tools/deck-patch-kit/README.md).
To change a deck, regenerate or edit it outside the repo and replace the PDF.
