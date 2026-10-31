# Grade 8 course map — AI + Python B

Official numbering and hours from [`docs/ministry-source/python-b-ai.pdf`](docs/ministry-source/python-b-ai.pdf)
(master syllabus table, pp. 3–4; one chapter per unit, pp. 5–23). Full framing strategy, provisional meeting outline and
depth boundaries: [`docs/annual-strategy.md`](docs/annual-strategy.md).

> **Hours rule (teacher's decision):** theory/practice hours come from the master table. The chapter tables of Units 1, 3,
> 5 and 7 give a different split (1: 2 / 4, 3: 1 / 5, 5: 3 / 5, 7: 4 / 6); they are used only for the order and weight of topics.

## Time budget

1 academic hour = 45 minutes, so the course is 60 hours = **2,700 minutes** = 30 double meetings of 90 minutes.
Minutes are written as **total (theory / practice)**. "Planned" counts only meetings that are built in the repo.

Status: ✅ built and approved by the teacher · 🔶 built, awaiting teacher approval (lesson notes, brief, code and slides all done) ·
⚠️ partly built (lesson notes, brief and code done for every meeting; slides not yet prepared) · ❌ / ⏳ not built yet.

| # | Unit | Official hours (T/P) | Official minutes (T/P) | Meetings | Planned minutes (T/P) | Remaining | Built |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | [Python A Review](units/u1-python-a-review) | 6 (1 / 5) | 270 (45 / 225) | 3 | 270 (45 / 225) | 0 | ✅ 2/3 · 🔶 1/3 (1.3 reworked) |
| 2 | [AI2 Year Opening](units/u2-ai2-year-opening) | 4 (2 / 2) | 180 (90 / 90) | 2 | 180 (90 / 90) | 0 | 🔶 2/2 (reworked) |
| 3 | [Functions](units/u3-functions) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | 🔶 3/3 (reworked) |
| 4 | [Bringing AI into Code (API)](units/u4-api) | 4 (1 / 3) | 180 (45 / 135) | 2 | 180 (45 / 135) | 0 | 🔶 2/2 (reworked) |
| 5 | [Strings](units/u5-strings) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (90 / 270) | 0 | 🔶 4/4 (reworked) |
| 6 | [Advanced Language Model](units/u6-advanced-language-model) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | ✅ 3/3 |
| 7 | [Lists](units/u7-lists) | 10 (3 / 7) | 450 (135 / 315) | 5 | 450 (135 / 315) | 0 | ✅ 5/5 |
| 8 | [Classification](units/u8-classification) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | ✅ 4/4 |
| 9 | [Recommender Systems](units/u9-recommender-systems) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | ✅ 4/4 |
|  | **TOTAL** | **60 (21 / 39)** | **2,700 (945 / 1,755)** | **30** | **2,700 (945 / 1,755)** | **0** | **30/30 built; 12 meetings reworked to the Ministry materials (🔶 awaiting re-approval), 18 approved (✅)** |

A unit has one Knowledge + Lab meeting (45 / 45) per theory hour; its other meetings are Lab + Lab (0 / 90).
Unit folders (`units/u<N>-<slug>/`) are created when a unit is built; see `CLAUDE.md` for the slugs.

## Deadline and pace

- **Assessment:** the Ministry exam (בחינת מפמ"ר) for "בינה מלאכותית בשילוב מדעי המחשב חלק ב'", set for **May 2027**
  ([`ministry-circular-tashpaz-he.pdf`](docs/ministry-source/ministry-circular-tashpaz-he.pdf), p. 2; the exact date is
  published during the year). Printed notes are allowed; calculators are not (p. 3).
- **Meetings needed:** 30 (plus any school-added meeting, as Python A's Unit 0).
- **Meetings available:** *to confirm with the teacher* — the weekly meeting day and the first meeting date.
- **Check after every lesson:** meetings left in the schedule below ≤ meetings left before the exam.

## Open coverage gaps

- **Source of truth (31 Oct 2026):** the Ministry's published teaching materials
  ([`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md)). Units 1.3, 2, 3, 4 and 5 were reworked to
  match them (🔶, awaiting re-approval; new NotebookLM decks pending — the old patched decks are marked superseded).
- **Units 6–9:** built from the Ministry program text and the teacher's own sources; the matching Ministry decks have not
  arrived yet. When they do, compare and rework the same way.
- **Unit 7 notes** need a small update because `split`/`join` now appear first in 5.4.
- Every official topic is covered (see each unit's `unit-strategy.md`). The tool choices flagged during planning were
  settled during each unit's build; the live-service steps are in each unit's README (Unit 4 now uses Gemini).

## Schedule

All meetings in teaching order. **Content** is the provisional outline from the annual strategy; it is refined when the unit
is built. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson.

| # | Meeting | Content | Built | Target week | Taught on |
|---:|---|---|---|---|---|
| 1 | 1.1 Python A Review | K+L · Who can come in? Compound conditions, `elif`, validation | ✅ | | |
| 2 | 1.2 Python A Review | L+L · Counting rounds: `range`, counter and total, five-scores analyzer | ✅ | | |
| 3 | 1.3 Python A Review | L+L · Until it's done: `while`, the stop condition, loops that never end; unit checkpoint (Ministry 2.0, 2.1, loop-trap deck) | 🔶 | | |
| 4 | 2.1 AI2 Year Opening | K+L · AI or not? Definition, revolutions, classic vs AI greeting (Ministry deck 3.1) | 🔶 | | |
| 5 | 2.2 AI2 Year Opening | K+L · Quick, Draw!, data and bias worksheet (Ministry 3.2), consumers to creators | 🔶 | | |
| 6 | 3.1 Functions | K+L · Several parameters and `return` (Ministry 4.1, 4.2) | 🔶 | | |
| 7 | 3.2 Functions | L+L · Practice: returning functions and loops inside functions (Ministry 4.2, 4.4, 4.5) | 🔶 | | |
| 8 | 3.3 Functions | K+L · Local and `global` variables, variable roles; checkpoint (Ministry 4.3, 4.5, 4.6) | 🔶 | | |
| 9 | 4.1 Bringing AI into Code (API) | K+L · What is an API, the Gemini call, f-strings, the `ask_the_ai` wrapper (Ministry 5.0–5.2) | 🔶 | | |
| 10 | 4.2 Bringing AI into Code (API) | L+L · The "יום מאוזן" project: `while` accumulation, one API call (Ministry 6.1, 6.2) | 🔶 | | |
| 11 | 5.1 Strings | K+L · A string as an ordered sequence: quotes, indices, `len`, `+`/`*` (Ministry 7.1, 7.2) | 🔶 | | |
| 12 | 5.2 Strings | K+L · Slicing `[start:end:jump]`, `count`, `replace`, `in`, `find` (Ministry 7.1, 7.2) | 🔶 | | |
| 13 | 5.3 Strings | L+L · More string methods and `for` over a string (Ministry 8.0, 8.1) | 🔶 | | |
| 14 | 5.4 Strings | L+L · String algorithms, `ord`/`chr` cipher, `split`/`join`; checkpoint (Ministry 8.1, 8.2, 8.7) | 🔶 | | |
| 15 | 6.1 Advanced Language Model | K+L · Tokens, tokenization and token IDs | ✅ | | |
| 16 | 6.2 Advanced Language Model | K+L · The context window, the meaning map, self-attention | ✅ | | |
| 17 | 6.3 Advanced Language Model | L+L · Semantic similarity + the "Semantle" checkpoint | ✅ | | |
| 18 | 7.1 Lists | K+L · What a list is: indices, traversal | ✅ | | |
| 19 | 7.2 Lists | K+L · List operations: append/extend/insert, remove/pop, sort/reverse, split/join | ✅ | | |
| 20 | 7.3 Lists | K+L · Advanced operations + the accumulation pattern | ✅ | | |
| 21 | 7.4 Lists | L+L · Counting, minimum, maximum, a report | ✅ | | |
| 22 | 7.5 Lists | L+L · Linear search + the "AI Experiment Analyzer" checkpoint | ✅ | | |
| 23 | 8.1 Classification | K+L · Classification, features, a decision boundary | ✅ | | |
| 24 | 8.2 Classification | K+L · The ML process + Teachable Machine | ✅ | | |
| 25 | 8.3 Classification | K+L · Project planning, data, bias | ✅ | | |
| 26 | 8.4 Classification | K+L · Accuracy, export, loading the model — checkpoint | ✅ | | |
| 27 | 9.1 Recommender Systems | K+L · What is a recommender system? + data collection | ✅ | | |
| 28 | 9.2 Recommender Systems | K+L · From CSV to a similarity score | ✅ | | |
| 29 | 9.3 Recommender Systems | K+L · From digital twin to recommendation — checkpoint | ✅ | | |
| 30 | 9.4 Recommender Systems | K+L · Filter bubbles, echo chambers, the attention economy | ✅ | | |

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Unit | Meeting | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 1 | 1.1 Python A Review | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u1-python-a-review/m1-lesson-notes.md) | From the codex deck + the raw 1.1; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 1 | 1.2 Python A Review | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u1-python-a-review/m2-lesson-notes.md) | From the codex deck + the raw 1.2; slides: `m2-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 1 | 1.3 Python A Review | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u1-python-a-review/m3-lesson-notes.md) | Reworked to Ministry 2.0, 2.1 and the loop-trap deck; unit checkpoint (`cubes_sum`); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 2 | 2.1 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u2-ai2-year-opening/m1-lesson-notes.md) | Reworked to Ministry deck 3.1; classic Python greeting vs an AI greeting; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 2 | 2.2 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u2-ai2-year-opening/m2-lesson-notes.md) | Reworked to Ministry deck 3.1 and worksheet 3.2 (Quick, Draw!, data, bias); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 3 | 3.1 Functions | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u3-functions/m1-lesson-notes.md) | Reworked to Ministry 4.1, 4.2; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 3 | 3.2 Functions | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u3-functions/m2-lesson-notes.md) | Reworked to Ministry 4.2, 4.4, 4.5; slides: superseded — pending new NotebookLM deck (prep folder ready, 16 slides, 90 min). |
| 3 | 3.3 Functions | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u3-functions/m3-lesson-notes.md) | Reworked to Ministry 4.3, 4.5, 4.6; `global` is taught; unit checkpoint; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 4 | 4.1 Bringing AI into Code (API) | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u4-api/m1-lesson-notes.md) | Reworked to Ministry 5.0–5.2 (Gemini); classroom stand-in `ask_the_ai()`; needs a live run with a real key; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 4 | 4.2 Bringing AI into Code (API) | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u4-api/m2-lesson-notes.md) | Reworked to Ministry 6.1, 6.2 ("Balanced Day"); unit checkpoint; stand-in for verification; slides: superseded — pending new NotebookLM deck (prep folder ready, 17 slides, 90 min). |
| 5 | 5.1 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u5-strings/m1-lesson-notes.md) | Reworked to Ministry 7.1, 7.2; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 5 | 5.2 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u5-strings/m2-lesson-notes.md) | Reworked to Ministry 7.1, 7.2; now Knowledge + Lab (official 90 / 270 split); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 5 | 5.3 Strings | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u5-strings/m3-lesson-notes.md) | Reworked to Ministry 8.0, 8.1; paper-classwork edition (45-min lesson + worksheet, [plan](units/u5-strings/m3-classwork-lesson-plan.md)) prepared 31 Oct 2026; slides: superseded — pending new NotebookLM deck (prep folder ready, 16 slides, 90 min). |
| 5 | 5.4 Strings | 90 | 0 / 90 | Lab + Lab | [`m4-lesson-notes.md`](units/u5-strings/m4-lesson-notes.md) | Reworked to Ministry 8.1, 8.2, 8.7; unit checkpoint; slides: superseded — pending new NotebookLM deck (prep folder ready, 18 slides, 90 min). |
| 6 | 6.1 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u6-advanced-language-model/m1-lesson-notes.md) | Slides: `m1-slides-he.pdf` (15 slides, 90 min; NotebookLM, patched) |
| 6 | 6.2 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u6-advanced-language-model/m2-lesson-notes.md) | Slides: `m2-slides-he.pdf` (15 slides, 90 min; NotebookLM, patched) |
| 6 | 6.3 Advanced Language Model | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u6-advanced-language-model/m3-lesson-notes.md) | Unit checkpoint ("Semantle"); classroom-mode similarity function (no model download needed); slides: `m3-slides-he.pdf` (11 slides, 90 min; NotebookLM, patched) |
| 7 | 7.1 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u7-lists/m1-lesson-notes.md) | Slides: `m1-slides-he.pdf` (15 slides, 90 min; NotebookLM, patched). |
| 7 | 7.2 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u7-lists/m2-lesson-notes.md) | Slides: `m2-slides-he.pdf` (14 slides, 90 min; NotebookLM, patched). |
| 7 | 7.3 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u7-lists/m3-lesson-notes.md) | Slides: `m3-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 7 | 7.4 Lists | 90 | 0 / 90 | Lab + Lab | [`m4-lesson-notes.md`](units/u7-lists/m4-lesson-notes.md) | Slides: `m4-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 7 | 7.5 Lists | 90 | 0 / 90 | Lab + Lab | [`m5-lesson-notes.md`](units/u7-lists/m5-lesson-notes.md) | Unit checkpoint ("AI Experiment Analyzer"); slides: `m5-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 8 | 8.1 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u8-classification/m1-lesson-notes.md) | Slides: `m1-slides-he.pdf` (15 slides, 90 min; NotebookLM, patched). |
| 8 | 8.2 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u8-classification/m2-lesson-notes.md) | Slides: `m2-slides-he.pdf` (12 slides, 90 min; NotebookLM, patched). |
| 8 | 8.3 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u8-classification/m3-lesson-notes.md) | Real photography (hands only; full privacy/consent rules in the lesson notes); slides: `m3-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 8 | 8.4 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m4-lesson-notes.md`](units/u8-classification/m4-lesson-notes.md) | Unit checkpoint; classroom-mode `classify_image()`; slides: `m4-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 9 | 9.1 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u9-recommender-systems/m1-lesson-notes.md) | Real class survey (full privacy rules in the lesson notes); slides: `m1-slides-he.pdf` (16 slides, 90 min; NotebookLM, patched). |
| 9 | 9.2 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u9-recommender-systems/m2-lesson-notes.md) | Real `ratings.csv` sample data (no mock needed); slides: `m2-slides-he.pdf` (12 slides, 90 min; NotebookLM, patched). |
| 9 | 9.3 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u9-recommender-systems/m3-lesson-notes.md) | Unit checkpoint; slides: `m3-slides-he.pdf` (13 slides, 90 min; NotebookLM, patched). |
| 9 | 9.4 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m4-lesson-notes.md`](units/u9-recommender-systems/m4-lesson-notes.md) | Live-browsing option with its own safety rules (offline card-simulation fallback); slides: `m4-slides-he.pdf` (14 slides, 90 min; NotebookLM, patched). |

## Assessments

Written tests made outside the 30-meeting plan (they do not change the time budget).

| Unit | Test | Length | Status | Files |
|---|---|---:|---|---|
| 1 | Python A Review — Grade 9 test | 60 min, 100 points | ✅ given 18/24 Oct 2026, graded (mean 77.1, median 80.75); Q5b wording and Q6b answer space fixed in Form B — see the key | [`unit-1-test-he.md`](units/u1-python-a-review/unit-1-test-he.md), [key](units/u1-python-a-review/unit-1-test-answer-key.md), [`Test_Reference.py`](units/u1-python-a-review/Test_Reference.py) |
| 1 | Python A Review — Form B (retest, 2 students) | 60 min, 100 points | 🔶 prepared 29 Oct 2026; mirrors Form A, Q5b/Q6b wording fixed; Word copies in `Downloads\python-b` | [`unit-1-test-form-b-he.md`](units/u1-python-a-review/unit-1-test-form-b-he.md), [key](units/u1-python-a-review/unit-1-test-form-b-answer-key.md), [`Test_B_Reference.py`](units/u1-python-a-review/Test_B_Reference.py) |

## Keeping this up to date

When a meeting is added or its timing changes:
1. Add or update its row in the **Meeting log**, and mark it 🔶 in the **Schedule** (✅ only after the teacher approves it).
2. Update that unit's **Planned minutes**, **Remaining** and **Built** in the time budget, and the totals.
3. A unit's planned minutes must not exceed its official minutes. If they would, cut the lesson or
   note the overrun in the unit row with the reason.
4. Update the status of the topics it covers in the unit's `unit-strategy.md` ("Official topics and hours"),
   and remove any gap it closes from **Open coverage gaps**.

After each lesson is taught:
1. Fill in **Taught on** in the **Schedule**.
2. Recheck **Deadline and pace**: meetings left in the schedule must not exceed meetings left before the exam.
