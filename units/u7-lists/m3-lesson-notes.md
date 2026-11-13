# Lessons 12.6, 13.0–13.1 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v3 (reconciled to the official Python B program, 9 Nov 2026)
### Topic: Walking a List (by Index and by Value) and the Accumulation Pattern

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **13.0 / 13.1** (Lists part C: the two ways to traverse, pp. 3–6 with the mixed list
`[24.7, "Itamar", -35, 4<3, "#"]` — the `4<3` prints `False`; `sum_listA` / `sum_listB` and the "why is `item` different?" question, pp. 7–11;
exercises #1 class names and #2 Roni's prices, pp. 12–13, worksheet **13.2**), worksheet **12.6** (Q4: the same question again, "same or
different outputs, and why?"; Q5 duplicate names, Q6 clothes), **12.0 pp. 6–10** (maximum, the two average loops, the temperature filter —
used as predict questions and in lessons 13.2, 14.0–14.2) and **14.0** exercise #10 (`remove_even`). Kept from v1: the accumulation pattern
(initialize, update, use after the loop), the average with an empty-list guard, copy before sort. **New (audit):** the `remove_even`
mutation trap, with its trace, as the warm-up; the alias trap `b = a`.
**Ministry naming, said once to the class:** the official files name the loop variable `item` even when it holds an index
(`for item in range(len(...))`). We keep `item` in the demo so the students recognise the Ministry's examples (that is the very point of the
"why is `item` different?" question); in the lab functions a clearer name (`index`) is welcome.
**Ministry bug not copied:** the 14.0 p. 23 solution of the grouped-grades exercise (`begin += 1 + i`) is used in lessons 13.2, 14.0–14.2 as a bug hunt.
Exercise #2 asks for a function that reads five prices; ours takes the number of prices as a parameter, `read_prices(count)`.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Links only (not offline):** 13.3 (practice) and the projects 13.4 "dance party" and 13.5 "hangman" (H5P / genially) — titles in the unit README.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** the functions block (lessons 4.1–4.6).

---

## 1. Position in the lists block (lessons 9.1–9.5, 12.0–14.5)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 9.1, 9.4 | what a list is; indices; slicing | 45 / 45 |
| Lessons 9.3, 9.5, 12.0–12.1 | list operations | 45 / 45 |
| **Lessons 12.6, 13.0–13.1 (this)** | **two ways to walk a list; accumulation; average; the "change while looping" trap; copies** | 45 / 45 |
| Lessons 13.2, 14.0–14.2 | counting, filters, maximum, flat menus, parallel lists | 0 / 90 |
| Lessons 12.5, 14.4 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 7: traverse directly or by index | ✅ the heart of the meeting |
| Goal 8: the summation and average patterns | ✅ Tasks 1–3 |
| Goal 11: small functions as black boxes | ✅ every task |

### Deliberate exclusions
Minimum/maximum and counting (lessons 13.2, 14.0–14.2), search (lessons 12.5, 14.4). Nested loops (14.0 pp. 25–29, a Ministry preview): **official item deliberately left out** (the new program dropped nested loops, clarifications p. 3).

---

## 3. Lesson Goal

**Walk a list by index when the position matters, by value when only the value matters; accumulate with `total = 0` before the
loop and `total = total + ...` inside it — and never change a list while a `for` loop walks over it.**

---

## 4. Core Mental Models

```python
def sum_by_index(values):
    total = 0
    for item in range(len(values)):     # item is a POSITION: 0, 1, 2 ...
        total = total + values[item]
    return total


def sum_by_value(values):
    total = 0
    for item in values:                 # item is a VALUE: 51, 84, 72 ...
        total = total + item
    return total
```

- Same name `item`, two meanings: after `range(len(values))` it is a **number of a position**; after `in values` it is **the value**.
- The accumulation pattern: initialize before the loop, update every iteration, use the result after the loop. Return the total, don't print it inside the loop.
- `calculate_average` divides by `len(values)` — for an empty list return `0` first.
- Changing a list while the `for` loop walks it skips neighbours: the loop's hidden position moves on while the items slide left.
- `b = a` does **not** copy a list: `a` and `b` are two names for the same list. `a.copy()` or `a[:]` make a real copy.

Verified outputs:

```text
[24.7, "Itamar", -35, 4<3, "#"] walked by index prints: 24.7  Itamar  -35  False  #
sum_listA([51, 84, 72, 13, 29]): item = 0 ... item = 4, total = 249     (item = the position)
sum_listB([51, 84, 72, 13, 29]): item = 51 ... item = 29, total = 249   (item = the value)

words = ["a", "b", "b", "c"]; for w in words: if w == "b": words.remove(w)   ->  ['a', 'b', 'c']
a = [3, 1, 2]; b = a; b.sort()    ->  a is [1, 2, 3] as well (same list)
c = a[:]; c.append(9)             ->  a stays [1, 2, 3], c is [1, 2, 3, 9]
```

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–4 | Recap: `append`, `remove`, `[::-1]`; why we need a loop over a list |
| 4–9 | Walking **by index**: `for item in range(len(my_list))` and `my_list[item]` on the mixed list `[24.7, "Itamar", -35, 4<3, "#"]` (13.0 pp. 4–5; `4<3` is the value `False`) |
| 9–13 | Walking **by value**: `for item in my_list` |
| 13–15 | **Predict (question only):** the two `sum` programs on `[51, 84, 72, 13, 29]` print `item` — same output or different? (13.0 pp. 10–11 = 12.6 Q4) |
| 15–19 | The answer (the two outputs above); `item` is a position vs. a value |
| 19–25 | The accumulation pattern: initialize, update, use; a trace table for `[51, 84, 72, 13, 29]` |
| 25–29 | Average, and the empty-list guard (`ZeroDivisionError: division by zero` without it); 12.0 p. 7: two average loops, one by index and one by value — same or different? |
| 29–31 | **Predict (question only):** removing every `"b"` from `["a", "b", "b", "c"]` inside a `for` loop |
| 31–37 | The answer `['a', 'b', 'c']`; trace; two fixes: build a new list, or walk a copy |
| 37–41 | Copies: `b = a` is the same list; `.copy()` and `[:]`; sort a copy to keep the original order |
| 41–45 | Summary and the lab missions |

