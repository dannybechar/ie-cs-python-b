# Unit 7.4 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Counting, Filters, Maximum, Flat Menus and Parallel Lists

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** Lab + Lab (a 6-minute recap, then demo → task → demo → task)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** Ministry **13.0 / 13.1** exercises #3–#6 (grades report, the birthday presents, names, the restaurant menu),
**14.0 / 14.1** exercises #4–#13 (three parallel grade lists, the presents/grades/menu again with 20 / 8 / 10 inputs, evens first,
a 20% discount, the grouped-grades exercise), and **12.0 p. 6** (maximum from the first element). Kept from v1: the maximum that starts at
`0` as the warm-up bug, the counter that grows only when its condition holds, `count_in_range`, the edge-case table. **Dropped from v1:**
`build_report` (the new tasks give the same practice with the Ministry's own wording). **New (audit):** the above-average and
at-most-60 filters, the flat alternating name/price menu with even/odd index logic, parallel lists and their average per student,
`evens_first`, the 20% discount, a bug hunt in the grouped-grades solution.
**Ministry bugs not copied:** 14.0 p. 12 gives the averages `[90.5, 82.33, 82.0, 93.66, 100]` for `math = [100, 77, 85, 98, 100]`,
`comp = [95, 83, 77, 90, 100]`, `physics = [76, 87, 84, 93, 100]` — those lists really give `[90.33, 82.33, 82.0, 93.67, 100.0]`
(the slide's solution on p. 13 uses different numbers, `comp[0] = 80.5` and `physics[0] = 91`); and the p. 23 solution of the
grouped-grades exercise advances with `begin += (1 + i)`, which skips a grade per student — used here as the bug hunt in Task 5c.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3). Lists of lists and nested loops are **not** used: the menu is **one flat list** (name, price, name, price …),
exactly as the Ministry's own exercise #7 gives it; the Ministry previews nested loops and a list of lists in part E (not delivered) and
we leave them out.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | what a list is; indices; slicing | 45 / 45 |
| 7.2 | list operations | 45 / 45 |
| 7.3 | walking a list; accumulation | 45 / 45 |
| **7.4 (this)** | **counting, filters, maximum, flat menu, parallel lists** | 0 / 90 |
| 7.5 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 8: counting, average, minimum, maximum | ✅ every task |
| Goal 7: traverse by index or by value (choosing) | ✅ the menu needs the index, the grades do not |
| Goal 11: small functions as black boxes | ✅ |
| Goal 12: lists of AI experiment results | ✅ the closing question |

### Deliberate exclusions
Search (7.5). `remove_place_num` (14.0 exercise #11) is left as enrichment; the list-of-lists "magic list" (#13) is left out.

---

## 3. Lesson Goal

**A counter grows only when its condition holds; a maximum starts from a real value of the list, never from `0`; and when the data
sits in one flat list, the index tells what kind of item you are looking at (even position = name, odd position = price).**

---

## 4. Core Mental Models

```python
def find_maximum(values):
    if len(values) == 0:
        return None
    largest = values[0]            # a REAL value of the list, not 0
    for value in values:
        if value > largest:
            largest = value
    return largest
```

```python
menu = ["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18]
# even index: the name           odd index: the price
for index in range(len(menu)):
    if index % 2 == 1:
        print(menu[index - 1], menu[index])     # the name sits just before its price
```

- With all-negative values `largest = 0` is never beaten and the function returns a number that is not even in the list.
- Parallel lists: position `k` in `math`, `comp` and `physics` belongs to the same student — walk **by index** over any one of them.
- Verified results (all from `Stats_Reference.py`):

```text
find_maximum([-5, -2, -9])                                   -2        (the bug version prints 0)
grades_report([95, 72, 88, 100, 45, 78, 96, 56])             Average: 78.75 / Above average: [95, 88, 100, 96] / 60 or less: [45, 56]
grades_report([95, 100, 92, 98])                             Average: 96.25 / Above average: [100, 98] / 60 or less: [] / Excellent!
presents_report([200, 150, 300, 50, 100, 250, 500, 120, 80, 350])   Total: 2100 / Average: 210.0 / Above average: 4
count_in_range([81, 24, 67, 91], 60, 90)                     2
print_most_expensive(menu)                                   Most expensive: cornflakes 20
average_price(menu)  15.75        names_above_average(menu)  ['cornflakes', 'eggs']
menu[0::2]  ['milk', 'bread', 'cornflakes', 'eggs']          menu[1::2]  [15, 10, 20, 18]
student_averages(math, comp, physics)                        [90.33, 82.33, 82.0, 93.67, 100.0]
evens_first([5, 2, 8, 1, 4])  [2, 8, 4, 5, 1]                discount_20([100, 50])  [80.0, 40.0]
group_averages(grades, counts) fixed                         [68.33, 70.0, 76.25]   (the bug version: [68.33333333333333, 65.0, 42.5])
```

---

# 6. Lab (0–90)

Starter: [`Stats_Starter.py`](Stats_Starter.py). Reference: [`Stats_Reference.py`](Stats_Reference.py).

## 0–6 — Recap and demo

Counter (`count = 0`, grows only when the condition holds), accumulation (7.3), maximum from the first element — on the board with `[81, 24, 67, 91]`.

## 6–14 — Warm-up: the maximum that never updates

```python
def find_maximum(values):
    largest = 0
    for value in values:
        if value > largest:
            largest = value
    return largest


print(find_maximum([-5, -2, -9]))
```

Predict `-2`, run, get `0` — `0` is bigger than every negative value. Fix: `largest = values[0]`.

## 14–26 — Task 1: `grades_report(grades)` (Ministry 13.0 #3 / 14.0 #6)

Prints the average, the grades above the average, the grades that are 60 or less, and `Excellent!` when the average is above 90.
Test on `[95, 72, 88, 100, 45, 78, 96, 56]`, `[95, 100, 92, 98]` and `[]` (prints `No grades`).

## 26–34 — Task 2: `presents_report(presents)` and `count_in_range`

Total, average, and how many presents are above the average (Ministry 13.0 #4 / 14.0 #5). Then `count_in_range(values, low, high)` with both ends included (`2` for `[81, 24, 67, 91]`, 60 and 90).

## 34–39 — Demo: one flat list

`menu = ["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18]` — which positions hold names and which hold prices? Show the loop with `index % 2 == 1`, and the shortcut: `menu[0::2]` and `menu[1::2]`.

## 39–57 — Task 3: the menu (Ministry 13.0 #6 / 14.0 #7)

(a) `print_most_expensive(menu)` → `Most expensive: cornflakes 20`; (b) `average_price(menu)` → `15.75`; (c) `names_above_average(menu)` → `['cornflakes', 'eggs']`. Finish with the slicing shortcut.

## 57–61 — Demo: parallel lists

Three lists, one student per position: how do you reach student 3's three grades?

## 61–73 — Task 4: `student_averages(math, comp, physics)` (Ministry 14.0 #4)

Returns a new list with every student's average rounded to 2 decimals: `[90.33, 82.33, 82.0, 93.67, 100.0]`.

## 73–85 — Task 5 (if time, choose at least one)

(a) `evens_first(values)` — new list, evens first (`[5, 2, 8, 1, 4]` → `[2, 8, 4, 5, 1]`); (b) `discount_20(prices)` — new list, 20% off
(`[100, 50]` → `[80.0, 40.0]`); (c) **bug hunt:** `group_averages(grades, counts)` should give `[68.33, 70.0, 76.25]` for
`[80, 35, 90, 85, 55, 75, 60, 80, 90]` and `[3, 2, 4]`; it gives `[68.33333333333333, 65.0, 42.5]` — find the bug (`begin += 1 + count` skips a grade).

### Edge cases to test (any task)

| List | What to check |
|---|---|
| `[]` | no division by zero; maximum and minimum return `None` |
| `[50]` | average, minimum and maximum are 50 |
| `[7, 7, 7]` | minimum and maximum are equal |
| `[-5, -2, -9]` | the maximum is `-2`, not `0` |

## 85–90 — Save and exit check

Save As `G8_U7_M4_Stats_<Name>.py`.

1. What is a counter's initial value?
2. How do you initialize a maximum on a non-empty list?
3. In the flat menu, which positions hold prices?
4. What does `menu[1::2]` give?
5. Why is a similarity score from a model not a probability?

**Answers:** `0`; `values[0]`; odd positions; all the prices; it is one model's number for closeness of meaning, not a chance of being right — check it, don't trust it blindly.

### Tool Note – Thonny
Run `find_maximum([])` in the Shell to confirm it returns `None`; test every function alone before combining them.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A counter should grow on every iteration | It grows only when its condition holds |
| `0` is a safe start for a maximum | It fails when all values are negative — start from `values[0]` |
| Parallel lists can be walked by value | You need the position to reach the same student in the other lists |
| In the flat menu, `menu[index]` is always a price | Only at odd positions; the name is at `index - 1` |
| A filter changes the original list | Build a new list; the original stays |
| An empty list can be skipped | Handle it, or the average divides by zero |

---

# 8. Assessment Evidence (formative)

- The warm-up's wrong `0` explained by the negative numbers
- `grades_report` correct on all three tests, including `[]`
- The menu functions use even/odd index logic correctly
- `student_averages` matches `[90.33, 82.33, 82.0, 93.67, 100.0]`
- The bug in `group_averages` found and explained
- Exit check
