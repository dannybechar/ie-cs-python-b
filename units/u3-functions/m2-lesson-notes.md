# Unit 3.2 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Same Function, Different Input — Parameters

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** Lab + Lab (24 min guided practice, then 66 min lab)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** the codex deck `python_b_unit03_m02_parameters_and_reuse_delivery.pptx` (the "what's
missing to greet someone else" recap, the parameter/argument definitions, the two-call trace table, the
missing-argument prediction ending in `TypeError`, the `show_mission` writing task, the multi-parameter `draw_bar`
example, the parameter bug clinic, the `show_card` signature-design challenge, the three-line refactor challenge,
the signature peer review, the exit card kept; "מפגש" labels removed; the bug clinic's three bugs — wrong body
variable, swapped argument order, a missing argument — trimmed to one clean warm-up bug, wrong body variable; the
other two move to enrichment)
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 3.1 | `def`, the call, execution order, procedural abstraction | 45 / 45 |
| **3.2 (this)** | **parameters vs arguments, multiple parameters, refactoring repeats** | 0 / 90 |
| 3.3 | `return`, `print` vs `return`, local scope, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 2: write and call a function with parameters and no return value | ✅ every task |
| Concepts: function, parameters | ✅ parameter vs argument, positional matching |
| SC 2–3: use a building block via its interface, without its internal description | ✅ the signature-design task |

### Deliberate exclusions
`return` (3.3), keyword or default arguments, more than three parameters.

---

## 3. Lesson Goal

**A parameter is a name in the `def` that receives a value; an argument is the value sent at the call — arguments
match parameters in order, one for one.**

---

## 4. Core Mental Models

```python
def greet(name):        # name: a parameter - a local placeholder
    print("Hello", name)


greet("Dana")            # "Dana": an argument - matched to name, in order
greet("Omar")             # a new argument, the same parameter, a new result
```

- Same body, different result — because the parameter receives a different value each call.
- With two or more parameters, arguments match by **position**: the first argument fills the first parameter.
- Calling with too few arguments is a `TypeError` — Python never guesses a missing value.
- Add a parameter only when something genuinely changes between calls; a fixed message needs none (3.1).

---

# 5. Guided Practice (0–24)

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.2 – פעולות · "אותה פעולה, קלטים שונים" |
| 2–7 | **Recap (pairs):** `def greet(): print("Hello, Dana")`, called twice — what's missing to greet a different student each time, without writing a separate function per student? |
| 7–11 | Parameter vs argument: the parameter is a local placeholder in the `def`; the argument is the value sent at the call |
| 11–16 | `def greet(name): print("Hello", name)`, `greet("Dana")`, `greet("Omar")` — point at the parameter and at each argument |
| 16–24 | **Trace table (pairs):** `show_score(player, score)` called twice with different values — fill `player`, `score` and the output for each call |

---

# 6. Lab (24–90)

Starter: [`Card_Starter.py`](Card_Starter.py). Reference: [`Card_Reference.py`](Card_Reference.py).

## 24–33 — Warm-up: the body doesn't know that name

```python
# Warm-up: run this with "Maya" and 4. Read the error, then fix one word.


def show_result(name, stars):
    print(student, "has", stars, "stars")


show_result("Maya", 4)
```

```text
NameError: name 'student' is not defined
```

The parameter is named `name`, but the body refers to `student` — a name Python never gave a value. Fix: change
`student` to `name` inside the body → `Maya has 4 stars`.

## 33–42 — Predict before running

```python
def repeat_word(word, times):
    print(word * times)


repeat_word("Go! ", 2)
repeat_word("Hi ", 3)
repeat_word("Stop ")
```

Predict the first two outputs, then explain why the third call fails.

```text
Go! Go!
Hi Hi Hi
TypeError: repeat_word() missing 1 required positional argument: 'times'
```

## 42–54 — Task 1: `show_mission(student, mission)`

One line: `"<student> will complete <mission>"`. Call it three times with different students and missions; predict
the output first.

```text
Dana will complete maze
Omar will complete quiz
Noa will complete debugging
```

## 54–68 — Task 2: designing `show_card(student, level, points)`

Three parameters, three printed lines (`Student:` / `Level:` / `Points:`). Call it twice with different values. Plan
the parameter order on paper before typing: which value changes between calls, and in what order will you send them?

```text
Student: Maya
Level: easy
Points: 10
Student: Ali
Level: hard
Points: 30
```

## 68–80 — Task 3 (refactor): one function, three calls

Replace these three lines with **one** function, called three times — same output, less duplication:

```python
print("Level", 1, "needs", 10, "points")
print("Level", 2, "needs", 20, "points")
print("Level", 3, "needs", 35, "points")
```

```text
Level 1 needs 10 points
Level 2 needs 20 points
Level 3 needs 35 points
```

Identify what's fixed (the wording) and what changes (the two numbers) before writing the signature.

## 80–85 — Signature peer review

Swap with a partner. Check one signature: does the name describe a role? Does every parameter really change between
calls? Is the order clear? Do the three test calls cover different values? Give one suggested improvement, then
re-run.

## 85–90 — Save and exit check

Save As `G8_U3_M2_Card_<Name>.py`.

1. Complete: "I chose to add a parameter when…"
2. Complete: "Before I call a function, I check that…"

### Tool Note – Thonny
Thonny's error message names the **missing** parameter by name (e.g. `missing 1 required positional argument:
'times'`) — read that name before guessing which argument is missing.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The parameter and the argument are the same thing | The parameter is a name in the `def`; the argument is the value sent at the call |
| Arguments match parameters by meaning | They match by **position** — order matters |
| A parameter can be left out if Python can guess it | Python never guesses; a missing argument is a `TypeError` |
| Every value a function uses should be a parameter | Only values that actually change between calls need to be parameters |
| Swapping two arguments' order just changes which prints first | It can silently send the wrong value to the wrong parameter, with no error at all |

---

# 8. Assessment Evidence (formative)

- The `repeat_word` predictions, including the reasoned `TypeError` explanation
- `show_mission()` passing all three test calls
- `show_card()`'s signature planned on paper before coding
- The three-line refactor producing identical output to the original
- One concrete improvement from the signature peer review
- Exit check