Trace for the accumulation (slide):

| `item` (value) | `total` after the step |
|---:|---:|
| 51 | 51 |
| 84 | 135 |
| 72 | 207 |
| 13 | 220 |
| 29 | 249 |

---

# 6. Second 45 Minutes — Lab

Starter: [`Accumulate_Starter.py`](Accumulate_Starter.py). Reference: [`Accumulate_Reference.py`](Accumulate_Reference.py).

## 45–50 — Warm-up: `remove_even` that keeps evens

```python
def remove_even(values):
    for item in values:
        if item % 2 == 0:
            values.remove(item)


numbers = [2, 4, 6, 8, 1]
remove_even(numbers)
print(numbers)
```

Predict `[1]`, run, get `[4, 8, 1]`. Trace: position 0 holds 2 → removed, everything slides left; position 1 now holds 6 (the 4 was
jumped over) → removed; position 2 holds 1 → kept. Fix in the "if time" task: build a new list. (Ministry 14.0 #10 asks for `remove_even`.)

## 50–58 — Task 1: `sum_by_index` and `sum_by_value` (Ministry 13.0 p. 7, 12.6 Q4)

Both return the total of `[51, 84, 72, 13, 29]` (`249`); inside each loop print `item` first, to see what it holds. Then the question of 12.6 Q4,
written on paper: **are the printed values the same or different, and what causes it?** (`item` is a position in one, a value in the other.)

## 58–64 — Task 2: `calculate_average(values)`

Returns the average; `0` for an empty list. `[25.1, 20.0, 21.5, 24.0, 21.4, 24.5, 21.5, 16.0, 23.3]` → `21.922222222222224`; `[]` → `0`.

## 64–72 — Task 3: class names (Ministry 13.2 #1, 12.6 Q5)

`register_students(count)` reads `count` names with `input()`; a name already in the class prints `We cannot place you in this class`, a new name is added; it returns the list.
Verified run with the names `Dana`, `Avi`, `Dana`, `Noa`, `Avi`:

```text
Enter a name: Dana
Enter a name: Avi
Enter a name: Dana
We cannot place you in this class
Enter a name: Noa
Enter a name: Avi
We cannot place you in this class
['Dana', 'Avi', 'Noa']
```

(Capital letters count: `Dana` and `dana` are two names — the lesson on list operations, lessons 9.3, 9.5, 12.0–12.1.)

## 72–81 — Task 4: Roni's prices (Ministry 13.2 #2)

`read_prices(count)` reads `count` prices with `input()` into a list and returns it. Outside the function print the list and the total **twice** — by index
(`sum_by_index`) and by value (`sum_by_value`), as the Ministry asks (a, b).

```text
Enter price: 400
Enter price: 350
Enter price: 100
Enter price: 250
Enter price: 70
[400.0, 350.0, 100.0, 250.0, 70.0]
total = 1170.0
```

## 81–86 — If time: new list instead of change; a sorted copy

`without_even(values)` returns a **new** list without the even numbers; `sorted_copy(values)` returns a sorted copy and the original keeps its order.
On `[5, 2, 8, 1, 4]`: `[5, 1] [5, 2, 8, 1, 4]` and `[1, 2, 4, 5, 8] [5, 2, 8, 1, 4]`.

## 87–90 — Save and exit check

Save As `G8_U7_M3_Accumulate_<Name>.py`.

1. For `for item in range(len(values))`, what is `item`? For `for item in values`?
2. Before the loop, what is `total`?
3. Why must `calculate_average` check for an empty list?
4. Why not remove items from a list inside a `for` loop over the same list?

**Answers:** a position / a value; `0`; dividing by `len(values)` = 0 is an error; the loop skips the item that slides into the removed one's place.

### Tool Note – Thonny
Step through the warm-up with **Debugger ▸ Step over**: watch `item` and `numbers` change line by line — the skipped `4` is visible.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `item` always holds the value | Only in `for item in values`; after `range(len(values))` it is a position |
| The two `sum` functions give different totals | Same total, different `item` |
| `total` can start without a value | `total = 0` before the loop, or `UnboundLocalError` |
| `print(total)` inside the loop is the result | The function should return the total after the loop |
| Removing inside a `for` loop is safe | It skips neighbours; build a new list |
| `b = a` copies a list | It is one list with two names; use `.copy()` |
| An average of an empty list is fine | Guard it first (`ZeroDivisionError`) |

---

# 8. Assessment Evidence (formative)

- The prediction about `item` written before running
- The warm-up traced by hand (which item was skipped, and why)
- `sum_by_index` and `sum_by_value` both give `249`
- `calculate_average([])` returns `0` and does not crash
- `register_students` rejects the repeated name; Roni's total is `1170.0` both ways
- (if time) `without_even` and `sorted_copy` leave the original list unchanged
- Exit check
