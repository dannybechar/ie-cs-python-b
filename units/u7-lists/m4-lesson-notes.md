# Unit 7.4 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Counting, Minimum, Maximum, a Report

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** Lab + Lab (24 min guided practice, then 66 min lab)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit07_lists_complete_unit.md`, meeting 4 — its own clock table, the
conditional-counting example, the minimum/maximum functions with the "why not initialize to 0" explanation, the
modular report function, both practice drills, and the four-row edge-case table kept nearly unchanged; the
minimum/maximum init warning is used directly as this meeting's warm-up bug (see `unit-strategy.md`).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | a list as an ordered, dynamic collection; indices; traversal | 45 / 45 |
| 7.2 | list operations: append/extend/insert, remove/pop, sort/reverse, split/join | 45 / 45 |
| 7.3 | advanced operations + the accumulation pattern | 45 / 45 |
| **7.4 (this)** | **counting, minimum, maximum, a report** | 0 / 90 |
| 7.5 | linear search + the "AI Experiment Analyzer" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 18) | Covered here |
|---|---|
| Goal 8: the counting, minimum and maximum patterns | ✅ every task |
| Goal 11: split a solution into functions used as black boxes | ✅ `build_report` |
| Goal 12: apply lists to AI experiment results | ✅ every example |

### Deliberate exclusions
Search (7.5), the full capstone project (7.5).

---

## 3. Lesson Goal

**A counter grows only when its condition holds; minimum and maximum are initialized from the list's own first
element — never from `0` — so the starting candidate is always a real value from the data.**

---

## 4. Core Mental Models

```python
def count_above(values, threshold):
    count = 0
    for value in values:
        if value >= threshold:
            count += 1            # grows only when the condition is True
    return count
```

```python
def find_maximum(values):
    if len(values) == 0:
        return None
    largest = values[0]            # start from a REAL value in the list, not 0
    for value in values:
        if value > largest:
            largest = value
    return largest
```

- If every value were negative, `largest = 0` would never be beaten — the function would wrongly return `0`, a
  value that isn't even in the list. Starting from `values[0]` avoids this entirely.
- Always guard the empty-list case (`len(values) == 0`) before computing an average, a minimum or a maximum.

---

# 6. Lab (0–90)

Starter: [`Stats_Starter.py`](Stats_Starter.py). Reference: [`Stats_Reference.py`](Stats_Reference.py).

## 0–8 — Recap
The accumulation pattern (7.3): initialize, traverse, update, use after the loop.

## 8–16 — Warm-up: the maximum that never updates

```python
def find_maximum(values):
    largest = 0
    for value in values:
        if value > largest:
            largest = value
    return largest


print(find_maximum([-5, -2, -9]))
```

Predict `-2` (the largest of the three), run, get `0` — `0` is bigger than every negative value in the list, so
`largest` is never updated at all. Fix: `largest = values[0]`.

## 16–30 — Task 1: `count_above(values, threshold)` and `count_in_range(values, low, high)`

`count_in_range` includes both bounds. Test both on `[81, 24, 67, 91]`.

```text
count_above(scores, 70)         -> 2
count_in_range(scores, 60, 90)   -> 2
```

## 30–44 — Task 2: `find_minimum(values)`

Mirrors the warm-up's fix: `None` for an empty list, otherwise initialized from `values[0]`. Test on
`[81, 24, 67, 91]` and on `[]`.

## 44–62 — Task 3: `build_report(values)`

`"No data"` for an empty list; otherwise a string with the count, the average (rounded to 1 decimal place), the
minimum and the maximum, one per line — combining `calculate_total`, `calculate_average`, `find_minimum` and
`find_maximum` into one report. Test on `[81, 24, 67, 91]`.

## 62–78 — Testing the edge cases

<div dir="rtl">

| רשימה | תוצאה שיש לבדוק |
|---|---|
| `[]` | אין חלוקה באפס; מינימום ומקסימום מחזירים `None` |
| `[50]` | ממוצע, מינימום ומקסימום הם 50 |
| `[7, 7, 7]` | מינימום ומקסימום שווים |
| `[-5, -2, -9]` | המקסימום הוא `-2`, לא 0 |

</div>

Run `build_report()` on each of the last three and confirm against the table.

## 78–86 — Discussion: what a similarity score is (and isn't)

On `scores = [81, 24, 67, 91, 73]` (similarity scores from Unit 6's game), print the average, the count above 70,
the minimum and the maximum. These numbers describe scores under one model — they don't prove a word was
"correct," and they aren't automatically comparable to another model's scores.

## 86–90 — Save and exit check

Save As `G8_U7_M4_Stats_<Name>.py`.

1. What's a counter's initial value?
2. How do you initialize a minimum on a non-empty list?
3. What do you return for the minimum of an empty list?
4. Why isn't a similarity score a probability?

### Tool Note – Thonny
Run `find_maximum([])` directly in the Shell to confirm it returns `None` rather than crashing — a quick, isolated
edge-case check before wiring it into the report.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A counter should grow on every iteration | It grows only when its condition is `True` |
| `0` is a safe starting point for a minimum or maximum | It fails whenever every value is negative (max) or positive (min) — start from `values[0]` |
| An empty list can be safely skipped without a check | It must be handled explicitly, or a later step (like an average) divides by zero |
| A report function should recompute everything itself | It should combine values already produced by other functions, not repeat their logic |
| A high similarity score guarantees a "correct" answer | It's one model's numeric estimate — not a fact or a universal ranking |

---

# 8. Assessment Evidence (formative)

- The warm-up's wrong `0` explained by the negative-numbers case specifically, not just patched
- `count_above()` and `count_in_range()` both correct
- `find_minimum()` correct on both a normal list and an empty one
- `build_report()` matching all four rows of the edge-case table
- Exit check
