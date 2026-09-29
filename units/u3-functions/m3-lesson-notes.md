# Unit 3.3 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Returning a Value + Scope (Unit Checkpoint)

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the codex deck `python_b_unit03_m03_return_values_and_scope_delivery.pptx` ("can the
result be used in another calculation" hook, the `print` vs `return` comparison, the `double()` trace table, a
no-parameter function that still returns a value, `is_even()` used without an `if`, the discount-completion task, a
returned value used directly inside `if`, the local-variable and scope-error examples, the independent-vs-global
comparison, the "what vs how" reprise, the bottom-up task-calculator challenge and its architecture, the three-case
peer test, the exit card kept; "מפגש" labels removed; the discount task's `# complete here` blank turned into a
missing-`return` warm-up bug, since it demonstrates the same point — a value computed but never returned — while
giving students something that runs and produces a wrong (not blank) result to react to)
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 3.1 | `def`, the call, execution order, procedural abstraction | 45 / 45 |
| 3.2 | parameters vs arguments, multiple parameters, refactoring repeats | 0 / 90 |
| **3.3 (this)** | **`return`, `print` vs `return`, local scope, unit checkpoint** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 3: write and call a function with parameters that returns a value | ✅ every task |
| Goal Py 4: distinguish a variable's scope inside a function from outside it | ✅ the scope-error prediction |
| Concepts: scope — local variable, a variable with the `global` attribute | ✅ |
| SC 4: reflect on bottom-up development and "what" vs "how" | ✅ the task-calculator checkpoint |
| Assessment 1–2: trace an algorithm using procedural abstraction; develop and implement one | ✅ checkpoint |

### Deliberate exclusions
The `global` keyword itself (only named as the risk to avoid), recursion, nested function definitions.

---

## 3. Lesson Goal

**`return` sends a value back to the line that called the function — only a returned value can be stored, compared,
or used in a further calculation; a variable created inside a function does not exist outside it.**

---

## 4. Core Mental Models

```python
def double(number):        # number: parameter, gets 6
    result = number * 2    # result: local - exists only inside double()
    return result           # sends 12 back to the call


answer = double(6)          # answer receives the returned value, 12
print(answer + 1)            # 13
```

- `print` shows a value on screen; the calling code gets nothing back. `return` hands a value back to the call —
  save it in a variable, compare it, or use it in another expression.
- A function can return a value with **no** parameters (3.1's kind, plus `return`), or with parameters and no return
  (3.2's kind, unchanged) — the three combinations are independent choices.
- A variable created inside a function is **local**: it exists only while that call runs, and cannot be read from
  outside it.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.3 – פעולות · "ערך חוזר וטווח הכרה" |
| 2–6 | **Recap (pairs):** `show_total(price, amount)` prints `price * amount` — can the result be used in another calculation right now? |
| 6–8 | Answer: not yet — there is nothing to catch; the value only appears on screen |
| 8–14 | `print` vs `return`, side by side |
| 14–20 | **Trace table (pairs):** `double(number)` with `result = number * 2` and `return result`, called as `answer = double(6); print(answer + 1)` — track `number`, `result`, the returned value, `answer` |
| 20–22 | Answer: `13` |
| 22–26 | A no-parameter function that still returns a value (`get_school_year()`); the count of parameters and the presence of `return` are independent choices |
| 26–30 | A returning function with no `print` inside it: `is_even(number)` |
| 30–36 | **Predict:** which line raises an error, and why — a local variable read from outside its function |
| 36–39 | Answer: `answer` is `31`; `print(secret)` outside the function raises `NameError` — the value travels out through `return`, the local name `secret` does not |
| 39–43 | Independent function (gets input via parameters, returns a clear result) vs. one that depends on a variable from outside its own signature — why the first is easier to test |
| 43–45 | The lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Points_Starter.py`](Points_Starter.py). Reference: [`Points_Reference.py`](Points_Reference.py).

## 45–53 — Warm-up: computed, never returned

```python
# Warm-up: predict what will print, run it, then add one word to fix it.


def discounted(price, percent):
    discount = price * percent / 100
    price - discount


final_price = discounted(80, 25)
print(final_price)
```

Predicting first: 25% of 80 is 20, so the price after the discount should be 60. Running it instead prints:

```text
None
```

The function computes `price - discount` but never sends it back — with no `return`, Python's default returned
value is `None`. Fix: add `return` before `price - discount` → `60.0`.

## 53–63 — Task 1: `is_even(number)`

Returns `True` or `False` — no `print` inside the function. Test with 14 and with 9.

```text
True
False
```

## 63–73 — Task 2: `passed(score)` used inside `if`

Returns `True` when `score >= 60`. Use the returned value directly inside an `if` / `else` that prints `Continue` or
`Try again`. Test with 72.

```text
Continue
```

Ask: could you write this without ever storing the returned value in a variable? (Yes — `if passed(72):` uses it
directly.)

## 73–86 — Task 3 (checkpoint): the task calculator

Three small functions, built and tested **one at a time**, bottom-up:

- `calculate_points(level, tasks)` → `level * tasks * 10`
- `passed_checkpoint(points)` → `True` when `points >= 100`
- `show_result(name, points, success)` → prints all three

Then combine them from the main program for at least three students, including one boundary case at exactly 100
points.

```text
Maya 120 True
Ali 100 True
Noa 30 False
```

`show_result` never recomputes the points — it only prints values it's handed.

## 86–90 — Save and exit check

Save As `G8_U3_M3_Points_<Name>.py`.

1. Write one short function that takes a value and returns a different one. Add a call that uses the returned
   value (not just discards it).
2. Why did `print(secret)` fail outside `build_code()`, even though `secret` clearly held a value while the function
   ran?

### Tool Note – Thonny
Thonny's Shell prints `>>> None` for any expression that evaluates to `None` — a quick way to notice a missing
`return` even outside a full program run.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `print` and `return` do the same thing | `print` only displays; `return` hands the value back to the calling code |
| A function without an explicit `return` returns nothing at all | It returns `None` — a real value that can cause confusing bugs |
| The number of parameters decides whether a function can return a value | The two are independent: any combination is possible |
| A local variable is somehow "secret" or protected | It's simply out of scope outside the function — nothing about it is hidden or safe |
| `show_result` should recompute `points` itself | It only reports values already computed and passed to it — one job per function |

---

# 8. Assessment Evidence (formative)

- The `double()` trace table completed before running
- The warm-up's missing-`return` bug explained (why `None`, not a wrong number)
- `is_even()` and `passed()` tested with the given values, `passed()` used directly inside a condition
- **Unit 3 checkpoint** — the task-calculator's three functions built and tested separately, then combined, with the
  boundary case at exactly 100 points
- Exit check
