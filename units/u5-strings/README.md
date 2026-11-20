# Lessons 7.1–8.7 — Strings

Python B, Grade 8 · 8 academic hours = 4 meetings = 360 minutes (90 theory / 270 practice, official master table). 4 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Lesson 7.1**<br>A String Is an Ordered Sequence<br>[md](lessons/L01-a-string-is-a-sequence.md) · [html](lessons/L01-a-string-is-a-sequence.html) · [live-slides](lessons/L01-a-string-is-a-sequence/live-slides-he.pdf) · [paper-lab-worksheet](lessons/L01-a-string-is-a-sequence/paper-lab-worksheet-he.md) · [slides PDF](lessons/L01-a-string-is-a-sequence/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 7.1–7.2**<br>Slicing and Searching — `[start:end:jump]`, `count`, `replace`, `in`, `find`<br>[md](lessons/L02-slicing-and-searching.md) · [html](lessons/L02-slicing-and-searching.html) · [live-slides](lessons/L02-slicing-and-searching/live-slides-he.pdf) · [paper-lab-worksheet](lessons/L02-slicing-and-searching/paper-lab-worksheet-he.md) · [slides PDF](lessons/L02-slicing-and-searching/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 3 | **Lessons 8.0–8.1**<br>More String Methods and Walking Over a String with `for`<br>[md](lessons/L03-string-methods-and-for.md) · [html](lessons/L03-string-methods-and-for.html) · [classwork-worksheet](lessons/L03-string-methods-and-for/classwork-worksheet-he.md) · [live-slides](lessons/L03-string-methods-and-for/live-slides-he.pdf) · [paper-lab-worksheet](lessons/L03-string-methods-and-for/paper-lab-worksheet-he.md) · [slides PDF](lessons/L03-string-methods-and-for/slides-he.pdf) · [string-commands-table](lessons/L03-string-methods-and-for/string-commands-table-he.md) | 0 / 90 | Built, awaiting approval |
| 4 | **Lessons 8.2–8.7**<br>String Algorithms, a Secret Code, and the Unit Checkpoint<br>[md](lessons/L04-string-algorithms-and-cipher.md) · [html](lessons/L04-string-algorithms-and-cipher.html) · [challenge](lessons/L04-string-algorithms-and-cipher/challenge-he.pdf) · [countdown-cases](lessons/L04-string-algorithms-and-cipher/countdown-cases-he.md) · [countdown-worksheet](lessons/L04-string-algorithms-and-cipher/countdown-worksheet-he.md) · [live-slides](lessons/L04-string-algorithms-and-cipher/live-slides-he.pdf) · [paper-lab-worksheet](lessons/L04-string-algorithms-and-cipher/paper-lab-worksheet-he.md) · [slides PDF](lessons/L04-string-algorithms-and-cipher/slides-he.pdf) | 0 / 90 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-a-string-is-a-sequence-live-problem-he.md`](teacher/L01-a-string-is-a-sequence-live-problem-he.md) | Live-lesson problem and stages |
| [`teacher/L01-a-string-is-a-sequence-notes.md`](teacher/L01-a-string-is-a-sequence-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L01-a-string-is-a-sequence-paper-lab-answer-key.md`](teacher/L01-a-string-is-a-sequence-paper-lab-answer-key.md) | Answer key and rubric |
| [`teacher/L02-slicing-and-searching-live-problem-he.md`](teacher/L02-slicing-and-searching-live-problem-he.md) | Live-lesson problem and stages |
| [`teacher/L02-slicing-and-searching-notes.md`](teacher/L02-slicing-and-searching-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-slicing-and-searching-paper-lab-answer-key.md`](teacher/L02-slicing-and-searching-paper-lab-answer-key.md) | Answer key and rubric |
| [`teacher/L03-string-methods-and-for-classwork-answer-key.md`](teacher/L03-string-methods-and-for-classwork-answer-key.md) | Answer key and rubric |
| [`teacher/L03-string-methods-and-for-classwork-lesson-plan.md`](teacher/L03-string-methods-and-for-classwork-lesson-plan.md) | Lesson plan |
| [`teacher/L03-string-methods-and-for-live-problem-he.md`](teacher/L03-string-methods-and-for-live-problem-he.md) | Live-lesson problem and stages |
| [`teacher/L03-string-methods-and-for-notes.md`](teacher/L03-string-methods-and-for-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-string-methods-and-for-paper-lab-answer-key.md`](teacher/L03-string-methods-and-for-paper-lab-answer-key.md) | Answer key and rubric |
| [`teacher/L04-string-algorithms-and-cipher-challenge-source-slides.md`](teacher/L04-string-algorithms-and-cipher-challenge-source-slides.md) | Source text of a generated deck |
| [`teacher/L04-string-algorithms-and-cipher-countdown-answer-key.md`](teacher/L04-string-algorithms-and-cipher-countdown-answer-key.md) | Answer key and rubric |
| [`teacher/L04-string-algorithms-and-cipher-countdown-cases.json`](teacher/L04-string-algorithms-and-cipher-countdown-cases.json) | Countdown cases (input of `tools/countdown`) |
| [`teacher/L04-string-algorithms-and-cipher-countdown-lesson-plan.md`](teacher/L04-string-algorithms-and-cipher-countdown-lesson-plan.md) | Lesson plan |
| [`teacher/L04-string-algorithms-and-cipher-live-problem-he.md`](teacher/L04-string-algorithms-and-cipher-live-problem-he.md) | Live-lesson problem and stages |
| [`teacher/L04-string-algorithms-and-cipher-live-source-slides.md`](teacher/L04-string-algorithms-and-cipher-live-source-slides.md) | Source text of a generated deck |
| [`teacher/L04-string-algorithms-and-cipher-notes.md`](teacher/L04-string-algorithms-and-cipher-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L04-string-algorithms-and-cipher-paper-lab-answer-key.md`](teacher/L04-string-algorithms-and-cipher-paper-lab-answer-key.md) | Answer key and rubric |
| [`teacher/L04-string-algorithms-and-cipher-paper-lab-teacher-guide-he.md`](teacher/L04-string-algorithms-and-cipher-paper-lab-teacher-guide-he.md) | Teacher guide with full solutions |
| [`teacher/live-steps/`](teacher/live-steps) | Live-demo code that grows step by step (20 files) |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (23 files) |

## Status and open checks

- 0 of 4 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

8 academic hours = 4 meetings = 360 minutes (**90 theory / 270 practice**). Reworked from the Ministry's teaching materials 🔶
(built, awaiting approval).

**Theory / practice labels.** Official plan: Lesson 7.1 and Lessons 7.1–7.2 are Knowledge + Lab (45 / 45), Lessons 8.0–8.1 and Lessons 8.2–8.7 are Lab + Lab (0 / 90) = 90 / 270. Lessons 8.0–8.1 was taught as the paper-classwork edition (live lesson + 45-minute paper lab) and the teacher recorded it as 45 / 45, so the unit as taught is 135 / 225; the 360 minutes are the same. Details: [`unit-strategy.md`](unit-strategy.md).

**No functions in this unit (teacher, 2 Nov 2026):** the class learns `def` after the strings block (lessons 7.1–8.7), so every lab, worksheet and
countdown case is plain code — a variable with the text, the code under it, `print`. The Lessons 8.0–8.1 classwork worksheet (already
taught) and its `Classwork_Starter.py` / `Classwork_Reference.py` still use `def` / `return` (the one documented exception to the rulebook; the official exercises are all functions); its rubric gives plain code full marks.

### Lesson 7.1 — Strings

**Topic:** A String Is an Ordered Sequence

90 minutes: 45 knowledge + 45 lab · **quotes → indices (+/−) → `len` → `+`/`*` → `int`/`str`**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-a-string-is-a-sequence-notes.md`](teacher/L01-a-string-is-a-sequence-notes.md) | Lesson plan |
| Teacher | [`L01-a-string-is-a-sequence-live-problem-he.md`](teacher/L01-a-string-is-a-sequence-live-problem-he.md), [`L01-a-string-is-a-sequence-live-program.py`](teacher/solutions/L01-a-string-is-a-sequence-live-program.py) | Frontal live-coding problem (6 stages) and full solution (Robot ID Card) |
| Teacher | [`live-slides-he.pdf`](lessons/L01-a-string-is-a-sequence/live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md), not NotebookLM) |
| Student | [`paper-lab-worksheet-he.md`](lessons/L01-a-string-is-a-sequence/paper-lab-worksheet-he.md), [`PaperLab_Starter.py`](exercises/PaperLab_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 challenging questions with 4 sub-questions each (question box on the right, large code box on the left), handed in on paper |
| Teacher | [`L01-a-string-is-a-sequence-paper-lab-answer-key.md`](teacher/L01-a-string-is-a-sequence-paper-lab-answer-key.md), [`PaperLab_Q1_Solution.py`](teacher/solutions/PaperLab_Q1_Solution.py), [`PaperLab_Q2_Solution.py`](teacher/solutions/PaperLab_Q2_Solution.py) | Answer key, rubric (100), reference solutions |
| Teacher | `Live_Step1_…` to `Live_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`L01-a-string-is-a-sequence.md`](lessons/L01-a-string-is-a-sequence.md) | Hebrew lab brief |
| Student | [`Indices_Starter.py`](exercises/Indices_Starter.py) | `word[len(word)]` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Indices_Reference.py`](teacher/solutions/Indices_Reference.py) | Solutions, one block of plain code per task (no functions) |
| Teacher | [`slides-he.pdf`](lessons/L01-a-string-is-a-sequence/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 18 slides) |

