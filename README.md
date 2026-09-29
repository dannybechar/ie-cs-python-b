# Grade 8 — AI + Python B

This repository is the source of truth for working examples and teaching
resources for the Grade 8 course **"בינה מלאכותית בשילוב מדעי המחשב — AI2
בשילוב פייתון ב'"**, the Ministry of Education's new program, first taught in
תשפ"ז. Content here is built directly against
[`docs/ministry-source/python-b-ai.pdf`](docs/ministry-source/python-b-ai.pdf):
60 hours (21 theory + 39 practice), 9 units, 30 double meetings of 90 minutes.

It follows the structure, conventions and workflow of the Grade 7 Python A course,
[`ie-cs-python-a`](https://github.com/dannybechar/ie-cs-python-a). How meetings are built, reviewed
and approved is described in [`CLAUDE.md`](CLAUDE.md).

## Current build status

**5 of 30 official double meetings are built** (Units 1–2 approved). See [`course-map.md`](course-map.md)
for the unit-by-unit breakdown, the schedule and the pace check, and [`docs/annual-strategy.md`](docs/annual-strategy.md) for the
year plan.

- [Unit 1 — Python A Review](units/u1-python-a-review) — ✅ approved (3/3 meetings)
- [Unit 2 — AI2 Year Opening](units/u2-ai2-year-opening) — ✅ approved (2/2 meetings)
- Unit 3 — Functions — not started (0/3 meetings)
- Unit 4 — Bringing AI into Code (API) — not started (0/2 meetings)
- Unit 5 — Strings — not started (0/4 meetings)
- Unit 6 — Advanced Language Model — not started (0/3 meetings)
- Unit 7 — Lists — not started (0/5 meetings)
- Unit 8 — Classification — not started (0/4 meetings)
- Unit 9 — Recommender Systems — not started (0/4 meetings)

## Repository layout

```
CLAUDE.md                   — the build / review / approve workflow
docs/
  annual-strategy.md        — year-wide strategy (hours, meeting outline, depth boundaries, tools, exit profile)
  annual-work-plan-he.docx  — annual work plan for the school (Hebrew)
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
  **Unit {U}.{M} — {unit name}** (e.g. *Unit 3.1 — Functions*);
  in Hebrew, **יחידה {U}.{M} – {שם היחידה}** (e.g. *יחידה 3.1 – פעולות*).
  Unit names follow the Ministry program (`python-b-ai.pdf`); the list is in
  [`CLAUDE.md`](CLAUDE.md). A lesson's theme appears only as a subtitle, never
  as its name. This applies to headings, the course map, lab briefs, slide
  titles and footers, and NotebookLM notebook names.
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
- Code that calls an outside AI service or library (Units 4, 6 and 8) is
  verified with a stand-in that returns fixed answers, and needs a live run
  in Thonny with the real service before class.
- **Never commit an API key**, student information, passwords, tokens, or
  private school data. Survey and image data from Units 8–9 stay out of the repo.
- Generated files (`__pycache__/`, etc.) are not committed.

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
