# Lessons 4.1–4.6 — Functions

**6h = 2 Theory + 4 Practice = 3 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 3 (pp. 10–11); hours from the master table (p. 3).
Content: the Ministry's teaching materials ([`../../docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)) — files 4.1–4.6.
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked from the Ministry's teaching materials — all 3 meetings built, awaiting approval by the teacher.
The first version (codex decks, no `global`, no exam questions) is replaced; its three slide decks are kept in the folder
but are superseded until new NotebookLM decks are made.

## Official topics and hours

Unit totals from the master table (2 theory / 4 practice). The chapter's own table (p. 11) splits differently —
"function without/with parameters, no return" 0 T + 2 P, "function with parameters and return" 1 T + 3 P, totaling
1 / 5 — used only for the order and weight of topics (hours rule, `CLAUDE.md`).
Minutes = hours × 45.

| Topic (Ministry, p. 11) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| פעולה בלי/עם פרמטר/ים שאינה מחזירה ערך — function with/without parameters, no return | 0 / 2 | 4.1–4.2 (7-minute recap, `print_total`), practice inside 4.1–4.5 | (see below) | 🔶 |
| פעולה עם פרמטרים ומחזירה ערך — function with parameters and return | 1 / 3 | 4.1–4.2 (theory + lab), 4.4–4.5 (90 P) | (see below) | 🔶 |
| טווח הכרה — scope: local variable, `global` | | 4.3, 4.6 (45 T + 45 P) | 45 / 45 | 🔶 |
| **Total (master table)** | **2 / 4** | | **90 / 180** | |

Planned by meeting: **4.1–4.2** 45 T + 45 P · **4.4–4.5** 0 T + 90 P · **4.3, 4.6** 45 T + 45 P = 90 theory + 180 practice minutes.

Chapter goals (p. 10), in the official order:

1. Write and call a function with no parameters and no return value → **4.1–4.2** recap (7 min); the Ministry assumes this from Grade 7
2. Write and call a function with parameters and no return value → **4.1–4.2** (`print_total`, `calculate_box`)
3. Write and call a function with parameters that returns a value → **4.1–4.2**, **4.4–4.5**
4. Distinguish a variable's scope inside a function from outside it → **4.3, 4.6**

Also required: procedural abstraction and the black-box idea (SC 1–4) → every meeting. Concepts: function, parameters,
scope (local variable, `global`) → 4.1–4.6. Python syntax: colon, indentation, `def` → 4.1–4.2 recap. Assessment: tracing an
algorithm that uses procedural abstraction; developing and implementing one → 4.4–4.5 exam questions, 4.3, 4.6 checkpoint.

## Meeting outline (Ministry files in brackets)

### Lessons 4.1–4.2 — Knowledge + Lab: Several Parameters and `return` (4.1, 4.2)
- 7-minute recap: a zero-parameter and a one-parameter function (Grade 7; covers students who never saw a no-parameter function).
- several parameters; their order; `TypeError` for a wrong argument count; `print_total`.
- `print` vs `return`; `return` ends the function; `None` when `return` is missing; using the returned value in `if` / an expression;
  the four-kinds table.
- lab: worksheet 4.2 exercises 1–6; warm-up bug: missing `return` (prints `None`).

### Lessons 4.4–4.5 — Lab + Lab: Returning Functions and Loops Inside Functions (4.2, 4.1, 4.4, 4.5)
- `three_averages`, `calculate_shipping`, `find_max`, `final_grade`; early `return`.
- exam questions with `while` inside functions: digit extraction with `% 10` and `// 10`, the `secret1`–`secret4` tracing, "special" number, "perfect" number, `calculate_gift`.
- warm-up bug: arguments in the wrong order (no error, wrong answer).

### Lessons 4.3, 4.6 — Knowledge + Lab: Local and Global Variables (4.3, 4.5, 4.6)
- life cycle of a local variable, `NameError` outside, each function has its own world.
- a global variable: reading, `score = 100` creates a local, `global`, the `UnboundLocalError` trap (Python 3.14 wording).
- lab: local-vs-global identification and tracing (4.5), `add_bonus`, parking lots, `how_many_legs` (4.6), unit checkpoint: donation campaign with two global variables (4.6 question 4, adapted).
- warm-up bug: forgotten `global`.

### Scope decisions
- **The Ministry's materials are the source of truth** (teacher's decision, 31 Oct 2026). Their examples, exercise names and
  solutions are used as written, except where they use something the course has not taught; those adaptations are listed in the
  "Source of inspiration" line of each meeting's notes.
- **`global` is taught** (previous version of this file said it is only named). **`+=`** is allowed (the Ministry uses it in 4.5 and 4.6).
- **Not used from the Ministry's files:** returning several values and unpacking (`a, b, c, d = calculator(...)`; 4.6 questions 3 and 4) — a tuple, not taught; f-strings (4.6 question 1; the API block (lessons 5.0–6.2)); `%d` formatting and `int(number / 10)` in 4.4 (replaced by a comma in `print` and `//`).
  4.6 question 3 appears only as an "if time" idea in four single-value functions; question 4 is the checkpoint, with global variables instead of a pair of returned values.
- The previous version's task-calculator checkpoint, the control-panel mini-project and the refactor tasks are dropped.
- **Teacher decision before the May 2027 exam:** the two official items above (multiple return values, 4.6 q3/q4 and key 4.5.0) and the **4.7 H5P "default argument in a function"** (https://h5p.org/node/1498619, only the link was delivered) are left out by the rulebook default; replacement for 4.6 q4 is two global variables. Details in `m3-lesson-notes.md` section 2. The 4.4 exam questions have no official key.
- **Not taught:** default or keyword arguments in our own functions, `*args`, docstrings, type hints, recursion, `nonlocal`, nested functions, lists (lessons 9.1–9.5 and 12.0–14.5), classes.

## Exit criteria
The student writes and calls a function with several parameters, in the right order, and with a `return`; explains the
difference between `print` and `return` and what `None` means; writes a function that uses `if` or a `while` loop and returns
one result; explains why a variable made inside a function disappears after the call; changes a global variable from
inside a function with `global` and reads the `UnboundLocalError` when `global` is missing.

## Checkpoint
4.3, 4.6 donation campaign: `add_donation` changes two global variables (a sum and a counter) from inside a function; the main
program reads the input and prints the results; boundary test at exactly 100.

## Enrichment
- 4.1–4.2: `average_grade` with the returned value in an `if` (in the lab as "if time").
- 4.4–4.5: `calculate_gift` for ten customers; `find_location()` (positions of a digit in an ID).
- 4.3, 4.6: `add_coins`, `weight_of_number`, a four-function calculator.
