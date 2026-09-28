# Unit 7.3 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Advanced Operations + the Accumulation Pattern

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit07_lists_complete_unit.md`, meeting 3 — its own clock table, the
index-based-update example, the remove-while-iterating warning (with its "build a new list" fix), the copy-before-
sort example, the summation pattern walkthrough, `calculate_total`/`calculate_average` and both practice drills kept
nearly unchanged; the remove-while-iterating example's numbers changed to an all-even list so the bug's wrong
result is dramatic and immediately visible (see `unit-strategy.md`).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | a list as an ordered, dynamic collection; indices; traversal | 45 / 45 |
| 7.2 | list operations: append/extend/insert, remove/pop, sort/reverse, split/join | 45 / 45 |
| **7.3 (this)** | **advanced operations + the accumulation pattern** | 45 / 45 |
| 7.4 | counting, minimum, maximum, a report | 0 / 90 |
| 7.5 | linear search + the "AI Experiment Analyzer" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17–18) | Covered here |
|---|---|
| Goal 3: update an element by index | ✅ guided practice |
| Goal 7: traverse a list safely | ✅ the remove-while-iterating warning |
| Goal 8: the summation pattern | ✅ every task |
| Goal 11: split a solution into functions used as black boxes | ✅ `calculate_total`/`calculate_average` |

### Deliberate exclusions
Counting and min/max (7.4), search (7.5).

---

## 3. Lesson Goal

**Never remove from a list while directly looping over it — build a new list instead; a summing function
initializes before the loop, updates every iteration, and returns after it.**

---

## 4. Core Mental Models

```python
values = [1, 2, 3, 4, 5, 6]
odd_values = []
for value in values:
    if value % 2 != 0:
        odd_values.append(value)   # build a NEW list - never remove from the one being looped over
```

```python
def calculate_total(values):
    total = 0                       # 1. initialize before the loop
    for value in values:
        total += value                # 2-3. traverse, update
    return total                       # 4. use the result after the loop
```

- Changing a list's length while looping directly over it can shift later items into already-checked positions —
  they get silently skipped.
- `.copy()` (or `[:]`) before `.sort()` when the original order also needs to survive.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** `append`, `pop`, `sort`, and what a list looks like after each |
| 10–20 | Updating by index in a loop: `for index in range(len(scores)): scores[index] += 5` |
| 20–30 | **Why not remove like this?** `for value in values: if value % 2 == 0: values.remove(value)` — walk through why it skips items; the fix: build a new list of what to **keep** |
| 30–37 | Copying before sorting: `ordered = scores.copy(); ordered.sort()` |
| 37–45 | The need for accumulation (a running sum, without a variable per item); the four-step summation pattern |

---

# 6. Second 45 Minutes — Lab

Starter: [`Accumulate_Starter.py`](Accumulate_Starter.py). Reference: [`Accumulate_Reference.py`](Accumulate_Reference.py).

## 45–54 — Warm-up: skipped by shifting

```python
values = [2, 4, 6, 8, 10]
for value in values:
    if value % 2 == 0:
        values.remove(value)
print(values)
```

Predict `[]` (every value is even), run, get `[4, 8]` — two values slipped through. Removing shifts every later
item one position left, but the loop's position keeps advancing regardless — some items are never checked. Fix:
build a new list of what to **keep**, don't mutate the list being looped over.

## 54–64 — Task 1: `get_sorted_copy(values)`

Returns a **new** sorted list, leaving the original untouched. Test on `[72, 95, 61]` and confirm the original is
still `[72, 95, 61]` afterward.

## 64–80 — Task 2: `calculate_total(values)` and `calculate_average(values)`

`calculate_average` returns `0` for an empty list (never divide by zero). Test both on `[72, 84, 65]`.

## 80–90 — Save and exit check

Save As `G8_U7_M3_Accumulate_<Name>.py`.

1. What's the initial value of a sum?
2. Where does `return` go in a summing function — inside the loop, or after it?
3. Why check for an empty list before computing an average?
4. How do you make a sorted copy without disturbing the original order?

### Tool Note – Thonny
Set a breakpoint inside the `for` loop and watch `total` grow in the **Variables** view, one iteration at a time —
a fast way to confirm the accumulation pattern is wired correctly.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Removing while looping directly over the same list is safe | It silently skips elements — build a new list instead |
| `total` can be initialized inside the loop | It resets every iteration — initialize once, before the loop |
| `return` can sit inside the loop, after the first item | It would return after just one iteration — put it after the loop finishes |
| `.sort()` on the original preserves the input order elsewhere | It sorts in place — copy first if the original order is still needed |
| Dividing by `len(values)` is always safe | Guard for the empty list first, or it's a `ZeroDivisionError` |

---

# 8. Assessment Evidence (formative)

- The warm-up's skipped elements explained mechanically (why shifting causes it), not just patched
- `get_sorted_copy()` correct, with the original list confirmed unchanged
- `calculate_total()` and `calculate_average()` both correct, including the accumulation pattern's four steps stated aloud
- Exit check
