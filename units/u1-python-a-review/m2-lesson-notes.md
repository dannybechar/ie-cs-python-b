# Unit 1.2 — Python A Review

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Counting Rounds — `for`, `range` and the Five-Scores Analyzer

**Status:** Built, awaiting teacher approval  
**Duration:** 90 minutes  
**Structure:** Lab + Lab (25 min guided practice, then 65 min lab)  
**Minutes (theory / practice):** 0 / 90  
**Current tool:** Thonny  
**Source of inspiration:** the codex deck `python_b_unit01_m02_for_loops_final.pptx` (`range(3)` prediction, the three forms of `range` with a negative step, the step-and-total prediction, counter vs total, the 80 / 70 / 100 trace table, the overwritten-total bug, the five-scores analyzer with three tests, the `10, 8, 6, 4` exit question kept; `+=` → `x = x + 1`; its 12-minute explanation blocks turned into predict-then-answer steps for a Lab + Lab meeting; the warm-up takes one of its two bugs) and the teacher's raw `G8_Unit1_M2` (countdown kept as Task 1; its `while` half moved to 1.3)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 1

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 1.1 | comparisons → `and` / `or` / `not` → `elif` → trace → input validation | 45 / 45 |
| **1.2 (this)** | **`for` + `range` (start, stop, step) → counter and total → trace → five-scores analyzer** | 0 / 90 |
| 1.3 | `while` → stop condition → ask until valid → three-try locker → unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf pp. 6–7) | Covered here |
|---|---|
| CS 1: identify problems that need repetition | ✅ hook, Task 3 |
| CS 5 / Py 1: write and implement a counted loop | ✅ Tasks 1–3 |
| Concepts: counted repetition with any step size, the loop variable's range | ✅ `range` forms, Task 1 |
| Teaching 3: `for item in range(n)` / `for item in range(start, stop, step)` | ✅ |
| Py 3: a function without parameters that contains a loop | ✅ every task |
| Assessment 1, 3: trace a loop; how many times a loop runs | ✅ trace table, exit check |

90 practice minutes of "counted repetition".

### Deliberate exclusions
`while` (1.3), nested loops (not in the new program), lists (Unit 7), `+=`.

---

## 3. Lesson Goal

**`range(start, stop, step)` decides the loop variable's values — stop is never included; a counter grows only when its condition is `True`, a total grows every round.**

---

## 4. Core Mental Models

```python
total = 0                          # set up BEFORE the loop
above = 0
for i in range(5):                 # 0, 1, 2, 3, 4 -> five rounds
    score = int(input("Score: "))
    total = total + score          # total: every round
    if score >= 80:
        above = above + 1          # counter: only when the condition is True
print("Average:", total / 5)       # report AFTER the loop
print("Scores >= 80:", above)
```

<div dir="rtl">

| תבנית | דוגמה | ערכים |
|---|---|---|
| `range(stop)` | `range(4)` | 0, 1, 2, 3 |
| `range(start, stop)` | `range(2, 6)` | 2, 3, 4, 5 |
| `range(start, stop, step)` | `range(10, 3, -2)` | 10, 8, 6, 4 |

</div>

---

# 5. Guided Practice (0–25)

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 1.2 – חזרה על פייתון א' · "סופרים סבבים" |
| 2–6 | **Predict (alone):** `for i in range(3): print(i)` — how many lines, which values? |
| 6–8 | Answer: 0, 1, 2 — three rounds; 3 is the stop, not a value |
| 8–14 | **Fill the table (pairs):** the values of `range(4)`, `range(2, 6)`, `range(10, 3, -2)` |
| 14–16 | Answers (table above). With a negative step, start must be bigger than stop |
| 16–20 | **Predict:** the values and the final total |
| 20–22 | Answer: 2, 4, 6, 8 and `20` |
| 22–25 | Counter vs total; both set up before the loop; the lab missions |

The prediction (16–22):

