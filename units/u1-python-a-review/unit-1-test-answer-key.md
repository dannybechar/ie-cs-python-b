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

(a) 6 pts: 1.5 per row. (b) 2 pts: 4 rounds. (c) 2 pts: `Total: 26 Big: 2`.

**Q3 (6):** (a) 2 pts: 4 checks (x = 20, 14, 8, 2). (b) 4 pts: `2 3` (2 for each value).

## Part B (16)

**Q4a (6):** `n` never changes → add `n = n + 1` inside the loop (3); `n < 5` stops before 5 → `n <= 5` (3).
The fixed program prints 1 2 3 4 5 Done.
**Q4b (4):** `or` lets every age pass; use `and` (`age >= 13 and age <= 15`). 2 for the diagnosis, 2 for the fix.

**Q5 (6, 1 each for the loop / the reason):** (a) `range(1, 10)` · (b) `range(20, 0, -5)` (any stop from 0 to 4 is fine) ·
(c) 1 → `for` (known number of rounds); 2 → `while` (the number of rounds depends on the input).

## Part C (60)

**Q6 (18):** input and `int` (2) · invalid age checked first, or equivalent logic (4) · `elif` chain with exactly one
message (6) · correct boundaries (2) · test values (4: should include −1 or 121, 0 or 5, 6, 17, 18).
Common errors: `age < 0 and age > 120` (never True); testing `age < 6` before validation (−1 gives `Free`);
`if` instead of `elif` (two messages).

**Q7 (18):** total and counter set to 0 **before** the loop (4) · `for` with 6 rounds (3) · `int(input())` inside the loop (2) ·
`total = total + grade` (3) · counter grows only when `grade >= 90` (3) · average computed **after** the loop, divided by 6 (3).
Common errors: `total = grade` (the 1.2 warm-up bug), dividing inside the loop, resetting inside the loop, `range(1, 6)` (5 rounds).

**Q8 (24):** `total` and `deposits` start at 0 (4) · `while total < 100 and deposits < 5` (8; 4 if only one side is right) ·
input and both updates inside the loop (6) · final `if`/`else` decides by the total (4) · both messages correct (2).
The flag style (`success = False`) from 1.3 is accepted if it is consistent.
Check: 60, 50 → `Goal reached after 2 deposits`; 10 ×5 → `Goal not reached. Total: 50`; 30, 40, 30 → `Goal reached after 3 deposits`.
Common errors: `or` instead of `and` (runs too long), no update to `deposits` (never ends when the goal is not reached),
`while total <= 100`.

## Model solutions

[`Test_Reference.py`](Test_Reference.py): `q1`–`q3` and `q4_fixed` (Parts A–B), `ticket()`, `grades()`, `savings()` (Q6–Q8).

## Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of Unit 1 |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `while` and accumulators |
| below 56 | Needs support before Unit 3 (functions) |
