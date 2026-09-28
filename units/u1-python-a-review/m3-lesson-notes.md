# Unit 1.3 — Python A Review

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Until It's Done — `while`, the Stop Condition and the Three-Try Locker (Unit Checkpoint)

**Status:** Built, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (22 min guided practice, then 68 min lab, including the unit checkpoint)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the codex deck `python_b_unit01_m03_while_loops_final.pptx` (robot-distance hook, the three parts of `while`, the `value = 5` prediction with four checks, "for or while", ask-again validation, the three-try locker with a `success` flag and four tests, the one-line-fix exit question kept; `+=` / `-=` → `x = x + 1`; its never-ending `print` loop replaced — Python A 5.3 used the same warm-up — by a validation loop that forgets to ask again) and the teacher's raw `G8_Unit1_M3` (points-goal diagnostic kept as the unit checkpoint)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 1

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 1.1 | comparisons → `and` / `or` / `not` → `elif` → trace → input validation | 45 / 45 |
| 1.2 | `for` + `range` (start, stop, step) → counter and total → trace → five-scores analyzer | 0 / 90 |
| **1.3 (this)** | **`while` → stop condition → ask until valid → three-try locker → unit checkpoint** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf pp. 6–7) | Covered here |
|---|---|
| CS 2, 7: tell a counted loop from a conditional loop; explain the difference | ✅ "for or while", exit check |
| CS 3: why a conditional loop needs a stop condition | ✅ hook, warm-up |
| CS 4: explain a loop algorithm's correctness | ✅ warm-up, Task 2 tests |
| CS 6 / Py 2: write a conditional loop | ✅ Tasks 1–2 |
| CS 8: a conditional loop whose stop depends on a variable | ✅ Task 2 (`attempts`, `success`) |
| Py 3: a function without parameters that contains a loop | ✅ every task |
| Teaching 4–5: a loop may never end; correctness = the goal holds and the loop ends | ✅ warm-up |
| Assessment 1–3, 6: trace, identify the loop type, count rounds, write a conditional loop | ✅ prediction, exit check |

90 practice minutes of "conditional repetition", including the unit's diagnostic checkpoint.

### Deliberate exclusions
`break`, `while True`, nested loops (not in the new program — no validation loop inside the points loop), `+=`.

---

## 3. Lesson Goal

**`while` repeats as long as its condition is `True` — something inside the loop must move it toward `False`, on every path.**

---

## 4. Core Mental Models

```python
secret = 4321
attempts = 0                              # 1. start values, before the loop
success = False
while attempts < 3 and not success:       # 2. condition: tries left AND not found yet
    guess = int(input("Code: "))
    attempts = attempts + 1               # 3. update: every round moves toward the end
    if guess == secret:
        success = True
if success:                               # after the loop: which way did we leave?
    print("Access granted. Attempts:", attempts)
else:
    print("Access blocked")
```

- The condition is checked before every round; the last check gives `False` and ends the loop.
- Ask again **inside** the loop, or the value never changes.
- The number of rounds is known before starting → `for`; the end depends on what happens → `while`.

---

# 5. Guided Practice (0–22)

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 1.3 – חזרה על פייתון א' · "עד שמסיימים" |
| 2–6 | **Hook (pairs, act it out):** a robot moves while its distance to the target is more than 0; it starts at 3 and each step takes 1 off. How many steps? What must change inside the loop? |
| 6–8 | Answer: 3 steps (3, 2, 1); `distance` must go down — `while distance > 0` |
| 8–12 | The three parts: start value, condition (checked before every round), update |
| 12–16 | **Predict:** output, and how many times the condition is checked |
| 16–18 | Answer: 5, 3, 1, `Done`; four checks — `value` ends at −1, and −1 > 0 is `False` |
| 18–22 | **for or while? (pairs):** print 10 rows · ask for a password until it is right · add 5 scores · read numbers until 0 → `for` · `while` · `for` · `while`; the lab missions |

The prediction (12–18):

```python
value = 5
while value > 0:
    print(value)
    value = value - 2
print("Done")
```

---

# 6. Lab (22–90)

