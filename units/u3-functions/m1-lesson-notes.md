# Unit 3.1 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: Several Parameters and `return`

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials (the source of truth for this unit):
deck **4.1 "פעולות חלק א"** (28 slides) feeds the whole first half — the reminder of a one-parameter function, several
parameters, parameter order, the `calculate average` and `print_total` examples, the wrong-argument-count `TypeError`,
`print` vs `return` (`square_print` / `square_return`), the five steps of a call that returns, `return` stops the
function, using the returned value, the forgotten-`return` `None` trap, the four-kinds table; and worksheet
**4.2 "דף תרגילים — פעולה המחזירה ערך"** (with the teacher solution **4.2.0**) feeds the lab: exercises 1–6.
**Changed from the previous version of 3.1** (codex deck: `def`, the call, execution order, a four-function control
panel, no parameters): the control-panel lab is gone; no-parameter functions are now a **7-minute recap** (the program
lists them, and some students may not have met one), and the meeting moves on to what the Ministry teaches here:
several parameters and `return`. The call-before-`def` warm-up bug became a recap question. Not used from 4.1:
nothing — slides 24–28 (`find_max`, `final_grade`) are held for 3.2. Changes to Ministry code: none in the lecture
examples; `check_pass` and the others run as written.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **3.1 (this)** | **recap; several parameters and their order; `return` vs `print`** | 45 / 45 |
| 3.2 | return practice, exam questions with `while` inside functions | 0 / 90 |
| 3.3 | local and global variables, `global`, variable roles, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 1–2: write and call a function without / with parameters, no return value | ✅ recap (7 min) and multi-parameter `print_total` |
| Goal Py 3: write and call a function with parameters that returns a value | ✅ `return`, using the value, worksheet 4.2 |
| SC 1–3: an algorithm as a building block, used by its name, not by its body | ✅ "the caller gets the value and does not care how it was computed" |
| Python syntax: colon, indentation, `def` | ✅ recap |

### Deliberate exclusions
Scope and `global` (3.3), exam-style loops inside functions (3.2), default and keyword arguments, returning more than
one value (the Ministry's worksheet 4.6 does it; it is a tuple and is not taught here), recursion, lists.

---

## 3. Lesson Goal

**A function can take several parameters (matched to the arguments by position) and can send a value back with
`return` — `print` only shows a value, `return` hands it to the line that called the function.**

---

## 4. Core Mental Models

```python
def print_total(product, price, quantity):   # three parameters, matched by position
    total = price * quantity
    print("Total for", product, "is:", total, "shekels")


def square_return(num):
    return num ** 2                           # the value goes back to the call


x = square_return(5)                          # x = 25
```

- The first argument fills the first parameter. Swapping the order does not always fail — it can silently give a wrong answer.
- The number of arguments must equal the number of parameters: `TypeError: print_total() missing 1 required positional argument: 'quantity'`.
- `print` shows a value on the screen. `return` gives a value to the call, so it can be saved, compared, added.
- `return` ends the function immediately: any line after it in the same branch never runs.
- A function with no `return` gives back `None`.
- Same idea students know: `name = input()` — `input()` is a function that returns a value.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.1 – פעולות · "כמה פרמטרים וערך חוזר" |
| 2–9 | **Recap (pairs, predict):** a zero-parameter `show_header()` and a one-parameter `greet(name)`; write the output of four lines of calls. Cover `def` vs the call, and that the `def` must come before the call (`NameError` otherwise) — students who have never seen a no-parameter function get it here |
| 9–17 | **Several parameters (deck 4.1, slides 4–7):** the comma in the `def` and in the call; `greet("Dana", 14)` vs `greet(14, "Dana")` — predict the second line; `print_average(85, 95)` |
| 17–25 | **Write it (alone, then check):** `print_total("pencil", 3, 5)` → `Total for pencil is: 15 shekels` (slides 8–9). Then show the wrong-count call and read the `TypeError` aloud |
| 25–28 | Hook: `name = input()` gives a value back. Can our own functions? |
| 28–36 | **`print` vs `return`:** `square_print(5)` vs `x = square_return(5)`; the five steps of a call; `return` stops the function; run the version with a `print` after the `return` |
| 36–40 | **Predict:** `result = double(6)` then `print(result)` (12). Using the returned value: in `print`, in an `if`, in an expression (`square_return(5) + 10`); `average_grade(55, 65)` with Passed / Failed |
| 40–43 | **The trap:** `square_no_return(5)` prints `None` — the most common `return` mistake. The four-kinds table (one / several parameters × without / with `return`) |
| 43–45 | The lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Return_Starter.py`](Return_Starter.py). Reference: [`Return_Reference.py`](Return_Reference.py).

## 45–50 — Warm-up: the function that prints `None`

```python
def triple(num):
    num * 3


result = triple(7)
print(result)
```

```text
None
```

The body computes `num * 3` and throws it away; with no `return` the function gives back `None`. Fix: `return num * 3` → `21`.

## 50–60 — Task 1: trace and find the error (worksheet 4.2, exercises 1–3)

On paper first, then run:

1. `calculate_box(4, 5)` — `Area is: 20`.
2. `sum_prices(25, 40)` — three parameters, two arguments: `TypeError: sum_prices() missing 1 required positional argument: 'item3'`. Fix: send three arguments (`25, 40, 30` → `Total price: 95`).
3. `check_pass(85)` — `Result: Pass`. The line `print("Congratulations!")` is after the `return`, so it never runs.

## 60–66 — Task 2: `rectangle_perimeter(length, width)` (exercise 4)

Fill in the blanks (`2 * (length + width)`, `return`); call with 6 and 3 → `Perimeter: 18`.

## 66–72 — Task 3: from `print` to `return` (exercise 5)

`calculate_pay(hours, wage)` prints the pay; change it to return the pay, save in `total`, print → `Total pay: 400` (8 hours, 50 per hour).

## 72–79 — Task 4: `get_cheaper(price1, price2)` (exercise 6)

Two returns inside `if` / `else`. `get_cheaper(80, 55)` → `Cheaper price is: 55`. Ask: what does the function give back if the prices are equal? (the second one — both are the same number.)

## 79–82 — If time

`average_grade(grade1, grade2)` returns the average; use the returned value in an `if` (`Passed` / `Failed`). `average_grade(55, 65)` → `Passed`.

## 82–90 — Save and exit check

Save As `G8_U3_M1_Return_<Name>.py`.

1. A function should return the double of a number but the call prints `None`. What is missing?
2. In `def f(a, b):` the call is `f(5)`. What happens, and what is the error called?
3. What is the difference between `print(x)` inside a function and `return x`?

### Tool Note – Thonny
Thonny's **Shell** shows the value of an expression when you type it, which can look like `print`. In a program file nothing is shown unless `print` is called.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `print` inside the function "returns" the result | It only shows it; the call gets `None` |
| Arguments match parameters by name | By position: `greet(14, "Dana")` runs, and is wrong |
| Code after `return` still runs | `return` ends the function at once |
| A function with no `return` gives nothing | It gives `None`, and `None` can be saved, printed — and break later arithmetic |
| Every function must return something | Both kinds are right; choose by what the caller needs (the four-kinds table) |

---

# 8. Assessment Evidence (formative)

- The recap prediction and the `greet(14, "Dana")` prediction written before running
- `print_total` written without looking at the slide
- The warm-up explained, not only fixed
- Tasks 1–4 done with the worksheet's expected output
- Exit check (all three questions)