### Lessons 7.1–7.2 — Strings

**Topic:** Slicing and Searching

90 minutes: 45 knowledge + 45 lab · **`[start:end:jump]` → `count` → `replace` → `in` → `find`**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-slicing-and-searching-notes.md`](teacher/L02-slicing-and-searching-notes.md) | Lesson plan |
| Teacher | [`L02-slicing-and-searching-live-problem-he.md`](teacher/L02-slicing-and-searching-live-problem-he.md), [`L02-slicing-and-searching-live-program.py`](teacher/solutions/L02-slicing-and-searching-live-program.py) | Live-lesson problem "Email Desk" (6 stages) and full solution |
| Teacher | [`live-slides-he.pdf`](lessons/L02-slicing-and-searching/live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md)) |
| Teacher | `Live2_Step1_…` to `Live2_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`paper-lab-worksheet-he.md`](lessons/L02-slicing-and-searching/paper-lab-worksheet-he.md), [`PaperLab2_Starter.py`](exercises/PaperLab2_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 questions × 4 sub-questions (file name and item code) |
| Teacher | [`L02-slicing-and-searching-paper-lab-answer-key.md`](teacher/L02-slicing-and-searching-paper-lab-answer-key.md), [`PaperLab2_Q1_Solution.py`](teacher/solutions/PaperLab2_Q1_Solution.py), [`PaperLab2_Q2_Solution.py`](teacher/solutions/PaperLab2_Q2_Solution.py) | Answer key, rubric (100), full solutions |
| Student | [`L02-slicing-and-searching.md`](lessons/L02-slicing-and-searching.md) | Hebrew lab brief |
| Student | [`Slicing_Starter.py`](exercises/Slicing_Starter.py) | Discarded-`upper()` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Slicing_Reference.py`](teacher/solutions/Slicing_Reference.py) | Solutions, one block of plain code per task (no functions) |
| Teacher | [`slides-he.pdf`](lessons/L02-slicing-and-searching/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 16 slides) |

### Lessons 8.0–8.1 — Strings

**Topic:** More Methods and Walking Over a String with `for`

90 minutes: Lab + Lab (official plan; taught as the paper-classwork edition, recorded 45 / 45) · **`lower`/`upper` → `startswith`/`endswith` → `isalpha`/`isdigit` → `for` → counters → `+=`**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-string-methods-and-for-notes.md`](teacher/L03-string-methods-and-for-notes.md) | Lesson plan |
| Teacher | [`L03-string-methods-and-for-live-problem-he.md`](teacher/L03-string-methods-and-for-live-problem-he.md), [`L03-string-methods-and-for-live-program.py`](teacher/solutions/L03-string-methods-and-for-live-program.py) | Live-lesson problem "Account safety checker" (6 stages) and full solution |
| Teacher | [`live-slides-he.pdf`](lessons/L03-string-methods-and-for/live-slides-he.pdf) | Live-lesson deck, 20 slides, 54 min (built with [`tools/live-deck`](../../tools/live-deck/README.md)) |
| Teacher | `Live3_Step1_…` to `Live3_Step5_…` (5 files) | Live-demo code that grows step by step; the last one is the full program |
| Student | [`paper-lab-worksheet-he.md`](lessons/L03-string-methods-and-for/paper-lab-worksheet-he.md), [`PaperLab3_Starter.py`](exercises/PaperLab3_Starter.py) | Handwritten 45-minute lab: one sheet, two sides, 2 questions × 4 sub-questions (message analysis and ticket code) |
| Teacher | [`L03-string-methods-and-for-paper-lab-answer-key.md`](teacher/L03-string-methods-and-for-paper-lab-answer-key.md), [`PaperLab3_Q1_Solution.py`](teacher/solutions/PaperLab3_Q1_Solution.py), [`PaperLab3_Q2_Solution.py`](teacher/solutions/PaperLab3_Q2_Solution.py) | Answer key, rubric (100), full solutions |
| Student | [`L03-string-methods-and-for.md`](lessons/L03-string-methods-and-for.md) | Hebrew lab brief |
| Student | [`Traverse_Starter.py`](exercises/Traverse_Starter.py) | Counter-reset warm-up bug, stubs for Tasks 1–5 |
| Teacher | [`Traverse_Reference.py`](teacher/solutions/Traverse_Reference.py) | Solutions, one block of plain code per task (no functions; Task 4 reads input) |
| Teacher | [`slides-he.pdf`](lessons/L03-string-methods-and-for/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 15 slides) |

