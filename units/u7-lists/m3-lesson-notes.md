# Unit 7.3 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Walking a List (by Index and by Value) and the Accumulation Pattern

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **13.0 / 13.1** (Lists part C: the two ways to traverse, pp. 3–6 with the mixed list
`[24.7, "Itamar", -35, 4<3, "#"]`; `sum_listA` / `sum_listB` and the "why is `item` different?" question, pp. 7–11; exercise #2, Roni's
prices, p. 13), **12.0 p. 7** (the two average loops) and **14.0** exercise #10 (`remove_even`). Kept from v1: the accumulation pattern
(initialize, update, use after the loop), the average with an empty-list guard, copy before sort. **New (audit):** the `remove_even`
mutation trap, with its trace, as the warm-up; the alias trap `b = a`.
**Ministry bug not copied:** the 14.0 p. 23 solution of the grouped-grades exercise (`begin += 1 + i`) is used in 7.4 as a bug hunt.
Exercise #2 asks for a function that reads five prices; ours takes the number of prices as a parameter, `read_prices(count)`.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3).

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | what a list is; indices; slicing | 45 / 45 |
| 7.2 | list operations | 45 / 45 |
| **7.3 (this)** | **two ways to walk a list; accumulation; average; the "change while looping" trap; copies** | 45 / 45 |
| 7.4 | counting, filters, maximum, flat menus, parallel lists | 0 / 90 |
| 7.5 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 7: traverse directly or by index | ✅ the heart of the meeting |
| Goal 8: the summation and average patterns | ✅ Tasks 1–3 |
| Goal 11: small functions as black boxes | ✅ every task |

### Deliberate exclusions
Minimum/maximum and counting (7.4), search (7.5). Nested loops (14.0 pp. 25–29, a Ministry preview): not taught.

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
| 4–9 | Walking **by index**: `for item in range(len(my_list))` and `my_list[item]` on the mixed list |
| 9–13 | Walking **by value**: `for item in my_list` |
| 13–15 | **Predict (question only):** the two `sum` programs print `item` — same output or different? |
| 15–19 | The answer (the two outputs above); `item` is a position vs. a value |
| 19–25 | The accumulation pattern: initialize, update, use; a trace table for `[51, 84, 72, 13, 29]` |
| 25–29 | Average, and the empty-list guard (`ZeroDivisionError: division by zero` without it) |
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

## 45–52 — Warm-up: `remove_even` that keeps evens

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
jumped over) → removed; position 2 holds 1 → kept. Fix in Task 4: build a new list.

## 52–62 — Task 1: `sum_by_index` and `sum_by_value`

Both return the total of `[51, 84, 72, 13, 29]` (`249`); inside each loop print `item` first, to see what it holds.

## 62–70 — Task 2: `calculate_average(values)`

Returns the average; `0` for an empty list. `[25.1, 20.0, 21.5, 24.0, 21.4, 24.5, 21.5, 16.0, 23.3]` → `21.922222222222224`; `[]` → `0`.

## 70–80 — Task 3: Roni's shopping (Ministry 13.0 exercise #2)

`read_prices(count)` reads `count` prices with `input()` into a list and returns it. Outside the function print the list and the total.

```text
Enter price: 400
Enter price: 350
Enter price: 100
Enter price: 250
Enter price: 70
[400.0, 350.0, 100.0, 250.0, 70.0]
total = 1170.0
```

## 80–87 — Task 4: new list instead of change; a sorted copy

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
- `without_even` and `sorted_copy` leave the original list unchanged
- Exit check
