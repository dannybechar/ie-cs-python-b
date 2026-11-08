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
| 5 | [Strings](units/u5-strings) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (135 / 225) | 0 | 🔶 4/4 (reworked); 5.3 taught as 45 / 45 (teacher's decision) — 45 more theory, 45 less practice than official |
| 6 | [Advanced Language Model](units/u6-advanced-language-model) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | 🔶 3/3 (reworked 8 Nov 2026 to Ministry 10–11) |
| 7 | [Lists](units/u7-lists) | 10 (3 / 7) | 450 (135 / 315) | 5 | 450 (135 / 315) | 0 | 🔶 5/5 (reworked 8 Nov 2026 to Ministry 12–14) |
| 8 | [Classification](units/u8-classification) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | 🔶 4/4 (reworked 8 Nov 2026 to Ministry 16–19) |
| 9 | [Recommender Systems](units/u9-recommender-systems) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | 🔶 4/4 (reworked 8 Nov 2026 to Ministry 20–22) |
|  | **TOTAL** | **60 (21 / 39)** | **2,700 (945 / 1,755)** | **30** | **2,700 (990 / 1,710)** | **0** | **30/30 built; 28 meetings reworked to the Ministry materials (🔶 awaiting re-approval), 2 approved (✅: 1.1, 1.2)** |

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

- **Teaching order differs from the schedule (teacher, 2 Nov 2026):** Unit 5 (strings) is being taught **before Unit 3
  (functions)** — the class has not learned `def` yet. The 5.4 countdown edition is written without functions. All Unit 5 lab
  versions (5.1–5.4) were converted to plain code the same day (a variable, the code, `print`). Only the 5.3 classwork
  worksheet (already taught) still asks for functions; its rubric gives plain code full marks. Revisit the Unit 5 "function
  that takes a string" goal (goal 9) after Unit 3. **The NotebookLM prep folders for 5.1–5.4 (on the Windows machine) were
  made before this change** — regenerate their slide content before building the new decks. Units 2–4 were skipped for now (6 Nov 2026, see
  [`class-progress.md`](class-progress.md)).
- **Source of truth (31 Oct 2026):** the Ministry's published teaching materials
  ([`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md)). Units 1.3, 2, 3, 4 and 5 were reworked to
  match them (🔶, awaiting re-approval; new NotebookLM decks pending — the old patched decks are marked superseded).
- **Ministry lessons 10–22 arrived 8 Nov 2026**, were audited (see [`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md),
  "Audit of lessons 10–22") and **Units 6, 7, 8 and 9 were all reworked the same day (🔶; new NotebookLM prep folders ready, decks pending)**.
  Still open: Lists parts A and E and many worksheets and keys were not delivered (the reworks assume nothing the Ministry did not show);
  defaults chosen without the teacher (change if wrong): `def` allowed in Units 6–9 (they follow Unit 3 in the schedule); no nested loops and no lists
  of lists in Unit 7; Unit 9 keeps 4 meetings (the Ministry has 3). Live runs needed before class: Unit 8.4 (TensorFlow + a real exported model),
  Unit 9.1 (Google Forms export) and 9.4 (incognito demo), the Unit 6 model download.
- **Unit 7 notes** need a small update *if* the 90-minute lab version of 5.4 is taught (it shows `split`/`join` first). The
  countdown edition of 5.4 leaves `split`/`join` to Unit 7.2, so no change is needed if that edition is taught.
- Every official topic is covered (see each unit's `unit-strategy.md`). The tool choices flagged during planning were
  settled during each unit's build; the live-service steps are in each unit's README (Unit 4 now uses Gemini).

## Waiting for the teacher (as of 2 Nov 2026)

- Dates 5.1–5.3 were taught, the weekly meeting day and the first meeting date (for the pace check).
- When Units 2–4 will be taught (skipped so far, 6 Nov 2026; Unit 4 uses functions, so it must follow Unit 3) — see [`class-progress.md`](class-progress.md).
- Re-approval of the 12 reworked meetings (1.3, 2.1–2.2, 3.1–3.3, 4.1–4.2, 5.1–5.4) and their new NotebookLM decks.
- 5.2 and 5.3 lesson + lab packages (built 6 Nov 2026 with the 5.1 recipe): confirm the themes, that 5.3 uses `find`/slicing/`count` from 5.2 in stage 6 and the lab, and that 5.2 leaves `lower`/`upper` to 5.3.
- 5.1 live lesson: it brings `for … in range(len(name))` and `while` into 5.1 (the unit plan teaches the `for` loop over strings in 5.3–5.4) — confirm that is wanted, and whether the deck stays at 54 minutes.
- 5.4 countdown: which loop per case is shown first, whether the worksheet is collected at the end of class, whether a deck is wanted.
- Thonny's comment shortcut (Ctrl+3, written in `Cipher_Starter.py`) — confirm.
- After grading: 5.3 classwork and 5.4 worksheet aggregates (in their keys); Form B results after 11 Nov 2026.

## Schedule

All meetings in teaching order. **Content** is the provisional outline from the annual strategy; it is refined when the unit
is built. Fill in **Target week** once the school calendar is known, and **Taught on** after each lesson. What the class has actually completed is tracked in [`class-progress.md`](class-progress.md).

| # | Meeting | Content | Built | Target week | Taught on |
|---:|---|---|---|---|---|
| 1 | 1.1 Python A Review | K+L · Who can come in? Compound conditions, `elif`, validation | ✅ | | ✅ |
| 2 | 1.2 Python A Review | L+L · Counting rounds: `range`, counter and total, five-scores analyzer | ✅ | | ✅ |
| 3 | 1.3 Python A Review | L+L · Until it's done: `while`, the stop condition, loops that never end; unit checkpoint (Ministry 2.0, 2.1, loop-trap deck) | 🔶 | | ✅ |
| 4 | 2.1 AI2 Year Opening | K+L · AI or not? Definition, revolutions, classic vs AI greeting (Ministry deck 3.1) | 🔶 | | ⏭ skipped for now |
| 5 | 2.2 AI2 Year Opening | K+L · Quick, Draw!, data and bias worksheet (Ministry 3.2), consumers to creators | 🔶 | | ⏭ skipped for now |
| 6 | 3.1 Functions | K+L · Several parameters and `return` (Ministry 4.1, 4.2) | 🔶 | | ⏭ skipped for now |
| 7 | 3.2 Functions | L+L · Practice: returning functions and loops inside functions (Ministry 4.2, 4.4, 4.5) | 🔶 | | ⏭ skipped for now |
| 8 | 3.3 Functions | K+L · Local and `global` variables, variable roles; checkpoint (Ministry 4.3, 4.5, 4.6) | 🔶 | | ⏭ skipped for now |
| 9 | 4.1 Bringing AI into Code (API) | K+L · What is an API, the Gemini call, f-strings, the `ask_the_ai` wrapper (Ministry 5.0–5.2) | 🔶 | | ⏭ skipped for now |
| 10 | 4.2 Bringing AI into Code (API) | L+L · The "יום מאוזן" project: `while` accumulation, one API call (Ministry 6.1, 6.2) | 🔶 | | ⏭ skipped for now |
| 11 | 5.1 Strings | K+L · A string as an ordered sequence: quotes, indices, `len`, `+`/`*` (Ministry 7.1, 7.2) | 🔶 | | ✅ (date to confirm) |
| 12 | 5.2 Strings | K+L · Slicing `[start:end:jump]`, `count`, `replace`, `in`, `find` (Ministry 7.1, 7.2) | 🔶 | | ✅ (date to confirm) |
| 13 | 5.3 Strings | K+L · More string methods and `for` over a string (Ministry 8.0, 8.1) | 🔶 | | ✅ paper-classwork edition, 45 / 45 (date to confirm) |
| 14 | 5.4 Strings | L+L · String algorithms, `ord`/`chr` cipher, `split`/`join`; checkpoint (Ministry 8.1, 8.2, 8.7) | 🔶 | | ▶ next |
| 15 | 6.1 Advanced Language Model | K+L · Tokens, tokenization and token IDs (Ministry 10.0–10.2) | 🔶 | | |
| 16 | 6.2 Advanced Language Model | K+L · The meaning map, self-attention, context window, `calculate_similarity` (Ministry 11.1, 11.2) | 🔶 | | |
| 17 | 6.3 Advanced Language Model | L+L · The "Semantle" project, unit checkpoint (Ministry 11.3) | 🔶 | | |
| 18 | 7.1 Lists | K+L · Lists: `[]`, `list()`, indices, `in`, `+`, slicing (Ministry 12.0, 12.1) | 🔶 | | |
| 19 | 7.2 Lists | K+L · List methods, `split`/`join`, `random.choice`, building new lists (Ministry 12.0–12.7) | 🔶 | | |
| 20 | 7.3 Lists | K+L · Traversal by index vs value, accumulation, average, the change-while-looping trap (Ministry 13.0, 13.1) | 🔶 | | |
| 21 | 7.4 Lists | L+L · Counters, maximum, filters, the flat name/price menu, parallel lists (Ministry 13.1, 14.0, 14.1) | 🔶 | | |
| 22 | 7.5 Lists | L+L · Linear search, `index()`, phone numbers + the "AI Experiment Analyzer" checkpoint | 🔶 | | |
| 23 | 8.1 Classification | K+L · Rule-based classification, features, the separating line (Ministry 16.0–16.2.0) | 🔶 | | |
| 24 | 8.2 Classification | K+L · Training vs test, bias, the first Teachable Machine try (Ministry 17.0–17.1) | 🔶 | | |
| 25 | 8.3 Classification | K+L · Accuracy, the fist/OK project, saving the model (Ministry 18.0, 18.1) | 🔶 | | |
| 26 | 8.4 Classification | K+L · The trained model in Python, confidence, "act only above 85%" — checkpoint (Ministry 19.0, 19.1) | 🔶 | | |
| 27 | 9.1 Recommender Systems | K+L · The feed riddle, content-based vs user-based, the culinary twin, the V/X/0 survey (Ministry 20.0, 20.1) | 🔶 | | |
| 28 | 9.2 Recommender Systems | K+L · The table, similarity points, the twin (Ministry 21.1) | 🔶 | | |
| 29 | 9.3 Recommender Systems | K+L · `find_twin`, `recommend_item` — checkpoint (Ministry 21.1) | 🔶 | | |
| 30 | 9.4 Recommender Systems | K+L · Fact or fake, who is the product, filter bubble, echo chamber, addiction engineering (Ministry 22.0, 22.1) | 🔶 | | |

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
| 5 | 5.1 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u5-strings/m1-lesson-notes.md) | Reworked to Ministry 7.1, 7.2; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026 for the 45-minute frontal part: one problem ("Robot ID Card", six stages with `while`/`for` loops), a 20-slide deck built directly as a PDF ([`m1-live-slides-he.pdf`](units/u5-strings/m1-live-slides-he.pdf), 54 minutes — the lab part is shorter, ~35), problem text ([`m1-live-problem-he.md`](units/u5-strings/m1-live-problem-he.md)), full solution and five cumulative demo files (`Live_Step1`–`Live_Step5`); NotebookLM prep folder `unit5-m1-live-slides` also ready. |
| 5 | 5.2 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u5-strings/m2-lesson-notes.md) | Reworked to Ministry 7.1, 7.2; now Knowledge + Lab (official 90 / 270 split); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026: problem "Email Desk" in six stages (slicing, `find`, `count`, `in`, `replace`), 20-slide deck [`m2-live-slides-he.pdf`](units/u5-strings/m2-live-slides-he.pdf) (54 min), five `Live2_Step` files, handwritten paper lab (file name and item code; [key](units/u5-strings/m2-paper-lab-answer-key.md)). |
| 5 | 5.3 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab (paper-classwork edition, as taught) | [`m3-lesson-notes.md`](units/u5-strings/m3-lesson-notes.md) | Reworked to Ministry 8.0, 8.1; paper-classwork edition (45-min lesson + worksheet, [plan](units/u5-strings/m3-classwork-lesson-plan.md)) prepared 31 Oct 2026 (its own 20-slide NotebookLM prep files, loose in `Downloads\python-b\`; the Word worksheet is `Downloads\Unit 5.3 - Strings classwork worksheet.docx`; plus a one-page [string commands table](units/u5-strings/string-commands-table-he.md) for the whole unit); slides of the 90-minute lab version: superseded — pending new NotebookLM deck (prep folder ready, 16 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026 (separate from the paper-classwork edition): problem "Account safety checker" in six stages (`lower`, `startswith`, `endswith`, `isalpha`, `isdigit`, `for` over a string, `+=`), 20-slide deck [`m3-live-slides-he.pdf`](units/u5-strings/m3-live-slides-he.pdf) (54 min), five `Live3_Step` files, handwritten paper lab (message analysis and ticket code; [key](units/u5-strings/m3-paper-lab-answer-key.md)). |
| 5 | 5.4 Strings | 90 | 0 / 90 | Lab + Lab | [`m4-lesson-notes.md`](units/u5-strings/m4-lesson-notes.md) | Reworked to Ministry 8.1, 8.2, 8.7; unit checkpoint; **countdown edition** prepared 2 Nov 2026 (4 timed cases on a projected page, `for` and `while` solutions — the DP1/PDP countdown method — then a graded 5-question worksheet; [plan](units/u5-strings/m4-countdown-lesson-plan.md), Word worksheet `Downloads\python-b\Unit 5.4 - Strings countdown worksheet.docx`; Mashov zip `Downloads\python-b\Unit 5.4 - Strings.zip`); slides of the lab version: superseded — pending new NotebookLM deck (prep folder ready, 18 slides, 90 min). |
| 6 | 6.1 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u6-advanced-language-model/m1-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 10.0–10.2: real tokenizer (`model.tokenizer`), token quiz, playground; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m1-slides`, 17 slides, 90 min). |
| 6 | 6.2 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u6-advanced-language-model/m2-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 11.1, 11.2: meaning map, self-attention, real `calculate_similarity`, thresholds, playground; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m2-slides`, 16 slides, 90 min). |
| 6 | 6.3 Advanced Language Model | 90 | 0 / 90 | Lab + Lab | [`m3-lesson-notes.md`](units/u6-advanced-language-model/m3-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 11.3: unit checkpoint ("Semantle", real model, 20-emoji thermometer); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m3-slides`, 13 slides, 90 min). |
| 7 | 7.1 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u7-lists/m1-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 12.0, 12.1: `[]`, `list()`, `in`, `+`, slicing `[a:b:c]` and `[::-1]`; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m1-slides`, 19 slides, 90 min). |
| 7 | 7.2 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u7-lists/m2-lesson-notes.md) | Reworked to Ministry 12.0–12.7: list methods, `split`/`join`, `random.choice`; the Ministry's `append(i)` bug as the warm-up; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m2-slides`, 18 slides, 90 min). |
| 7 | 7.3 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u7-lists/m3-lesson-notes.md) | Reworked to Ministry 13.0, 13.1: index vs value traversal, accumulation, the change-while-looping trap; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m3-slides`, 19 slides, 90 min). |
| 7 | 7.4 Lists | 90 | 0 / 90 | Lab + Lab | [`m4-lesson-notes.md`](units/u7-lists/m4-lesson-notes.md) | Reworked to Ministry 13.1, 14.0, 14.1: counters, filters, the flat menu, parallel lists; Ministry slide errors noted in the lesson notes; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m4-slides`, 13 slides, 90 min). |
| 7 | 7.5 Lists | 90 | 0 / 90 | Lab + Lab | [`m5-lesson-notes.md`](units/u7-lists/m5-lesson-notes.md) | Reworked: linear search, `index()`, phone numbers with `random`; unit checkpoint ("AI Experiment Analyzer", 20-point rubric); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m5-slides`, 14 slides, 90 min). |
| 8 | 8.1 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u8-classification/m1-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 16.0–16.2.0: Louvre boundary-bug trace, two-feature separating line, `classify_fruit(softness, color)`; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m1-slides`, 20 slides, 90 min). |
| 8 | 8.2 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u8-classification/m2-lesson-notes.md) | Reworked to Ministry 17.0–17.1: training vs test, bias, first Teachable Machine try; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m2-slides`, 20 slides, 90 min). |
| 8 | 8.3 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u8-classification/m3-lesson-notes.md) | Reworked to Ministry 18.0, 18.1: accuracy, the fist/OK project (the Ministry's image zips stay outside the repo); photography privacy rules kept; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m3-slides`, 20 slides, 90 min). |
| 8 | 8.4 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m4-lesson-notes.md`](units/u8-classification/m4-lesson-notes.md) | Reworked to Ministry 19.0, 19.1: SavedModel + `TFSMLayer`, 85% rule; **needs a live run with TensorFlow and a real exported model**; stand-in `classify_image()` keeps the files runnable; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m4-slides`, 20 slides, 90 min). |
| 9 | 9.1 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m1-lesson-notes.md`](units/u9-recommender-systems/m1-lesson-notes.md) | Reworked 8 Nov 2026 to Ministry 20.0, 20.1: feed riddle, culinary-twin game, V/X/0 survey (privacy rules kept); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m1-slides`, 20 slides, 90 min). |
| 9 | 9.2 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m2-lesson-notes.md`](units/u9-recommender-systems/m2-lesson-notes.md) | Reworked to Ministry 21.1: table, similarity points, the twin (V/X/0; no tuples or defaults); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m2-slides`, 19 slides, 90 min). |
| 9 | 9.3 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m3-lesson-notes.md`](units/u9-recommender-systems/m3-lesson-notes.md) | Reworked to Ministry 21.1: `find_twin`, `recommend_item`; unit checkpoint with a new 20-point rubric; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m3-slides`, 18 slides, 90 min). |
| 9 | 9.4 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`m4-lesson-notes.md`](units/u9-recommender-systems/m4-lesson-notes.md) | Reworked to Ministry 22.0, 22.1: fact or fake, incognito demo, Plato's cave, three traps; offline card-simulation fallback; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m4-slides`, 19 slides, 90 min). |

