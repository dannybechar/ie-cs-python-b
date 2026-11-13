# Lessons 9.1–9.5, 12.0–14.5 — Lists

**10h = 3 Theory + 7 Practice = 5 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 7 (pp. 17–18); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reconciled 9 Nov 2026 to the official Python B program (Lists parts A, B, C, D: files 9.1, 9.3, 9.4, 9.5, the printable operations help sheet,
12.0, 12.1, 12.5, 12.6, 12.7, 13.0, 13.1, 13.2, 13.6, 14.0, 14.1, 14.2, 14.4, 14.5); awaiting re-approval. The v1 build (approved earlier) came from
`Downloads\python-b-codex\python_b_unit07_lists_complete_unit.md`; its linear search with `-1` and its capstone are kept as **course additions** (the Ministry files
never name them; the exam-bank question 14.4 Q10 is the official early-stop analogue). Decks: superseded, new NotebookLM decks pending (prep folders refreshed).

### Ministry file mapping

| Ministry file | What it holds | Used in |
|---|---|---|
| 9.1 (part A deck), 9.4 (worksheet) | the hook, `list()`/`[]`, mixed types, index table, slices `[1:3]`, `[-4:-1]`, `+`, `len`; the "write the output" tables Q1–Q3 | lessons 9.1, 9.4 |
| 9.1 pp. 9–43, help sheet, 9.3 | `count`, `in`, `index`, `remove`, `pop`, `append`, `insert`, `sort`, `reverse`, `list(text)`, `split`, `join`, the 13-row table; the **Sandwich** challenge; the "even list" | lessons 9.3, 9.5, 12.0–12.1 |
| 12.0 / 12.1 (part B) | maximum, average, the temperature filter, `in`, `+`, `join`/`split`, colours with `%`, palindrome list, name occurrence, name letters, phone numbers, `random.choice`, songs `sort()`, bug severities | lessons 9.3, 9.5, 12.0–12.1; 13.2, 14.0–14.2; 12.5, 14.4 |
| 12.5 (worksheet #2) | "A new phone number" steps a–c | lessons 12.5, 14.4 |
| 12.6 (master Python) | Q4 same-or-different `item`, Q5 duplicate names, Q6 clothes (flat name/price list) | lessons 12.6, 13.0–13.1; 13.2, 14.0–14.2 |
| 12.7, 13.6, 9.5 | short summaries | lessons 9.3, 9.5, 12.0–12.1; 12.6, 13.0–13.1 (closing slides) |
| 13.0 / 13.1 (part C), 13.2 | traversal by index and by value, `sum_listA/B`, class names, Roni's prices, grades, presents, names, menu | lessons 12.6, 13.0–13.1; 13.2, 14.0–14.2 |
| 14.0 / 14.1 (part D) | Robber language, IP address, encryption, three parallel lists, presents/grades/menu, evens first, 20% discount, `remove_even`, `remove_place_num`, `avg_stud`, the "magic list" | lessons 12.6, 13.0–13.1 (`remove_even`), lessons 13.2, 14.0–14.2 (everything else; Robber/IP/encryption as stretch) |
| 14.2 (worksheet) | Q1 half 0 / half 1, Q4 ascending, Q5 two lists equal, Q6 best grade, Q7 pass/fail (Q2, Q3: the above-average pattern) | lessons 13.2, 14.0–14.2 |
| 14.4 (exam bank) | Q3 shift right, Q4 strictly ascending (code is an image, ⚠️ not in the text), Q8 permutation, Q9 improvement, **Q10 early-stop ranking** | lessons 12.5, 14.4 |
| 14.5 (guided video slides) | words in a sentence with `split` | lessons 13.2, 14.0–14.2 |
| **Links only** | 9.2, 9.3 video, 12.2, 12.3, 12.4, 13.4 "dance party", 13.5 "hangman", 14.3 | titles in the README; nothing invented |
| **Not delivered** | Lists part E (list of lists) | left out anyway (rulebook) |

## Official topics and hours

Unit totals from the master table (3 theory / 7 practice). The chapter's own table sums to 4 theory + 6 practice
(what is a list 1/1, list operations 1/2, summation 1/2, linear search 1/1) — a hint disagreement of exactly the
kind the hours rule expects (`CLAUDE.md`); used only for the order and weight of topics. The source's own
meeting-by-meeting table follows its chapter hours literally (giving four Knowledge + Lab meetings and one Lab +
Lab); that pattern is adjusted here to fit the master table's 3/7 instead — see "Scope decisions".

| Topic (Ministry) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| מהי רשימה — what a list is, slicing | 1 / 1 | lessons 9.1, 9.4 (45 T + 45 P) | 45 / 45 | 🔶 |
| פעולות על רשימה — list operations | 1 / 2 | lessons 9.3, 9.5, 12.0–12.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| סכימת איברים — traversal, accumulation, counting, filters | 1 / 2 | lessons 12.6, 13.0–13.1 (45 T + 45 P), lessons 13.2, 14.0–14.2 (90 P) | 45 / 135 | 🔶 |
| חיפוש סדרתי — linear search, phone numbers, capstone | 1 / 1 | lessons 12.5, 14.4 (90 P) | 0 / 90 | 🔶 |
| **Total (master table)** | **3 / 7** | | **135 / 315** | |

Chapter goals (source §1, twelve in all):

1. Explain what a list is and its purpose → lessons 9.1, 9.4
2. Create an empty list or one with initial values → lessons 9.1, 9.4
3. Access an element by index and update an existing element → lessons 9.1, 9.4
4. Use `len` and `in` with lists → lessons 9.1, 9.4
5. Use `append`, `extend`, `insert`, `remove`, `pop`, `count`, `sort`, `reverse` appropriately → lessons 9.3, 9.5, 12.0–12.1
6. Convert text to a list with `split` and join strings with `join` → lessons 9.3, 9.5, 12.0–12.1
7. Traverse a list directly or by index → lessons 9.1, 9.4; 12.6, 13.0–13.1
8. Implement the summation, counting, average, minimum and maximum patterns → lessons 12.6, 13.0–13.1; 13.2, 14.0–14.2
9. Implement linear search, returning an index or `-1` → lessons 12.5, 14.4
10. Explain how a sorted list's order allows a search to stop early → lessons 12.5, 14.4
11. Split a solution into functions used as black boxes → every meeting; capstone in lessons 12.5, 14.4
12. Apply lists to AI experiment results, preparing for classification and recommenders → every meeting

## Lessons 9.1, 9.4 — Knowledge + Lab: What Is a List?
- why separate variables don't scale; `[]`, `list()`, a literal; `len`, indexing (positive and negative), updating an element and `IndexError`.
- `in` / `not in`; `+` (a new list); slicing `[start:stop:step]` and `[::-1]` (the same notation as strings, the strings block (lessons 7.1–8.7)).
- the two ways to walk a list, as a preview (full treatment in lessons 12.6, 13.0–13.1).
- the part-A hook and mixed types, the index table, `[1:3]`, `[-4:-1]`, `+` of three lists (9.1 pp. 3–9).
- lab: an `==`-instead-of-`=` warm-up bug, the 9.4 predict table, an AI-results report, a bounds-checked update, a slicing report, `+`.

## Lessons 9.3, 9.5, 12.0–12.1 — Knowledge + Lab: List Operations
- `append` / `insert` / `extend`; `count` / `in` / `index` (case-sensitive, first match, the `ValueError` and the `in` guard); `remove` / `pop` (returns the value); `sort` / `reverse` (in place, return `None`); `sort(reverse=True)`.
- building a new list in a loop; `list("text")`; `split` / `join`; `random.choice`; the 13-row table (9.1 pp. 42–43, help sheet).
- lab: the Ministry's `append(i)` NameError as the warm-up, `colder_than`, `name_check`, `all_palindromes`, the Sandwich challenge, the even list; if time: name letters, split/join/random.

## Lessons 12.6, 13.0–13.1 — Knowledge + Lab: Walking a List and Accumulation
- by index (`range(len(...))`) vs. by value; what `item` holds in each; the accumulation pattern; the average with an empty-list guard.
- the "change while looping" trap and its two fixes; `b = a` vs. `.copy()`; a sorted copy.
- lab: a `remove_even` warm-up bug (with its trace), `sum_by_index` / `sum_by_value` (+ the 12.6 Q4 question), `calculate_average`, class names (13.2 #1), Roni's prices (13.2 #2); if time `without_even`, `sorted_copy`.

## Lessons 13.2, 14.0–14.2 — Lab + Lab: Counting, Filters, Maximum, Flat Menus, Parallel Lists
- a counter that grows only when its condition holds; maximum from the first element, never from `0`.
- reports: grades (average, above average, at most 60, "Excellent!"), presents, `count_in_range`.
- one flat list name/price/name/price with even/odd index logic and the slices `[0::2]`, `[1::2]`; parallel lists and an average per student.
- names report (13.2 #5); worksheet 14.2 (Q1, Q4, Q6, Q7; Q5 as challenge); Odelia's clothes (12.6 Q6).
- challenge menu: `evens_first`, `discount_20`, `remove_place_num`, `magic`, `count_words`, `can_release`, an `avg_stud` bug hunt; stretch: Robber, IP address, encryption.

## Lessons 12.5, 14.4 — Lab + Lab: Linear Search, a New Phone Number, the "AI Experiment Analyzer"
- linear search returns an index or `-1`, never tested as a plain boolean; early stop on a sorted list (and the official 14.4 Q10 ranking); the built-in `index()` and its `ValueError`.
- "A new phone number": `random.choice`, `random.randint`, a taken list, a special list, `str.count`, a rising/falling run; split into functions.
- the unit's capstone (a course addition), combining every pattern from the unit, with the 20-point rubric; one exam-bank question (14.4 Q3 / Q4 / Q8 / Q9).

### Scope decisions
1. **Five meetings and 450 minutes are kept** (3 Knowledge + Lab, 2 Lab + Lab, from the master table: 135 theory + 315 practice). The Ministry's four lists lessons (parts A–D, 360 minutes)
   plus their worksheets and the exam bank are mapped onto them in the table above; the Ministry's own exercises are used wherever they exist.
2. **Part A is built in** (9 Nov 2026): the hook, mixed types, the index table, negative slices and the 9.4 predict table in lessons 9.1, 9.4; the 13-row table, `count`/`index`/`remove`
   first-match and case-sensitivity demos, `pop` returning its value, `sort(reverse=True)`, the Sandwich challenge and the even list in lessons 9.3, 9.5, 12.0–12.1.
3. **`def` is allowed**: the lists block (lessons 9.1–9.5, 12.0–14.5) follows the functions block (lessons 4.1–4.6) in the schedule, and the Ministry worksheets are written with `def`.
4. **Rulebook unchanged — no nested loops, no lists of lists, no tuples, sets, dictionaries, comprehensions, `enumerate`, `sort(key=...)`/`sorted(key=...)`.** Official items
   deliberately left out, each recorded in the lesson notes: nested loops (14.0 pp. 25–29), the list of lists (14.0 p. 30), `turtle.Turtle()` (12.0 p. 17), the 9.4 Q1 row that
   puts `list(range(2, 5))` inside a list, `sort(key=...)` of the exam help sheet. The restaurant menu is one **flat** list, as the Ministry's own exercise #7 gives it.
   Functions return **one** value (no tuples). The "magic list" (14.0 #13) and `avg_stud` (#12) are **not** lists of lists — they are in lessons 13.2, 14.0–14.2.
5. **Ministry-deck bugs are never copied as they stand**: `append(i)` for `append(item)` (12.0 p. 10) is used only as the lessons 9.3, 9.5, 12.0–12.1 warm-up; the old `index` error text (9.1 p. 14), the garbled
   `pop` default, `index = input()` into `insert`, `text.join(list)` worded backwards, curly quotes, stray parentheses, the stale `print(item, ...)` in the palindrome `else` branch,
   the wrong example averages on 14.0 p. 12 and the `begin += (1 + i)` solution on p. 23 (lessons 13.2, 14.0–14.2's bug hunt uses the last one deliberately; our `avg_stud` is fixed).
6. **Not offline, not invented**: 9.2, the 9.3 solution video, 12.2–12.4, 13.3–13.5, 14.3 (links only); part E; the answer keys of the worksheets; the image of the 14.4 Q4 code.
7. **Ministry stretch exercises placed in lessons 13.2, 14.0–14.2**: Robber language, IP address validation, the `replace` encryption (14.0 pp. 4–11), `remove_place_num`, `magic`, `avg_stud` bug hunt,
   `count_words` (14.5), bug-severity counting (12.1 p. 40).
8. **Kept from v1**: the `==` / `=` warm-up, the max-from-`0` warm-up, the index-0 search warm-up, linear search returning `-1` with early stop, the capstone
   "AI Experiment Analyzer" (**a course addition**, not Ministry material), its seven test cases and the 20-point rubric. **Dropped from v1**: the stand-alone safe-remove and `pop(0)`
   queue tasks and `build_report`.
9. **Meeting structure** follows the master table's 3 / 7 split (the chapter table's 4 / 6 is used only for the weight of topics), as in v1.

## Exit criteria
The student creates, indexes, updates and traverses a list; chooses correctly among `append`/`extend`/`insert` and
`remove`/`pop`; implements the summation, counting, minimum/maximum and average patterns, all starting from a
correct initial value; implements linear search (with early stop on a sorted list) and checks its result against
`-1`, never as a boolean; and splits a solution into small, tested functions.

## Checkpoint
Lessons 12.5, 14.4's "AI Experiment Analyzer" is the unit's capstone, with the source's own 20-point rubric (list creation and
input 3, list operations 3, accumulation and average 3, minimum and maximum 3, linear search 3, modularity 3,
testing and explanation 2) — see the lesson notes for the full rubric and performance bands. Verified here against
all seven of the source's own test cases (no data, a single item, invalid input mixed with valid, duplicates,
search success, search failure, and that sorting the copy never touches the original's order).

## Enrichment
From the source: also report the number of comparisons a search made; find the index of the highest score without
`max` or `.index()`; remove duplicates without using a `set`; merge two score lists into one sorted copy; build a
`while`-driven menu (add / remove / report / search); compare a full search against an early-stopping one by
comparison count.
