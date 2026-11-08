# Unit 7 — Lists

**10h = 3 Theory + 7 Practice = 5 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 7 (pp. 17–18); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked 8 Nov 2026 to the Ministry teaching materials (Lists parts B, C, D: files 12.0, 12.1, 12.5, 12.6, 12.7, 13.0, 13.1, 13.6,
14.0, 14.1); awaiting re-approval. The v1 build (approved earlier) came from `Downloads\python-b-codex\python_b_unit07_lists_complete_unit.md`;
its linear search and capstone are kept because the Ministry files are silent there. Decks: superseded, new NotebookLM decks pending.

### Ministry file mapping

| Ministry file | What it holds | Used in |
|---|---|---|
| 12.0 / 12.1 (part B) | `list()`, `append`, `insert`, indexing, `[a:b:c]`, `[::-1]`, max, average, the temperature filter, `in`, `+`, `join`/`split`, colours with `%`, operations summary, palindrome list, name occurrence, name-letter comparison, phone numbers, `random.choice` | 7.1, 7.2, 7.5 |
| 12.5 (worksheet #2) | "A new phone number" steps a–c | 7.5 |
| 12.6 (master Python) | Q5 duplicate names, Q6 clothes (flat name/price list, total by index and by value) | 7.2, 7.4 |
| 12.7, 13.6 | short summaries | 7.2, 7.3 (closing slides) |
| 13.0 / 13.1 (part C) | traversal by index and by value, `sum_listA/B`, class names, Roni's prices, grades, presents, names, menu | 7.3, 7.4 |
| 14.0 / 14.1 (part D) | Robber language, IP address, encryption, three parallel lists, presents/grades/menu, evens first, 20% discount, `remove_even`, `remove_place_num`, grouped grades, "magic list", nested-loop preview | 7.3 (`remove_even`), 7.4 (parallel lists, filters, menu, evens first, discount, grouped grades) |
| **Not delivered** | Lists part A, part E (list of lists), worksheets 12.2–12.4, 13.2–13.5, 14.2 onward, and the Colab projects "dance party" / "hangman" of 13.x | assumed: part A = our 7.1 basics; part E and the projects are left out |

Robber language, IP address validation and the encryption exercise (14.0 pp. 4–11) use string methods and `split`; they are **not** built here
(they belong to the strings theme, Unit 5); they are enrichment for fast students.

## Official topics and hours

Unit totals from the master table (3 theory / 7 practice). The chapter's own table sums to 4 theory + 6 practice
(what is a list 1/1, list operations 1/2, summation 1/2, linear search 1/1) — a hint disagreement of exactly the
kind the hours rule expects (`CLAUDE.md`); used only for the order and weight of topics. The source's own
meeting-by-meeting table follows its chapter hours literally (giving four Knowledge + Lab meetings and one Lab +
Lab); that pattern is adjusted here to fit the master table's 3/7 instead — see "Scope decisions".

| Topic (Ministry) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| מהי רשימה — what a list is, slicing | 1 / 1 | 7.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| פעולות על רשימה — list operations | 1 / 2 | 7.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| סכימת איברים — traversal, accumulation, counting, filters | 1 / 2 | 7.3 (45 T + 45 P), 7.4 (90 P) | 45 / 135 | 🔶 |
| חיפוש סדרתי — linear search, phone numbers, capstone | 1 / 1 | 7.5 (90 P) | 0 / 90 | 🔶 |
| **Total (master table)** | **3 / 7** | | **135 / 315** | |

Chapter goals (source §1, twelve in all):

1. Explain what a list is and its purpose → 7.1
2. Create an empty list or one with initial values → 7.1
3. Access an element by index and update an existing element → 7.1
4. Use `len` and `in` with lists → 7.1
5. Use `append`, `extend`, `insert`, `remove`, `pop`, `count`, `sort`, `reverse` appropriately → 7.2
6. Convert text to a list with `split` and join strings with `join` → 7.2
7. Traverse a list directly or by index → 7.1, 7.3
8. Implement the summation, counting, average, minimum and maximum patterns → 7.3–7.4
9. Implement linear search, returning an index or `-1` → 7.5
10. Explain how a sorted list's order allows a search to stop early → 7.5
11. Split a solution into functions used as black boxes → every meeting; capstone in 7.5
12. Apply lists to AI experiment results, preparing for classification and recommenders → every meeting

## Unit 7.1 — Knowledge + Lab: What Is a List?
- why separate variables don't scale; `[]`, `list()`, a literal; `len`, indexing (positive and negative), updating an element and `IndexError`.
- `in` / `not in`; `+` (a new list); slicing `[start:stop:step]` and `[::-1]` (the same notation as strings, Unit 5).
- the two ways to walk a list, as a preview (full treatment in 7.3).
- lab: an `==`-instead-of-`=` warm-up bug, an AI-results report, a bounds-checked update, a slicing report, `+` and `list()`.

## Unit 7.2 — Knowledge + Lab: List Operations
- `append` / `insert` / `extend`; `count` / `index` (with the `ValueError` and the `in` guard); `remove` / `pop`; `sort` / `reverse` (in place, return `None`).
- building a new list in a loop; `split` / `join`; `list("text")`; `random.choice`.
- lab: the Ministry's `append(i)` NameError as the warm-up, `colder_than`, `join_class` (duplicate names), `all_palindromes`, split/join/random.

## Unit 7.3 — Knowledge + Lab: Walking a List and Accumulation
- by index (`range(len(...))`) vs. by value; what `item` holds in each; the accumulation pattern; the average with an empty-list guard.
- the "change while looping" trap and its two fixes; `b = a` vs. `.copy()`; a sorted copy.
- lab: a `remove_even` warm-up bug (with its trace), `sum_by_index` / `sum_by_value`, `calculate_average`, Roni's prices, `without_even`, `sorted_copy`.

## Unit 7.4 — Lab + Lab: Counting, Filters, Maximum, Flat Menus, Parallel Lists
- a counter that grows only when its condition holds; maximum from the first element, never from `0`.
- reports: grades (average, above average, at most 60, "Excellent!"), presents, `count_in_range`.
- one flat list name/price/name/price with even/odd index logic and the slices `[0::2]`, `[1::2]`; parallel lists and an average per student.
- if time: `evens_first`, `discount_20`, a bug hunt in the grouped-grades solution.

## Unit 7.5 — Lab + Lab: Linear Search, a New Phone Number, the "AI Experiment Analyzer"
- linear search returns an index or `-1`, never tested as a plain boolean; early stop on a sorted list; the built-in `index()` and its `ValueError`.
- "A new phone number": `random.choice`, `random.randint`, a taken list, a special list, `str.count`, a rising/falling run; split into functions.
- the unit's capstone, combining every pattern from the unit, with the 20-point rubric.

### Scope decisions
1. **Five meetings and 450 minutes are kept** (3 Knowledge + Lab, 2 Lab + Lab, from the master table). The Ministry's parts B, C, D (about three
   of its own meetings plus worksheets) are mapped onto them in the table above; where the Ministry is silent (linear search, the capstone) the
   v1 content stays.
