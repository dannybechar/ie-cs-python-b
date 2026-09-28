# Unit 3 — Functions

**6h = 2 Theory + 4 Practice = 3 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 3 (pp. 10–11); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 built from the codex decks only — **staged in `python-b-built/`, not yet in `units/`.**
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit03_m01–m03_*.pptx`
(three decks, one per meeting — the same shape as Units 1–2's codex decks: slide text plus teacher speaker notes).

## Official topics and hours

Unit totals from the master table (2 theory / 4 practice). The chapter's own table (p. 11) splits differently —
"function without/with parameters, no return" 0 T + 2 P, "function with parameters and return" 1 T + 3 P, totaling
1 / 5 — used only for the order and weight of topics (hours rule, `CLAUDE.md`).
Minutes = hours × 45.

| Topic (Ministry, p. 11) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| פעולה בלי/עם פרמטר/ים שאינה מחזירה ערך — function with/without parameters, no return | 0 / 2 | 3.1 (45 T + 45 P), 3.2 (90 P) | 45 / 135 | 🔶 |
| פעולה עם פרמטרים ומחזירה ערך; טווח הכרה — function with parameters and return; scope | 1 / 3 | 3.3 (45 T + 45 P) | 45 / 45 | 🔶 |
| **Total (master table)** | **2 / 4** | | **90 / 180** | |

Chapter goals (p. 10), in the exact official order — this unit's meetings follow it directly:

1. Write and call a function with no parameters and no return value → **3.1** 🔶
2. Write and call a function with parameters and no return value → **3.2** 🔶
3. Write and call a function with parameters that returns a value → **3.3** 🔶
4. Distinguish a variable's scope inside a function from outside it → **3.3** 🔶

Also required: procedural abstraction and the black-box idea (goal SC 1–4: an algorithmic building block, using it
without its internal description, use vs. implementation, bottom-up development and "what" vs "how") → every
meeting, explicit in 3.1 (slides 5–6) and 3.3 (slide 15). Concepts: function, parameters, scope (local variable,
`global`) → 3.1–3.3. Python syntax: colon, indentation, `def` → 3.1. Assessment: tracing an algorithm that uses
procedural abstraction; developing and implementing one → 3.3 checkpoint.

## Unit 3.1 — Knowledge + Lab: A Function as a Building Block (no parameters, no return)
- why break a program into functions: repeated code, one place to fix, a main program that reads like an outline.
- `def name():`, the colon, the indented body, the call; defining does not run the body.
- execution order: Python reads every `def` first, then runs the main program top to bottom; a call before its `def`
  is a `NameError`.
- procedural abstraction: use the function by its name without reading its body ("what" vs "how").
- lab: call-before-def warm-up bug, `show_welcome()` called twice, a four-function control panel mini-project.

## Unit 3.2 — Knowledge + Lab: Same Function, Different Input (parameters)
- parameter (a name in the `def`) vs argument (the value sent at the call); positional matching, in order.
- when a function needs a parameter: only when something changes between calls.
- multiple parameters; calling with too few arguments is a `TypeError`.
- lab: wrong-variable-name warm-up bug, `show_mission(student, mission)`, designing `show_card(student, level, points)`,
  refactoring three near-identical `print` lines into one function.

## Unit 3.3 — Knowledge + Lab: Returning a Value + Scope (unit checkpoint)
- `print` shows a value to the user; `return` sends a value back to the line that called the function — only a
  returned value can be stored, compared or reused.
- a function with parameters and a return value; using the returned value directly inside an `if`.
- local variables belong to the function; after it returns, only the returned value exists outside it.
- bottom-up design: build and test small returning functions, then combine them.
- lab: missing-`return` warm-up bug (prints `None`), `is_even()`, `passed()` used inside `if`/`else`, the task-calculator
  checkpoint (`calculate_points`, `passed_checkpoint`, `show_result`).

### Scope decisions
- **Codex decks are the only source** (no raw teacher material for this unit). Kept their examples, trace tables, bug
  clinics and mini-projects closely — they map directly onto the four official goals in order. Changed: "מפגש" labels
  removed; every bug-hunt task trimmed from the source's 2–3 bugs to **one** bug per warm-up (house convention — Units
  1–2's warm-ups are always a single bug); the multi-bug versions (call-before-def + bad keyword + bad indentation in
  3.1; wrong variable + wrong argument order + missing argument in 3.2) are kept as extra practice in the lesson notes'
  misconception/enrichment material instead of the graded warm-up.
- The provisional outline in `docs/annual-strategy.md` (written before any Unit 3 source was reviewed) guessed 3.1
  would cover both parameter-free and parameterized functions together, with 3.2 introducing `return`. The real codex
  decks split more finely and match the official goal order exactly (goal 1 → 3.1, goal 2 → 3.2, goal 3–4 → 3.3) — that
  split is used here instead.
- **Not taught:** default or keyword arguments, `*args`, docstrings, type hints, recursion, lists (Unit 7 — no list
  parameters or list returns here), classes (not in this course).

## Exit criteria
The student defines and calls a function with any combination of parameters and a return value, traces the order
class code runs in (including a `NameError` from calling before defining), and explains the difference between
`print` and `return` and between a local variable and one outside the function.

## Checkpoint
3.3 Task 3 (the task calculator: `calculate_points`, `passed_checkpoint`, `show_result`) is the unit's checkpoint —
three small functions built and tested separately, then combined, with a boundary test at exactly 100 points.

## Enrichment
- 3.1: the full three-bug clinic from the source deck (keyword `function` instead of `def`, missing colon, wrong
  indentation, call before `def` — all in one broken file).
- 3.2: the signature-design challenge (`show_card`) and the refactor challenge, both already in the lab; for more,
  add a fourth near-duplicate `print` line to Task 3 and refactor it too.
- 3.3: predict which line raises `NameError` when a local variable is printed from outside its function (source
  slide 12) as an oral or written question.
