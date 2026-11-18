# Plan to the mafmar exam — Python B, Wednesday 17 March 2027

Source of scope: [`ministry-source/focus-python-b-tashpaz-he.pdf`](ministry-source/focus-python-b-tashpaz-he.pdf) (the תשפ"ז focus document; red = not on the exam).
Course status: [`../class-progress.md`](../class-progress.md), [`../course-map.md`](../course-map.md), numbering: [`official-numbering.md`](official-numbering.md).
Status: **draft, written 18 Nov 2026, waiting for the teacher's approval.** Meeting day (Sundays), "no closures known", "Lessons 8.2–8.7 not yet taught",
"non-exam blocks after the exam" and "teach only focus items, keep the rest optional" are the teacher's answers of 18 Nov 2026.

## 1. What is on the exam (from the focus document)

| Focus ch. | Name | On the exam | Not on the exam (red) | Repo meetings (file key, official lessons) |
|---|---|---|---|---|
| 1 | Python A review | A new meeting with algorithmic concepts, work environment, variables, conditions, loops (`for`, `while`) | — | `u1/m1`–`u1/m3`, Lessons 1.0–2.3 (taught) |
| 2 | AI2 opening lesson | — | **Whole chapter** | `u2/m1`, `u2/m2`, Lessons 3.0–3.2 |
| 3 | Operations (functions) | Function without / with parameters, not returning a value; without / with parameters, returning a value | — | `u3/m1`, `u3/m2`, `u3/m3`, Lessons 4.1–4.6 |
| 4 | API: bringing AI into code | AI in code; an API key (emphasis on functions); prompt writing; project: conditions, loops, functions and API | — | `u4/m1`, `u4/m2`, Lessons 5.0–6.2 |
| 5 | Strings | Empty string; `+` `*`; `in`; slicing `[]` and `[::]`; `len`, `find`, `upper`, `lower`, `count`, `replace`; bounded loop, index vs content: `for i in range(len(st))`, `for ch in st` | **`startswith`, `endswith`, `isalpha`, `isnumeric`** | `u5/m1`–`u5/m4`, Lessons 7.1–8.7 |
| 6 | Advanced language model | Tokens; meaning map; self-attention (context) | — | `u6/m1`, `u6/m2`, Lessons 10.0–10.2, 11.1–11.2 (`u6/m3`, Lesson 11.3 Semantle: beyond the focus) |
| 7 | Lists | — | **Whole chapter** | `u7/m1`–`u7/m5`, Lessons 9.1–9.5, 12.0–14.5 |
| 8 | Classification | — | **Whole chapter** | `u8/m1`–`u8/m4`, Lessons 16.0–19.1 |
| 9 | Recommender systems | — | **Whole chapter** | `u9/m1`–`u9/m4`, Lessons 20.0–22.1 |

**Consequence:** of the 30 meetings, 15 carry exam material (`u1` ×3, `u3` ×3, `u4` ×2, `u5` ×4, `u6` ×2 plus Semantle as optional); 15 are not examined
(`u2` ×2, `u7` ×5, `u8` ×4, `u9` ×4). Differences from Python A: `while` is on the exam, functions with parameters and return values are on it, and strings,
API and the language model are examined.

## 2. Audit of the built material against the focus (nothing was edited)

| Where | Out of scope for the exam | Decision |
|---|---|---|
| Lessons 8.0–8.1 (`u5/m3`): brief, commands table, classwork worksheet and key, live problem and steps, paper lab | `startswith`, `endswith`, `isalpha`, `isdigit` (the focus names `isnumeric`; treat all as out) | Taught already; mark as "not on the exam" in the student page; keep in the files as optional. Do not use in any quiz or test |
| Lessons 8.2–8.7 (`u5/m4`): live lesson, paper lab, countdown | `isalpha`/`isdigit` in one lab question; `ord`/`chr` cipher, `split`/`join` (not named in the focus; `split`/`join` appear red under lists) | Teach the index-vs-content loops, counting, building strings; the cipher stays as the early-finisher challenge, `split`/`join` optional |
| Lessons 4.3, 4.6 (`u3/m3`) | `global`, local variables, variable roles are not named in the focus (not red) | Teach briefly as one consolidation meeting; not in quizzes or tests unless the teacher decides |
| Lessons 4.1–4.6 | Returning several values and default arguments are already excluded in the notes | No change |
| Lessons 10.0–10.2, 11.1–11.2 (`u6/m1`, `u6/m2`) | The sentence-transformers code, `calculate_similarity`, token IDs in code: the focus names only tokens, the meaning map, self-attention (concepts) | Teach the concepts; the code is the demonstration, not examined |
| Lesson 11.3 (`u6/m3`) | Semantle project | After the exam |
| Lessons 5.0–6.2 (`u4`) | none; needs the functions block first | Ordered after functions |
| Required by the focus but not built | none found: all four function kinds (Lessons 4.1–4.2), the empty string, `in`, `[::]`, `len`/`find`/`upper`/`lower`/`count`/`replace`, `range(len(st))` vs `for ch in st` and `while` are covered | — |

## 3. Calendar

Sundays from **22 Nov 2026 to 14 Mar 2027: 17 meetings** (no closures known; Hanukkah is not skipped). The 14 Mar meeting is three days before the exam.
Lessons 8.2–8.7 were **not** taught on 15 Nov, so they open the plan. Exam length, room and aids are not yet known; the circular says printed notes are allowed and calculators are not.

## 4. The plan

Phases: **A** teach the exam material (P1–P9) · **B** full-scope tests and gap closing (P10–P13) · **C** rehearsal and final preparation (P14–P17).

| # | Sunday | Content | Quiz / test | Built |
|---:|---|---|---|---|
| P1 | 22 Nov | Lessons 8.2–8.7: string algorithms, loops by index and by content, building strings (the strings block is complete) | — | 🔶 |
| P2 | 29 Nov | Lessons 4.1–4.2: functions with parameters and `return`; the four kinds | **Quiz Q1** (10 min, strings) | 🔶 |
| P3 | 6 Dec | Lessons 4.4–4.5: returning functions, loops (`for`, `while`) inside functions | — | 🔶 |
| P4 | 13 Dec | Lessons 4.3, 4.6 trimmed: local variables, `global` briefly, then a mixed functions + strings lab | **Quiz Q2** (15 min, functions) | 🔶 |
| P5 | 20 Dec | Lessons 5.0–5.2: what an API is, the key, the call, prompts, f-strings | — | 🔶 (live run with a real key needed) |
| P6 | 27 Dec | Lessons 6.1–6.2: the "Balanced Day" project (conditions, loops, functions, API) | **Quiz Q3** (15 min, API and prompts) | 🔶 |
| P7 | 3 Jan | Mixed lab on chapters 1, 3, 4, 5 | **Test T1** (45 min, loops, strings, functions) | ❌ to build |
| P8 | 10 Jan | T1 feedback (15 min), then Lessons 10.0–10.2: tokens | — | 🔶 |
| P9 | 17 Jan | Lessons 11.1–11.2: meaning map, self-attention, context | **Quiz Q4** (10 min, language model) | 🔶 |
| P10 | 24 Jan | Mixed lab across all chapters | **Test T2** (60 min, full scope, mafmar format) | ❌ to build |
| P11 | 31 Jan | T2 feedback and gap closing by weak topic | Short retake quizzes by topic | ❌ to build |
| P12 | 7 Feb | Exam-style programs: loops + strings + functions (index vs content, `while`) | **Quiz Q5** (15 min, strings and loops) | ❌ to build |
| P13 | 14 Feb | Flex: second gap closing, or exam-style API / prompt practice | — | ❌ to build |
| P14 | 21 Feb | — | **Rehearsal R1**: a past mafmar exam under exam conditions | ❌ to obtain |
| P15 | 28 Feb | Item-by-item review of R1; exam technique (reading the task, trace tables, time split) | — | ❌ |
| P16 | 7 Mar | — | **Rehearsal R2**: a second past exam or a mock | ❌ |
| P17 | 14 Mar | Review of R2, aids sheet, logistics, quick-fire questions per chapter, Q&A. **No new material** | None | ❌ |

Totals: 9 meetings of new teaching (P1–P6, P8–P9, plus the consolidation P4), 2 tests, 5 quizzes, 2 full rehearsals, 4 review and gap-closing meetings, 1 flex.
**It fits:** 9 meetings of teaching and 17 available leave 8 for assessment and review; P13 is the slack.

## 5. Rules of the plan

- **Exam-first order:** nothing out of scope is taught before 17 Mar. Functions come before the API (the API block uses functions).
- **Trim, don't extend:** Lessons 4.3/4.6 and the language-model code are compressed; the official unit minutes of the trimmed blocks are not met before the exam.
- **Optional, not removed:** `startswith`, `endswith`, `isalpha`, `isdigit`, the cipher and `split`/`join` stay in the files; they never appear in a quiz, test or rehearsal. No lesson file is edited without the teacher's decision.
- **If a Sunday is lost:** drop P13 first; if a second is lost, make T2 a 45-minute test and fold P12's quiz into P11. If a third is lost, merge P15 into P16 (R2 as a half exam).
- **Past exams:** use only items inside the focus; older exams may include lists, `startswith`-style methods or other red items — replace or skip those. Check the aids sheet of the year.
- **Quizzes are teacher-only:** students see tests and rehearsals on their page. A quiz is a **בוחן**, a test is a **מבחן**.

## 6. After the exam (from 21 Mar 2027)

Not examined, 15 meetings: the AI2 opening (`u2` ×2), Semantle (`u6/m3`) and the lists (`u7` ×5), classification (`u8` ×4) and recommender (`u9` ×4) blocks, plus the optional strings methods.
There are about 11–14 Sundays left in the school year, so merging will be needed. That is a later decision.

## 7. Open questions

1. Exam length, number of parts and points: not in the repo; confirm from the Ministry.
2. Is `global` examined? The focus lists only the four function kinds. Default: not examined.
3. Is `isdigit` out like `isnumeric`? Default: yes.
4. Did the Form B retest of 11 Nov happen? (Not answered; the tracker keeps it as open.)
5. Hanukkah and other school events: none known; confirm before the student page is printed.

## 8. Material to build (not done yet)

| Item | For | Status |
|---|---|---|
| Quizzes Q1–Q5 with keys | P2, P4, P6, P9, P12 | Not built |
| Tests T1, T2 with keys | P7, P10 | Not built |
| Mixed labs and gap-closing stations | P7, P10–P13 | Not built |
| Exam-style practice sheets: loops by index vs by content, `while`, functions with return, prompt writing | P4, P12, P13 | Not built |
| Mock exam in mafmar format and keys (if past exams are unsuitable) | P14, P16 | Not built |
| Decks for the meetings still pending regeneration (NotebookLM) | P2–P9 | Pending |
| Update `course-map.md` and `class-progress.md` to this order | — | After approval |
| Student page `docs/mafmar-plan-python-b-he.html` | — | After approval |
