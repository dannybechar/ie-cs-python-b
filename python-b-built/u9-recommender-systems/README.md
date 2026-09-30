# Unit 9 — Recommender Systems

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Staging note:** built in `python-b-built/`, not `units/` — see [`../README.md`](../README.md).
> **Data note:** [`ratings.csv`](ratings.csv) is real sample data (synthetic aliases, no personal information),
> genuinely read from disk by 9.2–9.3's code — unlike Units 4/6/8, no mock is needed here.
> **Safety note:** Unit 9.1 involves a real class survey and Unit 9.4 a live-browsing option — read each meeting's
> privacy/safety section before teaching it.

## Unit 9.1 — Recommender Systems

**Topic:** What Is a Recommender System? + Data Collection

90 minutes: 45 knowledge + 45 lab · **content-based vs user-based → the rating scale → survey design**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan, including full survey privacy rules |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`SurveyData_Starter.py`](SurveyData_Starter.py) | Inverted-rating-meaning warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`SurveyData_Reference.py`](SurveyData_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Hebrew slide deck (16 slides, NotebookLM, patched) |

## Unit 9.2 — Recommender Systems

**Topic:** From CSV to a Similarity Score

90 minutes: 45 knowledge + 45 lab · **load_ratings → the shared-rating rule → similarity_score → similarity_rate**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Similarity_Starter.py`](Similarity_Starter.py) | `0 == 0`-counts-as-a-match warm-up bug, stubs for Tasks 1–3 |
| Teacher | [`Similarity_Reference.py`](Similarity_Reference.py) | Solutions, verified against all 4 official asserts |
| Data | [`ratings.csv`](ratings.csv) | Sample rating data (3 users, 4 items), read for real |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Hebrew slide deck (12 slides, NotebookLM, patched) |

## Unit 9.3 — Recommender Systems

**Topic:** From Digital Twin to Recommendation — unit checkpoint

90 minutes: 45 knowledge + 45 lab · **find_digital_twin → recommend_item → main() → the full pipeline**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including the project rubric |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`TwinRecommend_Starter.py`](TwinRecommend_Starter.py) | Compared-to-itself warm-up bug, the project brief |
| Teacher | [`TwinRecommend_Reference.py`](TwinRecommend_Reference.py) | Solutions, all 7 official test cases verified |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Hebrew slide deck (13 slides, NotebookLM, patched) |

## Unit 9.4 — Recommender Systems

**Topic:** Filter Bubbles, Echo Chambers, the Attention Economy

90 minutes: 45 knowledge + 45 lab · **a controlled experiment → filter bubble vs echo chamber → feed-control toolkit**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including full experiment safety rules |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Bubble_Starter.py`](Bubble_Starter.py) | Inverted-count warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`Bubble_Reference.py`](Bubble_Reference.py) | Solutions, a deterministic simulation of the card experiment |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | Hebrew slide deck (14 slides, NotebookLM, patched) |