**Paper-classwork edition of Lessons 8.0–8.1** (a 45-minute lesson, then a printed worksheet done with the computer; the rest is homework):

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-string-methods-and-for-classwork-lesson-plan.md`](teacher/L03-string-methods-and-for-classwork-lesson-plan.md) | 45-minute lesson derived from the worksheet |
| Student | [`classwork-worksheet-he.md`](lessons/L03-string-methods-and-for/classwork-worksheet-he.md) | Hebrew worksheet: read and predict, write functions on paper, homework part (Word copy for printing in `Downloads\python-b`) |
| Teacher | [`L03-string-methods-and-for-classwork-answer-key.md`](teacher/L03-string-methods-and-for-classwork-answer-key.md) | Answers, trace table, what to look for while circulating, grading rubric (100 points + 10 bonus) and marking sheet |
| Student | [`string-commands-table-he.md`](lessons/L03-string-methods-and-for/string-commands-table-he.md) | One-page table of every string operation and method in the unit, each with a small example and result (Word copy for printing) |
| Student | [`Classwork_Starter.py`](exercises/Classwork_Starter.py) | Part A snippets, the counter-reset bug (B1), stubs for B2–B5 and homework |
| Teacher | [`Classwork_Reference.py`](teacher/solutions/Classwork_Reference.py) | Solutions with expected values |
| Teacher | slides | Pending (NotebookLM): 20 slides, 90 min; prep files (loose, beside the Word worksheet) in `Downloads\python-b\` (save the reviewed deck as `m3-classwork-slides-he.pdf`) |

### Lessons 8.2–8.7 — Strings

**Topic:** String Algorithms, a Secret Code, and the Unit Checkpoint

90 minutes: Lab + Lab · **exercises 4–7 → `ord`/`chr` cipher → `split`/`join` (shown) → checkpoint**

| For | File | What it is |
|---|---|---|
| Teacher | [`L04-string-algorithms-and-cipher-notes.md`](teacher/L04-string-algorithms-and-cipher-notes.md) | Lesson plan, including the checkpoint scoring |
| Student | [`L04-string-algorithms-and-cipher.md`](lessons/L04-string-algorithms-and-cipher.md) | Hebrew lab brief |
| Student | [`Cipher_Starter.py`](exercises/Cipher_Starter.py) | `or "e"` warm-up bug, stubs for Tasks 1–6 and the checkpoint |
| Teacher | [`Cipher_Reference.py`](teacher/solutions/Cipher_Reference.py) | Solutions, one block of plain code per task (no functions), plus worksheet 8.2 enrichment |
| Teacher | [`slides-he.pdf`](lessons/L04-string-algorithms-and-cipher/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 13 slides) |

**Live lesson + paper lab edition of Lessons 8.2–8.7** (the Lessons 7.1–8.1 recipe, built 13 Nov 2026): problem "Secret Message Machine" in six stages
(`while` checks, `ord`/`chr`, shift cipher with wrap-around, number cipher and initials with `+=`, frame with `split`/`join` shown only,
decode); a 10-slide deck (five pairs: content slide, then a code-examples slide to copy into Thonny) and a one-sheet paper lab (five separate questions, three on the first side and two on the second, enlarged font).

| Audience | File | Purpose |
|---|---|---|
| Teacher | [`L04-string-algorithms-and-cipher-live-problem-he.md`](teacher/L04-string-algorithms-and-cipher-live-problem-he.md) | The problem and the six stages |
| Teacher | [`L04-string-algorithms-and-cipher-live-program.py`](teacher/solutions/L04-string-algorithms-and-cipher-live-program.py), `Live4_Step1_Checks.py` … `Live4_Step5_ReportAndReceiver.py` | Full solution and five cumulative demo files |
| Teacher | [`live-slides-he.pdf`](lessons/L04-string-algorithms-and-cipher/live-slides-he.pdf) | 10-slide deck, five content + code-example pairs, no title slide (54 min; source [`L04-string-algorithms-and-cipher-live-source-slides.md`](teacher/L04-string-algorithms-and-cipher-live-source-slides.md)) |
| Student | [`paper-lab-worksheet-he.md`](lessons/L04-string-algorithms-and-cipher/paper-lab-worksheet-he.md), `PaperLab4_Starter.py` | One-sheet handwritten lab: five separate questions, each with its own string and task (3 + 2 per side, enlarged font; 45 min) |
| Teacher | [`L04-string-algorithms-and-cipher-paper-lab-teacher-guide-he.md`](teacher/L04-string-algorithms-and-cipher-paper-lab-teacher-guide-he.md) | Printable teacher guide (Hebrew, 6 pages): full solutions, expected output, accepted variants, common errors and points for the five questions and the challenge, grade scale, marking sheet |
| Teacher | [`challenge-he.pdf`](lessons/L04-string-algorithms-and-cipher/challenge-he.pdf), [`L04-string-algorithms-and-cipher-challenge-source-slides.md`](teacher/L04-string-algorithms-and-cipher-challenge-source-slides.md), [`PaperLab4_Challenge_Solution.py`](teacher/solutions/PaperLab4_Challenge_Solution.py) | One-slide early-finisher challenge for the wall projector (extra-large fonts, solved in Thonny, nothing written on paper): the mirror cipher `a`↔`z` |
| Teacher | [`L04-string-algorithms-and-cipher-paper-lab-answer-key.md`](teacher/L04-string-algorithms-and-cipher-paper-lab-answer-key.md), `PaperLab4_Q1_Solution.py` … `PaperLab4_Q5_Solution.py` | Key, 100-point rubric, one solution per question |

**Exam-review edition of Lessons 8.2–8.7 (built 20 Nov 2026; this is the edition for P1, Sun 22 Nov):** a 5-slide consolidation of exactly the strings material of the Ministry's מיקוד (chapter 5), then a five-question paper lab; it closes the strings block and prepares Quiz Q1 on 29 Nov. Out of scope on purpose: `startswith`, `endswith`, `isalpha`, `isnumeric`, `ord`, `chr`, `split`, `join`.

| For | File | What it is |
|---|---|---|
| Teacher | [`exam-review-slides-he.pdf`](lessons/L04-string-algorithms-and-cipher/exam-review-slides-he.pdf), [`L04-string-algorithms-and-cipher-exam-review-source-slides.md`](teacher/L04-string-algorithms-and-cipher-exam-review-source-slides.md) | 5-slide deck (45 min), code blocks to copy into Thonny |
| Student | [`exam-review-lab-he.md`](lessons/L04-string-algorithms-and-cipher/exam-review-lab-he.md), [`ExamReview_Starter.py`](exercises/ExamReview_Starter.py) | One-sheet handwritten lab: five questions (bug, e-mail, sentence, vowels, two loops), 2 + 3 per side, 45 min |
| Teacher | [`L04-string-algorithms-and-cipher-exam-review-answer-key.md`](teacher/L04-string-algorithms-and-cipher-exam-review-answer-key.md), `ExamReview_Q1_Solution.py` … `ExamReview_Q5_Solution.py` in [`teacher/solutions/`](teacher/solutions/) | Guide, accepted variants, 100-point rubric, marking sheet, one solution per question |

**Countdown edition of Lessons 8.2–8.7** (the countdown method of the teacher's DP1/PDP classes: four timed cases done together on a projected
page, each solved with `for` and with `while`; then a graded five-question worksheet):

| For | File | What it is |
|---|---|---|
| Teacher | [`L04-string-algorithms-and-cipher-countdown-lesson-plan.md`](teacher/L04-string-algorithms-and-cipher-countdown-lesson-plan.md) | Lesson plan: 48 min of cases, 37 min of worksheet, 5 min exit check |
| Teacher | [`L04-string-algorithms-and-cipher-countdown-he.html`](teacher/L04-string-algorithms-and-cipher-countdown-he.html) | The countdown page (open in a browser and project; generated — rebuild with [`tools/countdown`](../../tools/countdown/README.md)) |
| Student | [`countdown-cases-he.md`](lessons/L04-string-algorithms-and-cipher/countdown-cases-he.md) | The four cases as instructions, no solutions (generated; as `Countdown_Cases.pdf` in the Mashov zip `Downloads\python-b\Lessons 8.2–8.7 - Strings.zip`) |
| Teacher | [`L04-string-algorithms-and-cipher-countdown-cases.json`](teacher/L04-string-algorithms-and-cipher-countdown-cases.json) | The page's content: Hebrew titles and goals, minutes, test calls, how the two solutions differ |
| Student | [`FirstStarLast_Starter.py`](exercises/FirstStarLast_Starter.py), [`MiddleChar_Starter.py`](exercises/MiddleChar_Starter.py), [`Initials_Starter.py`](exercises/Initials_Starter.py), [`NumberCipher_Starter.py`](exercises/NumberCipher_Starter.py) | One file per case (generated): goal, test values, expected output — no `def`, the class has not learned functions yet |
| Teacher | [`Countdown_Reference.py`](teacher/solutions/Countdown_Reference.py) | Each case with `for` and with `while`, by different ideas (plain code, no functions) |
| Student | [`countdown-worksheet-he.md`](lessons/L04-string-algorithms-and-cipher/countdown-worksheet-he.md) | Hebrew worksheet: the `or` bug, count `is` without `count`, first and last four characters, last letter of every word, alternating case, bonus, exit check (Word copy for printing in `Downloads\python-b`) |
| Student | [`Worksheet_Starter.py`](exercises/Worksheet_Starter.py) | The `or "e"` bug (Q1) and a variable to write under for Q2–Q5 and the bonus (no functions) |
| Teacher | [`Worksheet_Reference.py`](teacher/solutions/Worksheet_Reference.py) | Solutions with expected values |
| Teacher | [`L04-string-algorithms-and-cipher-countdown-answer-key.md`](teacher/L04-string-algorithms-and-cipher-countdown-answer-key.md) | Answers, grading rubric (100 points + 5 bonus), marking sheet, what to look for |