```python
total = 0
for n in range(2, 9, 2):
    print(n)
    total = total + n
print(total)
```

---

# 6. Lab (25–90)

Starter: [`Scores_Starter.py`](Scores_Starter.py). Reference: [`Scores_Reference.py`](Scores_Reference.py).

## 25–33 — Warm-up: the total that forgets

```python
# Warm-up: the total is wrong. Predict the output for 1, 2, 3, 4, 5, run it, then fix one line.


def sum_five():
    total = 0
    for day in range(1, 6):
        score = int(input("Score: "))
        total = score
    print("Total:", total)
```

Inputs 1, 2, 3, 4, 5 → `Total: 5`. `total = score` replaces the total every round. Fix: `total = total + score` → `Total: 15`. Ask: `range(1, 6)` — how many rounds? (five: 1–5)

## 33–43 — Task 1: `countdown()` and `evens()`

`countdown()`: 10, 9, … 1, then `Go!` — `range(10, 0, -1)` (stop 0 so that 1 is included). `evens()`: 2, 4, … 20 — `range(2, 21, 2)`. One `for` each; students write the `range` on paper before typing.

## 43–55 — Task 2: `trace_me()` — trace first, then run

```python
def trace_me():
    total = 0
    high = 0
    for i in range(3):
        score = int(input("Score: "))
        total = total + score
        if score >= 80:
            high = high + 1
    print("Total:", total, "High:", high)
```

Inputs 80, 70, 100. Students fill the table on paper, then run and compare:

<div dir="rtl">

| i | score | total | high |
|---|---|---|---|
| 0 | 80 | 80 | 1 |
| 1 | 70 | 150 | 1 |
| 2 | 100 | 250 | 2 |

</div>

Output `Total: 250 High: 2`. `i` counts rounds — it is not the score.

## 55–72 — Task 3: `five_scores()`

Read five scores; print the average and how many are 80 or more. One `for`, a total and a counter; divide after the loop. Tests:

<div dir="rtl">

| ציונים | Average | Scores >= 80 |
|---|---|---|
| 80, 70, 100, 60, 90 | 80.0 | 3 |
| 0, 0, 0, 0, 0 | 0.0 | 0 |
| 80, 80, 80, 80, 80 | 80.0 | 5 |
| 79, 81, 90, 50, 65 | 73.0 | 2 |

</div>

The average prints as `80.0` — `/` always gives a decimal number. The counter starts at 0, not 1. The 79 / 81 test checks the boundary.

## 72–80 — If time: `sevens()`

How many numbers from 1 to 100 divide by 7? `range(1, 101)`, `n % 7 == 0` → `Numbers that divide by 7: 14`.

## 80–84 — Document and save

Save As `G8_U1_M2_Scores_<Name>.py`.

## 84–90 — Exit check

1. Write a `range` that gives 10, 8, 6, 4. (`range(10, 3, -2)` — any stop from 3 down to 2 works)
2. How many rounds does `for i in range(2, 12, 3)` run? (4: 2, 5, 8, 11)
3. In `five_scores()`, which variable grows every round, and which only sometimes? (`total` every round; `above` only when the score is 80 or more)

### Tool Note – Thonny
Thonny's **Variables** view (View › Variables) shows `total` and the counter change after each input — use it to check the trace table.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `range(3)` includes 3 | Stop is a boundary, never a value |
| `total = score` adds to the total | It replaces it; `total = total + score` adds |
| Set the total inside the loop | It resets every round — set it up before the loop |
| Divide inside the loop | The average needs all five scores — divide after the loop |
| `i` is the score | `i` only counts rounds |
| A negative step works with start < stop | Then there are no values at all |

---

# 8. Assessment Evidence (formative)

- `range` values written before running (official assessment 3)
- The trace table matches the run (assessment 1)
- The warm-up bug explained, not only fixed
- `five_scores()` passing all four tests, including the 79 / 81 boundary (Py 1)
- Exit check