## Assessments

Written tests made outside the 30-meeting plan (they do not change the time budget), and graded classwork.

| Unit | Test | Length | Status | Files |
|---|---|---:|---|---|
| 1 | Python A Review — Grade 9 test | 60 min, 100 points | ✅ given 18/24 Oct 2026, graded (mean 77.1, median 80.75); Q5b wording and Q6b answer space fixed in Form B — see the key | [`unit-1-test-he.md`](units/u1-python-a-review/unit-1-test-he.md), [key](units/u1-python-a-review/unit-1-test-answer-key.md), [`Test_Reference.py`](units/u1-python-a-review/Test_Reference.py) |
| 1 | Python A Review — Form B (retest, 2 students) | 60 min, 100 points | 🔶 prepared 29 Oct 2026; mirrors Form A, Q5b/Q6b wording fixed; Word copies and a PDF in `Downloads\python-b`; **to be given 11 Nov 2026** by another teacher | [`unit-1-test-form-b-he.md`](units/u1-python-a-review/unit-1-test-form-b-he.md), [key](units/u1-python-a-review/unit-1-test-form-b-answer-key.md), [`Test_B_Reference.py`](units/u1-python-a-review/Test_B_Reference.py) |
| 5 | 5.1 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026 for the lab half of 5.1; code written by hand beside each problem and handed in on paper; Word + PDF in `Downloads` (root); built with [`tools/problem_sheet_docx.py`](tools/problem_sheet_docx.py) | [worksheet](units/u5-strings/m1-paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/m1-paper-lab-answer-key.md), [`PaperLab_Starter.py`](units/u5-strings/PaperLab_Starter.py), [`PaperLab_Q1_Solution.py`](units/u5-strings/PaperLab_Q1_Solution.py), [`PaperLab_Q2_Solution.py`](units/u5-strings/PaperLab_Q2_Solution.py) |
| 5 | 5.2 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026; handed in on paper; Word + PDF in `Downloads\פדגוגיה\python-b\מעבדות-יחידה-5.2` | [worksheet](units/u5-strings/m2-paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/m2-paper-lab-answer-key.md), [`PaperLab2_Q1_Solution.py`](units/u5-strings/PaperLab2_Q1_Solution.py), [`PaperLab2_Q2_Solution.py`](units/u5-strings/PaperLab2_Q2_Solution.py) |
| 5 | 5.3 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026; handed in on paper; Word + PDF in `Downloads\פדגוגיה\python-b\מעבדות-יחידה-5.3` | [worksheet](units/u5-strings/m3-paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/m3-paper-lab-answer-key.md), [`PaperLab3_Q1_Solution.py`](units/u5-strings/PaperLab3_Q1_Solution.py), [`PaperLab3_Q2_Solution.py`](units/u5-strings/PaperLab3_Q2_Solution.py) |
| 5 | 5.3 Strings — paper classwork (worksheet) | 45-min lesson + ~46 min classwork, rest at home; 100 points + 10 bonus | 🔶 taught; worksheets handed in next week, to be graded with the rubric (plain code without `def` gets full marks — functions not taught yet; exit item 3, `print` vs `return`, not graded) | [worksheet](units/u5-strings/m3-classwork-worksheet-he.md), [key and rubric](units/u5-strings/m3-classwork-answer-key.md), [`Classwork_Reference.py`](units/u5-strings/Classwork_Reference.py) |
| 5 | 5.4 Strings — countdown edition worksheet | 37 min in class + 5-min exit check; 100 points + 5 bonus | 🔶 prepared 2 Nov 2026 for the next lesson | [worksheet](units/u5-strings/m4-countdown-worksheet-he.md), [key and rubric](units/u5-strings/m4-countdown-answer-key.md), [`Worksheet_Reference.py`](units/u5-strings/Worksheet_Reference.py) |

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
