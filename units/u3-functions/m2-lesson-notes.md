# Unit 3.2 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: Practice — Returning Functions and Loops Inside Functions

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** Lab + Lab (two short demos, then tasks)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials (the source of truth for this unit): worksheet **4.2** exercises
7–8 (`three_averages`, `calculate_shipping`, solutions in **4.2.0**); deck **4.1** slides 24–28 (`find_max`, `final_grade`);
**4.4 "תרגול לפיצוח — שאלות מבחינות"** (four exam-style questions, with `while` and `for` inside functions: the `secret1`–`secret4`
digit loops, a "special" number, a "perfect" number, positions of a digit in an ID); worksheet **4.5** exercise 6 (the
club-gift story, `calculate_gift`, with its solution in **4.5.0**).
**Changed from the previous version of 3.2** (codex deck: parameters and arguments, `show_mission`, `show_card`, a refactor
task): that meeting is now 3.1's theory (several parameters). This meeting is the practice of `return`, the point where the
unit meets the exam — functions that return, and loops that live inside functions.
**Changes to Ministry code** (all small, listed so the teacher can undo them): `int(number / 10)` → `number // 10`
(same result for whole numbers, and the class has `//` from the Ministry's own question 2); the `"%d" % result` printing in
`secret3` / `secret4` → `print("The digit sum is:", total)` (the `%` format is not taught); the variable name `sum`
(shadows a Python function) → `total`; question 2's blanks follow the definition in the question
(`digit > total / 2`; in the Ministry file the `if` slot is a drop-down that shows `num != 0`, which does not match the
definition); question 4's blanks use `range(1, 10)` for a nine-digit ID.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 3.1 | recap; several parameters and their order; `return` vs `print` | 45 / 45 |
| **3.2 (this)** | **return practice; exam questions with `while` inside functions** | 0 / 90 |
| 3.3 | local and global variables, `global`, variable roles, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 3: write and call a function with parameters that returns a value | ✅ every task |
| Assessment: tracing an algorithm that uses procedural abstraction, developing one | ✅ digit-loop tracing, writing exam-style functions |
| Program loops (Unit 1 review): `while`, `for`, counters, accumulators | ✅ used inside functions |

### Deliberate exclusions
Returning more than one value; `global` (3.3); recursion; lists.

---

## 3. Lesson Goal

**The function is the unit of an exam answer: it takes values, uses a loop or an `if`, and returns one result — and the
first matching `return` ends it.**

---

## 4. Core Mental Models

```python
def find_max(a, b, c):
    biggest = a                 # assume a is the biggest...
    if b > biggest:
        biggest = b             # ...and replace it when something bigger shows up
    if c > biggest:
        biggest = c
    return biggest


def final_grade(grade, bonus):
    total = grade + bonus
    if total > 100:
        return 100              # early return: nothing below it runs
    return total
```

- Digit extraction: `number % 10` is the last digit, `number // 10` removes it; a `while number > 0` loop visits every digit.
- A variable that is **built up** inside a loop (`total`, `counter`, `result`) starts before the loop — and the right start differs: `0` for a sum or a count, `1` for a product.
- Several branches, one `return` each: only one of them runs.
- Exam shape: read the code, trace it with a table, then write or complete a function.

---

# 5. Lab (0–90)

Starter: [`Practice_Starter.py`](Practice_Starter.py). Reference: [`Practice_Reference.py`](Practice_Reference.py).
The tasks are in order of difficulty; Tasks 6 and 7 are the heaviest — if the class is slow, move one of them to "if time".

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.2 – פעולות · "ערך חוזר וקוד שמחשב" |
| 2–8 | Warm-up |
| 8–12 | Demo 1: several `return`s, the first one that runs ends the function |
| 12–20 | Task 1 |
| 20–30 | Task 2 |
| 30–37 | Task 3 |
| 37–43 | Task 4 |
| 43–48 | Demo 2: digits with `%` and `//` |
| 48–58 | Task 5 |
| 58–66 | Task 6 |
| 66–76 | Task 7 |
| 76–84 | Task 8 |
| 84–90 | Save and exit check (the "if time" block fills any gap before it) |

## 2–8 — Warm-up: arguments in the wrong order

```python
def price_after_discount(price, percent):
    discount = price * percent / 100
    return price - discount


print(price_after_discount(20, 200))
```

```text
-20.0
```

The price is 200 and the discount is 20 percent: the call has them swapped (`20` is taken as the price, `200` as the percent). No error — only a wrong answer. Fix the call: `price_after_discount(200, 20)` → `160.0`.

## 8–12 — Demo 1: the first `return` ends it

Show `get_cheaper` and `check_pass` from 3.1: a `return` in each branch. Predict the output for different inputs before running.

## 12–20 — Task 1: `three_averages(g1, g2, g3)` (worksheet 4.2, exercise 7)

Returns the average. `three_averages(80, 90, 100)` → `The average is: 90.0`.

## 20–30 — Task 2: `calculate_shipping(price, is_express)` (exercise 8)

Free shipping from 200; otherwise 30 if express, else 15; returns price + shipping. Test three cases: `(150, True)` → 180, `(250, True)` → 250, `(100, False)` → 115. Ask why `elif` and not three `if`s: the first rule that matches decides.

## 30–37 — Task 3: `find_max(a, b, c)` (deck 4.1)

Start by assuming `a` is the biggest. `find_max(7, 15, 9)` → `The biggest number is: 15`. Role: `biggest` holds the best value so far.

## 37–43 — Task 4: `final_grade(grade, bonus)` (deck 4.1)

Grade plus bonus, never above 100. `(95, 10)` → 100; `(70, 10)` → 80.

## 43–48 — Demo 2: digits

```python
def print_digits(number):
    while number > 0:
        print(number % 10)
        number = number // 10
```

`print_digits(4072)` → `2`, `7`, `0`, `4`. Trace table on the board: `number`, `number % 10`, printed. The loop ends when `number` reaches 0.

## 48–58 — Task 5: what do they do? (worksheet 4.4, question 1)

Four functions, `secret1`–`secret4`, in the starter. On paper, predict each output, then run:

| Call | Output |
|---|---|
| `secret1(12345)` | `5` `4` `3` `2` `1` (one per line) |
| `secret2(12345)` | `5` — it counts the digits |
| `secret3(1024)` | `The digit sum is: 7` — it also returns 7 |
| `secret4(1024)` | `The digit product is: 0` |

`secret4` loops `while number > 1`, so the leading `1` is skipped — which happens not to matter here, because `4 * 2 * 0` is already 0. Ask: what would `secret4(12)` give? (`result = 1 * 2 = 2`, then `number = 1`, the loop stops: 2 — the leading digit 1 would not change a product anyway.)

## 58–66 — Task 6: `special_number()` (question 2)

A number is "special" when its last digit is more than half the digit sum. Code with blanks (also in the brief):

```python
def special_number():
    num = int(input("Please enter a number: "))
    total = 0
    digit = num % 10
    while num != 0:
        total = total + ______
        num = num // ______
    if ______ > total / 2:
        print("Number is special")
    else:
        print("Number is not special")
```

Answers: `num % 10`, `10`, `digit`. Test: `129` → special (9 > 6.0), `867` → not special (7 > 10.5 is false). Part (a) of the Ministry's question — decide on paper whether 867 is special — is the first thing students do.

## 66–76 — Task 7: `perfect_number()` (question 3)

A number is "perfect" when it equals the sum of its divisors (not including itself): 28 = 1 + 2 + 4 + 7 + 14. Blanks: start `total = 0`; `if num % x == 0:`; `total = total + x`; `x = x + 1`; `if total == num:`. Test `28` → `Perfect number`, `12` → `Not perfect number`.

## 76–84 — Task 8: `calculate_gift(years, monthly)` (worksheet 4.5, exercise 6a)

A customer with monthly purchases of more than 1,200 gets a voucher: 50 per year of membership under 8 years, 100 per year from 8 years. Otherwise 0. `calculate_gift(5, 1500)` → 250; `(10, 1500)` → 1000; `(10, 1000)` → 0. Two early returns.

## If time (students who finish early; not part of the whole-class clock)

- Exercise 6 parts b and c: ten customers read with `input()`, count and total of the vouchers (`count += 1`, `total += voucher`) — `gifts_for_ten()` in the reference. (`+=` is allowed.)
- Question 4, `find_location()`: the positions of a digit in a nine-digit ID, counted from the right (`found` is a flag).

## 84–90 — Save and exit check

Save As `G8_U3_M2_Practice_<Name>.py`.

1. A function ends with `return` inside an `if`. What happens to the lines below it when the condition is true?
2. Why does `secret2` start `counter = 0` and `secret4` start `result = 1`?

### Tool Note – Thonny
Use Thonny's **Debugger** (the "step into" button) on `secret3(1024)` to watch `number` and `total` change on every pass of the loop. Input prompts for Tasks 6 and 7 appear in the Shell.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The biggest of three needs `and` with every comparison spelled out | A "best so far" variable scales to any number of values (`find_max`) |
| A variable inside a loop can start anywhere | The start value must be neutral to the operation: 0 for `+`, 1 for `*` |
| `number // 10` and `number / 10` are the same | `/` gives a float (`123 / 10` is `12.3`), so the digits are not cut off; `//` drops the last digit |
| Digit loops always visit digits left to right | `% 10` gives them right to left |
| `return` inside a loop is "wrong" | It is valid — it ends the function (not only the loop) |

---

# 8. Assessment Evidence (formative)

- Warm-up explained (the cause, not only the fix)
- Task 5 predictions written before running, with a trace table for at least one function
- Tasks 1–4 and 8 passing the test calls above
- Tasks 6–7 completed with the blanks justified aloud
- Exit check
