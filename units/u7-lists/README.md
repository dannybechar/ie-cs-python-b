# Unit 7 — Lists

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

10 academic hours = 5 meetings = 450 minutes (135 theory / 315 practice).

> **Reconciled 9 Nov 2026 to the official Python B program** — Lists part A (files 9.1, 9.3, 9.4, 9.5 and the printable operations help sheet) was delivered
> and is now built in; parts B, C, D (12.0–14.5) as before (see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Part E (list of lists) was not delivered. The code uses `def` (Unit 3 comes
> first in the schedule); no nested loops, no lists of lists, no `sort(key=...)` — each official item left out for that reason is recorded in the lesson notes
> ("Official items deliberately left out"). **Slides:** the five NotebookLM decks of the v1 build are superseded; the prep folders (`unit7-m1-slides` … `unit7-m5-slides`)
> were refreshed on 9 Nov 2026 — **all five decks need regeneration** in NotebookLM.

### Official items that exist only as links (not offline, nothing invented for them)

Titles as in the Ministry's `links.md`: **9.2** "תרגול לפיצוח | אינטראקטיבי" (genially matching game) · the **9.3** guided-exercise solution video "רשימה זוגית" ·
**12.2** "סרטון תרגול מודרך | סכום מיקום זוגי ואי זוגי" (YouTube, exam question 4 of תשפ"ה) · **12.3** "תרגול לפיצוח #1" (genially) ·
**12.4** "סרטון תרגול מודרך | הוספת מספר לרשימה" (YouTube, exam question 4 of תשפ"ה) · **13.4** "מאסטר פייתון | מסיבת ריקודים" (H5P) ·
**13.5** "מאסטר פייתון | איש תלוי" (genially) · **14.3** "תרגול לפיצוח #2" (H5P). The 12.5, 12.6, 13.2, 14.2, 14.4 worksheets and 9.4 are used as lab sources.

## Unit 7.1 — Lists

**Topic:** What Is a List? Creating, Indexing, Slicing

90 minutes: 45 knowledge + 45 lab · **hook (9.1) → `[]`/`list()`, mixed types → indices → update → `in`, `+` → slicing `[a:b:c]`, `[::-1]`, `[-4:-1]` → predict table (9.4 Q1–Q3)**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Lists_Starter.py`](Lists_Starter.py) | `==` vs `=` warm-up bug, the 9.4 predict table, Tasks 1–4 (report, bounds-checked update, slicing, `+`) |
| Teacher | [`Lists_Reference.py`](Lists_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

## Unit 7.2 — Lists

**Topic:** List Operations

90 minutes: 45 knowledge + 45 lab · **`append`/`insert` → `count`/`in`/`index` (case, first match) → `remove`/`pop` → `sort`/`reverse` → `list(text)` → `split`/`join` → the 13-row operations table**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Operations_Starter.py`](Operations_Starter.py) | `append(i)` NameError warm-up bug (the Ministry's own), Tasks 1–5 (new list, name occurrence, palindromes, the Sandwich challenge, the even list), if time: name letters, `split`/`join`/`random` |
| Teacher | [`Operations_Reference.py`](Operations_Reference.py) | Solutions, one function per task, plus the verified `demo()` and `table_demo()` (the 13 rows) |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | **Superseded** deck of the v1 build (14 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

## Unit 7.3 — Lists

**Topic:** Walking a List and the Accumulation Pattern

90 minutes: 45 knowledge + 45 lab · **by index vs. by value (13.0, 12.6 Q4) → accumulation → average → class names and Roni's prices (13.2) → the "change while looping" trap → copies**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Accumulate_Starter.py`](Accumulate_Starter.py) | `remove_even` skipping warm-up bug, Tasks 1–4 (two sums, average, duplicate class names, Roni's prices), if time: new list and sorted copy |
| Teacher | [`Accumulate_Reference.py`](Accumulate_Reference.py) | Solutions, one function per task, with the trace of the trap |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

## Unit 7.4 — Lists

**Topic:** Counting, Filters, Maximum, Flat Menus, Parallel Lists

90 minutes: Lab + Lab · **counter → maximum from the data → grades, presents, names (13.2) → one flat name/price list → parallel lists → worksheet 14.2 → challenge menu (`magic`, `remove_place_num`, `avg_stud` bug hunt …) → stretch: Robber, IP, encryption**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Stats_Starter.py`](Stats_Starter.py) | Max-initialized-to-0 warm-up bug, Tasks 1–6, the challenge menu (with a documented bug in `avg_stud`) and the stretch |
| Teacher | [`Stats_Reference.py`](Stats_Reference.py) | Solutions, tested on the edge cases |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

## Unit 7.5 — Lists

**Topic:** Linear Search, a New Phone Number, and the "AI Experiment Analyzer" — unit checkpoint

90 minutes: Lab + Lab · **linear search → early stop on sorted data, `index()` and the 14.4 Q10 ranking → phone numbers with `random` → the capstone project → exam-bank question**

| For | File | What it is |
|---|---|---|
| Teacher | [`m5-lesson-notes.md`](m5-lesson-notes.md) | Lesson plan |
| Student | [`m5-lab-brief-he.md`](m5-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Analyzer_Starter.py`](Analyzer_Starter.py) | Index-0-as-`False` warm-up bug, early-stop search and `position_in_ranking`, the phone-number task, the project brief, the 14.4 exam-bank choices |
| Teacher | [`Analyzer_Reference.py`](Analyzer_Reference.py) | Solutions; all 7 test cases verified |
| Teacher | [`m5-slides-he.pdf`](m5-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — **needs regeneration** (NotebookLM prep folder refreshed 9 Nov 2026) |

