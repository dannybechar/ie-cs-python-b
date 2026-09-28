# Grade 8 course map — AI + Python B

Official numbering and hours from [`docs/ministry-source/python-b-ai.pdf`](docs/ministry-source/python-b-ai.pdf)
(master syllabus table, pp. 3–4; one chapter per unit, pp. 5–23). Full framing strategy, provisional meeting outline and
depth boundaries: [`docs/annual-strategy.md`](docs/annual-strategy.md).

> **Hours rule (teacher's decision):** theory/practice hours come from the master table. The chapter tables of Units 1, 3,
> 5 and 7 give a different split (1: 2 / 4, 3: 1 / 5, 5: 3 / 5, 7: 4 / 6); they are used only for the order and weight of topics.

## Time budget

1 academic hour = 45 minutes, so the course is 60 hours = **2,700 minutes** = 30 double meetings of 90 minutes.
Minutes are written as **total (theory / practice)**. "Planned" counts only meetings that are built in the repo.

Status: ✅ built and approved by the teacher · 🔶 built, awaiting teacher approval · ⚠️ partly built · ❌ / ⏳ not built yet.

| # | Unit | Official hours (T/P) | Official minutes (T/P) | Meetings | Planned minutes (T/P) | Remaining | Built |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | [Python A Review](units/u1-python-a-review) | 6 (1 / 5) | 270 (45 / 225) | 3 | 270 (45 / 225) | 0 | ✅ 3/3 |
| 2 | [AI2 Year Opening](units/u2-ai2-year-opening) | 4 (2 / 2) | 180 (90 / 90) | 2 | 180 (90 / 90) | 0 | 🔶 2/2 |
| 3 | Functions | 6 (2 / 4) | 270 (90 / 180) | 3 | 0 | 270 | ❌ 0/3 |
| 4 | Bringing AI into Code (API) | 4 (1 / 3) | 180 (45 / 135) | 2 | 0 | 180 | ❌ 0/2 |
| 5 | Strings | 8 (2 / 6) | 360 (90 / 270) | 4 | 0 | 360 | ❌ 0/4 |
| 6 | Advanced Language Model | 6 (2 / 4) | 270 (90 / 180) | 3 | 0 | 270 | ❌ 0/3 |
| 7 | Lists | 10 (3 / 7) | 450 (135 / 315) | 5 | 0 | 450 | ❌ 0/5 |
| 8 | Classification | 8 (4 / 4) | 360 (180 / 180) | 4 | 0 | 360 | ❌ 0/4 |
| 9 | Recommender Systems | 8 (4 / 4) | 360 (180 / 180) | 4 | 0 | 360 | ❌ 0/4 |
|  | **TOTAL** | **60 (21 / 39)** | **2,700 (945 / 1,755)** | **30** | **450 (135 / 315)** | **2,250** | **5/30 meetings built** |

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

Official topics that no planned meeting fully covers yet. Details are in each unit's `unit-strategy.md`, under "Official topics and hours".

| Unit | Gap | Fix to plan |
|---|---|---|
| 3–9 | Nothing built yet | Build unit by unit |
| 4, 6, 8, 9 | Tools not chosen: the language-model API and key (4), the embedding library (6), the model-loading library (8), the survey and CSV (9) | Settle with the teacher before building each unit ([annual strategy §8](docs/annual-strategy.md#8-tools-and-safety-to-settle-before-the-unit-is-built)) |

## Schedule

All meetings in teaching order. **Content** is the provisional outline from the annual strategy; it is refined when the unit
is built. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson.

| # | Meeting | Content | Built | Target week | Taught on |
|---:|---|---|---|---|---|
| 1 | 1.1 Python A Review | K+L · Who can come in? Compound conditions, `elif`, validation | ✅ | | |
| 2 | 1.2 Python A Review | L+L · Counting rounds: `range`, counter and total, five-scores analyzer | ✅ | | |
| 3 | 1.3 Python A Review | L+L · Until it's done: `while`, three-try locker; unit checkpoint | ✅ | | |
| 4 | 2.1 AI2 Year Opening | K+L · Rules or learning? Kettle rule, Quick, Draw!, dataset detectives | 🔶 | | |
| 5 | 2.2 AI2 Year Opening | K+L · Data, bias and responsibility; dataset audit; from consumers to creators | 🔶 | | |
| 6 | 3.1 Functions | K+L · Functions without `return` (review); the black box | ❌ | | |
| 7 | 3.2 Functions | K+L · `return`; `print` vs `return`; local and global | ❌ | | |
| 8 | 3.3 Functions | L+L · Bottom-up design with returning functions | ❌ | | |
| 9 | 4.1 Bringing AI into Code (API) | K+L · API, safe key, wrapper function | ❌ | | |
| 10 | 4.2 Bringing AI into Code (API) | L+L · Dynamic prompts, collecting loop, "יום מאוזן" mini-project | ❌ | | |
| 11 | 5.1 Strings | K+L · Operators, indexing, `len`, `in` | ❌ | | |
| 12 | 5.2 Strings | K+L · String methods and validation | ❌ | | |
| 13 | 5.3 Strings | L+L · Slicing | ❌ | | |
| 14 | 5.4 Strings | L+L · Traversal; text-processing program | ❌ | | |
| 15 | 6.1 Advanced Language Model | K+L · Tokens and the context window | ❌ | | |
| 16 | 6.2 Advanced Language Model | K+L · Semantic map and self-attention | ❌ | | |
| 17 | 6.3 Advanced Language Model | L+L · The Semantle game | ❌ | | |
| 18 | 7.1 Lists | K+L · What a list is; access and update | ❌ | | |
| 19 | 7.2 Lists | K+L · List operations; `split` / `join` | ❌ | | |
| 20 | 7.3 Lists | K+L · The summation pattern | ❌ | | |
| 21 | 7.4 Lists | L+L · The sequential-search pattern | ❌ | | |
| 22 | 7.5 Lists | L+L · Integrated list problem | ❌ | | |
| 23 | 8.1 Classification | K+L · Features, decision boundary, rule-based classifier | ❌ | | |
| 24 | 8.2 Classification | K+L · Training vs test; Teachable Machine | ❌ | | |
| 25 | 8.3 Classification | K+L · Planned data collection (fist vs OK) | ❌ | | |
| 26 | 8.4 Classification | K+L · Accuracy; loading the model in Python | ❌ | | |
| 27 | 9.1 Recommender Systems | K+L · Content- vs user-based; the survey | ❌ | | |
| 28 | 9.2 Recommender Systems | K+L · Similarity score | ❌ | | |
| 29 | 9.3 Recommender Systems | K+L · The digital twin and the recommendation | ❌ | | |
| 30 | 9.4 Recommender Systems | K+L · Filter bubbles and the attention economy | ❌ | | |

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Unit | Meeting | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 1 | 1.1 Python A Review | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u1-python-a-review/m1-lesson-notes.md) | From the codex deck + the raw 1.1; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 1 | 1.2 Python A Review | 90 | 0 / 90 | Lab + Lab | [`m2-lesson-notes.md`](units/u1-python-a-review/m2-lesson-notes.md) | From the codex deck + the raw 1.2; slides: `m2-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 1 | 1.3 Python A Review | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u1-python-a-review/m3-lesson-notes.md) | Unit diagnostic checkpoint; from the codex deck + the raw 1.3; slides: `m3-slides-he.pdf` (16 slides, 90 min; NotebookLM, patched) |
| 2 | 2.1 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u2-ai2-year-opening/m1-lesson-notes.md) | From the codex deck + the raw 2.1; needs Quick, Draw! (web); slides pending (NotebookLM) |
| 2 | 2.2 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u2-ai2-year-opening/m2-lesson-notes.md) | From the codex deck + the raw 2.2; slides pending (NotebookLM) |

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
