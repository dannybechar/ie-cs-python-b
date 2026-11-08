# Unit 9 — Recommender Systems

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 20.0, 20.1, 21.1, 22.1 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). The survey scale is now **V / X / 0** (liked / disliked /
> don't know, capital English letters), the twin is the participant with the most identical non-0 answers, and the code uses only strings,
> flat lists and `def` (no tuples, default arguments, dictionaries or comprehensions). The four NotebookLM decks are **superseded** — new
> NotebookLM prep folders are ready (`unit9-m1-slides` … `unit9-m4-slides`, 20 / 19 / 18 / 19 slides). The Ministry's worksheets 20.2, 21.2, 22.2
> and teacher notes 21.0, 22.0 were not delivered; see the scope decisions.
>
> **Data note:** [`ratings.csv`](ratings.csv) is the Ministry's sample table (four participants, five foods; aliases only, no personal
> information). Students do not read files: the data are three plain lists in the starter, and the teacher helper
> [`CsvToLists_Teacher.py`](CsvToLists_Teacher.py) turns the class's Forms CSV into those lists.
> **Safety note:** Unit 9.1 involves a real class survey and Unit 9.4 a live-browsing demo — read each meeting's privacy/safety section before teaching it.

## Unit 9.1 — Recommender Systems

**Topic:** The Feed Riddle, Two Kinds of Recommender, the Culinary Twin, the Survey

90 minutes: 45 knowledge + 45 lab · **feed riddle → content-based vs user-based → culinary-twin game → V / X / 0 survey**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan, including the survey privacy rules |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`SurveyData_Starter.py`](SurveyData_Starter.py) | `else`-swallows-`"v"` warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`SurveyData_Reference.py`](SurveyData_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | **Superseded** deck of the v1 build (16 slides) — pending a new NotebookLM deck |

## Unit 9.2 — Recommender Systems

**Topic:** The Table, Similarity Points, the Twin

90 minutes: 45 knowledge + 45 lab · **the V / X / 0 table → counting points → the twin → `count_same`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Similarity_Starter.py`](Similarity_Starter.py) | `0`-and-`0`-counts warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`Similarity_Reference.py`](Similarity_Reference.py) | Solutions, one function per task |
| Data | [`ratings.csv`](ratings.csv) | The Ministry's sample table (4 participants, 5 foods), V / X / 0 |
| Teacher | [`CsvToLists_Teacher.py`](CsvToLists_Teacher.py) | Helper: Forms CSV → three lines of Python for the students to paste |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | **Superseded** deck of the v1 build (12 slides) — pending a new NotebookLM deck |

## Unit 9.3 — Recommender Systems

**Topic:** From the Twin to a Recommendation — unit checkpoint

90 minutes: 45 knowledge + 45 lab · **`find_twin` → `recommend_item` → `main()` → edge cases**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including the 20-point project rubric |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`TwinRecommend_Starter.py`](TwinRecommend_Starter.py) | Compared-to-itself warm-up bug, the project brief |
| Teacher | [`TwinRecommend_Reference.py`](TwinRecommend_Reference.py) | Solutions and a `run_edge_cases()` check |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — pending a new NotebookLM deck |

## Unit 9.4 — Recommender Systems

**Topic:** The Trap of Recommendations — Fact or Fake, the Cave, Three Traps, Controls

90 minutes: 45 knowledge + 45 lab · **fact or fake → who is the product → the incognito demo → the cave → three traps → a toy bubble in code**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including the experiment safety rules |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Bubble_Starter.py`](Bubble_Starter.py) | `!=`-counts-the-wrong-cards warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`Bubble_Reference.py`](Bubble_Reference.py) | Solutions, a deterministic toy simulation of a narrowing feed |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | **Superseded** deck of the v1 build (14 slides) — pending a new NotebookLM deck |
