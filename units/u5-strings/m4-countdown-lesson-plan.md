# Lessons 8.2–8.7 — Strings: Countdown Cases + Worksheet

## Grade 8 / AI + Python B · Countdown edition of Lessons 8.2–8.7
### Topic: String algorithms — four timed cases together, then a five-question worksheet (v2: cases rebuilt from the official exercises not used before)

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**No functions:** the class has not learned `def` yet (teacher, 2 Nov 2026) — every case and question is a few statements
under a variable (`text = "…"`), ending in `print`; to test another value, students change the variable and run again.
**Structure:** Lab + Lab: 48 minutes of timed cases done together (countdown page), then 37 minutes of worksheet and a 5-minute exit check
**Minutes (theory / practice):** 0 / 90 (the same as the unit plan for Lessons 8.2–8.7)
**Current tool:** Thonny, the countdown page in a browser (projected), a printed worksheet
**Source of inspiration:** the **countdown method** of the teacher's IB DP1 and PDP classes
(`ib-cs-java-dp1/units/b2-programming/test-prep-2026-11-10/countdown/`): one case at a time is projected, a big clock runs
(green, amber, red), the room is "locked out" at zero, and the reveal shows a `for` solution and a `while` solution that use
**different ideas**. The cases and questions come from the Ministry's teaching materials
([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)): worksheet **8.2** Q2 (case 1), guided practice **8.4** task 1 (case 2), deck **8.1** exercise #5 (case 3) and the enrichment video "new cipher" (case 4, not for the exam); worksheet exercise **8.1 #6** (count `is`, worksheet Q2) and **8.2** Q4, Q5, Q6, Q7 (the worksheet); the `or` bug of the
existing Lessons 8.2–8.7 warm-up (worksheet question 1). **Changed from the 90-minute lab version** ([`m4-lesson-notes.md`](m4-lesson-notes.md)):
exercise #7 (five vowel counters) is left out — the Lessons 8.0–8.1 classwork did vowels; `split`/`join` (8.1 slides 20–23) are shown only in the lab edition, not here (decision: shown and printed only, never used on a task; lists proper start in the lists block (lessons 9.1–14.5)); the checkpoint (`middle`, `edges`, `alternate_case`) is now part of a graded worksheet.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction is isolated and labeled **Tool Note – Thonny**.

Files:

| File | For | What |
|---|---|---|
| [`m4-countdown-he.html`](m4-countdown-he.html) | Teacher (projected) | The countdown page: 4 cases, `for`/`while` choice, clock, reveal. Standalone — open it in any browser, no internet needed |
| [`FirstStarLast_Starter.py`](FirstStarLast_Starter.py), [`MiddleChar_Starter.py`](MiddleChar_Starter.py), [`Initials_Starter.py`](Initials_Starter.py), [`NumberCipher_Starter.py`](NumberCipher_Starter.py) | Students | One file per case: the goal, the test values with expected output, and the `text = …` line to write under (generated with the page) |
| [`Countdown_Reference.py`](Countdown_Reference.py) | Teacher | Each case solved with `for` and with `while`, by a different idea (`# === case N for ===` sections); the page's reveal and expected output are built from it |
| [`m4-countdown-cases-he.md`](m4-countdown-cases-he.md) | Students | The four cases as instructions (goal, file, test values, expected output — no solutions); generated with the page, printed to `Countdown_Cases.pdf` for the Mashov zip |
| [`m4-countdown-cases.json`](m4-countdown-cases.json) | Teacher | The page's content (Hebrew titles, goals, minutes, test calls, how the two solutions differ) |
| [`m4-countdown-worksheet-he.md`](m4-countdown-worksheet-he.md) | Students | The worksheet (Word copy for printing in `Downloads\python-b`) |
| [`Worksheet_Starter.py`](Worksheet_Starter.py) / [`Worksheet_Reference.py`](Worksheet_Reference.py) | Students / Teacher | Question 1's bug and a variable to write under for each question; solutions with expected values |
| [`m4-countdown-answer-key.md`](m4-countdown-answer-key.md) | Teacher | Answers, rubric (100 points + 5 bonus), marking sheet, what to look for |

