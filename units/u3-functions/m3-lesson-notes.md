# Unit 3.3 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: Local and Global Variables

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials (the source of truth for this unit): deck **4.3 "משתנים בפעולות"**
(24 slides) feeds the theory — life cycle of a local variable, `NameError` outside, "each function has its own world",
`print_double`, the "weight of a number" exercise, a global read inside a function, the `score = 100` trap, `global`,
`add_bonus`, the forgotten-`global` error, the local / global table; worksheet **4.5** (with the teacher solution **4.5.0**)
exercises 1–5 feed the lab; **4.6 "תפקידי משתנים בפעולות"** (solutions in **4.5.0**) questions 1, 2 and 4 feed the lab and
the checkpoint.
**Changed from the previous version of 3.3** (codex deck: `print` vs `return`, bottom-up design, the task-calculator
checkpoint): `return` moved to 3.1 and 3.2; this meeting is now the scope meeting and `global` is **taught** (the previous
version only named it). The task-calculator checkpoint was dropped — the Ministry exercises win; the new checkpoint is a
donation campaign adapted from 4.6 question 4. **Changes to Ministry code:** 4.6 question 1 builds its answer with an
f-string and question 4 returns two values at once (`return sumOfDonations, numberOfHighDonors`, unpacked with
`totalSum, highDonors = ...`); f-strings come in Unit 4 and returning several values (a tuple) is not taught, so the
parking function returns a short phrase (the main program prints the hours), and the donation checkpoint uses two
global variables that `add_donation` changes — which also fits this meeting's topic. Question 3 (the calculator that returns
four values) is held out for the same reason; the "if time" block has the four-function version. The error text on the
Ministry's slide 21 is older than Python 3.14; the lab uses the real message (see Misconception Risks).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 3.1 | recap; several parameters and their order; `return` vs `print` | 45 / 45 |
| 3.2 | return practice; exam questions with `while` inside functions | 0 / 90 |
| **3.3 (this)** | **local and global variables, `global`, variable roles, unit checkpoint** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 4: distinguish a variable's scope inside a function from outside it | ✅ whole meeting |
| Concepts: scope (local variable, `global`) | ✅ |
| SC: use a building block through its interface — the caller does not see the function's local variables | ✅ "each function has its own world" |
| Assessment: tracing; developing and implementing | ✅ checkpoint |

### Deliberate exclusions
`nonlocal`, nested functions, returning several values (tuple), f-strings (Unit 4), lists as global variables (Unit 7).
Style note for the teacher: a program that depends on many globals is harder to read than one that passes values with
parameters and `return`. The lab teaches `global` because the program and the exam use it, and the last slide says
"prefer parameters and `return`; use `global` when several calls must share one running value".

---

## 3. Lesson Goal

**A variable made inside a function lives only while it runs. A variable made outside every function can be read by all
functions — and to change it from inside, the function must say `global`.**

---

## 4. Core Mental Models

```python
score = 0                       # global: defined outside every function


def add_bonus(bonus):
    global score                # "this score is the outside one"
    score = score + bonus       # without the line above: UnboundLocalError


def show_square(num):
    result = num ** 2           # local: born when the function starts, gone when it ends
    print(result)
```

- Calling a function opens a clean workspace. Its parameters and the variables it creates are local.
- Each function has its own world — two functions may each have a local `result`, and they never meet.
- Reading a global needs nothing. **Assigning** to a name inside a function makes that name local, unless `global` was declared.
- `score = 100` inside a function creates a new local `score`; the outside `score` does not change.
- Variable roles seen in functions: a **counter** (counts events), an **accumulator** (adds up), a **best-so-far holder** (`biggest`), a **flag** (`found`). Role names are for classroom talk; the Ministry's 4.6 worksheet practices the roles without naming them.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.3 – פעולות · "משתנה מקומי ומשתנה גלובלי" |
| 2–6 | **Hook:** `average_grade(85, 95)` — `grade1` and `grade2` are used inside the function. Can `print(grade1)` work after the call? Vote, then test |
| 6–13 | **A local variable's life (deck 4.3, slides 4–6):** `print_square(4)`; `result` is born and dies with the call; **predict** `print(result)` at the end → `NameError` (question slide first, answer on the next) |
| 13–17 | **Separate worlds:** `print_square(3)`, `print_cube(2)` — both use `result`; no clash |
| 17–24 | **Write it (pairs):** `print_double(num)` with a local `doubled` → `Doubled number is: 10`. Then check and discuss |
| 24–30 | **A global variable (slides 13–15):** `score = 0`; `print_score()` reads it. **Predict:** `change_score()` sets `score = 100` and prints inside; what do the two prints show? → inside 100, outside 0 |
| 30–36 | **Why:** the assignment made a new local. **The fix:** `global score` → inside 100, outside 100 |
| 36–41 | **The trap:** `counter = counter + 1` without `global` → `UnboundLocalError`. Read the real message on Python 3.14; Python decides at compile time that `counter` is local because it is assigned in the function |
| 41–44 | The local / global table: where defined, who can see it, when it disappears, how to change it from inside |
| 44–45 | The lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Scope_Starter.py`](Scope_Starter.py). Reference: [`Scope_Reference.py`](Scope_Reference.py).

## 45–49 — Warm-up: the counter that does not count

```python
counter = 0


