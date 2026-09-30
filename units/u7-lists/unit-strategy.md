# Unit 7 — Lists

**10h = 3 Theory + 7 Practice = 5 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 7 (pp. 17–18); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 5 meetings built and approved by the teacher.
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit07_lists_complete_unit.md` —
one detailed document covering all five meetings, including its own exact 90-minute clock tables and meeting split.

## Official topics and hours

Unit totals from the master table (3 theory / 7 practice). The chapter's own table sums to 4 theory + 6 practice
(what is a list 1/1, list operations 1/2, summation 1/2, linear search 1/1) — a hint disagreement of exactly the
kind the hours rule expects (`CLAUDE.md`); used only for the order and weight of topics. The source's own
meeting-by-meeting table follows its chapter hours literally (giving four Knowledge + Lab meetings and one Lab +
Lab); that pattern is adjusted here to fit the master table's 3/7 instead — see "Scope decisions".

| Topic (Ministry) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| מהי רשימה — what a list is | 1 / 1 | 7.1 (45 T + 45 P) | 45 / 45 | ✅ |
| פעולות על רשימה — list operations | 1 / 2 | 7.2 (45 T + 45 P) | 45 / 45 | ✅ |
| סכימת איברים — the accumulation pattern | 1 / 2 | 7.3 (45 T + 45 P), 7.4 (90 P) | 45 / 135 | ✅ |
| חיפוש סדרתי — linear search | 1 / 1 | 7.5 (90 P) | 0 / 90 | ✅ |
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
- why separate variables don't scale for a growing collection of results; creating a list (empty, or with initial
  values); `len`, indexing (positive and negative), updating an element.
- `in` / `not in`, `count`; a direct loop vs. an index loop, same distinction as strings (Unit 5).
- lab: an `==`-instead-of-`=` warm-up bug, a small AI-results report, a bounds-checked update function.

## Unit 7.2 — Knowledge + Lab: List Operations
- `append` (one item) vs. `extend` (items from a collection) vs. `insert` (at a position); `remove` (by value,
  check first) vs. `pop` (by index, returns the removed value); `sort`/`reverse` mutate in place and return `None`.
- `split` (a string method returning a list) and `join` (a string method that joins list items with a separator).
- lab: a `sort()`-returns-`None` warm-up bug, a safe-remove function, a task-queue built with `pop(0)`, a
  split/join round trip.

## Unit 7.3 — Knowledge + Lab: Advanced Operations + the Accumulation Pattern
- why removing from a list while directly looping over it skips elements — build a new list instead; `.copy()` (or
  `[:]`) before sorting when the original order must survive.
- the accumulation pattern: initialize before the loop, update every iteration, use the result after the loop;
  `calculate_total` and `calculate_average` (with an empty-list guard).
- lab: a remove-while-iterating warm-up bug (with a dramatic wrong result), a sort-without-losing-the-original task,
  the summation/average functions.

## Unit 7.4 — Lab + Lab: Counting, Minimum, Maximum, a Report
- a counter that grows only when its condition holds; minimum/maximum initialized from the list's **own first
  element** — never from `0`, which silently breaks on an all-negative list.
- combining several small functions into one text report.
- lab: a max-initialized-to-`0` warm-up bug (using the source's own all-negative edge case), counting functions,
  `find_minimum`, `build_report` — tested against the source's own four edge cases.

## Unit 7.5 — Lab + Lab: Linear Search + the "AI Experiment Analyzer" (unit checkpoint)
- linear search: check each element in order, return its index on the first match, `-1` if the loop finishes
  without one; never test the result as a plain boolean (index `0` is falsy in Python, but a valid, successful
  result).
- on a **sorted** list, stop as soon as the current element is no longer less than the target.
- lab: an index-`0`-treated-as-`False` warm-up bug, early-stop search, then the "AI Experiment Analyzer" — the
  unit's capstone, combining every pattern from the unit.

### Scope decisions
- **The source document is the only material and is unusually complete** — clock tables (verified to sum to 90 for
  each meeting), worked code, common mistakes, a project rubric and closing summary questions. Followed closely;
  adapted into the house lesson-notes/lab-brief split and warm-up-bug convention.
- **Meeting structure changed from the source's own table to fit the master-table hours.** The source's own plan
  gives meetings 1–3 Knowledge + Lab and meetings 4–5 mixed/Lab + Lab in a way that sums to 4 theory + 6 practice
  hours (its chapter table's own total, not the master table's 3/7). Since the hours rule (`CLAUDE.md`) requires the
  master table's split, this build instead makes 7.1–7.3 Knowledge + Lab and 7.4–7.5 Lab + Lab (3 × 45 min theory =
  135 min = 3 h; 3 × 45 + 2 × 90 = 315 min = 7 h practice). This keeps every one of the source's own examples, tasks
  and edge cases in the same relative place — only the theory/practice label per meeting changes, and 7.5's search
  explanation moves into that meeting's guided-practice minutes rather than a separate 45-minute Knowledge block
  (linear search is a small addition to an already-familiar loop-and-compare pattern, the same way Unit 5's slicing
  and traversal meetings handled new syntax within Lab + Lab).
- **Not taught:** lists of lists, list comprehensions, tuples, sets, dictionaries — all outside this course (moved
  to Part C, per `clarifications-tashpaz-he.pdf` p. 3, or simply not in this program). Binary search is deliberately
  **not** built; only the early-stop linear search the source specifies.

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
