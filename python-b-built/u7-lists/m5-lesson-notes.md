# Unit 7.5 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Linear Search + the "AI Experiment Analyzer" (Unit Checkpoint)

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** Lab + Lab (24 min guided practice, then 66 min lab, including the capstone project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit07_lists_complete_unit.md`, meeting 5 — its own clock table, the
linear-search example (with the index-`0`-as-`False` warning), the early-stop sorted search with its trace table,
the full project brief, skeleton, solution and seven-case test table, the peer-review checklist and the closing
reflection kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | a list as an ordered, dynamic collection; indices; traversal | 45 / 45 |
| 7.2 | list operations: append/extend/insert, remove/pop, sort/reverse, split/join | 45 / 45 |
| 7.3 | advanced operations + the accumulation pattern | 45 / 45 |
| 7.4 | counting, minimum, maximum, a report | 0 / 90 |
| **7.5 (this)** | **linear search + the "AI Experiment Analyzer" checkpoint** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 18) | Covered here |
|---|---|
| Goal 9: implement linear search, returning an index or `-1` | ✅ every task |
| Goal 10: a sorted list's order allows an early stop | ✅ Task 1 |
| Goal 11: split a solution into functions used as black boxes | ✅ the whole project |
| Goal 12: apply lists to AI experiment results | ✅ the project's subject matter |
| Assessment (source §4): a graded modular list project | ✅ the checkpoint |

### Deliberate exclusions
Any new list method or pattern — this meeting applies 7.1–7.4's tools in one combined project.

---

## 3. Lesson Goal

**Linear search checks elements in order and returns the first matching index, or `-1` if none match — checked
explicitly against `-1`, never used as a plain yes/no condition.**

---

## 4. Core Mental Models

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


position = linear_search(scores, 81)
if position != -1:              # explicit comparison - index 0 is a valid, successful result
    print("Found at", position)
```

```python
def linear_search_sorted(values, target):
    index = 0
    while index < len(values) and values[index] < target:
        index += 1                          # stop advancing once we've gone far enough
    if index < len(values) and values[index] == target:
        return index
    return -1
```

- `if linear_search(...):` is a bug waiting to happen — Python treats `0` as `False`, but index `0` means "found at
  the very first position," a success.
- On a **sorted** list, once the current value is no longer less than the target, there's no point checking further.

---

# 6. Lab (0–90)

Starter: [`Analyzer_Starter.py`](Analyzer_Starter.py). Reference: [`Analyzer_Reference.py`](Analyzer_Reference.py).

## 0–10 — Recap + hook
Searching for one particular card in a row of cards — check them in order.

## 10–18 — Warm-up: found at 0, reported as not found

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


scores = [81, 24, 67, 91]
if linear_search(scores, 81):
    print("Found")
else:
    print("Not found")
```

Predict `Found` (81 is right there, at index 0), run, get `Not found` — `if 0:` is `False` in Python, even though
index `0` is a genuine, successful result. Fix: `position = linear_search(scores, 81); if position != -1: ...`.

## 18–32 — Task 1: `linear_search_sorted(values, target)`

Stops as soon as the current element is no longer less than the target. Test on `[10, 20, 35, 50, 80]` with target
`35` (present) and target `40` (absent).

<div dir="rtl">

| `index` | `values[index]` | קטן מהמטרה? | פעולה |
|---:|---:|---|---|
| 0 | 10 | כן | הגדלת אינדקס |
| 1 | 20 | כן | הגדלת אינדקס |
| 2 | 35 | לא | בדיקת שוויון והחזרת 2 |

</div>

## 32–35 — Planning the project

Input → list operations → statistics → search → output. Which function handles each step, and what does each one
take in and return?

## 35–62 — Task 2 (project): "AI Experiment Analyzer" — unit checkpoint

Build a program that: reads similarity scores with `input()` until `-1` (the sentinel — not stored), keeping only
scores from `0` to `100`; prints the count, average, minimum and maximum; makes a sorted **copy** without changing
the original; reads a threshold and prints how many scores are at or above it; reads a target score and prints its
position in the sorted copy. Reuse every function from 7.1–7.4 as a black box — don't reimplement any of their
logic inline.

## 62–75 — Testing, using all seven of the source's own cases

<div dir="rtl">

| מקרה | קלט | תוצאה צפויה |
|---|---|---|
| אין נתונים | `-1` מיד | `No valid scores` וללא חלוקה באפס |
| איבר יחיד | `75, -1` | ממוצע, מינימום ומקסימום הם 75 |
| קלט לא תקין | `120, -5, 80, -1` | רק 80 נשמר; `-5` אינו מסיים כי רק `-1` הוא זקיף |
| כפילויות | `70, 70, 80, -1` | שתי הופעות של 70 נשמרות |
| חיפוש הצלחה | מטרה שקיימת | מוחזר האינדקס הראשון ברשימה הממוינת |
| חיפוש כישלון | מטרה שאינה קיימת | מוחזר `-1` |
| סדר | רשימה לא ממוינת | המקור נשמר והעותק בלבד ממוין |

</div>

## 75–84 — Peer review

Checklist: does only valid input enter the list? is the sentinel value itself kept out? does every function do one
clear job, taking a parameter and returning a value? is the empty list handled? is the original list still
unsorted after making the sorted copy? does search receive the sorted list? does a failed search give `-1`? is a
similarity score explicitly explained as not a probability?

## 84–90 — Presentation and exit check

Each pair explains one function's job to another pair — what it takes in, what it returns, and why it's separate
from the others.

1. Why is linear search called "linear"?
2. What's returned when the value isn't found?
3. When can a sorted-list search stop early?
4. What's the advantage of splitting the project into functions?

### Tool Note – Thonny
Test each function alone in the Shell (`find_maximum([1, 2, 3])`, `linear_search_sorted([1,2,3], 2)`) before
running the full project — much faster to isolate a problem in one function than inside the whole flow.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A search result can be tested as a plain `if` condition | Index `0` is `False`-y but a real success — always compare explicitly to `-1` |
| `linear_search_sorted` works on any list | It assumes the list is already sorted — sort first, or use plain `linear_search` |
| The sentinel value (`-1`) should be stored like any other input | It signals "stop," and is never added to the list |
| `-5` (an invalid score) also ends the input loop | Only the exact sentinel `-1` ends it — other invalid values are rejected and the loop continues |
| Reimplementing logic inline is fine if it's quick | Reuse the tested functions from earlier meetings — that's the point of building them as black boxes |

---

# 8. Assessment Evidence (formative)

- The warm-up's index-`0` bug explained precisely (why `0` is falsy but still a real success), not just fixed
- `linear_search_sorted()` correct for both a present and an absent target, matching the trace table
- **Unit 7 checkpoint — "AI Experiment Analyzer"**, scored against the source's 20-point rubric: list creation and
  input 3, list operations 3, accumulation and average 3, minimum and maximum 3, linear search 3, modularity 3,
  testing and explanation 2. Bands: 18–20 complete, modular, tested and well explained · 14–17 works, one small
  flaw in an operation, an edge case, or the explanation · 10–13 partial, missing a core pattern or clear function
  split · 0–9 needs support with lists, accumulation, search, or `return`.
- All seven test cases run and matched against the table above
- The peer review and the one-function presentation