def do_step():
    counter = counter + 1
    print("Step done!")


do_step()
print("Counter:", counter)
```

```text
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

(Python 3.14. The Ministry slide shows the older wording, `local variable 'counter' referenced before assignment`.)
Fix: add `global counter` as the first line of the function → `Step done!` then `Counter: 1`.

## 49–54 — Task 1: local or global? (worksheet 4.5, exercises 1 and 3)

On paper, then run. (1) In the code with `app_name` and `show_greeting`: which variable is global, which are local, and what does `print(welcome_msg)` at the end of the program do (`NameError: name 'welcome_msg' is not defined`)? (2) In the code with `score = 50` and `update_score()`: write the two printed lines, and explain why the outside `score` stays 50.

## 54–59 — Task 2: `add_bonus` (deck 4.3, practice 2)

A global `total_points = 0`; a function `add_bonus(bonus)` adds the bonus to it. Call it twice with 10 and print the total: `20`.

## 59–67 — Task 3: the two parking lots (worksheet 4.6, question 1)

Lot A costs 20 per day. Lot B: up to 3 hours 5, up to 4 hours 15, more 30. Write `parking_a()`, `parking_b(hours)` and `compare_parking(hours)`, which uses the other two and returns the phrase of the cheaper lot (or `"Same price"`). Print for 2, 4, 10 and 24 hours: B, B, A, A. A function that calls other functions: each keeps its own locals.

## 67–71 — Task 4: `how_many_legs(animal)` (question 2)

`elif` chain, one `return` per animal, `-1` for anything else. `spider` 8, `ant` 6, `dog` / `cat` 4, `chicken` 2.

## 71–83 — Checkpoint: donation campaign (question 4, adapted)

Two global variables with roles: `sum_of_donations` (an accumulator) and `number_of_high_donors` (a counter). `add_donation(donation)` adds the donation; above 100 it also counts the donor and prints `Thank you, the certificate is on the way`. The main program reads the number of donors, then one donation each, calls `add_donation`, and prints both globals. Example with 3 donors `150`, `80`, `200`: two thank-yous, `Total donations: 430`, `Number of donations above 100 nis: 2`. Boundary test: a donation of exactly 100 is **not** a high donation.

## If time

`add_coins(new_coins)` with a global `coins` (worksheet 4.5 exercise 4: `coins = 10`, `add_coins(5)` → `15`); `weight_of_number(number)` for a two-digit number — the product of its digits (`75` → 35, `12` → 2), and a main program that reads two numbers and prints the one with the bigger weight (deck 4.3, slide 10); the calculator of question 3 as four small functions, each returning one value.

## 83–90 — Save and exit check

Save As `G8_U3_M3_Scope_<Name>.py`.

1. A function does `total = total + 5` and fails with an error. What is the error, and what single line fixes it?
2. A variable named `area` is created inside `calculate_rectangle`. Why does `print(area)` after the call raise `NameError`?
3. When is it better to pass a value as a parameter instead of using a global?

### Tool Note – Thonny
Thonny's **Variables** view (View › Variables) lists the global variables of the program; while stepping inside a function, Thonny shows the function's locals in the call frame. Use it on `do_step()` before and after adding `global`.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A function can change an outside variable just by assigning to it | Assignment creates a new local; `global` is what ties the name to the outside one |
| "I only read it, so I need `global` too" | Reading a global needs nothing; only assignment does |
| `UnboundLocalError` is a new kind of rule | It is the same rule: the name is local because the function assigns it, and the right side reads it before it has a value |
| After the call, the function's variables are still there | They are gone; only a returned value or a global survives |
| Using `global` everywhere is good style | Fine for a shared running value (score, counter); otherwise parameters and `return` are clearer |
| The error message is the same as the slide | Python 3.14: `UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value` |

---

# 8. Assessment Evidence (formative)

- The `NameError` and the `change_score` predictions written before running
- The warm-up explained: why `global` fixes it
- Task 1 answers on paper
- Tasks 2–4 passing their test values
- **Unit checkpoint:** `add_donation` with two globals, the total 430 and the high-donor count 2 for the example, the boundary 100 handled correctly
- Exit check
