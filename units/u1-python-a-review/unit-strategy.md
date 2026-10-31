# Unit 1 — Python A Review

**6h = 1 Theory + 5 Practice = 3 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 1 (pp. 5–8); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 1.1 and 1.2 built and approved; **1.3 reworked on 31 Oct 2026 around the Ministry teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)) — built, awaiting approval.**
Inspired by two sets of raw material: the codex decks (`Downloads\python-b-codex\python_b_unit01_m01–m03_*.pptx`,
the main source) and the teacher's raw meetings (`Downloads\python-b-raw-meterials\ie-cs-python-b\U1_M1–M3`).

## Official topics and hours

Unit totals from the master table (1 theory / 5 practice). The chapter's own table (pp. 7–8) splits the unit as
conditions 2 h, counted loops 1 h … and totals 2 / 4 — used only for the order and weight of topics (hours rule, `CLAUDE.md`).
Minutes = hours × 45.
Status: ✅ built and approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry, p. 7) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| תנאים לוגיים וביצוע מותנה — logical conditions and conditional execution | 0 / 2 | 1.1 (45 T + 45 P) | 45 / 45 | ✅ |
| ביצוע חוזר באורך ידוע מראש — counted repetition | 1 / 1 | 1.2 (90 P) | 0 / 90 | ✅ |
| ביצוע חוזר מותנה — conditional repetition | 1 / 1 | 1.3 (90 P) | 0 / 90 | 🔶 |
| **Total (master table)** | **1 / 5** | | **45 / 225** | |

Also required by the chapter's goals (pp. 5–7):

- Compound conditions with `and`, `or`, `not` (goals CS 1–2, Py 1) → 1.1 ✅, 1.3 (`not success`, `or` in the 3-digit loop) 🔶
- `elif` — "ביצוע מותנה מתגלגל" (CS 6, concepts p. 5) → 1.1 ✅ — **new**: Python A left `elif` as an optional extension
- Nested conditions (CS 6, Py 5) → 1.1 Task 1 ✅
- Input validation with a condition (CS 7) → 1.1 Task 3 ✅; asking again with `while` → 1.3 warm-up and Task 1 🔶
- `range(n)` and `range(start, stop, step)` (teaching 3) → 1.2 ✅
- A loop that never ends; correctness = the goal holds and the loop ends (teaching 4–5) → 1.3 warm-up, Task 4 and the Safe Loop Checklist 🔶
- A loop whose stop depends on a variable (CS 8) → 1.3 Tasks 2, 6, 8 🔶
- A function without parameters that contains a loop (Py 3) → every lab task is such a function ✅
- Trace tables, counting rounds, choosing the loop type (assessment 1–6) → 1.2 ✅, 1.3 🔶

## Unit 1.1 — Knowledge + Lab: Who can come in? (compound conditions, `elif`, validation)
- comparisons give `True` / `False`; `=` vs `==`; `input()` gives text.
- `and`, `or`, `not`; a range written as `age >= 13 and age <= 15`.
- `elif`: the first `True` branch runs, the rest are skipped.
- trace table for an `if` / `elif` / `else` chain; checking input before using it.
- lab: `int()` warm-up bug, a gate with two bugs, the entry check, a validated score level.

## Unit 1.2 — Lab + Lab: Counting rounds (`for` and `range`)
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`; stop is never included; a negative step.
- counter vs total; set up before the loop, report after it.
- lab: overwritten-total warm-up bug, countdown and evens, a trace table, the five-scores analyzer.

## Unit 1.3 — Lab + Lab: Until it's done (`while`) + unit checkpoint 🔶 (reworked from the Ministry materials)
- the loop variable (sentinel): start value before the loop, condition, update inside the loop; 10 rounds = 11 checks; trace tables.
- asking again until the input is valid (3-digit number); counting inside a conditional loop (3 even numbers); counting forward (score) and backward (timer).
- finite and infinite loops: the Safe Loop Checklist (start value, condition can become `False`, update inside, right direction), the three traps (frozen clock, wrong direction, always-true condition), stopping a runaway program in Thonny.
- `for i in range(0, 5, 1)` = `while`; three snippets with the same output; `+=` allowed.
- a loop with a compound condition (the three-try locker); the exam task "exciting number" done as a shared trace-then-run; a series with a stop condition on the sum (the unit checkpoint).
- lab: never-ending validation warm-up bug, `three_digit()`, `three_evens()`, `score_and_timer()`, `loop_a`-`loop_d`, `for_to_while()`, `locker()`, `exciting_number()`, `cubes_sum()` (checkpoint); if time `count_red()` and `twos()`.
- sources: Ministry 2.0 (deck), 2.1 (worksheet), "מלכודת הלולאה האינסופית" (deck); see the lesson notes.

### Scope decisions
- **Codex decks were the main source** — their examples, trace tables, bug hunts and core tasks follow the official chapter
  closely. Changed: "מפגש" labels removed; `+=` / `-=` → `x = x + 1` (Python A style; `+=` needs the teacher's approval);
  the chained comparison `13 <= age <= 15` → `age >= 13 and age <= 15` (Python A never taught chaining); the bug slide's
  `"כן"` / `"yes"` mismatch fixed; 1.2 and 1.3 recast from Knowledge + Lab to **Lab + Lab** (the master table gives the
  unit one theory hour, used in 1.1).
- **Raw meetings:** kept the ticket-price program (1.1 warm-up), the countdown (1.2 Task 1) and the points-goal diagnostic
  (1.3 checkpoint). Dropped the English-only scaffolding slides and the 1.2 "for + while" mix (while is 1.3's topic).
- **1.3 (31 Oct 2026):** reworked to follow the Ministry teaching materials (2.0, 2.1, loop-trap deck); `+=` and `-=` are now allowed (Ministry rule); the old robot hook, `value = 5` prediction, "for or while?" quiz and `points_goal()` checkpoint were replaced; worksheet 2.1 questions 3 (logic-bug snippets) and 4 (prime numbers, a nested loop) are not used.
- **Not taught:** nested loops (dropped from the new program — clarifications p. 3), `break`, `while True`, lists,
  string methods (Unit 5), functions with parameters or `return` (Unit 3).
- `not` was used in Python A only in its last unit (event handlers) — it is reviewed here as part of the official
  "שלילה".

## Exit criteria
The student writes compound conditions and an `if` / `elif` / `else` chain, validates input, chooses `for` or `while`
for a problem, traces a loop (including the last `False` check) and explains why it stops.

## Checkpoint
1.3 Task 8 (`cubes_sum()`) plus the 1.3 exit check are the unit's **diagnostic** checkpoint — evidence of what each
student brings from Python A, not a grade.

## Enrichment
- `club_open()` (1.1), `sevens()` (1.2), `guess_number()` (secret 7, `Too high` / `Too low`, `Correct in N tries`) and `count_red()` / `twos()` (1.3) — harder problems with no new syntax.
