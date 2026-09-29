# Unit 3.1 — Functions

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: A Function as a Building Block — No Parameters, No Return

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the codex deck `python_b_unit03_m01_functions_no_parameters_delivery.pptx` (the "what to
name this repeated block" hook, the before/after comparison, the `def` anatomy, the execution-order trace, the
reading task, the `show_welcome()` writing task, the call-before-`def` multiple-choice question, the bug clinic, the
control-panel mini-project and its four-function architecture, the peer-review-by-names-alone activity, the exit
card kept; "מפגש" labels removed; the bug clinic's three bugs split so the lab warm-up carries one clean bug
(call-before-`def`) and the other two — the `function` keyword and bad indentation — move to enrichment)
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 3

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **3.1 (this)** | **`def`, the call, execution order, procedural abstraction** | 45 / 45 |
| 3.2 | parameters vs arguments, multiple parameters, refactoring repeats | 0 / 90 |
| 3.3 | `return`, `print` vs `return`, local scope, unit checkpoint | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept (python-b-ai.pdf p. 10) | Covered here |
|---|---|
| Goal Py 1: write and call a function with no parameters and no return value | ✅ every task |
| SC 1–3: an algorithm as a building block; use vs. internal description; use vs. implementation | ✅ the before/after comparison, procedural abstraction |
| Concepts: function; Python syntax: colon, indentation, `def` | ✅ |
| Teaching: introduce every concept in the context of a real problem; black box | ✅ hook, black-box slide |

### Deliberate exclusions
Parameters (3.2), `return` (3.3), any function with parameters or a return value.

---

## 3. Lesson Goal

**`def` defines a function; only a call runs it — and Python must already know the `def` before that call.**

---

## 4. Core Mental Models

```python
def show_header():          # def: this defines the function, it does not run it
    print("MISSION CONTROL")
    print("---------------")


show_header()                # only the call runs the body
```

- Python reads every `def` top to bottom first, then runs the main program from the top; a call written **before**
  its `def` fails with `NameError` — the name isn't known yet.
- Indentation marks what belongs to the function's body; the first unindented line is back in the main program.
- **Procedural abstraction:** once a function has a name, you use it by that name — you don't need to reread its body
  every time.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 3.1 – פעולות · "פעולה כאבן בניין" |
| 2–8 | **Hook (pairs):** a game program prints a round title, a divider line and short instructions every round. Which lines deserve one shared name? |
| 8–13 | Before/after: repeated code vs. named functions — one place to fix, a main program that reads like an outline |
| 13–20 | Anatomy of `def show_header():` — line by line: `def`, name, empty parentheses, colon, indented body, the call |
| 20–24 | Procedural abstraction: use a function by its name; the body explains "how", the name explains "what" |
| 24–31 | **Trace (alone, then check):** `def beep(): print("BEEP")` then `print("A"); beep(); print("B"); beep()` — write the four output lines before running |
| 31–35 | Answer: `A`, `BEEP`, `B`, `BEEP` — defining `beep` doesn't print anything by itself |
| 35–41 | **Read and predict (alone, 2 min, then pairs):** a `signal()` function with two `print`s, called twice with one line between — mark the function body and the main program in two colors, then write all four output lines |
| 41–43 | Answer: `READY`, `GO`, `PAUSE`, `READY`, `GO` |
| 43–45 | The lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Panel_Starter.py`](Panel_Starter.py). Reference: [`Panel_Reference.py`](Panel_Reference.py).

## 45–53 — Warm-up: called before it's known

```python
# Warm-up: run this. Read the error message, then move one line to fix it.

show_status()


def show_status():
    print("READY")
```

```text
NameError: name 'show_status' is not defined
```

Python runs the main program top to bottom; at the call, `show_status` hasn't been defined yet. Fix: move the `def`
above the call → `READY`.

## 53–65 — Task 1: `show_welcome()`

Define `show_welcome()` — two lines, no parameters, no return. Call it twice, with something else printed between
the calls. Write the expected output before running.

```text
WELCOME
Choose a mission
---
WELCOME
Choose a mission
```

Ask: why does changing the text inside `show_welcome()` change both calls at once?

## 65–80 — Task 2 (mini-project): control panel

Four functions — `show_title`, `show_status`, `show_help`, `show_end` — each printing one line, no parameters, no
return. Call them in a sensible order from the main program; call `show_status` twice (once near the start, once
near the end).

```text
MISSION PANEL
READY
Press ENTER to continue
READY
Session complete
```

Build **bottom-up**: write and test one function at a time before calling them all together.

## 80–84 — Peer review by name alone

Swap with a partner. They read only your function **names** (not the bodies) and guess what the program does. If
the guess is right, the names are clear; if not, rename or split a function that does more than one job.

## 84–90 — Save and exit check

Save As `G8_U3_M1_Panel_<Name>.py`.

1. What does defining a function do, and what makes it actually run?
2. Two lines in a program are identical. What is the first sign that they belong in a function?

### Tool Note – Thonny
The **Variables** view (View › Variables) only shows variables in the currently running frame — while stepping
through a function call, it will not show the main program's variables. That's expected, not a bug.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Defining a function runs it | Only a call runs the body |
| A call can appear anywhere in the file | It must come after the `def`, in the order Python runs the file |
| Fewer lines in the main program is the whole point | The real win is one place to fix and a clear outline — a function that hides one bad job is not an improvement |
| A function must print something to be useful | It can also just organize repeated steps (this meeting); returning a value comes in 3.3 |
| Indentation is just style | It marks exactly which lines belong to the function's body |

---

# 8. Assessment Evidence (formative)

- The `beep()` and `signal()` predictions written before running
- The call-before-`def` warm-up explained, not only fixed
- `show_welcome()` called twice with the expected output written first
- The four-function control panel, built and tested one function at a time
- The peer-name-guessing review completed with at least one rename or split, if needed
- Exit check
