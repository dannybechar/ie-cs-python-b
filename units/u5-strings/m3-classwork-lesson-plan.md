# Unit 5.3 — Strings: Walking Over a String (45-minute lesson + paper classwork)

## Grade 8 / AI + Python B · Paper-classwork edition of 5.3
### Topic: `for` over a string, counters, building a string, methods inside a loop

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes = 45-minute lesson + about 46 minutes of paper-and-computer classwork (the rest finishes at home)
**Structure:** Knowledge + Lab. The lesson teaches exactly what the worksheet needs, in four short demos, each followed by a student action.
**Minutes (theory / practice):** 45 / 45 (the unit plan has 5.3 as Lab + Lab 0 / 90; see "Decision for the teacher" below)
**Current tool:** Thonny, with a printed worksheet
**Source of inspiration:** the Ministry's teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)):
decks **8.0 / 8.1** slides 7–15 (walking over a string with `for`, `end=`, the three read-the-code slides, exercises **#1, #2, #7**)
and deck **7.1** (`isalpha`, `isdigit`, `lower`). **What was built from them:** the worksheet
[`m3-classwork-worksheet-he.md`](m3-classwork-worksheet-he.md) was designed first (Ministry slides → tasks), and this lesson was
derived from it. **Changed from the Ministry text:** exercises are functions that take a string and *return* a value;
the Ministry's `print(count = ', count)` is a typing slip (syntax error), so the course prints with `print("num =", count)`;
exercise 3 (surnames with `input`) and exercises 4–6 stay in the existing 5.3 / 5.4 plans.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction is isolated and labeled **Tool Note – Thonny**.

Slides: the deck for this lesson (20 slides, 90 minutes) is built from the prep folder `Downloads\python-b\unit5-m3-classwork-slides\`; slides 1–17 are the 45-minute lesson, 18–20 the classwork block and exit check.

Files: worksheet [`m3-classwork-worksheet-he.md`](m3-classwork-worksheet-he.md) (Word copy for printing),
answer key [`m3-classwork-answer-key.md`](m3-classwork-answer-key.md), student file [`Classwork_Starter.py`](Classwork_Starter.py),
reference [`Classwork_Reference.py`](Classwork_Reference.py). The existing 90-minute lab version stays in
[`m3-lesson-notes.md`](m3-lesson-notes.md).

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice |
|---|---|---|
| 5.1 | what a string is, indices (+/−), `len`, `+`, `*` | 45 / 45 |
| 5.2 | slicing, `count`, `replace`, `in`, `find` | 45 / 45 |
| **5.3 (this edition)** | **`for` over a string, counters, `+=` building, `isalpha`/`isdigit`/`lower` inside a loop** | **45 / 45** |
| 5.4 | exercises 4–7, `ord`/`chr`, `split`/`join` (shown), worksheet 8.2, checkpoint | 0 / 90 |

**Decision for the teacher.** The unit plan gives 5.3 a 0 / 90 split (all practice, short demos). A 45-minute lesson followed by
classwork makes it 45 / 45. The unit then totals 135 theory / 225 practice instead of 90 / 270. Either accept that,
or treat the first 45 minutes as a guided demo-and-try block (it already has a student action every 7–10 minutes) and keep the
course map unchanged. This edition changes no other file.

---

## 2. What the Worksheet Needs (and therefore what the lesson must teach)

| Worksheet item | Skill the student must already have |
|---|---|
| A1–A3 | read `for ch in text`, `end=""`, predict the output, an accumulating string and a counter |
| A4 | fill a trace table for a loop with an `if` |
| B1 | why a counter is set **before** the loop |
| B2 | the counting pattern as a function that returns |
| B3 | building a string with `+=` from `""`, `ch * 3`, return vs print |
| B4 | `isalpha()` / `isdigit()` on one character; why `count()` does not fit |
| B5 | `lower()`, `ch in "aeiou"` |
| Part C | the same patterns again (`if/else` building, reuse of `count_char`) |

Nothing else is needed: no indices (5.4), no `range(len(text))`, no `ord`/`chr`, no lists.

---

## 3. Lesson Goal

**A `for` loop gives you the characters of a string one at a time. Put a counter (starts at 0) or a new string
(starts as `""`) before the loop, change it inside, and return it after the loop.**

---

## 4. First 45 Minutes — the Lesson

Rule: students are doing something at least every 10 minutes.

| Clock | Activity | Student action |
|---|---|---|
| 0–5 | **Hook.** On the board: `text = "banana"`. "How many `a`? You counted with your eyes. How would a program do it, one letter at a time?" Show the loop in Demo 1 as the answer | Say the count aloud; vote on what the loop variable will hold |
| 5–15 | **Demo 1 — the loop variable.** Run `for ch in "hi!": print(ch * 2)` → `hh`, `ii`, `!!`. Show a small drawing: `ch` takes `"h"`, then `"i"`, then `"!"`. Then `end=","` on `"sometimes"` → `s,o,m,e,t,i,m,e,s,`; `print()` afterwards to end the line | **Predict (paper):** `for ch in "go": print(ch, end="-")` → `g-o-`. Then run Worksheet A1 together |
| 15–25 | **Demo 2 — the counter pattern.** Write `count_a("banana")` on the board. `count = 0` **before** `for`; `if ch == "a": count += 1`; `return count` **after** the loop. Fill the trace table together (this is exactly Worksheet A4): `b F 0 · a T 1 · n F 1 · a T 2 · n F 2 · a T 3`. Show the two classic bugs on `"abc"` (deck slide 9): `count = 0` inside the loop gives `0` (on `""` it crashes with `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`), and `return` indented inside the loop gives `1` (the loop stops after the first letter) | Students fill the trace-table rows themselves as the teacher runs it; then **predict** both bugs on `"abc"` (`0` and `1`) and explain why |
| 25–35 | **Demo 3 — building a string.** `dashed(text)`: `result = ""`; `result += ch + "-"`; `return result`. Trace `dashed("ab")` → `""` → `"a-"` → `"a-b-"`. Compare `print(result)` (shows it, the value is gone) with `return result` (the caller can use it) | **Mini-task (3 min, paper):** write `double(text)`. Compare with the neighbour, then with the board |
| 35–42 | **Demo 4 — methods inside the loop.** `if ch.isdigit(): count += 1` on `"a1b22"` → `3`. `ch.lower() in "aeiou"` on `"Hello World"` → `3` (`e`, `o`, `o`). Why `text.count("5")` is not enough for "any digit" | **Predict:** how many vowels in `"Education"`? (`5`: `E`, `u`, `a`, `i`, `o`.) Then check with the demo code |
| 42–45 | **How to work.** Show the worksheet. The cycle: write on paper → type in `Classwork_Starter.py` → run → compare with "expected" → correct in another colour. Part A and B are class work; what is not finished is homework. Invented texts only | Open Thonny and the starter file |

Then 45+ minutes of classwork (see the worksheet; suggested pace A 10 · B1 5 · B2 7 · B3 8 · B4 8 · B5 8).

## 5. Classwork — What the Teacher Does

- Walk the room during **B1** and **B2**: they show whether the student has the counter pattern. Ask "where does `count` start, and when?"
- Do not type the code for a student. Ask them to read their paper line, then predict the first two rounds.
- Students who finish Part B early go to Part C; **C3** (checking an AI answer) is the discussion to bring back to the whole class.
- At about 80 minutes: collect the exit check (three questions, no computer) and tell the class what is homework.

---

## 6. Core Mental Models

```python
def count_char(text, letter):
    count = 0                      # once, before the loop
    for ch in text:                # ch is a different one-letter string each round
        if ch == letter:
            count += 1
    return count                   # after the loop
