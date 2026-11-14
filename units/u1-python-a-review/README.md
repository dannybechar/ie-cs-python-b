# Lessons 1.0–2.3 — Python A Review

Python B, Grade 8 · 6 academic hours = 3 meetings = 270 minutes (45 theory / 225 practice, official master table). 3 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief, HTML deck, PDFs, worksheets) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code and data files | [`exercises/`](exercises) |
| Open the student test sheets | [`assessment/`](assessment) |
| Plan a lesson, see solutions, answer keys, live-demo code (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | none yet: this repository has no per-unit `feedback/` folder |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the Ministry sources are indexed in [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (label · theme · Hebrew lab brief as `.md`, HTML deck, slide PDFs and worksheets) | Theory / practice min | Review status |
|---|---|---|---|
| 1 | **Lessons 1.0–1.1**<br>Who Can Come In? — Compound Conditions, `elif` and Input Validation<br>[md](lessons/L01-who-can-come-in.md) · [html](lessons/L01-who-can-come-in.html) · [slides PDF](lessons/L01-who-can-come-in/slides-he.pdf) | 45 / 45 | Approved by the teacher |
| 2 | **Lessons 1.2–1.4**<br>Counting Rounds — `for`, `range` and the Five-Scores Analyzer<br>[md](lessons/L02-counting-rounds.md) · [html](lessons/L02-counting-rounds.html) · [slides PDF](lessons/L02-counting-rounds/slides-he.pdf) | 0 / 90 | Approved by the teacher |
| 3 | **Lessons 2.0–2.3**<br>Until It's Done — the `while` Loop, the Stop Condition and Loops That Never End (Unit Checkpoint)<br>[md](lessons/L03-until-its-done.md) · [html](lessons/L03-until-its-done.html) · [slides PDF](lessons/L03-until-its-done/slides-he.pdf) | 0 / 90 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-who-can-come-in-notes.md`](teacher/L01-who-can-come-in-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-counting-rounds-notes.md`](teacher/L02-counting-rounds-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-until-its-done-notes.md`](teacher/L03-until-its-done-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (5 files) |
| [`teacher/unit-1-test-answer-key.md`](teacher/unit-1-test-answer-key.md) | Answer key and rubric |
| [`teacher/unit-1-test-chatgpt-review-prompt.md`](teacher/unit-1-test-chatgpt-review-prompt.md) | Test material |
| [`teacher/unit-1-test-for-chatgpt-review.md`](teacher/unit-1-test-for-chatgpt-review.md) | Test material |
| [`teacher/unit-1-test-form-b-answer-key.md`](teacher/unit-1-test-form-b-answer-key.md) | Answer key and rubric |

## Status and open checks

- 2 of 3 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

6 academic hours = 3 meetings = 270 minutes (45 theory / 225 practice).

### Lessons 1.0–1.1 — Python A Review

**Topic:** Who Can Come In? (compound conditions, `elif` and input validation)

90 minutes: 45 knowledge + 45 lab · **comparisons → and / or / not → elif → trace → validate first**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-who-can-come-in-notes.md`](teacher/L01-who-can-come-in-notes.md) | Lesson plan |
| Student | [`L01-who-can-come-in.md`](lessons/L01-who-can-come-in.md) | Hebrew lab brief |
| Student | [`Entry_Starter.py`](exercises/Entry_Starter.py) | `int()` warm-up bug, the two-bug gate, stubs for Tasks 2–3 |
| Teacher | [`Entry_Reference.py`](teacher/solutions/Entry_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L01-who-can-come-in/slides-he.pdf) | Hebrew slide deck (20 slides, NotebookLM, patched) |

### Lessons 1.2–1.4 — Python A Review

**Topic:** Counting Rounds (`for`, `range` and the five-scores analyzer)

90 minutes: Lab + Lab · **range forms → stop is excluded → counter vs total → trace → average**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-counting-rounds-notes.md`](teacher/L02-counting-rounds-notes.md) | Lesson plan |
| Student | [`L02-counting-rounds.md`](lessons/L02-counting-rounds.md) | Hebrew lab brief |
| Student | [`Scores_Starter.py`](exercises/Scores_Starter.py) | Overwritten-total warm-up bug, the trace task, stubs |
| Teacher | [`Scores_Reference.py`](teacher/solutions/Scores_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L02-counting-rounds/slides-he.pdf) | Hebrew slide deck (17 slides, NotebookLM, patched) |

### Lessons 2.0–2.3 — Python A Review

**Topic:** Until It's Done (the `while` loop, the stop condition and loops that never end) — unit checkpoint · 🔶 reworked from the Ministry teaching materials (2.0, 2.1, loop-trap deck)

90 minutes: Lab + Lab · **sentinel, condition, update → counting up and down → never-ending loops and the Safe Loop Checklist → `for` ↔ `while` → locker → exciting number → series checkpoint**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-until-its-done-notes.md`](teacher/L03-until-its-done-notes.md) | Lesson plan, including the diagnostic checkpoint |
| Student | [`L03-until-its-done.md`](lessons/L03-until-its-done.md) | Hebrew lab brief |
| Student | [`While_Starter.py`](exercises/While_Starter.py) | Never-ending validation warm-up bug, four never-ending loops, stubs |
| Teacher | [`While_Reference.py`](teacher/solutions/While_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L03-until-its-done/slides-he.pdf) | **Superseded — pending new NotebookLM deck** (the old 16-slide deck of the previous 2.0–2.3; do not teach from it) |

Cross-checked on 13 Nov 2026 against the Ministry's loop-trap deck (2.3, image-only; rendered to images): the four engine parts, the three traps (frozen clock, wrong direction, always-true condition), the user-typed sentinel and the four-point checklist are all covered by this meeting. Extra series tasks (alternating squares, factorial sum) were added to the if-time block from Ministry worksheet 2.1.

**Ministry self-check forms (Master Python), for homework or Classroom:** [1.3 Master Python — `for` loop](https://docs.google.com/forms/d/1WUsETmUxov-vwmOvYFyUP2Z_DvkNL31lyC_0G7iGbbk/edit) (for 1.2–1.4) · [2.2 Master Python — `while` loop](https://docs.google.com/forms/d/1iVIu9A1WjI1BOVbBhOSiwelbBcOfQL38EZjM8INNy9A/edit) (for 2.0–2.3).

**About the Ministry's lessons 0.1–0.6:** these are Google Classroom onboarding only (the Classroom, a screenshot, a file upload, a Google Form — no Python, no AI). They have no meeting and no hours in the master table; the class is past them. The 0.5 Forms task, if the teacher wants it: [0.5 Forms task](https://docs.google.com/forms/d/1yKQi6ZiFGpd7DH8khMaxQ2Qiq0IPaWJGJGkNqZBMuwU/edit).

### Lessons 1.0–2.3 test (Grade 9)

60-minute written test on the whole unit, 100 points (trace 24 · debug and `range` 16 · write three programs 60).
Reviewed by ChatGPT as an expert school teacher; the accepted corrections are in the files.
Word copies for Google Drive: `Downloads\python-b\unit 1 - Python A Review - Test.docx` and `... - Test Solution.docx`
(made with [`tools/md_to_docx.py`](../../tools/md_to_docx.py)).

First sitting: 18 and 24 Oct 2026, 32 students, mean 77.1 (aggregates and the two wording problems found are in the key).

| For | File | What it is |
|---|---|---|
| Student | [`unit-1-test-he.md`](assessment/unit-1-test-he.md) | The Hebrew test |
| Teacher | [`unit-1-test-answer-key.md`](teacher/unit-1-test-answer-key.md) | Answer key, rubric, common errors, grading scale |
| Teacher | [`Test_Reference.py`](teacher/solutions/Test_Reference.py) | Model solutions (run and checked) |
| Teacher | [`unit-1-test-for-chatgpt-review.md`](teacher/unit-1-test-for-chatgpt-review.md) | One file with the request, test, key and solutions, to paste into ChatGPT |
| Teacher | [`unit-1-test-chatgpt-review-prompt.md`](teacher/unit-1-test-chatgpt-review-prompt.md) | The review request alone (source of the combined file) |
| Student | [`unit-1-test-form-b-he.md`](assessment/unit-1-test-form-b-he.md) | Form B (retest): same structure and difficulty as Form A; Q5b and Q6b wording fixed |
| Teacher | [`unit-1-test-form-b-answer-key.md`](teacher/unit-1-test-form-b-answer-key.md) | Form B key and rubric (question-by-question map to Form A) |
| Teacher | [`Test_B_Reference.py`](teacher/solutions/Test_B_Reference.py) | Form B model solutions (run and checked) |
