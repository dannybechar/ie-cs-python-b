# Unit 5 — Strings

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (**90 theory / 270 practice**). Reworked from the Ministry's teaching materials 🔶
(built, awaiting approval).

## Unit 5.1 — Strings

**Topic:** A String Is an Ordered Sequence

90 minutes: 45 knowledge + 45 lab · **quotes → indices (+/−) → `len` → `+`/`*` → `int`/`str`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Indices_Starter.py`](Indices_Starter.py) | `word[len(word)]` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Indices_Reference.py`](Indices_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 18 slides) |

## Unit 5.2 — Strings

**Topic:** Slicing and Searching

90 minutes: 45 knowledge + 45 lab · **`[start:end:jump]` → `count` → `replace` → `in` → `find`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Slicing_Starter.py`](Slicing_Starter.py) | Discarded-`upper()` warm-up bug, stubs for Tasks 1–4 |
| Teacher | [`Slicing_Reference.py`](Slicing_Reference.py) | Solutions, one function per task |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 16 slides) |

## Unit 5.3 — Strings

**Topic:** More Methods and Walking Over a String with `for`

90 minutes: Lab + Lab · **`lower`/`upper` → `startswith`/`endswith` → `isalpha`/`isdigit` → `for` → counters → `+=`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Traverse_Starter.py`](Traverse_Starter.py) | Counter-reset warm-up bug, stubs for Tasks 1–5 |
| Teacher | [`Traverse_Reference.py`](Traverse_Reference.py) | Solutions, one function per task (Task 4 reads input) |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 15 slides) |

**Paper-classwork edition of 5.3** (a 45-minute lesson, then a printed worksheet done with the computer; the rest is homework):

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-classwork-lesson-plan.md`](m3-classwork-lesson-plan.md) | 45-minute lesson derived from the worksheet |
| Student | [`m3-classwork-worksheet-he.md`](m3-classwork-worksheet-he.md) | Hebrew worksheet: read and predict, write functions on paper, homework part (Word copy for printing in `Downloads\python-b`) |
| Teacher | [`m3-classwork-answer-key.md`](m3-classwork-answer-key.md) | Answers, trace table, what to look for while circulating, grading rubric (100 points + 10 bonus) and marking sheet |
| Student | [`string-commands-table-he.md`](string-commands-table-he.md) | One-page table of every string operation and method in the unit, each with a small example and result (Word copy for printing) |
| Student | [`Classwork_Starter.py`](Classwork_Starter.py) | Part A snippets, the counter-reset bug (B1), stubs for B2–B5 and homework |
| Teacher | [`Classwork_Reference.py`](Classwork_Reference.py) | Solutions with expected values |
| Teacher | slides | Pending (NotebookLM): 20 slides, 90 min; prep files (loose, beside the Word worksheet) in `Downloads\python-b\` (save the reviewed deck as `m3-classwork-slides-he.pdf`) |

## Unit 5.4 — Strings

**Topic:** String Algorithms, a Secret Code, and the Unit Checkpoint

90 minutes: Lab + Lab · **exercises 4–7 → `ord`/`chr` cipher → `split`/`join` (shown) → checkpoint**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including the checkpoint scoring |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Cipher_Starter.py`](Cipher_Starter.py) | `or "e"` warm-up bug, stubs for Tasks 1–6 and the checkpoint |
| Teacher | [`Cipher_Reference.py`](Cipher_Reference.py) | Solutions, one function per task, plus worksheet 8.2 enrichment |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 13 slides) |

**Countdown edition of 5.4** (the countdown method of the teacher's DP1/PDP classes: four timed cases done together on a projected
page, each solved with `for` and with `while`; then a graded five-question worksheet):

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-countdown-lesson-plan.md`](m4-countdown-lesson-plan.md) | Lesson plan: 48 min of cases, 37 min of worksheet, 5 min exit check |
| Teacher | [`m4-countdown-he.html`](m4-countdown-he.html) | The countdown page (open in a browser and project; generated — rebuild with [`tools/countdown`](../../tools/countdown/README.md)) |
| Student | [`m4-countdown-cases-he.md`](m4-countdown-cases-he.md) | The four cases as instructions, no solutions (generated; as `Countdown_Cases.pdf` in the Mashov zip `Downloads\python-b\Unit 5.4 - Strings.zip`) |
| Teacher | [`m4-countdown-cases.json`](m4-countdown-cases.json) | The page's content: Hebrew titles and goals, minutes, test calls, how the two solutions differ |
| Student | [`CountIs_Starter.py`](CountIs_Starter.py), [`Initials_Starter.py`](Initials_Starter.py), [`NextLetters_Starter.py`](NextLetters_Starter.py), [`FirstLastWord_Starter.py`](FirstLastWord_Starter.py) | One file per case (generated): goal, test values, expected output — no `def`, the class has not learned functions yet |
| Teacher | [`Countdown_Reference.py`](Countdown_Reference.py) | Each case with `for` and with `while`, by different ideas (plain code, no functions) |
| Student | [`m4-countdown-worksheet-he.md`](m4-countdown-worksheet-he.md) | Hebrew worksheet: the `or` bug, `middle`, `edges`, `last_letters`, `alternate_case`, bonus, exit check (Word copy for printing in `Downloads\python-b`) |
| Student | [`Worksheet_Starter.py`](Worksheet_Starter.py) | The `or "e"` bug (Q1) and a variable to write under for Q2–Q5 and the bonus (no functions) |
| Teacher | [`Worksheet_Reference.py`](Worksheet_Reference.py) | Solutions with expected values |
| Teacher | [`m4-countdown-answer-key.md`](m4-countdown-answer-key.md) | Answers, grading rubric (100 points + 5 bonus), marking sheet, what to look for |
