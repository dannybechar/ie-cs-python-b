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

**All 30 of 30 official double meetings are built** (9 program units, shown as blocks below). Only Lessons 1.0–1.1 and 1.2–1.4 are approved; the advanced-language-model, lists, classification and recommender blocks (lessons 9.1–9.5 and 10.0–22.1) were reworked on 8 Nov 2026 to the Ministry materials (🔶, awaiting approval); Lessons 2.0–2.3 and the AI2-opening, functions, API and strings blocks (lessons 3.0–8.7) were reworked on 31 Oct 2026 to follow the Ministry's published teaching materials (see [`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md)) and await approval.
Where the class actually is in the course: [`class-progress.md`](class-progress.md).
See [`course-map.md`](course-map.md) for the unit-by-unit breakdown, the schedule and the pace check, and
[`docs/annual-strategy.md`](docs/annual-strategy.md) for the year plan.

- [Python A Review, lessons 1.0–2.3](units/u1-python-a-review) — ✅ approved (2/3: Lessons 1.0–1.1, 1.2–1.4); 🔶 Lessons 2.0–2.3 reworked to the Ministry materials, awaiting approval
- [AI2 Year Opening, lessons 3.0–3.2](units/u2-ai2-year-opening) — 🔶 reworked to the Ministry materials, awaiting approval (2/2)
- [Functions, lessons 4.1–4.6](units/u3-functions) — 🔶 reworked to the Ministry materials, awaiting approval (3/3)
- [Bringing AI into Code (API), lessons 5.0–6.2](units/u4-api) — 🔶 reworked to the Ministry materials, awaiting approval (2/2)
- [Strings, lessons 7.1–8.7](units/u5-strings) — 🔶 reworked to the Ministry materials, awaiting approval (4/4); Lessons 7.1–8.1 taught, Lessons 8.2–8.7 next (countdown edition ready)
- [Advanced Language Model, lessons 10.0–11.3](units/u6-advanced-language-model) — 🔶 reworked to the Ministry materials (8 Nov 2026), awaiting approval; new decks pending
- [Lists, lessons 9.1–9.5 and 12.0–14.5](units/u7-lists) — 🔶 reworked to the Ministry materials (8 Nov 2026), awaiting approval (5/5); new decks pending
- [Classification, lessons 16.0–19.1](units/u8-classification) — 🔶 reworked to the Ministry materials (8 Nov 2026), awaiting approval (4/4); needs a live run with TensorFlow; new decks pending
- [Recommender Systems, lessons 20.0–22.1](units/u9-recommender-systems) — 🔶 reworked to the Ministry materials (8 Nov 2026), awaiting approval (4/4); new decks pending

## Numbering

The official lesson numbers of the Ministry's Python B program (`8.1`, `8.2` …) are the numbers of this repository; the old "Unit U.M" numbers are retired.
A 90-minute meeting is named by the range of official lessons it covers, e.g. **Lessons 8.2–8.7 — Strings**; the mapping of all 30 meetings is in
[`docs/official-numbering.md`](docs/official-numbering.md). Folders and file names (`units/u5-strings/m4-…`) keep their names as internal keys.

## Repository layout

```
CLAUDE.md                   — the build / review / approve workflow
docs/
  annual-strategy.md        — year-wide strategy (hours, meeting outline, depth boundaries, tools, exit profile)
  annual-work-plan-he.docx  — annual work plan for the school (Hebrew)
  ministry-source/          — the official ministry PDFs this course answers to
  ministry-teaching-materials.md — index of the Ministry decks/worksheets (source of truth) and the rulebook
tools/
  deck-patch-kit/           — scripts for reviewing and patching the NotebookLM slide decks
  countdown/                — builds a projected countdown page of timed cases (for/while reveal) from a unit JSON
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

- **Naming rule:** a meeting is named by the range of official lessons it covers, as
  **Lessons {A}–{B} — {block name}** (e.g. *Lessons 4.1–4.2 — Functions*);
  in Hebrew, **שיעורים {A}–{B} – {שם היחידה}** (e.g. *שיעורים 4.1–4.2 – פעולות*).
  The rule and the mapping are in [`docs/official-numbering.md`](docs/official-numbering.md);
  block names follow the Ministry program (`python-b-ai.pdf`, list in
  [`CLAUDE.md`](CLAUDE.md)). A lesson's theme appears only as a subtitle, never
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
- Code that calls an outside AI service or library (the API, advanced-language-model and classification blocks, lessons 5.0–6.2, 10.0–11.3 and 16.0–19.1) is
  verified with a stand-in that returns fixed answers, and needs a live run
  in Thonny with the real service before class.
- **Never commit an API key**, student information, passwords, tokens, or
  private school data. Survey and image data from lessons 16.0–22.1 stay out of the repo.
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
