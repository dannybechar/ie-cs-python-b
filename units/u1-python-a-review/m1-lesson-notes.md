# Unit 1.1 — Python A Review

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Who Can Come In? — Compound Conditions, `elif` and Input Validation

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the codex deck `python_b_unit01_m01_conditions_final.pptx` (entry hook, `True`/`False` comparisons, access-granted prediction, `and`/`or`/`not`, score trace table A–C, gate bug hunt, entry check with four tests, exit condition kept; `13 <= age <= 15` → `age >= 13 and age <= 15`, the `"כן"`/`"yes"` mismatch fixed, the bug hunt made runnable — `or` instead of a syntax error, "מפגש" labels removed) and the teacher's raw `G8_Unit1_M1` (ticket-price program kept as the warm-up bug; its English scaffolding slides dropped)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 1

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **1.1 (this)** | **comparisons → `and` / `or` / `not` → `elif` → trace → input validation** | 45 / 45 |
| 1.2 | `for` + `range` (start, stop, step) → counter and total → trace → five-scores analyzer | 0 / 90 |
| 1.3 | `while` → stop condition → ask until valid → three-try locker → unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf pp. 5–6) | Covered here |
|---|---|
| CS 1–2: compound conditions and the three Boolean operations (and, or, not) | ✅ hook, `and`/`or`/`not` slide, Tasks 1–3 |
| CS 3: what conditional execution is and the role of its condition | ✅ predict, trace table |
| CS 4–5: conditional execution with and without an alternative | ✅ `if` / `else`, Task 1 (`if` only) |
| CS 6: nesting and "ביצוע מותנה מתגלגל" (`elif`) | ✅ Task 1 (nested `if`), Tasks 2–3 (`elif`) |
| CS 7: input validation with a condition | ✅ Task 3 |
| Py 1, 3–5: write compound conditions; implement with / without alternative; nested | ✅ Tasks 1–3 |
| Concepts: Boolean type, simple and compound conditions, validation; Boolean operators, `elif` | ✅ |
| Assessment 1, 4: trace algorithms with compound conditions and conditional execution | ✅ trace table, exit check |

The unit's one theory hour (master table) is used here; 45 practice minutes of "conditions and conditional execution".

### Deliberate exclusions
Chained comparisons (`13 <= age <= 15` — not taught in Python A), asking again after invalid input (needs `while`, 1.3),
loops (1.2), `+=`.

---

## 3. Lesson Goal

**A compound condition joins comparisons with `and` / `or` / `not`; an `if` / `elif` / `else` chain runs exactly one branch — the first whose condition is `True`.**

---

## 4. Core Mental Models

```python
age = int(input("Age: "))                   # input() gives text -> int() makes a number
permission = input("Permission (yes/no): ")
if age >= 13 and age <= 15 and permission == "yes":   # and: every part must be True
    print("Access granted")
elif age < 13 or age > 15:                  # or: one True part is enough
    print("Age out of range")
else:                                       # none of the above
    print("Permission required")
```

- A comparison gives `True` or `False`; `=` stores a value, `==` compares.
- `and` needs every part `True`; `or` needs at least one; `not` flips `True` ↔ `False`.
- A range needs the variable twice: `age >= 13 and age <= 15` — never `age >= 13 and <= 15`.
- `elif` is checked only when everything above it was `False`; the chain stops at the first `True`.
- **Validate first:** check the invalid case (`score < 0 or score > 100`) before the levels.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 1.1 – חזרה על פייתון א' · "מי יכול להיכנס?" |
| 2–6 | **Hook (on paper, alone then in pairs):** the games club is for ages 13–15 with a permission note. Roni: 14, has a note · Maya: 12, has a note · Amir: 15, no note. Who gets in? |
| 6–8 | Answer: only Roni. Two conditions must hold together → "וגם" |
| 8–14 | Comparisons give `True` / `False`: `age = 14` → `age >= 13`, `age == 15`, `age != 12` (thumbs up / down); `=` vs `==`; `input()` gives text → `int()` |
| 14–18 | **Predict:** `age = 14`, `has_card = True`, `if age >= 13 and has_card:` → `Access granted` / `Access denied`? Write the value of each part first |
| 18–20 | Answer: `True and True` → `True` → `Access granted` |
| 20–26 | `and` / `or` / `not`; a range with the variable twice; `not is_blocked` |
| 26–30 | **Choose the operator (pairs):** "umbrella if it rains or snows", "enter if old enough and has a ticket", "open if it is not a holiday" |
| 30–35 | **New — `elif`:** the chain is checked top-down and stops at the first `True`; score levels 90 / 70 |
| 35–40 | **Trace table (in threes, one case each):** the `score` / `submitted` chain, cases A–C |
| 40–43 | Answers: A `Next stage` · B `Submission missing` · C `Needs improvement` |
| 43–45 | Validate first — the invalid case goes at the top · the lab missions |

