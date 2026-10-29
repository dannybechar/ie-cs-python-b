# Unit 1 Test, Form B (retest) — Teacher Answer Key and Rubric

Test: [`unit-1-test-form-b-he.md`](unit-1-test-form-b-he.md) · 60 minutes · 100 points · code: [`Test_B_Reference.py`](Test_B_Reference.py)
(every output below was produced by running that file).

**Form B mirrors Form A question by question** (same structure, points, skills and boundary cases; new contexts and numbers),
so the rubric and grading scale of [Form A](unit-1-test-answer-key.md) apply unchanged. Two Form A defects were fixed:
Q5b is now shown as a code line (`30, 25, 20, 15, 10`) with "in this order, from large to small", and Q6b is a
fill-in table with four value cells for each message.

| Q | Form A | Form B |
|---|---|---|
| 1 | age / member, 4 messages, boundary 18 | temp / rain, 4 messages, boundary 25 |
| 2 | `range(2, 12, 3)`, 4 rounds, `i > 6` | `range(1, 14, 4)`, 4 rounds, `i > 8` |
| 3 | `x = 20`, `x > 3`, step 6 → `2 3` | `x = 25`, `x > 4`, step 7 → `4 3` |
| 4a | 1 to 5, three faults | 1 to 8, three faults |
| 4b | `or` instead of `and`, range 13–15 | `or` instead of `and`, range 120–190 |
| 5 | odd 1–9 · 20 down to 5 · for/while | multiples of 4, 4–20 · 30 down to 10 · for/while |
| 6 | ticket by age, 0–120 | test score, 0–100 |
| 7 | 6 grades, average + count ≥ 90 | 5 runs, average + count ≥ 10 |
| 8 | 100 shekels / 5 deposits | 200 pages / 6 days |

## Part A (24)

**Q1 (8, 2 each):** Cold · Umbrella · Nice · Hot.

**Q2 (10):** `range(1, 14, 4)` = 1, 5, 9, 13.

| i | total | count |
|---:|---:|---:|
| 1 | 1 | 0 |
| 5 | 6 | 0 |
| 9 | 15 | 1 |
| 13 | 28 | 2 |

(a) 6 pts: 0.5 per cell (12 cells), with **follow-through**. (b) 2 pts: 4 rounds. (c) 2 pts: `Total: 28 Count: 2`.

**Q3 (6):** (a) 2 pts: 4 checks (x = 25, 18, 11, 4). (b) 4 pts: `4 3` (2 for each value).

## Part B (16)

**Q4a (6, 2 per fault):** the code is `for n in range(1, 8, 2):` with `print(n)` and `print("Done")` both inside the loop.
(1) the stop value 8 is excluded → `range(1, 9)`; (2) the step 2 skips numbers → remove it; (3) `print("Done")` is indented
inside the loop → move it out. Faults 1 and 2 can be fixed together by `range(1, 9)` (1 pt for each fault named, 1 pt for each fixed).
The fixed program prints 1 2 3 4 5 6 7 8 Done.
**Q4b (4):** `or` lets every height pass (so 100 gets in; the `else` branch can never run); use `and`
(`height >= 120 and height <= 190`). 2 for the diagnosis, 2 for the fix.

**Q5 (6):** (a) 2 pts: `for` with `range(4, 21, 4)` and `print(i)` (stop 21 to 24 fine; 1 pt if the loop and `range` are right but nothing is printed) ·
(b) 2 pts: `for i in range(30, 9, -5):` (any stop from 5 to 9 is fine; stop 10 loses the 10, stop 4 or lower adds 5) ·
(c) 1 pt each: 1 → `for` (known number of rounds); 2 → `while` (the number of rounds depends on the input).

## Part C (60)

General rule: code that is understandable with a minor syntax slip (colon, quote, indent) is penalised **once** per question, not per line.

**Q6 (18):** (a) 14 pts: input and `int` (2) · invalid score checked first, or equivalent logic (3) · categories with `elif` or an equivalent that is mutually exclusive (5) · exactly one correct message per input: `Invalid`, `Fail`, `Pass`, `Excellent` (4).
(b) 4 pts: 1 pt per row, given only if all four values really belong to that message and are different from each other
(`Excellent`: 85–100; `Pass`: 55–84; `Invalid`: below 0 or above 100; `Fail`: 0–54).
Example: Excellent 85, 90, 99, 100 · Pass 55, 60, 70, 84 · Invalid −1, −20, 101, 250 · Fail 0, 10, 30, 54.
Common errors: `score < 0 and score > 100` (never True); testing `score < 55` before validation (−1 gives `Fail`);
`if` instead of `elif` (two messages).
Wording note: "85 ומעלה" → 85 is `Excellent` (and 84 is `Pass`).

**Q7 (18):** total and counter set to 0 **before** the loop (4) · `for` with 5 rounds (3) · `int(input())` inside the loop (2) ·
`total = total + km` (3) · counter grows only when `km >= 10` (3) · average computed **after** the loop, divided by 5 (3).
Common errors: `total = km`, dividing inside the loop, resetting inside the loop, `range(1, 5)` (4 rounds), dividing by 6.
Output check: 5, 12, 10, 8, 15 → `Average: 10.0` / `Runs >= 10: 3`; 1, 2, 3, 4, 5 → `Average: 3.0` / `Runs >= 10: 0`.

**Q8 (24):** `total` and `days` start at 0 (4) · `while total < 200 and days < 6` (8: 2 for each of the two comparisons, 4 for joining them with `and`; `or` loses the 4) ·
input and both updates inside the loop (6) · final `if`/`else` decides by the total (4) · both messages correct (2).
A flag, `while True`/`break` or any other consistent way of stopping is accepted.
Check: 120, 90 → `Finished after 2 days`; 20 ×6 → `Not finished. Pages: 120`; 80, 70, 60 → `Finished after 3 days`;
30, 30, 30, 30, 30, 50 → `Finished after 6 days` (the goal is reached on the last allowed day).
Common errors: `or` instead of `and`, no update to `days`, `while total <= 200`.

## Model solutions

[`Test_B_Reference.py`](Test_B_Reference.py): `q1`–`q3`, `q4_fixed`, `q4b_fixed`, `q5a`, `q5b`, `score_message()`, `runs()`, `reading()`.
