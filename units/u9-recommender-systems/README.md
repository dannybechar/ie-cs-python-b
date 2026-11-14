# Lessons 20.0–22.1 — Recommender Systems

Python B, Grade 8 · 8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice, official master table). 4 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Lessons 20.0–20.1**<br>The Feed Riddle, Two Kinds of Recommender, the Culinary Twin, the Survey<br>[md](lessons/L01-feed-riddle-and-twin.md) · [html](lessons/L01-feed-riddle-and-twin.html) · [slides PDF](lessons/L01-feed-riddle-and-twin/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lesson 21.1**<br>The Table, Similarity Points, the Twin<br>[md](lessons/L02-the-table-and-similarity.md) · [html](lessons/L02-the-table-and-similarity.html) · [slides PDF](lessons/L02-the-table-and-similarity/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 3 | **Lessons 21.1–21.2**<br>From the Twin to a Recommendation — the Unit Checkpoint<br>[md](lessons/L03-from-twin-to-recommendation.md) · [html](lessons/L03-from-twin-to-recommendation.html) · [slides PDF](lessons/L03-from-twin-to-recommendation/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 4 | **Lessons 22.0–22.1**<br>The Trap of Recommendations — Fact or Fake, the Cave, Three Traps, Controls<br>[md](lessons/L04-traps-of-recommendations.md) · [html](lessons/L04-traps-of-recommendations.html) · [slides PDF](lessons/L04-traps-of-recommendations/slides-he.pdf) | 45 / 45 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-feed-riddle-and-twin-notes.md`](teacher/L01-feed-riddle-and-twin-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-the-table-and-similarity-notes.md`](teacher/L02-the-table-and-similarity-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-from-twin-to-recommendation-notes.md`](teacher/L03-from-twin-to-recommendation-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L04-traps-of-recommendations-notes.md`](teacher/L04-traps-of-recommendations-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (6 files) |

## Status and open checks

- 0 of 4 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 20.0, 20.1, 21.1, 22.1 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). The survey scale is now **V / X / 0** (liked / disliked /
> don't know, capital English letters), the twin is the participant with the most identical non-0 answers, and the code uses only strings,
> flat lists and `def` (no tuples, default arguments, dictionaries or comprehensions). The four NotebookLM decks are **superseded** — the
> NotebookLM prep folders (`unit9-m1-slides` … `unit9-m4-slides`) were refreshed on 13 Nov 2026 to the aligned content — **all four decks need regeneration**. The Ministry's worksheets 20.2, 21.2, 22.2
> and teacher notes 21.0, 22.0 were not delivered, so the lessons 21.1–21.2 code shape and the lessons 22.0–22.1 student activity are marked ⚠️ *unverified against official 21.2 / 22.2*; our fourth meeting is our own split of deck 21.1 (see the strategy).
>
> **Data note:** [`ratings.csv`](exercises/ratings.csv) is the Ministry's sample table (four participants, five foods; aliases only, no personal
> information). Students do not read files: the data are three plain lists in the starter, and the teacher helper
> [`CsvToLists_Teacher.py`](teacher/solutions/CsvToLists_Teacher.py) turns the class's Forms CSV into those lists.
> **Safety note:** Lessons 20.0–20.1 involves a real class survey and lessons 22.0–22.1 a live-browsing demo — read each meeting's privacy/safety section before teaching it.

### Lessons 20.0–20.1 — Recommender Systems

**Topic:** The Feed Riddle, Two Kinds of Recommender, the Culinary Twin, the Survey

90 minutes: 45 knowledge + 45 lab · **feed riddle → content-based vs user-based → culinary-twin game → V / X / 0 survey**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-feed-riddle-and-twin-notes.md`](teacher/L01-feed-riddle-and-twin-notes.md) | Lesson plan, including the survey privacy rules |
| Student | [`L01-feed-riddle-and-twin.md`](lessons/L01-feed-riddle-and-twin.md) | Hebrew lab brief |
| Student | [`SurveyData_Starter.py`](exercises/SurveyData_Starter.py) | `else`-swallows-`"v"` warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`SurveyData_Reference.py`](teacher/solutions/SurveyData_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L01-feed-riddle-and-twin/slides-he.pdf) | **Superseded** deck of the v1 build (16 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lesson 21.1 — Recommender Systems

**Topic:** The Table, Similarity Points, the Twin

90 minutes: 45 knowledge + 45 lab · **the V / X / 0 table → counting points → the twin → `count_same`**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-the-table-and-similarity-notes.md`](teacher/L02-the-table-and-similarity-notes.md) | Lesson plan |
| Student | [`L02-the-table-and-similarity.md`](lessons/L02-the-table-and-similarity.md) | Hebrew lab brief |
| Student | [`Similarity_Starter.py`](exercises/Similarity_Starter.py) | `0`-and-`0`-counts warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`Similarity_Reference.py`](teacher/solutions/Similarity_Reference.py) | Solutions, one function per task |
| Data | [`ratings.csv`](exercises/ratings.csv) | The Ministry's sample table (4 participants, 5 foods), V / X / 0 |
| Teacher | [`CsvToLists_Teacher.py`](teacher/solutions/CsvToLists_Teacher.py) | Helper: Forms CSV → three lines of Python for the students to paste |
| Teacher | [`slides-he.pdf`](lessons/L02-the-table-and-similarity/slides-he.pdf) | **Superseded** deck of the v1 build (12 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lessons 21.1–21.2 — Recommender Systems

**Topic:** From the Twin to a Recommendation — unit checkpoint

90 minutes: 45 knowledge + 45 lab · **`find_twin` → `recommend_item` → `main()` → edge cases**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-from-twin-to-recommendation-notes.md`](teacher/L03-from-twin-to-recommendation-notes.md) | Lesson plan, including the 20-point project rubric |
| Student | [`L03-from-twin-to-recommendation.md`](lessons/L03-from-twin-to-recommendation.md) | Hebrew lab brief |
| Student | [`TwinRecommend_Starter.py`](exercises/TwinRecommend_Starter.py) | Compared-to-itself warm-up bug, the project brief |
| Teacher | [`TwinRecommend_Reference.py`](teacher/solutions/TwinRecommend_Reference.py) | Solutions and a `run_edge_cases()` check |
| Teacher | [`slides-he.pdf`](lessons/L03-from-twin-to-recommendation/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lessons 22.0–22.1 — Recommender Systems

**Topic:** The Trap of Recommendations — Fact or Fake, the Cave, Three Traps, Controls

90 minutes: 45 knowledge + 45 lab · **fact or fake → who is the product → the incognito demo → the cave → three traps → a toy bubble in code**

| For | File | What it is |
|---|---|---|
| Teacher | [`L04-traps-of-recommendations-notes.md`](teacher/L04-traps-of-recommendations-notes.md) | Lesson plan, including the experiment safety rules |
| Student | [`L04-traps-of-recommendations.md`](lessons/L04-traps-of-recommendations.md) | Hebrew lab brief |
| Student | [`Bubble_Starter.py`](exercises/Bubble_Starter.py) | `!=`-counts-the-wrong-cards warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`Bubble_Reference.py`](teacher/solutions/Bubble_Reference.py) | Solutions, a deterministic toy simulation of a narrowing feed |
| Teacher | [`slides-he.pdf`](lessons/L04-traps-of-recommendations/slides-he.pdf) | **Superseded** deck of the v1 build (14 slides) — needs regeneration (NotebookLM prep folder refreshed) |