```

```python
result = ""                        # start with an empty string
for ch in "abc":
    result += ch * 2
print(result)                      # aabbcc
```

## 7. Tool Note – Thonny

- `Classwork_Starter.py` has the Part A snippets as functions `a1()` … `a4()`; the student calls them at the bottom of the file.
- The red Stop button is not needed (no loop here can run forever).
- The Variables view is useful for B1: students can watch `count` return to `0`.

## 8. Misconception Risks

| Risk | What the student does | Response |
|---|---|---|
| Counter inside the loop | `count = 0` after `for` | Trace table: the value after each round; run on `""` to see the error |
| `return` inside the loop | stops after one character | Ask "how many rounds ran?"; trace the first round |
| Compare with the whole word | `if text == letter` | Ask what `ch` is, versus `text`, in round 1 |
| `print` instead of `return` | prints, then `None` | Run `x = triple("a")`, `print(x)` |
| Uppercase letters | `count_vowels("AEIOU")` gives `0` | `ch.lower()` before the test |
| `.isdigit()` on the whole string | `"a1".isdigit()` is `False` | The method applies to one character here |

## 9. Assessment Evidence

- Part A: three correct predictions (or corrected in another colour) and a correct trace table.
- Part B: B1 explained in a sentence; B2, B3 and B5 correct on all test lines; B4 correct and the `count()` answer reasoned.
- Exit check on paper; homework (Part C) next lesson.
- AI framing (C3): the student can name one thing the program can count and one it cannot judge.