The trace-table code (35–43):

```python
if score >= 80 and submitted:
    print("Next stage")
elif score >= 80:
    print("Submission missing")
else:
    print("Needs improvement")
```

<div dir="rtl">

| מקרה | score | submitted | פלט |
|---|---|---|---|
| A | 85 | True | Next stage |
| B | 92 | False | Submission missing |
| C | 74 | True | Needs improvement |

</div>

B: the `if` is `False` (one part is `False`), so the `elif` is checked — and it is `True`. C: both conditions are `False` → `else`.

---

# 6. Second 45 Minutes — Lab

Starter: [`Entry_Starter.py`](Entry_Starter.py). Reference: [`Entry_Reference.py`](Entry_Reference.py).

## 45–52 — Warm-up: the price that crashes

```python
# Warm-up: this program crashes. Run it with age 10 and 2 tickets, read the error, then fix one line.
# Children under 12 pay 8 per ticket; everyone else pays 12.


def ticket_price():
    age = input("Age: ")
    tickets = int(input("Tickets: "))
    if age < 12:
        price = 8
    else:
        price = 12
    print("Total:", tickets * price)
```

Run with 10 and 2:

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

`input()` gave the text `"10"`; text can't be compared with a number. Fix: `age = int(input("Age: "))` → `Total: 16`. Then 12 and 3 → `Total: 36` (12 is not under 12).

## 52–61 — Task 1: `fix_the_gate()` — two bugs

```python
def fix_the_gate():
    age = int(input("Age: "))
    permission = input("Permission (yes/no): ")
    if age >= 13 or age <= 15:
        if permission == yes:
            print("Access granted")
```

Run with 20 and `yes`:

```text
NameError: name 'yes' is not defined
```

Bug 1: text needs quotes → `"yes"`. Run again with 20 and `yes` → `Access granted` — a 20-year-old got in! Bug 2: with `or`, every age passes → `and`. After both fixes, 20 → nothing printed; 14 and `yes` → `Access granted`. This is a nested `if` (official CS 6).

## 61–72 — Task 2: `entry_check()`

Exactly one message: `Access granted` (13–15 with permission) · `Age out of range` · `Permission required`. Plan the three cases on paper first. Tests:

<div dir="rtl">

| גיל | אישור | פלט |
|---|---|---|
| 14 | yes | Access granted |
| 14 | no | Permission required |
| 12 | yes | Age out of range |
| 16 | yes | Age out of range |
| 13 | yes | Access granted |
| 15 | yes | Access granted |

</div>

Ask: why can't a single `else` do the job of the `elif`? (It would mix "wrong age" with "no permission".)

## 72–81 — Task 3: `score_level()` — validate, then decide

Read a score. Outside 0–100 → `Invalid score`; 90+ → `Excellent`; 70+ → `Good`; otherwise `Keep practicing`. Tests: −5 and 101 → `Invalid score`; 100, 90 → `Excellent`; 89, 70 → `Good`; 69, 0 → `Keep practicing`.
Ask: what goes wrong if the `Invalid score` check comes last? (101 would print `Excellent`.)

## 81–84 — If time, then save

`club_open()`: open on days 1–5 when it is **not** a holiday — `day >= 1 and day <= 5 and not is_holiday`, where `is_holiday = input("Holiday (yes/no): ") == "yes"`. Tests: 3 / no → open · 3 / yes → closed · 6 / no → closed.
Save As `G8_U1_M1_Entry_<Name>.py`.

## 84–90 — Exit check

1. Write one condition that is `True` only when `number` is between 10 and 20 and is not 15. (`number >= 10 and number <= 20 and number != 15`)
2. In `score_level()`, the score is 95. Why does it print `Excellent` and not also `Good`? (the chain stops at the first `True` branch)
3. What type does `input()` return, and how do we get a number? (text; `int(...)`)

### Tool Note – Thonny
Thonny shows the error in the Shell, with the line number of the line that failed. Click the line link to jump to it.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `=` and `==` are the same | `=` stores, `==` compares |
| `input()` already gives a number | It gives text; `int()` converts |
| `age >= 13 and <= 15` works | Each side of `and` is a full comparison: `age >= 13 and age <= 15` |
| `or` means both | One `True` part is enough — so `age >= 13 or age <= 15` is always `True` |
| All `True` branches of an `elif` chain run | Only the first `True` branch runs |
| Validation can come anywhere | The invalid check goes first, or a later branch catches the bad value |

---

# 8. Assessment Evidence (formative)

- Hook and prediction answers written before the reveal (official assessment 1)
- The trace table A–C with a reason for each branch (assessment 4)
- Both gate bugs found and explained (Task 1)
- `entry_check()` passing all six tests, including the boundaries 13 and 15 (Py 5)
- `score_level()` with validation at the top (CS 7)
- Exit check
