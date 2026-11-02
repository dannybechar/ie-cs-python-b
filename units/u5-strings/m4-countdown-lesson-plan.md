# Unit 5.4 — Strings: Countdown Cases + Worksheet

## Grade 8 / AI + Python B · Countdown edition of 5.4
### Topic: String algorithms — four timed cases together, then a five-question worksheet

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** Lab + Lab: 48 minutes of timed cases done together (countdown page), then 37 minutes of worksheet and a 5-minute exit check
**Minutes (theory / practice):** 0 / 90 (the same as the unit plan for 5.4)
**Current tool:** Thonny, the countdown page in a browser (projected), a printed worksheet
**Source of inspiration:** the **countdown method** of the teacher's IB DP1 and PDP classes
(`ib-cs-java-dp1/units/b2-programming/test-prep-2026-11-10/countdown/`): one case at a time is projected, a big clock runs
(green, amber, red), the room is "locked out" at zero, and the reveal shows a `for` solution and a `while` solution that use
**different ideas**. The cases and questions come from the Ministry's teaching materials
([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)): decks **8.0 / 8.1** exercises **#4, #5, #6**
and the `ord`/`chr` next-letter cipher (the cases); worksheet **8.2** Q3, Q4, Q5, Q6, Q7 (the worksheet); the `or` bug of the
existing 5.4 warm-up (worksheet question 1). **Changed from the 90-minute lab version** ([`m4-lesson-notes.md`](m4-lesson-notes.md)):
exercise #7 (five vowel counters) is left out — the 5.3 classwork did vowels; `split`/`join` are not shown (Unit 7 teaches them
with lists — 7.2); the checkpoint (`middle`, `edges`, `alternate_case`) is now part of a graded worksheet.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction is isolated and labeled **Tool Note – Thonny**.

Files:

| File | For | What |
|---|---|---|
| [`m4-countdown-he.html`](m4-countdown-he.html) | Teacher (projected) | The countdown page: 4 cases, `for`/`while` choice, clock, reveal. Standalone — open it in any browser, no internet needed |
| [`Countdown_Starter.py`](Countdown_Starter.py) | Students | One file with the four case stubs and their checks |
| [`Countdown_Reference.py`](Countdown_Reference.py) | Teacher | Each case solved with `for` and with `while`, by a different idea; the page's reveal screen is built from it |
| [`m4-countdown-cases-he.md`](m4-countdown-cases-he.md) | Students | The four cases as instructions (goal, function, test calls, expected results — no solutions); generated with the page, printed to `Countdown_Cases.pdf` for the Mashov zip |
| [`m4-countdown-cases.json`](m4-countdown-cases.json) | Teacher | The page's content (Hebrew titles, goals, minutes, test calls, how the two solutions differ) |
| [`m4-countdown-worksheet-he.md`](m4-countdown-worksheet-he.md) | Students | The worksheet (Word copy for printing in `Downloads\python-b`) |
| [`Worksheet_Starter.py`](Worksheet_Starter.py) / [`Worksheet_Reference.py`](Worksheet_Reference.py) | Students / Teacher | Question 1's bug and stubs; solutions with expected values |
| [`m4-countdown-answer-key.md`](m4-countdown-answer-key.md) | Teacher | Answers, rubric (100 points + 5 bonus), marking sheet, what to look for |

**Mashov upload:** `Downloads\python-b\Unit 5.4 - Strings.zip` = `Countdown_Cases.pdf` + `Countdown_Starter.py` + `Worksheet_Starter.py`
(no solutions). The worksheet itself is printed. The page's "how to start" steps tell students to download this zip from Mashov.

