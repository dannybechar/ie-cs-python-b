# Unit 5.1 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: A String Is an Ordered Sequence

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)):
deck **7.1** (slides 2–13: what a string is, quotes, `str` vs `int`, positive and negative indices on `"love :)"` and
`"think big be bold show your color"`, `len`, the quiz) and worksheet **7.2** (questions 1–4: `+` and `*`, `len`,
`int()`/`str()`, positive and negative indices on `"PYTHON"`). **Changed from the previous version** (which followed
`python_b_unit05_strings_complete_unit.md`): the `ROBOT` index table is replaced by the Ministry's two index pictures; `in`,
`count`, `find`, `replace` and the other methods moved to 5.2–5.3 where the Ministry teaches them; the "prompt checker"
and `header_check` tasks are gone; the immutability idea stays but only as a preview (a method returns a new string)
because the Ministry meets it with the methods. Ministry slide wording was kept, but every example was run on Python 3.14.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **5.1 (this)** | **what a string is, quotes, indices (+/−), `len`, `+` and `*`, `int`/`str`** | 45 / 45 |
| 5.2 | slicing `[start:end:jump]`, `count`, `replace`, `in`, `find` | 45 / 45 |
| 5.3 | `lower`/`upper`, `startswith`/`endswith`, `isalpha`/`isdigit`, `for` over a string | 0 / 90 |
| 5.4 | exercises 4–7, `ord`/`chr` cipher, `split`/`join` (shown), worksheet 8.2, unit checkpoint | 0 / 90 |

Unit total 90 theory / 270 practice (master table: 8 h = 2 + 6).

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 13) | Covered here |
|---|---|
| Goal 1: a string is an ordered sequence of characters | ✅ 7.1 slides 2–3, 5 |
| Goal 2: the empty string; `+`, `*` | ✅ worksheet 7.2 Q1–2 (`in` comes in 5.2) |
| Goal 3: access by a positive or a negative index | ✅ 7.1 slides 9–11, worksheet Q4 |
| Goal 4: why the first index is `0` | ✅ "the first character is zero steps from the start" |
| Goal 6 (part): `len` | ✅ |

### What Grade 7 already did
Python A (Unit 6) taught `len`, `word[0]`, `word[len(word) - 1]`, `+`, `*` — but **no negative indices**. So `+`, `*`,
`len` are a fast review here, and negative indices are the new idea.

### Deliberate exclusions
Slicing and the string methods (5.2–5.3), loops over a string (5.3), lists.

---

## 3. Lesson Goal

**A string is an ordered sequence of characters; each one has a place (an index) counted from the left starting at `0`
and from the right starting at `-1`; the last valid index is `len(text) - 1`.**

---

## 4. Core Mental Models

```python
text = "love :)"          # 7 characters: l o v e, a space, a colon, a closing bracket
print(len(text))           # 7 - spaces and punctuation count
print(text[0], text[-1])   # l )
```

```python
text = "think big be bold show your color"
print(len(text))                   # 33
print(text[16], text[-17])         # d d  - the same character, counted from the left and from the right (slide 10)
```

- The quotes are not part of the string; they only show where it starts and ends. Use the same mark at both ends:
  `"it's fine"` or `'say "hi"'`.
- `"7"` is a string and `7` is a number: `"3" + "3"` is `"33"`, `3 + 3` is `6`; `"3" * 3` is `"333"`.
- `int("12")` turns a string of digits into a number; `str(12)` turns a number into a string.
- A string cannot be changed letter by letter: `text[0] = "x"` is a `TypeError` (shown now, understood in 5.2).

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–5 | **Hook:** a one-line AI answer saved in a variable (`answer = "Take a short break and drink water."`). Predict `type(answer)`, `len(answer)`, the first character. A program sees a model's answer as a string like any other |
| 5–12 | **What is a string** (7.1 slides 2–4): examples `"my school"`, `"a#%$!P_K"`, `"3+4=?"`; single or double quotes, same mark at both ends; the empty string `""`; `str` vs `int`: `"7"` is not `7` |
| 12–22 | **Indices** (slides 5, 9–11): `"love :)"` and `"think big be bold show your color"`, both numberings drawn on the board. **Predict** `text[1]`, `text[-1]`, `text[0]`, `text[-10]`, `text[16]`, `text[-17]`. Why `0`? The index is the distance from the start. The off-by-one: `text[len(text)]` |
| 22–29 | **`len`** (slides 6–7, quiz 12): `len("love :)")` is 7; `len("Python 3.12")` is 11; `len(" ")` is 1 (a space is a character); `len("")` is 0 |
| 29–38 | **`+` and `*` on strings** (worksheet Q1–2): predict `print(text1 + text2)` and `print(text3 * 2)` on paper, run, compare. Then `"3" + "3"`, `"3" * 3`, and the errors: `"a" + 1`, `"5" * "3"` (read the messages) |
| 38–45 | **`int()` and `str()`** (worksheet Q3): `input` always gives a string — `num = int(input(...))` vs `st = input(...)`; predict `num + num`, `st + st`, `num * 3`, `st * 3`. Preview of the next meeting: `text[0] = "x"` fails — a string can't be changed in place |

