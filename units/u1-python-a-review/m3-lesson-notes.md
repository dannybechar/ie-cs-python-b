# Unit 1.3 — Python A Review

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Until It's Done — the `while` Loop, the Stop Condition and Loops That Never End (Unit Checkpoint)

**Status:** Built, awaiting teacher approval 🔶 (reworked on 31 Oct 2026 to follow the Ministry's teaching materials)  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (8 min guided opening, then 82 min lab, including the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the **Ministry teaching materials** ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)) — three files:
- **2.0 "מצגת למורה — לולאת תנאי while — חזרה"** (12 slides): the loop variable (the *sentinel*, "זקיף") that must get a start value **before** the loop and change **inside** it; the `while` structure with `n = 0 / while n < 10 / print("hi") / n = n + 1`; question 1 (a 3-digit number, ask again) and question 2 (count until 3 even numbers); counting forward (score) and backward (timer); finite vs infinite loops (three snippets א–ג); `for i in range(0, 5, 1)` beside the equivalent `while` (`+=` allowed); three snippets with the same output; the exam task "מספר מעורר" from the Python A exam, done as a shared trace-then-run; the summary (including compound conditions in a loop).
- **2.1 "תרגול לפיצוח — לולאת while"** (4 questions): the series tasks with stop conditions (`1 + 8 + 27 + …` → Task 8; `2, 22, 222, …` → if time) and the red-beads counter with a "yes / no" sentinel (→ if time); question 3 (the four `num_even` snippets with a logic bug) and question 4 (primes, a nested loop) are **not** used — question 3 is left for Unit 3, where the course works with functions; question 4 is a nested loop.
- **"מלכודת הלולאה האינסופית"** (14-slide deck): the engine picture (setup · gate · body · accelerator), the sentinel's two duties, the three traps (the clock that does not update, the wrong direction, the condition that is always true), the sentinel typed by the user (the input must also be **inside** the loop), and the four-point **Safe Loop Checklist** → the diagnosis method used in the warm-up and Task 4.

**What changed from the previous version of 1.3** (built from the Ministry program text and a codex deck):
- **Kept:** the Lab + Lab structure; the warm-up convention (a never-ending validation loop, `ask_age()`; the Ministry's special case "the input must also be inside the loop"); the three-try locker with a `success` flag (now Task 6 — the Ministry's "compound condition in a loop"); the checkpoint role (now Task 8 plus the exit check); the red Stop button note.
- **Added:** the Ministry's vocabulary (loop variable / sentinel, "before the loop · condition · inside the loop"); trace tables for every loop; counting forward and backward; the four never-ending loops and the Safe Loop Checklist; `for` ↔ `while` conversion with `range(0, 5, 1)` and the three same-output snippets; the exam task "exciting number"; series with stop conditions on the sum.
- **Dropped:** the robot-distance hook, the `value = 5` prediction and the "for or while?" pairs quiz (replaced by the Ministry's `hi` loop and the `for` ↔ `while` task); `guess_number()` (kept in the unit strategy as enrichment only); the `points_goal()` checkpoint (it used a `for` loop — this meeting's checkpoint is now a `while` task, `cubes_sum()`).
- **Changed rule:** `+=` and `-=` are allowed (the Ministry uses them from this unit on); `x = x + 1` stays fine and is used side by side in Tasks 2 and 3.
- **Renamed files:** `Lock_Starter.py` / `Lock_Reference.py` → `While_Starter.py` / `While_Reference.py` (the meeting is no longer built around the locker alone).

**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 1

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 1.1 | comparisons → `and` / `or` / `not` → `elif` → trace → input validation | 45 / 45 |
| 1.2 | `for` + `range` (start, stop, step) → counter and total → trace → five-scores analyzer | 0 / 90 |
| **1.3 (this)** | **`while`: sentinel, condition, update → trace → counting up and down → loops that never end → `for` ↔ `while` → exciting number → series** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf pp. 6–7) | Covered here |
|---|---|
| CS 2, 7: tell a counted loop from a conditional loop; explain the difference | ✅ Task 5 (`for` ↔ `while`), exit check |
| CS 3: why a conditional loop needs a stop condition | ✅ anatomy, warm-up, Task 4 |
| CS 4: explain a loop algorithm's correctness | ✅ trace tables, Tasks 4 and 7 |
| CS 6 / Py 2: write a conditional loop | ✅ Tasks 1–3, 6–8 |
| CS 8: a conditional loop whose stop depends on a variable | ✅ Tasks 2 (counter), 6 (`attempts`, `success`), 8 (the sum) |
| Py 3: a function without parameters that contains a loop | ✅ every task |
| Teaching 4–5: a loop may never end; correctness = the goal holds and the loop ends | ✅ warm-up, Task 4, Safe Loop Checklist |
| Assessment 1–3, 6: trace, identify the loop type, count rounds, write a conditional loop | ✅ trace tables, exit check |