To change a case (wording, minutes, test calls), edit `m4-countdown-cases.json` or the reference and rebuild the page:
`python tools/countdown/build_countdown.py units/u5-strings/m4-countdown-cases.json` (see [`tools/countdown/README.md`](../../tools/countdown/README.md)).

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice |
|---|---|---|
| 5.1 | what a string is, indices (+/−), `len`, `+`, `*` | 45 / 45 |
| 5.2 | slicing, `count`, `replace`, `in`, `find` | 45 / 45 |
| 5.3 | `for` over a string, counters, `+=` building, `isalpha`/`isdigit`/`lower` (paper-classwork edition) | 45 / 45 |
| **5.4 (this edition)** | **loops over places (`for` with `range(len(text))` and `while` with an index), `ord`/`chr`, string algorithms; graded worksheet** | **0 / 90** |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 13–15) | Covered here |
|---|---|
| Goal 7: traverse with `for`, and with an index when the place matters | ✅ every case twice (`for` / `while`); worksheet Q4 |
| Goal 8: counting, searching, validation and text-cleaning algorithms | ✅ cases 1, 2, 4; worksheet Q2–Q5 |
| Goal 9: functions that take a string and return a value | ✅ every case and question |
| Goal 10: apply string skills to AI text | ✅ case 3's debrief (a cipher protects nothing); the exit discussion |
| Ministry addition: `ord` / `chr` | ✅ case 3, exit check 1 |

### Deliberate exclusions
`split` / `join` (Unit 7.2 teaches them with lists), lists, nested loops, `break` / `continue`, dictionaries.

---

## 3. Lesson Goal

**When the place in the text matters, the loop walks over places, not characters — with `for index in range(len(text))` or with
`while` and an index you move yourself; the same problem can be solved by two different ideas, and a function returns its answer.**

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
and 3, `while` for cases 2 and 4 — or let the faster students write the other version while the others finish.

| Clock | Activity |
|---|---|
| 0–3 | Open the page and `Countdown_Starter.py`; how the countdown works (clock, lock-out, reveal); run the starter: every line says `None` |
| 3–13 | **Case 1 — `count_is`** (clock 6): `"this is his list"` → 4. Reveal: every place vs `find` jumps. Why 4, not 1? |
| 13–24 | **Case 2 — `initials`** (clock 7): `"American Standard Code…"` → `"ASCII"`. Reveal: remember `previous` vs look back at `text[index - 1]` |
| 24–28 | **Demo — letters are numbers.** Predict first: `ord("a")`? (`97`.) `ord("b")`? `chr(98)`? `chr(ord("c") + 1)`? Then `ord("A")` (`65`) — capitals are different numbers |
| 28–38 | **Case 3 — `next_letters`** (clock 7): `"zoo"` → `"app"`. Reveal: `if` for `"z"` vs `% 26`. A cipher like this protects nothing |
| 38–48 | **Case 4 — `first_and_last_word`** (clock 8): `"Cats and dogs are great friends"` → `"Cats friends"`. Reveal: remember the last space vs walk back from the end |

If the class is slow, set case 4's clock to 6 minutes or do it as a live demo; do not cut the worksheet time.

---

## 6. Second 42 Minutes — Worksheet (graded)

Hand out the printed worksheet; students open `Worksheet_Starter.py`. Work cycle as in 5.3: write on paper → run → compare →
correct in another colour. Work alone. Collect the worksheets at the end; what is unfinished is finished at home and handed in
next lesson (teacher's choice).

| Clock | Question | Ministry source |
|---|---|---|
| 48–54 | **Q1 — find the bug:** `character == "a" or "e" or …` returns 19, not 8 | the 5.4 warm-up |
| 54–60 | **Q2 — `middle(word)`** | 8.2 Q3 |
| 60–67 | **Q3 — `edges(text)`** | 8.2 Q4 |
| 67–75 | **Q4 — `last_letters(text)`** | 8.2 Q5 |
| 75–85 | **Q5 — `alternate_case(text)`** | 8.2 Q7 |
| if time | **`count_word_it(text)`** (bonus) | 8.2 Q6 |
| 85–90 | Save As `G8_U5_M4_Worksheet_<Name>.py`; **exit check** on paper (`chr(ord("b") + 2)`, `"this is his".count("is")`, the line a `while` must not forget); collect |

### Tool Note – Thonny
Run each function alone in the **Shell** first (`middle("python")`) — faster than running the whole file. When a `while` loop
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
