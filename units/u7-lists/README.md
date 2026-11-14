# Lessons 9.1–9.5, 12.0–14.5 — Lists

Python B, Grade 8 · 10 academic hours = 5 meetings = 450 minutes (135 theory / 315 practice, official master table). 5 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Lessons 9.1, 9.4**<br>What Is a List? Creating, Indexing, Slicing<br>[md](lessons/L01-what-is-a-list.md) · [html](lessons/L01-what-is-a-list.html) · [slides PDF](lessons/L01-what-is-a-list/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 9.3, 9.5, 12.0–12.1**<br>List Operations<br>[md](lessons/L02-list-operations.md) · [html](lessons/L02-list-operations.html) · [slides PDF](lessons/L02-list-operations/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 3 | **Lessons 12.6, 13.0–13.1**<br>Walking a List (by Index and by Value) and the Accumulation Pattern<br>[md](lessons/L03-walking-a-list.md) · [html](lessons/L03-walking-a-list.html) · [slides PDF](lessons/L03-walking-a-list/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 4 | **Lessons 13.2, 14.0–14.2**<br>Counting, Filters, Maximum, Flat Menus and Parallel Lists<br>[md](lessons/L04-counting-and-filters.md) · [html](lessons/L04-counting-and-filters.html) · [slides PDF](lessons/L04-counting-and-filters/slides-he.pdf) | 0 / 90 | Built, awaiting approval |
| 5 | **Lessons 12.5, 14.4**<br>Linear Search, "A New Phone Number", and the "AI Experiment Analyzer" (Unit Checkpoint)<br>[md](lessons/L05-search-and-capstone.md) · [html](lessons/L05-search-and-capstone.html) · [slides PDF](lessons/L05-search-and-capstone/slides-he.pdf) | 0 / 90 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-what-is-a-list-notes.md`](teacher/L01-what-is-a-list-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-list-operations-notes.md`](teacher/L02-list-operations-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-walking-a-list-notes.md`](teacher/L03-walking-a-list-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L04-counting-and-filters-notes.md`](teacher/L04-counting-and-filters-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L05-search-and-capstone-notes.md`](teacher/L05-search-and-capstone-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (5 files) |

## Status and open checks

- 0 of 5 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

10 academic hours = 5 meetings = 450 minutes (135 theory / 315 practice).

> **Reconciled 9 Nov 2026 to the official Python B program** — Lists part A (files 9.1, 9.3, 9.4, 9.5 and the printable operations help sheet) was delivered
> and is now built in; parts B, C, D (12.0–14.5) as before (see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Part E (list of lists) was not delivered. The code uses `def` (the functions block (lessons 4.1–4.6) comes
> first in the schedule); no nested loops, no lists of lists, no `sort(key=...)` — each official item left out for that reason is recorded in the lesson notes
> ("Official items deliberately left out"). **Slides:** the five NotebookLM decks of the v1 build are superseded; the prep folders (`unit7-m1-slides` … `unit7-m5-slides`)
> were refreshed on 9 Nov 2026 — **all five decks need regeneration** in NotebookLM.

### Official items that exist only as links (not offline, nothing invented for them)

Titles as in the Ministry's `links.md`: **9.2** "תרגול לפיצוח | אינטראקטיבי" (genially matching game) · the **9.3** guided-exercise solution video "רשימה זוגית" ·
**12.2** "סרטון תרגול מודרך | סכום מיקום זוגי ואי זוגי" (YouTube, exam question 4 of תשפ"ה) · **12.3** "תרגול לפיצוח #1" (genially) ·
**12.4** "סרטון תרגול מודרך | הוספת מספר לרשימה" (YouTube, exam question 4 of תשפ"ה) · **13.4** "מאסטר פייתון | מסיבת ריקודים" (H5P) ·
**13.5** "מאסטר פייתון | איש תלוי" (genially) · **14.3** "תרגול לפיצוח #2" (H5P). The 12.5, 12.6, 13.2, 14.2, 14.4 worksheets and 9.4 are used as lab sources.

### Lessons 9.1, 9.4 — Lists

**Topic:** What Is a List? Creating, Indexing, Slicing

90 minutes: 45 knowledge + 45 lab · **hook (9.1) → `[]`/`list()`, mixed types → indices → update → `in`, `+` → slicing `[a:b:c]`, `[::-1]`, `[-4:-1]` → predict table (9.4 Q1–Q3)**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-what-is-a-list-notes.md`](teacher/L01-what-is-a-list-notes.md) | Lesson plan |
| Student | [`L01-what-is-a-list.md`](lessons/L01-what-is-a-list.md) | Hebrew lab brief |
| Student | [`Lists_Starter.py`](exercises/Lists_Starter.py) | `==` vs `=` warm-up bug, the 9.4 predict table, Tasks 1–4 (report, bounds-checked update, slicing, `+`) |
| Teacher | [`Lists_Reference.py`](teacher/solutions/Lists_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L01-what-is-a-list/slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

### Lessons 9.3, 9.5, 12.0–12.1 — Lists

**Topic:** List Operations

90 minutes: 45 knowledge + 45 lab · **`append`/`insert` → `count`/`in`/`index` (case, first match) → `remove`/`pop` → `sort`/`reverse` → `list(text)` → `split`/`join` → the 13-row operations table**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-list-operations-notes.md`](teacher/L02-list-operations-notes.md) | Lesson plan |
| Student | [`L02-list-operations.md`](lessons/L02-list-operations.md) | Hebrew lab brief |
| Student | [`Operations_Starter.py`](exercises/Operations_Starter.py) | `append(i)` NameError warm-up bug (the Ministry's own), Tasks 1–5 (new list, name occurrence, palindromes, the Sandwich challenge, the even list), if time: name letters, `split`/`join`/`random` |
| Teacher | [`Operations_Reference.py`](teacher/solutions/Operations_Reference.py) | Solutions, one function per task, plus the verified `demo()` and `table_demo()` (the 13 rows) |
| Teacher | [`slides-he.pdf`](lessons/L02-list-operations/slides-he.pdf) | **Superseded** deck of the v1 build (14 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

### Lessons 12.6, 13.0–13.1 — Lists

**Topic:** Walking a List and the Accumulation Pattern

90 minutes: 45 knowledge + 45 lab · **by index vs. by value (13.0, 12.6 Q4) → accumulation → average → class names and Roni's prices (13.2) → the "change while looping" trap → copies**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-walking-a-list-notes.md`](teacher/L03-walking-a-list-notes.md) | Lesson plan |
| Student | [`L03-walking-a-list.md`](lessons/L03-walking-a-list.md) | Hebrew lab brief |
| Student | [`Accumulate_Starter.py`](exercises/Accumulate_Starter.py) | `remove_even` skipping warm-up bug, Tasks 1–4 (two sums, average, duplicate class names, Roni's prices), if time: new list and sorted copy |
| Teacher | [`Accumulate_Reference.py`](teacher/solutions/Accumulate_Reference.py) | Solutions, one function per task, with the trace of the trap |
| Teacher | [`slides-he.pdf`](lessons/L03-walking-a-list/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

### Lessons 13.2, 14.0–14.2 — Lists

**Topic:** Counting, Filters, Maximum, Flat Menus, Parallel Lists

90 minutes: Lab + Lab · **counter → maximum from the data → grades, presents, names (13.2) → one flat name/price list → parallel lists → worksheet 14.2 → challenge menu (`magic`, `remove_place_num`, `avg_stud` bug hunt …) → stretch: Robber, IP, encryption**

| For | File | What it is |
|---|---|---|
| Teacher | [`L04-counting-and-filters-notes.md`](teacher/L04-counting-and-filters-notes.md) | Lesson plan |
| Student | [`L04-counting-and-filters.md`](lessons/L04-counting-and-filters.md) | Hebrew lab brief |
| Student | [`Stats_Starter.py`](exercises/Stats_Starter.py) | Max-initialized-to-0 warm-up bug, Tasks 1–6, the challenge menu (with a documented bug in `avg_stud`) and the stretch |
| Teacher | [`Stats_Reference.py`](teacher/solutions/Stats_Reference.py) | Solutions, tested on the edge cases |
| Teacher | [`slides-he.pdf`](lessons/L04-counting-and-filters/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

### Lessons 12.5, 14.4 — Lists

**Topic:** Linear Search, a New Phone Number, and the "AI Experiment Analyzer" — unit checkpoint

90 minutes: Lab + Lab · **linear search → early stop on sorted data, `index()` and the 14.4 Q10 ranking → phone numbers with `random` → the capstone project → exam-bank question**

| For | File | What it is |
|---|---|---|
| Teacher | [`L05-search-and-capstone-notes.md`](teacher/L05-search-and-capstone-notes.md) | Lesson plan |
| Student | [`L05-search-and-capstone.md`](lessons/L05-search-and-capstone.md) | Hebrew lab brief |
| Student | [`Analyzer_Starter.py`](exercises/Analyzer_Starter.py) | Index-0-as-`False` warm-up bug, early-stop search and `position_in_ranking`, the phone-number task, the project brief, the 14.4 exam-bank choices |
| Teacher | [`Analyzer_Reference.py`](teacher/solutions/Analyzer_Reference.py) | Solutions; all 7 test cases verified |
| Teacher | [`slides-he.pdf`](lessons/L05-search-and-capstone/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |
