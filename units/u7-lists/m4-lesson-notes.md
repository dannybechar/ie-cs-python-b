# Lessons 13.2, 14.0–14.2 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v3 (reconciled to the official Python B program, 9 Nov 2026)
### Topic: Counting, Filters, Maximum, Flat Menus and Parallel Lists

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** Lab + Lab (a 6-minute recap, then demo → task → demo → task)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** Ministry **13.0 / 13.1** exercises #3–#6 (grades report, the birthday presents, names, the restaurant menu; worksheet
**13.2**), **14.0 / 14.1** exercises #4–#13 (three parallel grade lists, the presents/grades/menu again with 20 / 8 / 10 inputs, evens first,
a 20% discount, `remove_place_num`, `avg_stud`, the "magic list") and the Robber / IP / encryption exercises (14.0 pp. 4–11), worksheet **14.2**
(Q1, Q4, Q5, Q6, Q7), **14.5** (words in a sentence, `split`), **12.1 p. 40** (bug severities), **12.6 Q6** (Odelia's clothes) and **12.0 p. 6** (maximum
from the first element). Kept from v1: the maximum that starts at `0` as the warm-up bug, the counter that grows only when its condition holds,
`count_in_range`, the edge-case table. **Dropped from v1:** `build_report`.
**Ministry bugs not copied:** 14.0 p. 12 gives the averages `[90.5, 82.33, 82.0, 93.66, 100]` for `math = [100, 77, 85, 98, 100]`,
`comp = [95, 83, 77, 90, 100]`, `physics = [76, 87, 84, 93, 100]` — those lists really give `[90.33, 82.33, 82.0, 93.67, 100.0]`
(the slide's solution on p. 13 uses different numbers, `comp[0] = 80.5` and `physics[0] = 91`); the p. 23 solution of `avg_stud` advances with
`begin += (1 + i)`, which skips a grade per student — **our `avg_stud` uses `begin += count`**, and the broken version is the bug hunt (challenge g);
the Ministry's IP check (14.0 p. 9) crashes on `"a.b.c.d"` (`int()` of text) — ours tests `isdigit()` first; 12.6 Q6's sample list has broken quotes and
some prices as text — ours uses numbers. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Corrections to earlier notes:** the "magic list" (14.0 #13) is **not** a list of lists (it only compares three slices, `my_list[:size]`, `[size:size*2]`,
`[size*2:]`), and neither is `avg_stud`; both are now in the lab.
**Official items deliberately left out (rulebook):** 14.0 pp. 25–29 the **nested loop** `for i in names: for j in names` (matching names, `count // 2`) —
nested loops were dropped from the new program (clarifications p. 3); 14.0 p. 30 the announced **list of lists** (part E); the exam help sheet's
`sort(key=...)`. Where a Ministry exercise offers two solutions, the one with the single loop is used.
**Links only (not offline):** 13.3, 13.4 (dance party), 13.5 (hangman), 14.3 (H5P practice) — titles in the unit README.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** the functions block (lessons 4.1–4.6). Lists of lists and nested loops are **not** used: the menu is **one flat list** (name, price, name, price …),
exactly as the Ministry's own exercise #7 gives it.

---

## 1. Position in the lists block (lessons 9.1–9.5, 12.0–14.5)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 9.1, 9.4 | what a list is; indices; slicing | 45 / 45 |
| Lessons 9.3, 9.5, 12.0–12.1 | list operations | 45 / 45 |
| Lessons 12.6, 13.0–13.1 | walking a list; accumulation | 45 / 45 |
| **Lessons 13.2, 14.0–14.2 (this)** | **counting, filters, maximum, flat menu, parallel lists** | 0 / 90 |
| Lessons 12.5, 14.4 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 8: counting, average, minimum, maximum | ✅ every task |
| Goal 7: traverse by index or by value (choosing) | ✅ the menu needs the index, the grades do not |
| Goal 11: small functions as black boxes | ✅ |
| Goal 12: lists of AI experiment results | ✅ the closing question |

### Deliberate exclusions
Search (lessons 12.5, 14.4). Nested loops and the list of lists (14.0 pp. 25–30): official items left out, see the header. Challenge items g–j are enrichment.

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
avg_stud(l1, l2) fixed                         [68.33, 70.0, 76.25]   (the bug version: [68.33333333333333, 65.0, 42.5])
```

---

# 6. Lab (0–90)

Starter: [`Stats_Starter.py`](Stats_Starter.py). Reference: [`Stats_Reference.py`](Stats_Reference.py).
Time budget: tasks 1–6 are the core (about 75 minutes); the challenge menu and the stretch are for students who finish early.

## 0–5 — Recap and demo

Counter (`count = 0`, grows only when the condition holds), accumulation (lessons 12.6, 13.0–13.1), maximum from the first element (12.0 p. 6) — on the board with `[81, 24, 67, 91]`.

## 5–11 — Warm-up: the maximum that never updates

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

## 11–21 — Task 1: `grades_report(grades)` (Ministry 13.0 #3 / 14.0 #6 / 9.4 Q7)

Prints the average, the grades above the average, the grades that are 60 or less, and `Excellent!` when the average is above 90.
Test on `[95, 72, 88, 100, 45, 78, 96, 56]`, `[95, 100, 92, 98]` and `[]` (prints `No grades`). (The official exercise says "above 90" for the message
"הצטיינות יתרה"; the Ministry's 9.4 Q7 gap-fill version prints `Perfect` — we print `Excellent!`.)

## 21–29 — Task 2: `presents_report(presents)` and `count_in_range`

Total, average, and how many presents are above the average (Ministry 13.0 #4 / 14.0 #5). Then `count_in_range(values, low, high)` with both ends included (`2` for `[81, 24, 67, 91]`, 60 and 90).

## 29–39 — Task 3: names (Ministry 13.2 #5)

`names_report(full_names)` on full names `"First Last"`: how many contain `"el"` (ignoring case, as the official examples Elinor, Eliyahu, Batel, Israel require),
how many are longer than 7 characters (the space counts), how many have a first and last name starting with the same letter (`split()`).
Verified on `["Elinor Cohen", "Dana Dikla", "Batel Levi", "Israel Israeli", "Carmi Cohen", "Eliyahu Katz", "Avi Li", "Noa Levi", "Dan Dror", "Mor Gil"]`:
`4`, `8`, `4`.

## 39–43 — Demo: one flat list

`menu = ["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18]` — which positions hold names and which hold prices? Show the loop with `index % 2 == 1`, and the shortcut: `menu[0::2]` and `menu[1::2]`.

## 43–57 — Task 4: the menu (Ministry 13.0 #6 / 14.0 #7, and 12.6 Q6)

(a) `read_menu(count)` reads a name and a price per dish into **one flat list**; (b) `print_most_expensive(menu)` → `Most expensive: cornflakes 20`;
(c) `average_price(menu)` → `15.75`; (d) `names_above_average(menu)` → `['cornflakes', 'eggs']`; (e) Odelia's clothes (12.6 Q6): the total by index and by value,
and the item names: `274.29`, `274.29`, then the five names. Finish with the slicing shortcut.

## 57–60 — Demo: parallel lists

Three lists, one student per position: how do you reach student 3's three grades?

## 60–70 — Task 5: `student_averages(math, comp, physics)` (Ministry 14.0 #4)

Returns a new list with every student's average rounded to 2 decimals: `[90.33, 82.33, 82.0, 93.67, 100.0]`.

## 70–80 — Task 6: worksheet 14.2 (choose two)

Q1 `half_zero_one(8)` → `[0, 0, 0, 0, 1, 1, 1, 1]`; Q4 `is_ascending` (`True` for `[11, 22, 33, 44]`, `False` for `[11, 22, 77, 44]`; the 14.4 Q4 in lessons 12.5, 14.4 asks for **strictly**
ascending, so say now that equal neighbours are allowed here); Q6 `best_grades(grade_a, grade_b)` (the 25-student input of the original is replaced by two ready lists:
`[90, 60, 70]` and `[80, 75, 70]` → `[90, 75, 70]`); Q7 `pass_fail(numbers)` (above 55 passes; `[90, 55, 56, 40]` → pass `[90, 56]`, fail `[55, 40]`; a function returns
one value, so it prints both lists). Q2 and Q3 are the "above the average" pattern of Task 2 and are not repeated; Q5 (two lists equal, two ways — `==` and a loop,
`same_items` / `same_items_loop` in the reference) is a good challenge.

## 80–86 — Challenge menu (students choose; the teacher walks around)

Verified in `Stats_Reference.py`: (a) `evens_first([5, 2, 8, 1, 4])` → `[2, 8, 4, 5, 1]`; (b) `discount_20([100, 50])` → `[80.0, 40.0]`;
(c) `remove_place_num([0, 1, 2, 3, 4, 5, 6])` → `[1, 2, 4, 5]` (positions are zero-based, so position 0 is deleted too; the in-place variant walks **backwards**
and gives the same result — the answer to the lessons 12.6, 13.0–13.1 trap); (d) `magic` → `True` for `[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]`, `False` for `[]`, `[1, 2, 3, 1, 2, 4]`, `[1, 2]`;
(e) `count_words("the quick brown fox")` → `4` (14.5); (f) `can_release` on a list of bug kinds (12.1 p. 40) — the Ministry gives no list, so any list will do;
(g) **bug hunt:** `avg_stud(l1, l2)` should give `[68.33, 70.0, 76.25]` for `[80, 35, 90, 85, 55, 75, 60, 80, 90]` and `[3, 2, 4]`; the broken version gives
`[68.33333333333333, 65.0, 42.5]` — `begin += 1 + count` skips a grade.

**Stretch (strings and `split`, Ministry 14.0 pp. 4–11):** (h) `robber("cat")` → `cocatot`, `robber("have fun")` → `hohavove fofunon` (uppercase vowels are not handled —
the official statement lists only `aeiou`); (i) `valid_ip` → `True` for `192.168.0.17`; `False` for `192.890.0.17`, `192.890.0.17.89`, `192.890`, `a.b.c.d`; (j) `encrypt("THE PARTY IS TODAY AT MIDNIGHT")` →
`@H& P%R@Y IS @OD%Y %@ MIDNIGH@` (three `replace` calls, each for capital and small letters).

### Edge cases to test (any task)

| List | What to check |
|---|---|
| `[]` | no division by zero; maximum and minimum return `None` |
| `[50]` | average, minimum and maximum are 50 |
| `[7, 7, 7]` | minimum and maximum are equal |
| `[-5, -2, -9]` | the maximum is `-2`, not `0` |

## 86–90 — Save and exit check

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
- Two of the 14.2 questions solved
- (challenge) The bug in `avg_stud` found and explained
- Exit check
