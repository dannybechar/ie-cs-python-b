# Unit 7.5 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Linear Search, "A New Phone Number", and the "AI Experiment Analyzer" (Unit Checkpoint)

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** Lab + Lab (a short recap, then three tasks and the project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** Ministry **12.5** (worksheet "Practice #2, a new phone number", steps a–c) with **12.1 pp. 28–35**
(the phone-number solution with `random.choice`, `random.randint`, `in`, a list of special numbers; random student), **12.6** Q5 (duplicate
names, already used in 7.2) and the Ministry's own `index()` in the operations table (12.0 p. 18). Linear search itself, the early-stop
version on a sorted list, the "AI Experiment Analyzer" project, its seven test cases and the 20-point rubric are **kept from v1**
(the Ministry files are silent on search). **New (audit):** `list.index()` and its error, the phone-number task with `random.choice`,
a taken list and a special list, and the project split into functions (step c of 12.5).
**Ministry bugs not copied:** the 12.1 p. 31–32 solution has an extra closing parenthesis (`if(new_phone_num in list_special)):`) and checks
the special list **after** the number was already added to the taken list; the `str = ...` variable hides the built-in `str`.
Our `new_phone_number` checks first and loops until the number is acceptable. See
[`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3). Part E of the Ministry's lists lessons (list of lists, nested loops; 14.0 p. 25–30) was not delivered
and is left out of this course.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | what a list is; indices; slicing | 45 / 45 |
| 7.2 | list operations | 45 / 45 |
| 7.3 | walking a list; accumulation | 45 / 45 |
| 7.4 | counting, filters, maximum, flat menu, parallel lists | 0 / 90 |
| **7.5 (this)** | **linear search, `index()`, phone numbers, the "AI Experiment Analyzer"** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 18) | Covered here |
|---|---|
| Goal 9: linear search, returning an index or `-1` | ✅ warm-up, Task 1 |
| Goal 10: a sorted list's order allows an early stop | ✅ Task 1 |
| Goal 11: functions as black boxes | ✅ Tasks 2 and 3 |
| Goal 12: lists of AI experiment results | ✅ the project |
| Assessment (chapter): a graded modular list project | ✅ the checkpoint |

### Deliberate exclusions
A new list method or pattern — this meeting applies 7.1–7.4. Binary search is not built.

---

## 3. Lesson Goal

**Linear search checks elements in order and returns the first matching index, or `-1` if none match — checked explicitly against
`-1`, never used as a plain yes/no condition; and a program is built from small functions tested one by one.**

---

## 4. Core Mental Models

```python
def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


position = linear_search(scores, 81)
if position != -1:              # index 0 is a real success
    print("Found at", position)
```

```python
def linear_search_sorted(values, target):
    index = 0
    while index < len(values) and values[index] < target:
        index += 1
    if index < len(values) and values[index] == target:
        return index
    return -1
```

- `if linear_search(...):` is a bug — `0` is falsy, but index `0` means "found at the very first position".
- `values.index(40)` on a missing value raises `ValueError: list.index(x): x not in list` (verified); our search returns `-1` instead.
- On a **sorted** list, stop once the current value is no longer less than the target.
- A number is *special* when it is in the special list, or its seven digits contain `"5"` more than once, or they are a rising or falling run
  (`digits in "0123456789"` is a string-membership trick the class knows from Unit 5).

Verified: `linear_search_sorted([10, 20, 35, 50, 80], 35)` → `2`, with `40` → `-1`; the warm-up fixed prints `Found at 0`.

---

# 6. Lab (0–90)

Starter: [`Analyzer_Starter.py`](Analyzer_Starter.py). Reference: [`Analyzer_Reference.py`](Analyzer_Reference.py).

## 0–8 — Recap + hook

A row of cards face down: find a particular card, one by one, in order.

## 8–14 — Warm-up: found at 0, reported as not found

```python
scores = [81, 24, 67, 91]
if linear_search(scores, 81):
    print("Found")
else:
    print("Not found")
```

Predict `Found`, run, get `Not found` — `if 0:` is `False`. Fix: `position = linear_search(scores, 81)` and `if position != -1:`.

## 14–26 — Task 1: `linear_search_sorted(values, target)` and `index()`

Stops as soon as the current element is no longer less than the target. Test on `[10, 20, 35, 50, 80]` with `35` and `40`. Then run
`[10, 20, 35, 50, 80].index(35)` (`2`) and `.index(40)` (the `ValueError` above): what does our search do better?

<div dir="rtl">

| `index` | `values[index]` | קטן מהמטרה? | פעולה |
|---:|---:|---|---|
| 0 | 10 | כן | הגדלת אינדקס |
| 1 | 20 | כן | הגדלת אינדקס |
| 2 | 35 | לא | בדיקת שוויון והחזרת 2 |

</div>

## 26–42 — Task 2: "A new phone number" (Ministry 12.5)

Prefixes `["050", "052", "053", "054"]`; a number looks like `052-8819853`. (a) `random_number(prefixes)`; (b) `is_special(number, special)`;
(c) `new_phone_number(taken, special)` loops until the number is not taken and not special; (d) build 10 different numbers.
A sample run (random, so **yours will differ**; this one is `random.seed(3)`):

```text
['052-3188131', '053-8953298', '050-1220922', '052-4216932', '054-8991880', '054-3526924', '052-3543801', '054-1254120', '050-3674287', '050-6054432']
```

Step c of the Ministry worksheet is exactly this: split the problem into functions and solve it again.

## 42–70 — Task 3 (project): the "AI Experiment Analyzer" — unit checkpoint

Reads similarity scores with `input()` until `-1` (the sentinel, not stored), keeping only scores from `0` to `100`; prints the original list,
a sorted **copy**, the average, minimum and maximum; reads a threshold and prints how many scores are at or above it; reads a target and prints its
position in the sorted copy. Reuse the functions of 7.3–7.4 as black boxes.

Sample run (inputs `81, 120, -5, 24, 67, 91, 73, -1`, threshold `70`, target `67`):

```text
Invalid score
Invalid score
Original: [81, 24, 67, 91, 73]
Ordered: [24, 67, 73, 81, 91]
Average: 67.2
Minimum: 24
Maximum: 91
At or above threshold: 3
Position in ordered list: 1
```

(the prompts, e.g. `Score from 0 to 100, or -1:`, appear on the same lines as the typed numbers).

## 70–80 — Testing with the seven cases

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

## 80–86 — Peer review

Does only valid input enter the list? Is the sentinel kept out? Does every function do one job (parameter in, value out)? Is the empty list handled? Is the original still unsorted? Does the search get the sorted list? Does a failed search give `-1`? Is a similarity score explained as **not** a probability?

## 86–90 — Save and exit check

Save As `G8_U7_M5_Analyzer_<Name>.py`.

1. Why is linear search called "linear"?
2. What is returned when the value is not found?
3. When can a search on a sorted list stop early?
4. What is the advantage of splitting a program into functions?

### Tool Note – Thonny
Test each function alone in the Shell (`find_maximum([1, 2, 3])`, `linear_search_sorted([1, 2, 3], 2)`) before running the whole project.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A search result can be tested as a plain `if` | Index `0` is falsy but a real success — compare to `-1` |
| `linear_search_sorted` works on any list | It assumes the list is already sorted |
| `index()` and our search behave the same when the value is missing | `index()` raises `ValueError`; ours returns `-1` |
| The sentinel (`-1`) should be stored | It signals "stop" and is never added |
| `-5` also ends the input loop | Only `-1` does; other invalid values are rejected and the loop goes on |
| Random numbers cannot repeat | They can — that is why `new_phone_number` checks the taken list |
| Re-implementing logic inline is fine | Reuse the tested functions |

---

# 8. Assessment Evidence

- The warm-up explained precisely (why `0` is falsy but a real success)
- `linear_search_sorted()` correct for a present and an absent target, matching the trace table
- `new_phone_number()` never repeats a number and never returns a special one
- **Unit 7 checkpoint — "AI Experiment Analyzer"**, scored against the 20-point rubric: list creation and input 3, list operations 3,
  accumulation and average 3, minimum and maximum 3, linear search 3, modularity 3, testing and explanation 2. Bands: 18–20 complete,
  modular, tested and well explained · 14–17 works, one small flaw · 10–13 partial, missing a core pattern or the function split · 0–9 needs support.
- All seven test cases matched against the table above
- The peer review