Predict-first rule: at 29–38 students write their prediction for `msg1 = "abc" + "d" * 3`, `print(msg1 + "ef")` and
`print(len(msg1))` *before* the answer goes on the board — `abcdddef` and `6`.

---

# 6. Second 45 Minutes — Lab

Starter: [`Indices_Starter.py`](Indices_Starter.py). Reference: [`Indices_Reference.py`](Indices_Reference.py).

## 45–52 — Warm-up: one index too far

```python
word = "ROBOT"
last_letter = word[len(word)]
print(last_letter)
```

Predict, then run: `IndexError: string index out of range`. `len(word)` is 5 but the valid indices are 0–4. Fix:
`word[len(word) - 1]` or `word[-1]`. (Python A used the first form; the second is new.)

## 52–60 — Task 1: predict and check (worksheet 7.2 Q1–2)

Predict the eight printed lines in the starter on paper, then run. Expected: `I like to play, piano` ·
`I like to play, guitar` · `guitarguitar` · `abcdddef` · `6` · `8` · `77` · `1`. *Teacher note: the Ministry printout of Q2
has a broken quote (`'abc' + d' * 3`); the starter uses the intended `"abc" + "d" * 3`.*

## 60–68 — Task 2: `add_as_numbers(first, second)` and `join_as_text(first, second)`

Both parameters are strings of digits. The first returns the sum as a number, the second the joined text.
`"12"`, `"30"` → `42` and `"1230"`.

## 68–76 — Task 3: `show_edges(st)` (worksheet Q4)

For `"PYTHON"`, print each wanted letter twice, once with a positive and once with a negative index:
`P`/`P`, `N`/`N`, `T`/`T` (positions 0 and −6, 5 and −1, 2 and −4).

## 76–84 — Task 4: `first_and_last(word)`

Return the first letter followed by the last letter. `"ROBOT"` → `"RT"`; `"A"` → `"AA"`.

## 84–87 — If time: `stars_for(word)`

Return as many `*` as the word has characters: `"hello"` → `"*****"`.

## 87–90 — Save and exit check

Save As `G8_U5_M1_Indices_<Name>.py`. For `text = "MODEL"`, complete:

1. `text[1]` is…
2. `text[-1]` is…
3. `len(text)` is…
4. `text[len(text)]` is…

**Answers:** `O`, `L`, `5`, an `IndexError`.

### Tool Note – Thonny
Hover a string in the **Variables** view to see its quotes — a stray leading or trailing space becomes visible there.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An index equal to the string's length is valid | The last valid index is `len(text) - 1` (or `-1`) |
| `-1` is the first character | `-1` counts from the right: it is the last character |
| `"7"` and `7` are the same | One is text, one is a number: `"7" * 2` is `"77"`, `7 * 2` is `14` |
| `input()` returns a number | It always returns a string; convert with `int()` when you need a number |
| `len` counts only letters | It counts every character, including spaces and punctuation |

---

# 8. Assessment Evidence (formative)

- Both index pictures answered before running anything (`text[16]`, `text[-17]`)
- The task 1 predictions written down before the run
- The warm-up error explained, not just patched
- `add_as_numbers`, `join_as_text`, `show_edges`, `first_and_last` passing their test inputs
- Exit check