**Mashov upload:** `Downloads\python-b\Lessons 8.2–8.7 - Strings.zip` = `Countdown_Cases.pdf` + the four case starters + `Worksheet_Starter.py`
(no solutions). The worksheet itself is printed. The page's "how to start" steps tell students to download this zip from Mashov.

To change a case (wording, minutes, test calls), edit `m4-countdown-cases.json` or the reference and rebuild the page:
`python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json` (see [`tools/countdown/README.md`](../../tools/countdown/README.md)).

---

## 1. Position in the strings block (lessons 7.1–8.7)

| Meeting | Focus | Theory / practice |
|---|---|---|
| Lesson 7.1 | what a string is, indices (+/−), `len`, `+`, `*` | 45 / 45 |
| Lessons 7.1–7.2 | slicing, `count`, `replace`, `in`, `find` | 45 / 45 |
| Lessons 8.0–8.1 | `for` over a string, counters, `+=` building, `isalpha`/`isdigit`/`lower` (paper-classwork edition, as taught) | 45 / 45 (official plan 0 / 90; see [`unit-strategy.md`](unit-strategy.md)) |
| **Lessons 8.2–8.7 (this edition)** | **loops over places (`for` with `range(len(text))` and `while` with an index), `ord`/`chr`, string algorithms; graded worksheet** | **0 / 90** |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 13–15) | Covered here |
|---|---|
| Goal 7: traverse with `for`, and with an index when the place matters | ✅ every case twice (`for` / `while`); worksheet Q4 |
| Goal 8: counting, searching, validation and text-cleaning algorithms | ✅ cases 1–4; worksheet Q2–Q5 |
| Goal 9: functions that take a string and return a value | ❌ not yet — **the class has not learned functions** (teacher, 2 Nov 2026), so every case and question is plain code: a variable, a loop, `print`. Revisit these exercises as functions after the functions block (lessons 4.1–4.6) |
| Goal 10: apply string skills to AI text | ✅ case 4's debrief (a cipher protects nothing); the exit discussion |
| Ministry addition: `ord` / `chr` | ✅ case 4 (the number cipher), exit check 1 |

### Deliberate exclusions
`split` / `join` (official 8.1 slides 20–23: shown in the lab edition only; the result is a list, so no task uses it here), the official 8.4 task 2 (middle letters of every word — needs `split` and a list), lists, nested loops, `break` / `continue`, dictionaries.

---

## 3. Lesson Goal

**When the place in the text matters, the loop walks over places, not characters — with `for index in range(len(text))` or with
`while` and an index you move yourself; the same problem can be solved by two different ideas.**

---

## 4. Core Mental Models

| Idea | `for` | `while` |
|---|---|---|
| look at a neighbour | `text[index + 1]`, `text[index - 1]` | the same, with `index` moved by hand |
| remember something from earlier | a variable updated every round (`previous`, `last_space`) | — |
| stop as soon as you find it | (walks to the end) | the stop is the condition (`while text[index] != " "`) |
| jump instead of step | — | `place = text.find("is", place + 1)` |
| the line you must not forget | — | `index += 1` (or the loop never ends) |

---

## 5. First 48 Minutes — Countdown Cases (together)

