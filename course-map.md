# Grade 8 course map — AI + Python B

Official numbering and hours from [`docs/ministry-source/python-b-ai.pdf`](docs/ministry-source/python-b-ai.pdf)
(master syllabus table, pp. 3–4; one chapter per unit, pp. 5–23). Full framing strategy, provisional meeting outline and
depth boundaries: [`docs/annual-strategy.md`](docs/annual-strategy.md).

> **Hours rule (teacher's decision):** theory/practice hours come from the master table. The chapter tables of program units 1, 3,
> 5 and 7 give a different split (1: 2 / 4, 3: 1 / 5, 5: 3 / 5, 7: 4 / 6); they are used only for the order and weight of topics.

> **Layout (14 Nov 2026):** unit folders are now `lessons/`, `teacher/`, `exercises/`, `assessment/` with entry pages and a [`CONTENTS.md`](CONTENTS.md) hub; the file names in the tables below that read `m<K>-…` are the old flat names, mapped in [`units/README.md`](units/README.md).

## Time budget

1 academic hour = 45 minutes, so the course is 60 hours = **2,700 minutes** = 30 double meetings of 90 minutes.
Minutes are written as **total (theory / practice)**. "Planned" counts only meetings that are built in the repo.

Status: ✅ built and approved by the teacher · 🔶 built, awaiting teacher approval (lesson notes, brief, code and slides all done) ·
⚠️ partly built (lesson notes, brief and code done for every meeting; slides not yet prepared) · ❌ / ⏳ not built yet.

| # | Program unit (block) | Official hours (T/P) | Official minutes (T/P) | Meetings | Planned minutes (T/P) | Remaining | Built |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | [Python A Review](units/u1-python-a-review) (lessons 1.0–2.3) | 6 (1 / 5) | 270 (45 / 225) | 3 | 270 (45 / 225) | 0 | ✅ 2/3 · 🔶 1/3 (Lessons 2.0–2.3 reworked) |
| 2 | [AI2 Year Opening](units/u2-ai2-year-opening) (lessons 3.0–3.2) | 4 (2 / 2) | 180 (90 / 90) | 2 | 180 (90 / 90) | 0 | 🔶 2/2 (reworked) |
| 3 | [Functions](units/u3-functions) (lessons 4.1–4.6) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | 🔶 3/3 (reworked) |
| 4 | [Bringing AI into Code (API)](units/u4-api) (lessons 5.0–6.2) | 4 (1 / 3) | 180 (45 / 135) | 2 | 180 (45 / 135) | 0 | 🔶 2/2 (reworked) |
| 5 | [Strings](units/u5-strings) (lessons 7.1–8.7) | 8 (2 / 6) | 360 (90 / 270) | 4 | 360 (135 / 225) | 0 | 🔶 4/4 (reworked); Lessons 8.0–8.1 taught as 45 / 45 (teacher's decision) — 45 more theory, 45 less practice than official |
| 6 | [Advanced Language Model](units/u6-advanced-language-model) (lessons 10.0–11.3) | 6 (2 / 4) | 270 (90 / 180) | 3 | 270 (90 / 180) | 0 | 🔶 3/3 (reworked 8 Nov 2026 to Ministry 10–11) |
| 7 | [Lists](units/u7-lists) (lessons 9.1–9.5, 12.0–14.5) | 10 (3 / 7) | 450 (135 / 315) | 5 | 450 (135 / 315) | 0 | 🔶 5/5 (reworked 8 Nov 2026 to Ministry 12–14) |
| 8 | [Classification](units/u8-classification) (lessons 16.0–19.1) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | 🔶 4/4 (reworked 8 Nov 2026 to Ministry 16–19) |
| 9 | [Recommender Systems](units/u9-recommender-systems) (lessons 20.0–22.1) | 8 (4 / 4) | 360 (180 / 180) | 4 | 360 (180 / 180) | 0 | 🔶 4/4 (reworked 8 Nov 2026 to Ministry 20–22) |
|  | **TOTAL** | **60 (21 / 39)** | **2,700 (945 / 1,755)** | **30** | **2,700 (990 / 1,710)** | **0** | **30/30 built; 28 meetings reworked to the Ministry materials (🔶 awaiting re-approval), 2 approved (✅: Lessons 1.0–1.1 and 1.2–1.4)** |

A unit has one Knowledge + Lab meeting (45 / 45) per theory hour; its other meetings are Lab + Lab (0 / 90).
Folders (`units/u<N>-<slug>/`) keep their names; the file key `u<N>/m<M>` below points to the folder and file (`u5/m4` = `units/u5-strings/m4-…`). The official lesson numbers are the numbers of this repo ([`docs/official-numbering.md`](docs/official-numbering.md)).

## Deadline and pace

- **Assessment:** the Ministry exam (בחינת מפמ"ר) for "בינה מלאכותית בשילוב מדעי המחשב חלק ב'" is on **Wednesday 17 March 2027**
  ([focus document](docs/ministry-source/focus-python-b-tashpaz-he.pdf); the earlier "May 2027" in the circular is obsolete). Printed notes are allowed; calculators are not
  ([`ministry-circular-tashpaz-he.pdf`](docs/ministry-source/ministry-circular-tashpaz-he.pdf), p. 3). Exam length and format: not yet known.
- **Plan:** [`docs/plan-to-mafmar-2027-03-17.md`](docs/plan-to-mafmar-2027-03-17.md), approved by the teacher on 18 Nov 2026. Exam-first: only the focus chapters
  (1, 3, 4, 5, 6) are taught before the exam; the non-exam blocks (AI2 opening, lists, classification, recommender systems, Semantle) move to after 17 Mar.
- **Meetings available:** 17 Sundays, 22 Nov 2026 – 14 Mar 2027 (no closures known). **Meetings needed:** 9 of teaching + 2 tests + 2 rehearsals + review (see the schedule). It fits; P13 (14 Feb) is the slack.
- **Check after every lesson:** meetings left in the exam-first schedule below ≤ Sundays left before 17 Mar; if a Sunday is lost, drop P13 first.

## Open coverage gaps

- **Teaching order differs from the schedule (teacher, 2 Nov 2026):** the strings block (lessons 7.1–8.7) is being taught **before the functions block
  (lessons 4.1–4.6)** — the class has not learned `def` yet. The countdown edition of Lessons 8.2–8.7 is written without functions. All lab
  versions of the strings block (lessons 7.1–8.7) were converted to plain code the same day (a variable, the code, `print`). Only the Lessons 8.0–8.1 classwork
  worksheet (already taught) still asks for functions; its rubric gives plain code full marks. Revisit the strings block's "function
  that takes a string" goal (goal 9) after the functions block. **The NotebookLM prep folders for the strings block (lessons 7.1–8.7) (on the Windows machine) were
  made before this change** — regenerate their slide content before building the new decks. The AI2-opening, functions and API blocks (lessons 3.0–6.2) were skipped for now (6 Nov 2026, see
  [`class-progress.md`](class-progress.md)).
- **Source of truth (31 Oct 2026):** the Ministry's published teaching materials
  ([`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md)). Lessons 2.0–2.3 and the AI2-opening, functions, API and strings blocks (lessons 3.0–8.7) were reworked to
  match them (🔶, awaiting re-approval; new NotebookLM decks pending — the old patched decks are marked superseded).
- **Ministry lessons 10–22 arrived 8 Nov 2026**, were audited (see [`docs/ministry-teaching-materials.md`](docs/ministry-teaching-materials.md),
  "Audit of lessons 10–22") and **the advanced-language-model, lists, classification and recommender blocks were all reworked the same day (🔶; new NotebookLM prep folders ready, decks pending)**.
  Still open: Lists parts A and E and many worksheets and keys were not delivered (the reworks assume nothing the Ministry did not show);
  defaults chosen without the teacher (change if wrong): `def` allowed in the blocks after functions (they follow the functions block in the schedule); no nested loops and no lists
  of lists in the lists block; the recommender block keeps 4 meetings (the Ministry has 3). Live runs needed before class: Lessons 19.0–19.1 (TensorFlow + a real exported model),
  Lessons 20.0–20.1 (Google Forms export) and 22.0–22.1 (incognito demo), the model download of lessons 10.0–11.3.
- **Converged to the classroom-downloader program (13 Nov 2026):** every block was audited against the official files
  (`docs/ministry-teaching-materials.md`, "Reconciliation") and patched; Lessons 8.2–8.7 were rebuilt (cases: first-star-last, middle character,
  initials, number cipher); the lists block now integrates lists part A and the official worksheets (slide prep folders: 20/20/20/15/16);
  Lessons 8.0–8.1 are recorded as 45/45 as taught vs 0/90 official (block total 360 min either way). Decks for all patched meetings need
  regeneration. Open teacher decisions are listed in the Reconciliation section.
- **Lists-block notes** (superseded by the 13 Nov rework above) need a small update *if* the 90-minute lab version of Lessons 8.2–8.7 is taught (it shows `split`/`join` first). The
  countdown edition of Lessons 8.2–8.7 leaves `split`/`join` to Lessons 9.3, 9.5, 12.0–12.1, so no change is needed if that edition is taught.
- Every official topic is covered (see each unit's `unit-strategy.md`). The tool choices flagged during planning were
  settled during each block's build; the live-service steps are in each unit folder's README (the API block, lessons 5.0–6.2, now uses Gemini).

## Waiting for the teacher (as of 2 Nov 2026)

- Dates Lessons 7.1–8.1 were taught, the weekly meeting day and the first meeting date (for the pace check).
- When lessons 3.0–6.2 will be taught (skipped so far, 6 Nov 2026; the API block uses functions, so it must follow the functions block) — see [`class-progress.md`](class-progress.md).
- Re-approval of the 12 reworked meetings (Lessons 2.0–2.3, 3.0–3.1, 3.1–3.2, 4.1–4.2, 4.4–4.5, 4.3 and 4.6, 5.0–5.2, 6.1–6.2, 7.1, 7.1–7.2, 8.0–8.1, 8.2–8.7) and their new NotebookLM decks.
- Lesson + lab packages of Lessons 7.1–7.2 and 8.0–8.1 (built 6 Nov 2026 with the Lesson 7.1 recipe): confirm the themes, that Lessons 8.0–8.1 use `find`/slicing/`count` from Lessons 7.1–7.2 in stage 6 and the lab, and that Lessons 7.1–7.2 leave `lower`/`upper` to Lessons 8.0–8.1.
- Lesson 7.1 live lesson: it brings `for … in range(len(name))` and `while` into Lesson 7.1 (the unit plan teaches the `for` loop over strings in Lessons 8.0–8.7) — confirm that is wanted, and whether the deck stays at 54 minutes.
- Lessons 8.2–8.7 countdown: which loop per case is shown first, whether the worksheet is collected at the end of class, whether a deck is wanted.
- Thonny's comment shortcut (Ctrl+3, written in `Cipher_Starter.py`) — confirm.
- After grading: Lessons 8.0–8.1 classwork and Lessons 8.2–8.7 worksheet aggregates (in their keys); Form B results after 11 Nov 2026.

## Schedule

**Exam-first schedule (approved 18 Nov 2026; plan: [`docs/plan-to-mafmar-2027-03-17.md`](docs/plan-to-mafmar-2027-03-17.md)).** Sundays; "Built": ✅ approved · 🔶 built, awaiting approval · ❌ to build.
What the class has actually completed is in [`class-progress.md`](class-progress.md). Quizzes (בחנים) are teacher-only.

| # | Sunday | Meeting (file key, official lessons) / content | Quiz / test | Built | Taught on |
|---:|---|---|---|---|---|
| P1 | 22 Nov 2026 | `u5/m4` Lessons 8.2–8.7 Strings: exam review of the מיקוד strings topics (5 slides) + 5-question lab, index vs content loops (completes the strings block; prepares Quiz Q1 on 29 Nov) | — | 🔶 | |
| P2 | 29 Nov | `u3/m1` Lessons 4.1–4.2 Functions: parameters and `return`, the four kinds | Quiz Q1 (strings) | 🔶 | |
| P3 | 6 Dec | `u3/m2` Lessons 4.4–4.5 Functions: returning functions, loops inside functions | — | 🔶 | |
| P4 | 13 Dec | `u3/m3` Lessons 4.3, 4.6 trimmed + mixed functions/strings lab | Quiz Q2 (functions) | 🔶 | |
| P5 | 20 Dec | `u4/m1` Lessons 5.0–5.2 API: the key, the call, prompts | — | 🔶 (live run with a key) | |
| P6 | 27 Dec | `u4/m2` Lessons 6.1–6.2 API: "Balanced Day" project | Quiz Q3 (API, prompts) | 🔶 | |
| P7 | 3 Jan 2027 | Mixed lab, chapters 1, 3, 4, 5 | **Test T1** (45 min) | ❌ | |
| P8 | 10 Jan | T1 feedback, then `u6/m1` Lessons 10.0–10.2 tokens | — | 🔶 | |
| P9 | 17 Jan | `u6/m2` Lessons 11.1–11.2 meaning map, self-attention | Quiz Q4 (language model) | 🔶 | |
| P10 | 24 Jan | Mixed lab, all chapters | **Test T2** (60 min, full scope) | ❌ | |
| P11 | 31 Jan | T2 feedback and gap closing | retake quizzes by topic | ❌ | |
| P12 | 7 Feb | Exam-style programs: loops, strings, functions | Quiz Q5 (strings, loops) | ❌ | |
| P13 | 14 Feb | Flex: second gap closing or API/prompt practice | — | ❌ | |
| P14 | 21 Feb | — | **Rehearsal R1** (past exam, exam conditions) | ❌ | |
| P15 | 28 Feb | R1 review, exam technique | — | ❌ | |
| P16 | 7 Mar | — | **Rehearsal R2** | ❌ | |
| P17 | 14 Mar | R2 review, aids sheet, Q&A; no new material | — | ❌ | |
| — | **Wed 17 Mar 2027** | **Mafmar exam** | | | |

**After the exam (from 21 Mar 2027), 15 meetings plus optional strings methods:** `u2/m1`–`u2/m2` (Lessons 3.0–3.2), `u6/m3` (Lesson 11.3 Semantle), `u7/m1`–`u7/m5` (lists), `u8/m1`–`u8/m4` (classification), `u9/m1`–`u9/m4` (recommender systems).
About 11–14 Sundays remain in the school year, so merging will be needed (later decision).

The file keys and built status of all 30 meetings stay in the **Meeting log** below; the pre-18-Nov block-order schedule is in the git history.

## Meeting log

One row per built meeting. Minutes come from the **Duration** and **Structure** lines of its lesson notes.

| Program unit | Meeting (file key, official lessons) | Minutes | Theory / Practice | Structure | Source | Notes |
|---|---|---:|---:|---|---|---|
| 1 | `u1/m1` Lessons 1.0–1.1 Python A Review | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-who-can-come-in-notes.md`](units/u1-python-a-review/teacher/L01-who-can-come-in-notes.md) | From the codex deck + the raw Lessons 1.0–1.1; slides: `m1-slides-he.pdf` (20 slides, 90 min; NotebookLM, patched) |
| 1 | `u1/m2` Lessons 1.2–1.4 Python A Review | 90 | 0 / 90 | Lab + Lab | [`L02-counting-rounds-notes.md`](units/u1-python-a-review/teacher/L02-counting-rounds-notes.md) | From the codex deck + the raw Lessons 1.2–1.4; slides: `m2-slides-he.pdf` (17 slides, 90 min; NotebookLM, patched) |
| 1 | `u1/m3` Lessons 2.0–2.3 Python A Review | 90 | 0 / 90 | Lab + Lab | [`L03-until-its-done-notes.md`](units/u1-python-a-review/teacher/L03-until-its-done-notes.md) | Reworked to Ministry 2.0, 2.1 and the loop-trap deck; unit checkpoint (`cubes_sum`); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 2 | `u2/m1` Lessons 3.0–3.1 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-ai-or-not-notes.md`](units/u2-ai2-year-opening/teacher/L01-ai-or-not-notes.md) | Reworked to Ministry deck 3.1; classic Python greeting vs an AI greeting; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 2 | `u2/m2` Lessons 3.1–3.2 AI2 Year Opening | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-quick-draw-notes.md`](units/u2-ai2-year-opening/teacher/L02-quick-draw-notes.md) | Reworked to Ministry deck 3.1 and worksheet 3.2 (Quick, Draw!, data, bias); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 3 | `u3/m1` Lessons 4.1–4.2 Functions | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-parameters-and-return-notes.md`](units/u3-functions/teacher/L01-parameters-and-return-notes.md) | Reworked to Ministry 4.1, 4.2; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 3 | `u3/m2` Lessons 4.4–4.5 Functions | 90 | 0 / 90 | Lab + Lab | [`L02-returning-functions-practice-notes.md`](units/u3-functions/teacher/L02-returning-functions-practice-notes.md) | Reworked to Ministry 4.2, 4.4, 4.5; slides: superseded — pending new NotebookLM deck (prep folder ready, 16 slides, 90 min). |
| 3 | `u3/m3` Lessons 4.3, 4.6 Functions | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-local-and-global-notes.md`](units/u3-functions/teacher/L03-local-and-global-notes.md) | Reworked to Ministry 4.3, 4.5, 4.6; `global` is taught; unit checkpoint; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 4 | `u4/m1` Lessons 5.0–5.2 Bringing AI into Code (API) | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-the-gemini-call-notes.md`](units/u4-api/teacher/L01-the-gemini-call-notes.md) | Reworked to Ministry 5.0–5.2 (Gemini); classroom stand-in `ask_the_ai()`; needs a live run with a real key; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). |
| 4 | `u4/m2` Lessons 6.1–6.2 Bringing AI into Code (API) | 90 | 0 / 90 | Lab + Lab | [`L02-balanced-day-notes.md`](units/u4-api/teacher/L02-balanced-day-notes.md) | Reworked to Ministry 6.1, 6.2 ("Balanced Day"); unit checkpoint; stand-in for verification; slides: superseded — pending new NotebookLM deck (prep folder ready, 17 slides, 90 min). |
| 5 | `u5/m1` Lesson 7.1 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-a-string-is-a-sequence-notes.md`](units/u5-strings/teacher/L01-a-string-is-a-sequence-notes.md) | Reworked to Ministry 7.1, 7.2; slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026 for the 45-minute frontal part: one problem ("Robot ID Card", six stages with `while`/`for` loops), a 20-slide deck built directly as a PDF ([`live-slides-he.pdf`](units/u5-strings/lessons/L01-a-string-is-a-sequence/live-slides-he.pdf), 54 minutes — the lab part is shorter, ~35), problem text ([`L01-a-string-is-a-sequence-live-problem-he.md`](units/u5-strings/teacher/L01-a-string-is-a-sequence-live-problem-he.md)), full solution and five cumulative demo files (`Live_Step1`–`Live_Step5`); NotebookLM prep folder `unit5-m1-live-slides` also ready. |
| 5 | `u5/m2` Lessons 7.1–7.2 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-slicing-and-searching-notes.md`](units/u5-strings/teacher/L02-slicing-and-searching-notes.md) | Reworked to Ministry 7.1, 7.2; now Knowledge + Lab (official 90 / 270 split); slides: superseded — pending new NotebookLM deck (prep folder ready, 20 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026: problem "Email Desk" in six stages (slicing, `find`, `count`, `in`, `replace`), 20-slide deck [`live-slides-he.pdf`](units/u5-strings/lessons/L02-slicing-and-searching/live-slides-he.pdf) (54 min), five `Live2_Step` files, handwritten paper lab (file name and item code; [key](units/u5-strings/teacher/L02-slicing-and-searching-paper-lab-answer-key.md)). |
| 5 | `u5/m3` Lessons 8.0–8.1 Strings | 90 | 45 / 45 | 45 knowledge + 45 lab (paper-classwork edition, as taught) | [`L03-string-methods-and-for-notes.md`](units/u5-strings/teacher/L03-string-methods-and-for-notes.md) | Reworked to Ministry 8.0, 8.1; paper-classwork edition (45-min lesson + worksheet, [plan](units/u5-strings/teacher/L03-string-methods-and-for-classwork-lesson-plan.md)) prepared 31 Oct 2026 (its own 20-slide NotebookLM prep files, loose in `Downloads\python-b\`; the Word worksheet is `Downloads\Unit 5.3 - Strings classwork worksheet.docx`; plus a one-page [string commands table](units/u5-strings/lessons/L03-string-methods-and-for/string-commands-table-he.md) for the whole unit); slides of the 90-minute lab version: superseded — pending new NotebookLM deck (prep folder ready, 16 slides, 90 min). **Live-lesson edition** prepared 6 Nov 2026 (separate from the paper-classwork edition): problem "Account safety checker" in six stages (`lower`, `startswith`, `endswith`, `isalpha`, `isdigit`, `for` over a string, `+=`), 20-slide deck [`live-slides-he.pdf`](units/u5-strings/lessons/L03-string-methods-and-for/live-slides-he.pdf) (54 min), five `Live3_Step` files, handwritten paper lab (message analysis and ticket code; [key](units/u5-strings/teacher/L03-string-methods-and-for-paper-lab-answer-key.md)). |
| 5 | `u5/m4` Lessons 8.2–8.7 Strings | 90 | 0 / 90 | Lab + Lab | [`L04-string-algorithms-and-cipher-notes.md`](units/u5-strings/teacher/L04-string-algorithms-and-cipher-notes.md) | Reworked to Ministry 8.1, 8.2, 8.7; unit checkpoint; **countdown edition** prepared 2 Nov 2026 (4 timed cases on a projected page, `for` and `while` solutions — the DP1/PDP countdown method — then a graded 5-question worksheet; [plan](units/u5-strings/teacher/L04-string-algorithms-and-cipher-countdown-lesson-plan.md), Word worksheet `Downloads\python-b\Unit 5.4 - Strings countdown worksheet.docx`; Mashov zip `Downloads\python-b\Unit 5.4 - Strings.zip`); slides of the lab version: superseded — pending new NotebookLM deck (prep folder ready, 18 slides, 90 min). |
| 6 | `u6/m1` Lessons 10.0–10.2 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-tokens-notes.md`](units/u6-advanced-language-model/teacher/L01-tokens-notes.md) | Reworked 8 Nov 2026 to Ministry 10.0–10.2: real tokenizer (`model.tokenizer`), token quiz, playground; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m1-slides`, 17 slides, 90 min). |
| 6 | `u6/m2` Lessons 11.1–11.2 Advanced Language Model | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-meaning-map-and-similarity-notes.md`](units/u6-advanced-language-model/teacher/L02-meaning-map-and-similarity-notes.md) | Reworked 8 Nov 2026 to Ministry 11.1, 11.2: meaning map, self-attention, real `calculate_similarity`, thresholds, playground; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m2-slides`, 16 slides, 90 min). |
| 6 | `u6/m3` Lesson 11.3 Advanced Language Model | 90 | 0 / 90 | Lab + Lab | [`L03-semantle-notes.md`](units/u6-advanced-language-model/teacher/L03-semantle-notes.md) | Reworked 8 Nov 2026 to Ministry 11.3: unit checkpoint ("Semantle", real model, 20-emoji thermometer); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit6-m3-slides`, 13 slides, 90 min). |
| 7 | `u7/m1` Lessons 9.1, 9.4 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-what-is-a-list-notes.md`](units/u7-lists/teacher/L01-what-is-a-list-notes.md) | Reworked 8 Nov 2026 to Ministry 12.0, 12.1: `[]`, `list()`, `in`, `+`, slicing `[a:b:c]` and `[::-1]`; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m1-slides`, 19 slides, 90 min). |
| 7 | `u7/m2` Lessons 9.3, 9.5, 12.0–12.1 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-list-operations-notes.md`](units/u7-lists/teacher/L02-list-operations-notes.md) | Reworked to Ministry 12.0–12.7: list methods, `split`/`join`, `random.choice`; the Ministry's `append(i)` bug as the warm-up; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m2-slides`, 18 slides, 90 min). |
| 7 | `u7/m3` Lessons 12.6, 13.0–13.1 Lists | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-walking-a-list-notes.md`](units/u7-lists/teacher/L03-walking-a-list-notes.md) | Reworked to Ministry 13.0, 13.1: index vs value traversal, accumulation, the change-while-looping trap; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m3-slides`, 19 slides, 90 min). |
| 7 | `u7/m4` Lessons 13.2, 14.0–14.2 Lists | 90 | 0 / 90 | Lab + Lab | [`L04-counting-and-filters-notes.md`](units/u7-lists/teacher/L04-counting-and-filters-notes.md) | Reworked to Ministry 13.1, 14.0, 14.1: counters, filters, the flat menu, parallel lists; Ministry slide errors noted in the lesson notes; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m4-slides`, 13 slides, 90 min). |
| 7 | `u7/m5` Lessons 12.5, 14.4 Lists | 90 | 0 / 90 | Lab + Lab | [`L05-search-and-capstone-notes.md`](units/u7-lists/teacher/L05-search-and-capstone-notes.md) | Reworked: linear search, `index()`, phone numbers with `random`; unit checkpoint ("AI Experiment Analyzer", 20-point rubric); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit7-m5-slides`, 14 slides, 90 min). |
| 8 | `u8/m1` Lessons 16.0–16.2 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-classification-by-rules-notes.md`](units/u8-classification/teacher/L01-classification-by-rules-notes.md) | Reworked 8 Nov 2026 to Ministry 16.0–16.2.0: Louvre boundary-bug trace, two-feature separating line, `classify_fruit(softness, color)`; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m1-slides`, 20 slides, 90 min). |
| 8 | `u8/m2` Lessons 17.0–17.1 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-training-and-test-notes.md`](units/u8-classification/teacher/L02-training-and-test-notes.md) | Reworked to Ministry 17.0–17.1: training vs test, bias, first Teachable Machine try; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m2-slides`, 20 slides, 90 min). |
| 8 | `u8/m3` Lessons 18.0–18.1 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-accuracy-and-project-notes.md`](units/u8-classification/teacher/L03-accuracy-and-project-notes.md) | Reworked to Ministry 18.0, 18.1: accuracy, the fist/OK project (the Ministry's image zips stay outside the repo); photography privacy rules kept; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m3-slides`, 20 slides, 90 min). |
| 8 | `u8/m4` Lessons 19.0–19.1 Classification | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L04-connecting-the-model-notes.md`](units/u8-classification/teacher/L04-connecting-the-model-notes.md) | Reworked to Ministry 19.0, 19.1: SavedModel + `TFSMLayer`, 85% rule; **needs a live run with TensorFlow and a real exported model**; stand-in `classify_image()` keeps the files runnable; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit8-m4-slides`, 20 slides, 90 min). |
| 9 | `u9/m1` Lessons 20.0–20.1 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L01-feed-riddle-and-twin-notes.md`](units/u9-recommender-systems/teacher/L01-feed-riddle-and-twin-notes.md) | Reworked 8 Nov 2026 to Ministry 20.0, 20.1: feed riddle, culinary-twin game, V/X/0 survey (privacy rules kept); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m1-slides`, 20 slides, 90 min). |
| 9 | `u9/m2` Lesson 21.1 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L02-the-table-and-similarity-notes.md`](units/u9-recommender-systems/teacher/L02-the-table-and-similarity-notes.md) | Reworked to Ministry 21.1: table, similarity points, the twin (V/X/0; no tuples or defaults); slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m2-slides`, 19 slides, 90 min). |
| 9 | `u9/m3` Lessons 21.1–21.2 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L03-from-twin-to-recommendation-notes.md`](units/u9-recommender-systems/teacher/L03-from-twin-to-recommendation-notes.md) | Reworked to Ministry 21.1: `find_twin`, `recommend_item`; unit checkpoint with a new 20-point rubric; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m3-slides`, 18 slides, 90 min). |
| 9 | `u9/m4` Lessons 22.0–22.1 Recommender Systems | 90 | 45 / 45 | 45 knowledge + 45 lab | [`L04-traps-of-recommendations-notes.md`](units/u9-recommender-systems/teacher/L04-traps-of-recommendations-notes.md) | Reworked to Ministry 22.0, 22.1: fact or fake, incognito demo, Plato's cave, three traps; offline card-simulation fallback; slides: superseded — pending new NotebookLM deck (prep folder ready in `Downloads\פדגוגיה\python-b\lessons\unit9-m4-slides`, 19 slides, 90 min). |

