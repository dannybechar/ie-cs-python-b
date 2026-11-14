# Lessons 4.1–4.6 — Functions

Python B, Grade 8 · 6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice, official master table). 3 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief, HTML deck, PDFs, worksheets) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code and data files | [`exercises/`](exercises) |
| Plan a lesson, see solutions, answer keys, live-demo code (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | none yet: this repository has no per-unit `feedback/` folder |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the Ministry sources are indexed in [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (label · theme · Hebrew lab brief as `.md`, HTML deck, slide PDFs and worksheets) | Theory / practice min | Review status |
|---|---|---|---|
| 1 | **Lessons 4.1–4.2**<br>Several Parameters and `return`<br>[md](lessons/L01-parameters-and-return.md) · [html](lessons/L01-parameters-and-return.html) · [slides PDF](lessons/L01-parameters-and-return/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 4.4–4.5**<br>Practice — Returning Functions and Loops Inside Functions<br>[md](lessons/L02-returning-functions-practice.md) · [html](lessons/L02-returning-functions-practice.html) · [slides PDF](lessons/L02-returning-functions-practice/slides-he.pdf) | 0 / 90 | Built, awaiting approval |
| 3 | **Lessons 4.3, 4.6**<br>Local and Global Variables<br>[md](lessons/L03-local-and-global.md) · [html](lessons/L03-local-and-global.html) · [slides PDF](lessons/L03-local-and-global/slides-he.pdf) | 45 / 45 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-parameters-and-return-notes.md`](teacher/L01-parameters-and-return-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-returning-functions-practice-notes.md`](teacher/L02-returning-functions-practice-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-local-and-global-notes.md`](teacher/L03-local-and-global-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (3 files) |

## Status and open checks

- 0 of 3 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice).
Content follows the Ministry's teaching materials (files 4.1–4.6): [`../../docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).

### Lessons 4.1–4.2 — Functions

**Topic:** Several Parameters and `return`

90 minutes: 45 knowledge + 45 lab · **recap → several parameters → `print` vs `return` → worksheet 4.2**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-parameters-and-return-notes.md`](teacher/L01-parameters-and-return-notes.md) | Lesson plan |
| Student | [`L01-parameters-and-return.md`](lessons/L01-parameters-and-return.md) | Hebrew lab brief |
| Student | [`Return_Starter.py`](exercises/Return_Starter.py) | Missing-`return` warm-up bug (prints `None`), stubs for Tasks 1–4 |
| Teacher | [`Return_Reference.py`](teacher/solutions/Return_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L01-parameters-and-return/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck: `def` and the call, 18 slides) |

### Lessons 4.4–4.5 — Functions

**Topic:** Returning Functions and Loops Inside Functions

90 minutes: Lab + Lab · **return practice → `find_max` → digit loops → exam questions**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-returning-functions-practice-notes.md`](teacher/L02-returning-functions-practice-notes.md) | Lesson plan |
| Student | [`L02-returning-functions-practice.md`](lessons/L02-returning-functions-practice.md) | Hebrew lab brief |
| Student | [`Practice_Starter.py`](exercises/Practice_Starter.py) | Swapped-arguments warm-up bug, stubs for Tasks 1–8, the `secret` functions |
| Teacher | [`Practice_Reference.py`](teacher/solutions/Practice_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L02-returning-functions-practice/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck: parameters, 17 slides) |

### Lessons 4.3, 4.6 — Functions

**Topic:** Local and Global Variables — unit checkpoint

90 minutes: 45 knowledge + 45 lab · **local variable → `global` → the `UnboundLocalError` trap → donation campaign**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-local-and-global-notes.md`](teacher/L03-local-and-global-notes.md) | Lesson plan, including the checkpoint |
| Student | [`L03-local-and-global.md`](lessons/L03-local-and-global.md) | Hebrew lab brief |
| Student | [`Scope_Starter.py`](exercises/Scope_Starter.py) | Forgotten-`global` warm-up bug, stubs for Tasks 1–4 and the checkpoint |
| Teacher | [`Scope_Reference.py`](teacher/solutions/Scope_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L03-local-and-global/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck: `return` and scope, 19 slides) |

**Teacher decisions open (before the May 2027 exam):** multiple return values (Ministry 4.6 q3/q4, key 4.5.0) and the 4.7 default-argument H5P are deliberately left out by the rulebook; see `m3-lesson-notes.md` section 2. The 4.4 exam questions have no official key.