### Deliberate exclusions
`break`, `while True`, nested loops (not in the new program — the Ministry's prime-number worksheet question 4 is a nested loop and is **not** used), lists. Digit extraction (`num % 10`, `num // 10`) is used in Task 7: `%` was met in 1.2; `//` takes one minute to introduce at the board (it is part of the Python A exam task) — **teacher: confirm that your class has met `//`**; if not, say "`//` cuts off the last digit: `789 // 10` is `78`".

---

## 3. Lesson Goal

**`while` repeats as long as its condition is `True`. The loop variable gets a start value before the loop, and something inside the loop must move it toward `False` — in the right direction.**

---

## 4. Core Mental Models

```python
n = 0                  # 1. setup: start value, before the loop
while n < 10:          # 2. gate: the condition, checked before every round
    print("hi")        # 3. body: the work
    n = n + 1          # 4. accelerator: update, inside the loop
print("End loop")
```

- The condition is checked before every round; the last check gives `False` and ends the loop: **10 rounds, 11 checks**.
- The **loop variable** (the Ministry's "זקיף", sentinel) marks the end of the run. If it is typed by the user, the input line goes **before** the loop (first value) **and** inside it (next values).
- A `for` loop is a `while` loop with the three parts built in: `for i in range(0, 5, 1)` = start 0, stop condition `i < 5`, update by 1.
- **Safe Loop Checklist** (loop-trap deck): 1 start value before the loop · 2 a condition that can become `False` · 3 an update inside the loop · 4 an update that moves toward the stop (the right direction).
- A program that prints nothing wrong can still never end — test the ways out.

---

# 5. Lab (0–90)

Starter: [`While_Starter.py`](While_Starter.py). Reference: [`While_Reference.py`](While_Reference.py).

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 1.3 – חזרה על פייתון א' · "עד שמסיימים" |
| 2–8 | **Guided 1:** the four parts of `while` (the engine picture); **predict** (2 min, pairs): how many `hi`, how many condition checks? Answer with a trace table: 10 and 11 |
| 8–14 | **Warm-up:** `ask_age()` never stops (the input is not inside the loop); Stop button; one line fixes it |
| 14–21 | **Task 1:** `three_digit()` — the Ministry's question 1 |
| 21–30 | **Task 2:** `three_evens()` — the Ministry's question 2: a counter inside a conditional loop; trace table |
| 30–35 | **Task 3:** `score_and_timer()` — counting forward and backward |
| 35–46 | **Guided 2 + Task 4:** what is an infinite loop, the Safe Loop Checklist (3 min demo); diagnose and fix `loop_a` … `loop_d` (6 min); answers (2 min) |
| 46–54 | **Task 5:** `for` ↔ `while`; `compare_loops()` (predict with tables, then run) |
| 54–62 | **Task 6:** `locker()` — a compound condition |
| 62–75 | **Task 7 (together):** the exciting number — trace first (10 min), then run (3 min) |
| 75–83 | **Task 8 — unit checkpoint (alone):** `cubes_sum()` |
| 83–85 | Document and save |
| 85–90 | Exit check (5 min) |

Total: 2 + 6 + 6 + 7 + 9 + 5 + 11 + 8 + 8 + 13 + 8 + 2 + 5 = **90**. **If time** (no minutes in the clock; for fast students from Task 5 on): `count_red()` and `twos()`.

## 2–8 — Guided 1: the four parts of `while` and the first prediction

Show the engine on the board and name each part: **setup** (start value), **gate** (condition), **engine room** (body), **accelerator** (update). Then pairs predict, no running yet:

```python
n = 0
while n < 10:
    print("hi")
    n = n + 1
print("End loop")
```

Answer: ten times `hi`, then `End loop`. Run it, then fill the trace table on the board (checks: 11):

<div dir="rtl">

| n | `n < 10` | פלט |
|---:|---|---|
| 0 | True | hi |
| 1 | True | hi |
| … | … | … |
| 9 | True | hi |
| 10 | False | (יוצאים) `End loop` |

</div>

Ask: "What if the last line of the body is missing?" (`n` stays 0 → the condition is `True` forever) — the next minutes show it for real.

## 8–14 — Warm-up: the question that never comes back

```python
# Warm-up: run it and type -2. Why does it never stop? Stop it (red Stop button), then add one line.


def ask_age():
    age = int(input("Age: "))
    while age < 0:
        print("Invalid age")
    print("Accepted:", age)
```

With −2: `Invalid age` again and again, forever — `age` is the sentinel and nothing inside the loop changes it, so `age < 0` stays `True`. Stop it (Tool Note). Fix: `age = int(input("Age: "))` as the last line of the loop body (the loop-trap deck's "special case": a user-typed sentinel needs its input line **inside** the loop). Test −2, −1, 0 → `Invalid age` twice, then `Accepted: 0` (0 is not below 0).

## 14–21 — Task 1: `three_digit()` (Ministry question 1)

Ask for a whole number; while it is not a 3-digit number (below 100 or above 999) ask again; at the end print `End loop`.

```python
num = int(input("Enter number: "))
while num < 100 or num > 999:
    num = int(input("Enter number: "))
print("End loop")
```

The three parts, found in the code: first input **before** the loop, condition, new input **inside** the loop. Ministry follow-up: name two values that print `End loop` (e.g. 100, 999) and two values that make the program ask again (e.g. 99, 1000, −5). Test: 5, 1000, −3, 123 → four `Enter number:` then `End loop`.

## 21–30 — Task 2: `three_evens()` (Ministry question 2)

Read whole numbers until **3 even numbers** were typed — a counter whose value is the loop variable. Students first fill the blanks on paper (the Ministry's form: `count = ___ / while ___ < 3: / if ___ == 0: / count = ___`), then type it:

```python
count = 0
while count < 3:
    n = int(input("Enter number: "))
    if n % 2 == 0:
        count = count + 1
print("End loop")
```

Trace table for 3, 4, 6, 7, 8 (6 checks, 5 rounds):

<div dir="rtl">

| קלט `n` | `n % 2 == 0` | `count` אחרי הסבב | `count < 3` |
|---:|---|---:|---|
| (לפני) | | 0 | True |
| 3 | False | 0 | True |
| 4 | True | 1 | True |
| 6 | True | 2 | True |
| 7 | False | 2 | True |
| 8 | True | 3 | False |

</div>

Point out: `count` is **not** the number of inputs; it counts the numbers that pass the `if`. Rounds ≠ count.

## 30–35 — Task 3: `score_and_timer()` — forward and backward

The Ministry: the code on the right counts up (a score), the code on the left counts down (a timer). Students write both in one function: score 0…10, then timer 10…1, then `Time is up!`.

```python
score = 0
while score <= 10:
    print("Score:", score)
    score += 1
timer = 10
while timer > 0:
    print("Timer:", timer)
    timer -= 1
print("Time is up!")
```

Compare: up → the condition is `<` / `<=` a limit, the update is `+`; down → the condition is `>` a limit, the update is `-`. 11 lines `Score:` (0 to 10, inclusive because of `<=`), 10 lines `Timer:` (10 to 1). `+=` and `-=` are introduced here as "shorter `n = n + 1`".

## 35–46 — Guided 2 and Task 4: loops that never end

**Demo, 3 minutes (loop-trap deck):** a loop that never ends is a loop whose condition never becomes `False`: the program keeps repeating (or waiting for input) and the computer seems frozen. Show the Safe Loop Checklist (start value · condition can become `False` · update inside · right direction) and the three traps with one picture each: **the frozen clock** (no update), **the wrong direction** (`n = n - 1` while waiting for 10), **the condition that is always true** (`while n > -1` with `n` only growing).

**Task 4, 6 minutes:** `loop_a` … `loop_d` in the starter. Students **predict first** (the Ministry asks: what is the output? is the code valid? is there a stop condition? is the loop finite? what must be added?), then run **one**, stop it with the red button, and fix it:

<div dir="rtl">

| פונקציה | מה קורה | הסיבה | התיקון |
|---|---|---|---|
| `loop_a` | מבקשת מספר שוב ושוב, בלי סוף (אין הדפסה) | `count` לא משתנה | `count += 1` בתוך הלולאה |
| `loop_b` | מדפיסה `0` שוב ושוב; `End loop` לא מגיעה | אין עדכון | `n += 1` |
| `loop_c` | מדפיסה `0`, `-1`, `-2`, … בלי סוף | הכיוון הפוך — מתרחקים מ-10 | `n = n + 1` |
| `loop_d` | מדפיסה `0`, `1`, `2`, … בלי סוף | `n > -1` תמיד `True` כש-`n` רק גדל | `while n < 10` |

</div>

Answers (2 min): `loop_a` is the Ministry's snippet א, `loop_b` is ב (`End loop` is never reached), `loop_c` is ג, `loop_d` is the loop-trap deck's third trap. After the fixes: `loop_b`, `loop_c`, `loop_d` print 0…9 then `End loop`; `loop_a` asks for 3 numbers.

### Tool Note – Thonny
A loop that never ends keeps printing, or waits for input. Press the red **Stop** button (or Ctrl+F2) in the toolbar to stop the program (in the shell, **Stop/Restart backend** also works), then fix the code. Before running a task that may never end, save the file.

## 46–54 — Task 5: `for` ↔ `while`

1. Write `for_to_while()`: the same output as `for i in range(0, 5, 1): print(i)` but with `while` — start `i = 0`, stop condition `i < 5`, update `i += 1` (the Ministry: "for does the update by itself; with while we must remember it"). Output: `0 1 2 3 4`, one per line.
2. **Predict with tables, then run `compare_loops()`:** three snippets A (`while n < 10`, `n += 2`), B (`for item in range(10)` with `if item % 2 == 0`), C (`for item in range(0, 10, 2)`). Ask: which one is not like the others? (A is the only `while`.) Which outputs are the same? **All three** print `0 2 4 6 8` and `Done!` (the Ministry asks "which output is the same" — the surprise is that all are).

## 54–62 — Task 6: `locker()` — a compound condition in a loop

Up to three tries to type 4321; then `Access granted. Attempts: N` or `Access blocked`. Students say the condition in words first: "tries left **and** not found yet". `attempts += 1` on every round; the flag `success` becomes `True` when the guess is right.

<div dir="rtl">

| קלט | פלט |
|---|---|
| 4321 | Access granted. Attempts: 1 |
| 1111, 4321 | Access granted. Attempts: 2 |
| 1111, 2222, 4321 | Access granted. Attempts: 3 |
| 1111, 2222, 3333 | Access blocked — and no fourth `Code:` |

</div>

Ask: what are the two ways out of this loop? (success, or three tries used) — one of the two parts of the `and` becoming `False` is enough.

## 62–75 — Task 7 (together): "מספר מעורר", the Python A exam task

**Exciting number:** a whole number in which the sum of the digits is at least **3 times** the number of digits. Read a number and print whether it is exciting.

Whole class, **trace first (10 min):** the teacher reads the plan — "take the last digit (`num % 10`), add it to the sum, count it, cut it off (`num // 10`); repeat while `num > 0`". Students fill the trace table on paper for **789**, then check **100** by themselves:

<div dir="rtl">

| `num` | `num > 0` | `digit` | `total` | `digits` |
|---:|---|---:|---:|---:|
| 789 | True | 9 | 9 | 1 |
| 78 | True | 8 | 17 | 2 |
| 7 | True | 7 | 24 | 3 |
| 0 | False | | 24 | 3 |

</div>

After the loop: `24 >= 3 * 3` → `Exciting number`. (100: `total` 1, `digits` 3 → `1 >= 9` is `False` → `Not an exciting number`.)

**Then run (3 min):** students type the function from the starter's plan; test 789, 100, 99, 123 → `Exciting number`, `Not an exciting number`, `Exciting number`, `Not an exciting number`. Name the three parts again: start values (`total`, `digits`) **before** the loop, the condition `num > 0`, the update `num = num // 10` **inside**. Positive numbers only (0 would skip the loop and print `Exciting number`).

```python
num = int(input("Enter a positive number: "))
total = 0
digits = 0
while num > 0:
    digit = num % 10
    total += digit
    digits += 1
    num = num // 10
if total >= 3 * digits:
    print("Exciting number")
else:
    print("Not an exciting number")
```

## 75–83 — Task 8: `cubes_sum()` — unit checkpoint (individual)

The Ministry worksheet 2.1, question 1: a series written as a loop with a stop condition on the **sum**. Add `1 + 8 + 27 + …` (the cubes) while the sum is below 100; print the sum after each term, and at the end `Stopped at <sum> after <N> terms`. Students plan on paper (start values · condition · what changes each round), build alone, and test:

<div dir="rtl">

| שורה | פלט |
|---|---|
| 1 | Sum so far: 1 |
| 2 | Sum so far: 9 |
| 3 | Sum so far: 36 |
| 4 | Sum so far: 100 |
| 5 | Stopped at 100 after 4 terms |

</div>

The teacher walks around and asks each student to trace one round aloud. **Diagnostic, not graded:** note who needs help with the start values, the stop condition, the update (the `i` that must grow), or the final message (see §7).

## If time (no minutes in the clock)

- `count_red()` — Ministry 2.1 question 2: colors typed one by one; after each color `Do you want to continue? yes/no`; at the end `The number of red beads is: N`. Test `red, yes, blue, yes, red, no` → `2`. The answer `"yes"` is the sentinel.
- `twos()` — the series `2, 22, 222, 2222` while the term is below 10000: `term = term * 10 + 2`.

## 83–85 — Document and save

Save As `G8_U1_M3_While_<Name>.py`.

## 85–90 — Exit check

1. `n = 0`, `while n < 10: print("hi"); n = n + 1` — how many `hi`, and how many times is the condition checked? (10; 11 — the last check gives `False`)
2. `n = 5`, `while n > 0: print(n); n = n + 1` — does it end? Which point of the checklist is broken, and how do you fix it? (never ends — direction: `n` moves away from 0; use `n = n - 1`)
3. Write `for i in range(0, 3, 1): print(i)` as a `while` loop. (`i = 0`, `while i < 3:`, `print(i)`, `i += 1`)

---

# 6. Misconception Risks

| Misconception | Correction |
|---|---|
| The condition is checked in the middle of a round | Only before each round |
| The value in the condition changes by itself | Something in the body must change it |
| `while` is an `if` | `if` checks once; `while` checks again after every round |
| A user-typed sentinel needs only one `input` | One before the loop (first value) and one inside (next values) |
| `count` counts the rounds | It counts what passes the `if` — rounds and count differ in Task 2 |
| Any update is fine | It must move **toward** the stop (`n - 1` while waiting for 10 never ends) |
| `n > -1` is a stop condition | A condition that is always `True` is never a stop |
| `and` in a `while` needs both parts `False` to stop | It stops as soon as one part is `False` |
| `for` and `while` give different results | They can be the same — `for` is `while` with the three parts built in |
| A program with no error message is correct | It can still never end — test every way out |

---

# 7. Assessment Evidence (formative)

- The `hi` prediction with the number of checks (official assessment 1, 3)
- The warm-up explained with the checklist: which variable never changed (CS 3, 4)
- Trace tables of Tasks 2 and 7 on paper (assessment 1)
- `loop_a`–`loop_d` diagnosed and fixed: which checklist point was broken (teaching 4–5)
- `locker()` passing all four tests, including "no fourth try" (CS 8)
- **Unit 1 diagnostic checkpoint** — `cubes_sum()` built alone, tested, one round traced aloud; plus the exit check. Record per student: conditions (1.1), counted loops and totals (1.2), conditional loops (1.3). Evidence for planning, not a grade.