## Assessments

Written tests made outside the 30-meeting plan (they do not change the time budget), and graded classwork.

| Program unit | Test | Length | Status | Files |
|---|---|---:|---|---|
| 1 | Python A Review (lessons 1.0–2.3) — Grade 9 test | 60 min, 100 points | ✅ given 18/24 Oct 2026, graded (mean 77.1, median 80.75); Q5b wording and Q6b answer space fixed in Form B — see the key | [`unit-1-test-he.md`](units/u1-python-a-review/assessment/unit-1-test-he.md), [key](units/u1-python-a-review/teacher/unit-1-test-answer-key.md), [`Test_Reference.py`](units/u1-python-a-review/teacher/solutions/Test_Reference.py) |
| 1 | Python A Review (lessons 1.0–2.3) — Form B (retest, 2 students) | 60 min, 100 points | 🔶 prepared 29 Oct 2026; mirrors Form A, Q5b/Q6b wording fixed; Word copies and a PDF in `Downloads\python-b`; **to be given 11 Nov 2026** by another teacher | [`unit-1-test-form-b-he.md`](units/u1-python-a-review/assessment/unit-1-test-form-b-he.md), [key](units/u1-python-a-review/teacher/unit-1-test-form-b-answer-key.md), [`Test_B_Reference.py`](units/u1-python-a-review/teacher/solutions/Test_B_Reference.py) |
| 5 | `u5/m1` Lesson 7.1 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026 for the lab half of Lesson 7.1; code written by hand beside each problem and handed in on paper; Word + PDF in `Downloads` (root); built with [`tools/problem_sheet_docx.py`](tools/problem_sheet_docx.py) | [worksheet](units/u5-strings/lessons/L01-a-string-is-a-sequence/paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L01-a-string-is-a-sequence-paper-lab-answer-key.md), [`PaperLab_Starter.py`](units/u5-strings/exercises/PaperLab_Starter.py), [`PaperLab_Q1_Solution.py`](units/u5-strings/teacher/solutions/PaperLab_Q1_Solution.py), [`PaperLab_Q2_Solution.py`](units/u5-strings/teacher/solutions/PaperLab_Q2_Solution.py) |
| 5 | `u5/m2` Lessons 7.1–7.2 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026; handed in on paper; Word + PDF in `Downloads\פדגוגיה\python-b\מעבדות-יחידה-5.2` | [worksheet](units/u5-strings/lessons/L02-slicing-and-searching/paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L02-slicing-and-searching-paper-lab-answer-key.md), [`PaperLab2_Q1_Solution.py`](units/u5-strings/teacher/solutions/PaperLab2_Q1_Solution.py), [`PaperLab2_Q2_Solution.py`](units/u5-strings/teacher/solutions/PaperLab2_Q2_Solution.py) |
| 5 | `u5/m3` Lessons 8.0–8.1 Strings — handwritten paper lab | 45 min; 2 questions × 4 sub-questions, one sheet (two sides); 100 points | 🔶 prepared 6 Nov 2026; handed in on paper; Word + PDF in `Downloads\פדגוגיה\python-b\מעבדות-יחידה-5.3` | [worksheet](units/u5-strings/lessons/L03-string-methods-and-for/paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L03-string-methods-and-for-paper-lab-answer-key.md), [`PaperLab3_Q1_Solution.py`](units/u5-strings/teacher/solutions/PaperLab3_Q1_Solution.py), [`PaperLab3_Q2_Solution.py`](units/u5-strings/teacher/solutions/PaperLab3_Q2_Solution.py) |
| 5 | `u5/m4` Lessons 8.2–8.7 Strings — live deck, paper lab, challenge, teacher guide | live deck 10 slides (five content + code pairs, 54 min); paper lab 45 min, 5 separate questions, one sheet (2 + 3 per side, tools boxes), 100 points; early-finisher challenge (1 projected slide) | 🔶 prepared 13–14 Nov 2026 for the lesson planned Sun 15 Nov 2026; Downloads: `Lessons 8.2-8.7 - Strings - lesson/lab/challenge/teacher guide` | [deck](units/u5-strings/lessons/L04-string-algorithms-and-cipher/live-slides-he.pdf), [worksheet](units/u5-strings/lessons/L04-string-algorithms-and-cipher/paper-lab-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L04-string-algorithms-and-cipher-paper-lab-answer-key.md), [teacher guide](units/u5-strings/teacher/L04-string-algorithms-and-cipher-paper-lab-teacher-guide-he.md), [challenge](units/u5-strings/lessons/L04-string-algorithms-and-cipher/challenge-he.pdf), [`PaperLab4_Q1_Solution.py`](units/u5-strings/teacher/solutions/PaperLab4_Q1_Solution.py) … `Q5`, [`PaperLab4_Challenge_Solution.py`](units/u5-strings/teacher/solutions/PaperLab4_Challenge_Solution.py) |
| 5 | `u5/m3` Lessons 8.0–8.1 Strings — paper classwork (worksheet) | 45-min lesson + ~46 min classwork, rest at home; 100 points + 10 bonus | 🔶 taught; worksheets handed in next week, to be graded with the rubric (plain code without `def` gets full marks — functions not taught yet; exit item 3, `print` vs `return`, not graded) | [worksheet](units/u5-strings/lessons/L03-string-methods-and-for/classwork-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L03-string-methods-and-for-classwork-answer-key.md), [`Classwork_Reference.py`](units/u5-strings/teacher/solutions/Classwork_Reference.py) |
| 5 | `u5/m4` Lessons 8.2–8.7 Strings — countdown edition worksheet | 37 min in class + 5-min exit check; 100 points + 5 bonus | 🔶 prepared 2 Nov 2026 for the next lesson | [worksheet](units/u5-strings/lessons/L04-string-algorithms-and-cipher/countdown-worksheet-he.md), [key and rubric](units/u5-strings/teacher/L04-string-algorithms-and-cipher-countdown-answer-key.md), [`Worksheet_Reference.py`](units/u5-strings/teacher/solutions/Worksheet_Reference.py) |

### Planned assessments before the exam (teacher-only; none built yet)

Quizzes Q1–Q5 (P2, P4, P6, P9, P12), tests T1 (3 Jan, 45 min) and T2 (24 Jan, 60 min, full scope), rehearsals R1 (21 Feb) and R2 (7 Mar). Items stay inside the focus: no `startswith`, `endswith`, `isalpha`, `isdigit`, lists, classification or recommender questions.

## Keeping this up to date

When a meeting is added or its timing changes:
1. Add or update its row in the **Meeting log**, and mark its **Built** column in the **Schedule** (✅ only after the teacher approves it).
2. Update that unit's **Planned minutes**, **Remaining** and **Built** in the time budget, and the totals.
3. A unit's planned minutes must not exceed its official minutes. If they would, cut the lesson or
   note the overrun in the unit row with the reason.
4. Update the status of the topics it covers in the unit's `unit-strategy.md` ("Official topics and hours"),
   and remove any gap it closes from **Open coverage gaps**.

After each lesson is taught:
1. Fill in **Taught on** in the **Schedule**.
2. Recheck **Deadline and pace**: meetings left in the schedule must not exceed meetings left before the exam.