Students work alone or in pairs at the computer; every case is projected. For each case: open the briefing (1 min — read the goal
and the test calls aloud; choose `for` or `while`), start the clock, circulate, and at "ננעל" reveal both solutions (3 min: what
did the two versions do differently? which would you write?). **Choose the loop per case:** a suggested order is `for` for cases 1
and 3, `while` for cases 2 and 4 (case 2's `while` is the clever one — nice for the faster students) — or let the faster students write the other version while the others finish.

| Clock | Activity |
|---|---|
| 0–3 | Open the page; how the countdown works (clock, lock-out, reveal); open case 1's file and run it: it prints nothing yet |
| 3–11 | **Case 1 — first, star, last** (clock 5, worksheet 8.2 Q2): `"Cats"` → `C*s`. Reveal: the last character seen in a loop vs the place `len(text) - 1`. A one-character text gives `a*a` |
| 11–20 | **Case 2 — middle character** (clock 6, guided practice 8.4 task 1): `"robot"` → `b`, `"python"` → `th`. Reveal: `// 2` and `% 2` vs two places moving inward |
| 20–31 | **Case 3 — initials** (clock 7, deck 8.1 exercise 5): `"American Standard Code…"` → `"ASCII"`. Reveal: remember `previous` vs look back at `text[index - 1]` |
| 31–35 | **Demo — letters are numbers.** Predict first: `ord("a")`? (`97`.) `ord("b")`? `chr(98)`? `chr(ord("c") + 1)`? Then `ord("A")` (`65`) — capitals are different numbers; `str(97)` makes text of a number |
| 35–48 | **Case 4 — the new cipher** (clock 8, the official enrichment video): `"Big Secret!"` → `66 105 103    83 101 99 114 101 116 !`. Reveal: `isalpha()` vs the number range 65–90 / 97–122 (`isalpha` is true for Hebrew letters too). A cipher like this protects nothing: `chr` undoes it |

Cipher rule used here (the official slide's last line shows the spaces collapsed): every English letter becomes its number followed by **one space**;
a space becomes **three spaces**; every other character stays. The earlier next-letter cipher (`zoo` → `app`) is in the lab edition ([`m4-lesson-notes.md`](m4-lesson-notes.md)).

If the class is slow, set case 4's clock to 6 minutes or do it as a live demo; do not cut the worksheet time.

---

## 6. Second 42 Minutes — Worksheet (graded)

Hand out the printed worksheet; students open `Worksheet_Starter.py`. Work cycle as in Lessons 8.0–8.1: write on paper → run → compare →
correct in another colour. Work alone. Collect the worksheets at the end; what is unfinished is finished at home and handed in
next lesson (teacher's choice).

| Clock | Question | Ministry source |
|---|---|---|
| 48–54 | **Q1 — find the bug:** `character == "a" or "e" or …` prints 19, not 8 | the Lessons 8.2–8.7 warm-up |
| 54–60 | **Q2 — count `is` without `count`** | 8.1 exercise 6 |
| 60–67 | **Q3 — first 4 and last 4 characters** | 8.2 Q4 |
| 67–75 | **Q4 — last letter of every word** | 8.2 Q5 |
| 75–85 | **Q5 — alternating case** | 8.2 Q7 |
| if time | **the word `it`** (bonus) | 8.2 Q6 |
| 85–90 | Save As `G8_U5_M4_Worksheet_<Name>.py`; **exit check** on paper (`chr(ord("b") + 2)`, `"this is his".count("is")`, the line a `while` must not forget); collect |

### Tool Note – Thonny
While working on one question, put a `#` before the other questions' code (or select it and press **Ctrl+3** (Edit › Toggle comment) to comment it out), so only one answer prints. When a `while` loop
never ends, press **Stop** (the red button) and look for the missing `index += 1`.

---

## 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `x == "a" or "e"` means "a or e" | each side of `or` is a full condition; `x in "aeiou"` |
| `count("is")` counts the word `is` | it counts the characters anywhere, also inside `this` |
| a `while` over a text moves by itself | only `index += 1` moves it; without it the loop never ends |
| `text[index + 1]` is safe everywhere | not on the last place — check the end first (`or` stops early) |
| `ord("a")` gives a letter | it gives a number; `chr` goes back |
| alternate by index | a space has an index too; remember whose turn it is |

---

## 8. Assessment Evidence

- **Countdown cases:** ungraded; watch who finishes in time and who needs the reveal. Note which loop the class found harder.
- **Worksheet:** graded with the rubric in [`m4-countdown-answer-key.md`](m4-countdown-answer-key.md) (100 points + 5 bonus).
- **Exit check:** three items on the worksheet (10 points of the 100).