Starter: [`Lock_Starter.py`](Lock_Starter.py). Reference: [`Lock_Reference.py`](Lock_Reference.py).

## 22–30 — Warm-up: the question that never comes back

```python
# Warm-up: run it and type -2. Why does it never stop? Stop it (red Stop button), then add one line.


def ask_age():
    age = int(input("Age: "))
    while age < 0:
        print("Invalid age")
    print("Accepted:", age)
```

With −2: `Invalid age` again and again, forever — `age` never changes, so `age < 0` stays `True`. Stop it (Tool Note). Fix: `age = int(input("Age: "))` as the last line of the loop body. Test −2, −1, 0 → two `Invalid age`, then `Accepted: 0` (0 is not below 0).

## 30–38 — Task 1: `valid_age()`

Accept only ages 0 to 120: `while age < 0 or age > 120:`. Tests: 130, −3, 14 → two `Invalid age`, then `Accepted: 14`. Links back to 1.1: there, an invalid score only got a message; now the program asks again.

## 38–52 — Task 2: `locker()` — three tries

Up to three tries to type 4321; then `Access granted. Attempts: N` or `Access blocked`. Students say the condition in words first: "tries left **and** not found yet". Tests:

<div dir="rtl">

| קלט | פלט |
|---|---|
| 4321 | Access granted. Attempts: 1 |
| 1111, 4321 | Access granted. Attempts: 2 |
| 1111, 2222, 4321 | Access granted. Attempts: 3 |
| 1111, 2222, 3333 | Access blocked — and no fourth `Code:` |

</div>

Ask: what are the two ways out of this loop? (success, or three tries used)

## 52–75 — Task 3: `points_goal()` — unit checkpoint (individual)

Three rounds; each round reads the points earned, adds them and prints the total so far; after the loop, 10 or more → `Goal reached`, otherwise `Keep going`. Students plan on paper (inputs → loop work → final decision), build alone, and run two required tests:

<div dir="rtl">

| קלט | סכום | פלט |
|---|---|---|
| 4, 4, 4 | 12 | Goal reached |
| 2, 3, 4 | 9 | Keep going |
| 5, 0, 5 | 10 | Goal reached |

</div>

The teacher walks around and asks each student to trace one round aloud. **Diagnostic, not graded:** note who needs help with the total, the loop choice or the `if` after the loop (see §8).

## 75–80 — If time: `guess_number()`

The secret is 7. Ask until the guess is right; after a wrong guess print `Too high` or `Too low`; at the end `Correct in N tries`. Test 3, 9, 7 → `Too low`, `Too high`, `Correct in 3 tries`. (An `if` inside a `while` — not a loop inside a loop.)

## 80–84 — Document and save

Save As `G8_U1_M3_Lock_<Name>.py`.

## 84–90 — Exit check

1. In the prediction, how many times was `value > 0` checked, and why one more than the rounds? (4 — the last check gives `False` and ends the loop)
2. `for` or `while`: ask for a code until it is right · print a table of 12 rows? (`while` · `for`)
3. `number = 7` and `while number > 0: print(number)` never ends. Add one line that makes it end. (`number = number - 1` inside the loop)

### Tool Note – Thonny
A loop that never ends keeps printing. Press the red **Stop** button (or Ctrl+F2) to stop the program, then fix the code.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The condition is checked in the middle of a round | Only before each round |
| The value in the condition changes by itself | Something in the body must change it |
| `while` is an `if` | `if` checks once; `while` checks again after every round |
| `and` in a `while` needs both parts `False` to stop | It stops as soon as one part is `False` |
| The goal check belongs inside the points loop | It runs once, after all rounds |
| A program with no error message is correct | It can still never end — test every way out |

---

# 8. Assessment Evidence (formative)

- The prediction with the number of checks (official assessment 1, 3)
- The warm-up explained: which variable never changed (CS 3, 4)
- `locker()` passing all four tests, including "no fourth try" (CS 8)
- **Unit 1 diagnostic checkpoint** — `points_goal()` built alone, tested, one round traced aloud; plus the exit check. Record per student: conditions (1.1), counted loops and totals (1.2), conditional loops (1.3). Evidence for planning, not a grade.
