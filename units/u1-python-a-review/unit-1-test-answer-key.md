# Unit 1 Test — Teacher Answer Key and Rubric

Test: [`unit-1-test-he.md`](unit-1-test-he.md) · 60 minutes · 100 points · code: [`Test_Reference.py`](Test_Reference.py)
(every output below was produced by running that file).

**Scope:** only Unit 1 (conditions with `and`/`or`/`not`, `elif`, `for` + `range`, `while`, counters and totals, input
validation). No lists, functions with parameters, `+=`, nested loops or string methods.
**Timing:** A 14 min · B 8 min · C 33 min · 5 min review.
**Grade level:** Grade 9 (students who took Python A and the Unit 1 review). Nothing beyond Python A + Unit 1 is required.

## Part A (24)

**Q1 (8, 2 each):** Child · Teen member · Teen · Adult.

**Q2 (10):** `range(2, 12, 3)` = 2, 5, 8, 11.

| i | total | count |
|---:|---:|---:|
| 2 | 2 | 0 |
| 5 | 7 | 0 |
| 8 | 15 | 1 |
| 11 | 26 | 2 |

(a) 6 pts: 0.5 per cell (12 cells), with **follow-through**: a value that is wrong only because of an earlier mistake is not penalised again. (b) 2 pts: 4 rounds. (c) 2 pts: `Total: 26 Big: 2`.

**Q3 (6):** (a) 2 pts: 4 checks (x = 20, 14, 8, 2). (b) 4 pts: `2 3` (2 for each value).

## Part B (16)

**Q4a (6, 2 per fault):** the code is `for n in range(1, 5, 2):` with `print(n)` and `print("Done")` both inside the loop.
(1) the stop value 5 is excluded → `range(1, 6)`; (2) the step 2 skips numbers → remove it (`range(1, 6)`);
(3) `print("Done")` is indented inside the loop → move it out (no indent), so it prints once at the end.
Faults 1 and 2 can be fixed together by `range(1, 6)` (1 pt for each fault named, 1 pt for each fixed). The fixed program prints 1 2 3 4 5 Done.
**Q4b (4):** `or` lets every age pass (so 20 gets in; the `else` branch can never run); use `and` (`age >= 13 and age <= 15`). 2 for the diagnosis, 2 for the fix.

**Q5 (6):** (a) 2 pts: a `for` loop with `range(1, 10, 2)` and `print(i)` (stop 10 or 11 both fine; 1 pt if the loop and `range` are right but nothing is printed) ·
(b) 2 pts: `for i in range(20, 0, -5):` (any stop from 0 to 4 is fine) ·
(c) 1 pt each: 1 → `for` (known number of rounds); 2 → `while` (the number of rounds depends on the input).

## Part C (60)

General rule: code that is understandable with a minor syntax slip (colon, quote, indent) is penalised **once** per question, not per line.

**Q6 (18):** (a) 14 pts: input and `int` (2) · invalid age checked first, or equivalent logic (3) · categories with `elif` or an equivalent that is mutually exclusive, e.g. nested `if` (5) · exactly one correct message per input: `Invalid`, `Free`, `Student`, `Regular` (4).
(b) 4 pts: four numeric values for **each** of the four ranges — 1 pt per range, given only if all four values really belong to that range (`Invalid`: below 0 or above 120; `Free`: 0–5; `Student`: 6–17; `Regular`: 18–120). Example: Free 0, 2, 4, 5 · Student 6, 10, 15, 17 · Regular 18, 40, 100, 120 · Invalid −1, −50, 121, 500.
Common errors: `age < 0 and age > 120` (never True); testing `age < 6` before validation (−1 gives `Free`);
`if` instead of `elif` (two messages); `Invalid` as a range given only below 0 or only above 120 in (b).
Wording note: the test says "18 ומעלה" for `Regular`, so 18 is `Regular` (and 17 is `Student`).

**Q7 (18):** total and counter set to 0 **before** the loop (4) · `for` with 6 rounds (3) · `int(input())` inside the loop (2) ·
`total = total + grade` (3) · counter grows only when `grade >= 90` (3) · average computed **after** the loop, divided by 6 (3).
Common errors: `total = grade` (the 1.2 warm-up bug), dividing inside the loop, resetting inside the loop, `range(1, 6)` (5 rounds).

**Q8 (24):** `total` and `deposits` start at 0 (4) · `while total < 100 and deposits < 5` (8: 2 for each of the two comparisons, 4 for joining them with `and`; `or` loses the 4) ·
input and both updates inside the loop (6) · final `if`/`else` decides by the total (4) · both messages correct (2).
The flag style (`success = False`) from 1.3 is accepted if it is consistent.
The test no longer requires `while` explicitly; a program that stops after 5 deposits or at 100 any other way the students have learned (e.g. a flag) is accepted if it is consistent.
Check: 60, 50 → `Goal reached after 2 deposits`; 10 ×5 → `Goal not reached. Total: 50`; 30, 40, 30 → `Goal reached after 3 deposits`.
Common errors: `or` instead of `and` (runs too long), no update to `deposits` (never ends when the goal is not reached),
`while total <= 100`.

## Model solutions

[`Test_Reference.py`](Test_Reference.py): `q1`–`q3`, `q4_fixed`, `q4b_fixed`, `q5a`, `q5b` (Parts A–B), `ticket()`, `grades()`, `savings()` (Q6–Q8).

## Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of Unit 1 |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `while` and accumulators |
| below 56 | Needs support before Unit 3 (functions) |