2. **Missing items added** (the audit of 8 Nov 2026): list slicing `[a:b:c]` and `[::-1]`, `list()`, `[]`, `index()`, `+`, `random.choice`, the flat
   alternating name/price menu with even/odd index logic, parallel lists and the average per student, the duplicate-name input check, the
   above-average and at-most-60 filters, the "evens first" list, the 20% discount, the `remove_even` mutation trap, the palindrome-list task.
3. **`def` is allowed**: Unit 7 follows Unit 3 in the schedule, and the Ministry worksheets are written with `def`.
4. **Rulebook unchanged — no nested loops, no lists of lists, no tuples, sets, dictionaries, comprehensions, `enumerate`, `sorted(key=...)`.** The Ministry
   previews nested loops (14.0 pp. 25–29, "will be learned later") and announces a list of lists in part E (not delivered); the course leaves both out. The
   restaurant menu is one **flat** list, as the Ministry's own exercise #7 gives it. Functions return **one** value (no tuples).
5. **Ministry-deck bugs are never copied as they stand**: `append(i)` for `append(item)` (12.0 p. 10) is used only as the 7.2 warm-up; the
   curly quotes, stray parentheses, the stale `print(item, ...)` in the palindrome `else` branch, the wrong example averages on 14.0 p. 12 and the
   `begin += (1 + i)` solution on p. 23 are documented in the lesson notes (7.4's bug hunt uses the last one deliberately).
6. **Not delivered, not invented**: Lists part A (assumed to be the 7.1 basics), part E, the numbered worksheets and their keys, and the Colab
   projects "dance party" and "hangman" (13.2–13.5). Ask the teacher for them before the next rework.
7. **Ministry exercises left as enrichment**: Robber language, IP address validation, the replace-based encryption (14.0 pp. 4–11, string work), `remove_place_num`, the
   "magic list" and the Turtle colour list (12.0 pp. 16–17, which uses `turtle.Turtle()`, against the course's Turtle rule).
8. **Kept from v1**: the `==` / `=` warm-up, the max-from-`0` warm-up, the index-0 search warm-up, linear search with early stop, the capstone
   "AI Experiment Analyzer", its seven test cases and the 20-point rubric. **Dropped from v1**: the stand-alone safe-remove and `pop(0)` queue tasks and
   `build_report` (replaced by Ministry exercises of the same weight).
9. **Meeting structure** follows the master table's 3 / 7 split (the chapter table's 4 / 6 is used only for the weight of topics), as in v1.

## Exit criteria
The student creates, indexes, updates and traverses a list; chooses correctly among `append`/`extend`/`insert` and
`remove`/`pop`; implements the summation, counting, minimum/maximum and average patterns, all starting from a
correct initial value; implements linear search (with early stop on a sorted list) and checks its result against
`-1`, never as a boolean; and splits a solution into small, tested functions.

## Checkpoint
7.5's "AI Experiment Analyzer" is the unit's capstone, with the source's own 20-point rubric (list creation and
input 3, list operations 3, accumulation and average 3, minimum and maximum 3, linear search 3, modularity 3,
testing and explanation 2) — see the lesson notes for the full rubric and performance bands. Verified here against
all seven of the source's own test cases (no data, a single item, invalid input mixed with valid, duplicates,
search success, search failure, and that sorting the copy never touches the original's order).

## Enrichment
From the source: also report the number of comparisons a search made; find the index of the highest score without
`max` or `.index()`; remove duplicates without using a `set`; merge two score lists into one sorted copy; build a
`while`-driven menu (add / remove / report / search); compare a full search against an early-stopping one by
comparison count.
