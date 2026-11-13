# Lessons 7.1–8.7 — Strings

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (**90 theory / 270 practice**). Reworked from the Ministry's teaching materials 🔶
(built, awaiting approval).

**Theory / practice labels.** Official plan: Lesson 7.1 and Lessons 7.1–7.2 are Knowledge + Lab (45 / 45), Lessons 8.0–8.1 and Lessons 8.2–8.7 are Lab + Lab (0 / 90) = 90 / 270. Lessons 8.0–8.1 was taught as the paper-classwork edition (live lesson + 45-minute paper lab) and the teacher recorded it as 45 / 45, so the unit as taught is 135 / 225; the 360 minutes are the same. Details: [`unit-strategy.md`](unit-strategy.md).

**No functions in this unit (teacher, 2 Nov 2026):** the class learns `def` after the strings block (lessons 7.1–8.7), so every lab, worksheet and
countdown case is plain code — a variable with the text, the code under it, `print`. The Lessons 8.0–8.1 classwork worksheet (already
taught) and its `Classwork_Starter.py` / `Classwork_Reference.py` still use `def` / `return` (the one documented exception to the rulebook; the official exercises are all functions); its rubric gives plain code full marks.

## Lesson 7.1 — Strings

**Topic:** A String Is an Ordered Sequence

90 minutes: 45 knowledge + 45 lab · **quotes → indices (+/−) → `len` → `+`/`*` → `int`/`str`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Teacher | [`m1-live-problem-he.md`](m1-live-problem-he.md), [`m1-live-program.py`](m1-live-program.py) | Frontal live-coding problem (6 stages) and full solution (Robot ID Card) |
| Teacher | [`m1-live-slides-he.pdf`](m1-live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md), not NotebookLM) |
| Student | [`m1-paper-lab-worksheet-he.md`](m1-paper-lab-worksheet-he.md), [`PaperLab_Starter.py`](PaperLab_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 challenging questions with 4 sub-questions each (question box on the right, large code box on the left), handed in on paper |
| Teacher | [`m1-paper-lab-answer-key.md`](m1-paper-lab-answer-key.md), [`PaperLab_Q1_Solution.py`](PaperLab_Q1_Solution.py), [`PaperLab_Q2_Solution.py`](PaperLab_Q2_Solution.py) | Answer key, rubric (100), reference solutions |
| Teacher | `Live_Step1_…` to `Live_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Indices_Starter.py`](Indices_Starter.py) | `word[len(word)]` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Indices_Reference.py`](Indices_Reference.py) | Solutions, one block of plain code per task (no functions) |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 18 slides) |

## Lessons 7.1–7.2 — Strings

**Topic:** Slicing and Searching

90 minutes: 45 knowledge + 45 lab · **`[start:end:jump]` → `count` → `replace` → `in` → `find`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Teacher | [`m2-live-problem-he.md`](m2-live-problem-he.md), [`m2-live-program.py`](m2-live-program.py) | Live-lesson problem "Email Desk" (6 stages) and full solution |
| Teacher | [`m2-live-slides-he.pdf`](m2-live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md)) |
| Teacher | `Live2_Step1_…` to `Live2_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`m2-paper-lab-worksheet-he.md`](m2-paper-lab-worksheet-he.md), [`PaperLab2_Starter.py`](PaperLab2_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 questions × 4 sub-questions (file name and item code) |
| Teacher | [`m2-paper-lab-answer-key.md`](m2-paper-lab-answer-key.md), [`PaperLab2_Q1_Solution.py`](PaperLab2_Q1_Solution.py), [`PaperLab2_Q2_Solution.py`](PaperLab2_Q2_Solution.py) | Answer key, rubric (100), full solutions |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Slicing_Starter.py`](Slicing_Starter.py) | Discarded-`upper()` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Slicing_Reference.py`](Slicing_Reference.py) | Solutions, one block of plain code per task (no functions) |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 16 slides) |

## Lessons 8.0–8.1 — Strings

**Topic:** More Methods and Walking Over a String with `for`

90 minutes: Lab + Lab (official plan; taught as the paper-classwork edition, recorded 45 / 45) · **`lower`/`upper` → `startswith`/`endswith` → `isalpha`/`isdigit` → `for` → counters → `+=`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan |
| Teacher | [`m3-live-problem-he.md`](m3-live-problem-he.md), [`m3-live-program.py`](m3-live-program.py) | Live-lesson problem "Account safety checker" (6 stages) and full solution |
| Teacher | [`m3-live-slides-he.pdf`](m3-live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md)) |
| Teacher | `Live3_Step1_…` to `Live3_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`m3-paper-lab-worksheet-he.md`](m3-paper-lab-worksheet-he.md), [`PaperLab3_Starter.py`](PaperLab3_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 questions × 4 sub-questions (message analysis and ticket code) |
| Teacher | [`m3-paper-lab-answer-key.md`](m3-paper-lab-answer-key.md), [`PaperLab3_Q1_Solution.py`](PaperLab3_Q1_Solution.py), [`PaperLab3_Q2_Solution.py`](PaperLab3_Q2_Solution.py) | Answer key, rubric (100), full solutions |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Traverse_Starter.py`](Traverse_Starter.py) | Counter-reset warm-up bug, stubs for Tasks 1–5 |
| Teacher | [`Traverse_Reference.py`](Traverse_Reference.py) | Solutions, one block of plain code per task (no functions; Task 4 reads input) |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 15 slides) |

**Paper-classwork edition of Lessons 8.0–8.1** (a 45-minute lesson, then a printed worksheet done with the computer; the rest is homework):

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-classwork-lesson-plan.md`](m3-classwork-lesson-plan.md) | 45-minute lesson derived from the worksheet |
| Student | [`m3-classwork-worksheet-he.md`](m3-classwork-worksheet-he.md) | Hebrew worksheet: read and predict, write functions on paper, homework part (Word copy for printing in `Downloads\python-b`) |
| Teacher | [`m3-classwork-answer-key.md`](m3-classwork-answer-key.md) | Answers, trace table, what to look for while circulating, grading rubric (100 points + 10 bonus) and marking sheet |
| Student | [`string-commands-table-he.md`](string-commands-table-he.md) | One-page table of every string operation and method in the unit, each with a small example and result (Word copy for printing) |
| Student | [`Classwork_Starter.py`](Classwork_Starter.py) | Part A snippets, the counter-reset bug (B1), stubs for B2–B5 and homework |
| Teacher | [`Classwork_Reference.py`](Classwork_Reference.py) | Solutions with expected values |
| Teacher | slides | Pending (NotebookLM): 20 slides, 90 min; prep files (loose, beside the Word worksheet) in `Downloads\python-b\` (save the reviewed deck as `m3-classwork-slides-he.pdf`) |

## Lessons 8.2–8.7 — Strings

**Topic:** String Algorithms, a Secret Code, and the Unit Checkpoint

90 minutes: Lab + Lab · **exercises 4–7 → `ord`/`chr` cipher → `split`/`join` (shown) → checkpoint**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including the checkpoint scoring |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Cipher_Starter.py`](Cipher_Starter.py) | `or "e"` warm-up bug, stubs for Tasks 1–6 and the checkpoint |
| Teacher | [`Cipher_Reference.py`](Cipher_Reference.py) | Solutions, one block of plain code per task (no functions), plus worksheet 8.2 enrichment |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 13 slides) |

**Live lesson + paper lab edition of Lessons 8.2–8.7** (the Lessons 7.1–8.1 recipe, built 13 Nov 2026): problem "Secret Message Machine" in six stages
(`while` checks, `ord`/`chr`, shift cipher with wrap-around, number cipher and initials with `+=`, frame with `split`/`join` shown only,
decode); a 10-slide deck (five pairs: content slide, then a code-examples slide to copy into Thonny) and a one-sheet paper lab (five separate questions, three on the first side and two on the second, enlarged font).

| Audience | File | Purpose |
|---|---|---|
| Teacher | [`m4-live-problem-he.md`](m4-live-problem-he.md) | The problem and the six stages |
| Teacher | [`m4-live-program.py`](m4-live-program.py), `Live4_Step1_Checks.py` … `Live4_Step5_ReportAndReceiver.py` | Full solution and five cumulative demo files |
| Teacher | [`m4-live-slides-he.pdf`](m4-live-slides-he.pdf) | 10-slide deck, five content + code-example pairs, no title slide (54 min; source [`m4-live-source-slides.md`](m4-live-source-slides.md)) |
| Student | [`m4-paper-lab-worksheet-he.md`](m4-paper-lab-worksheet-he.md), `PaperLab4_Starter.py` | One-sheet handwritten lab: five separate questions, each with its own string and task (3 + 2 per side, enlarged font; 45 min) |
| Teacher | [`m4-paper-lab-answer-key.md`](m4-paper-lab-answer-key.md), `PaperLab4_Q1_Solution.py` … `PaperLab4_Q5_Solution.py` | Key, 100-point rubric, one solution per question |

**Countdown edition of Lessons 8.2–8.7** (the countdown method of the teacher's DP1/PDP classes: four timed cases done together on a projected
page, each solved with `for` and with `while`; then a graded five-question worksheet):

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-countdown-lesson-plan.md`](m4-countdown-lesson-plan.md) | Lesson plan: 48 min of cases, 37 min of worksheet, 5 min exit check |
| Teacher | [`m4-countdown-he.html`](m4-countdown-he.html) | The countdown page (open in a browser and project; generated — rebuild with [`tools/countdown`](../../tools/countdown/README.md)) |
| Student | [`m4-countdown-cases-he.md`](m4-countdown-cases-he.md) | The four cases as instructions, no solutions (generated; as `Countdown_Cases.pdf` in the Mashov zip `Downloads\python-b\Lessons 8.2–8.7 - Strings.zip`) |
| Teacher | [`m4-countdown-cases.json`](m4-countdown-cases.json) | The page's content: Hebrew titles and goals, minutes, test calls, how the two solutions differ |
| Student | [`FirstStarLast_Starter.py`](FirstStarLast_Starter.py), [`MiddleChar_Starter.py`](MiddleChar_Starter.py), [`Initials_Starter.py`](Initials_Starter.py), [`NumberCipher_Starter.py`](NumberCipher_Starter.py) | One file per case (generated): goal, test values, expected output — no `def`, the class has not learned functions yet |
| Teacher | [`Countdown_Reference.py`](Countdown_Reference.py) | Each case with `for` and with `while`, by different ideas (plain code, no functions) |
| Student | [`m4-countdown-worksheet-he.md`](m4-countdown-worksheet-he.md) | Hebrew worksheet: the `or` bug, count `is` without `count`, first and last four characters, last letter of every word, alternating case, bonus, exit check (Word copy for printing in `Downloads\python-b`) |
| Student | [`Worksheet_Starter.py`](Worksheet_Starter.py) | The `or "e"` bug (Q1) and a variable to write under for Q2–Q5 and the bonus (no functions) |
| Teacher | [`Worksheet_Reference.py`](Worksheet_Reference.py) | Solutions with expected values |
| Teacher | [`m4-countdown-answer-key.md`](m4-countdown-answer-key.md) | Answers, grading rubric (100 points + 5 bonus), marking sheet, what to look for |
