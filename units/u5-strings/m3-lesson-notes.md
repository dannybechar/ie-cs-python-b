# Unit 5.3 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: More String Methods and Walking Over a String with `for`

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** Lab + Lab (short demo → task → short demo → task)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)):
deck **7.1** slides 29–38 and worksheet **7.2** Q12, Q14, Q16 (`lower`, `upper`, `startswith`/`endswith` with start and
end, `isalpha`, `isdigit`); decks **8.0 / 8.1** slides 7–15 (walking over a string with `for`, `end=`, the three
read-the-code slides, exercises **#1, #2, #3**). **Changed from the previous version** (which followed
`python_b_unit05_strings_complete_unit.md`): "dynamic slicing with `find`" and the digit-hiding task moved or were dropped
(`find` is taught in 5.2; building a string with `+=` now appears as the Ministry's "keep letters a–e" slide); the
`range(len(text) + 1)` warm-up is replaced by the counter-reset bug. **Fixes to the Ministry text:** the exercise-1
solution prints with `print(count = ', count)`, which is an extraction/typing slip (it is a syntax error) — the course uses
`print("num =", count)`; the exercises are rewritten as functions that **take a string and return a value**
(program goal 9), with the Ministry's `input`-based form kept only where the exercise asks for input (#3).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | what a string is, indices (+/−), `len`, `+`, `*`, `int`/`str` | 45 / 45 |
| 5.2 | slicing, `count`, `replace`, `in`, `find` | 45 / 45 |
| **5.3 (this)** | **`lower`/`upper`, `startswith`/`endswith`, `isalpha`/`isdigit`, `for` over a string, counting and building with `+=`** | 0 / 90 |
| 5.4 | exercises 4–7, `ord`/`chr` cipher, `split`/`join` (shown), worksheet 8.2, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 13–15) | Covered here |
|---|---|
| Goal 6: `upper`, `lower`, `startswith`, `endswith`, `isalpha`, `isnumeric` | ✅ (`isdigit`, which the Ministry uses; for digit characters it agrees with `isnumeric` — mention once) |
| Goal 7: traverse a string's characters with `for` | ✅ exercises 1–2, three read-the-code slides |
| Goal 8: counting and validation algorithms | ✅ `count_char`, `is_year`, `count_cohen` |
| Goal 9: functions that take a string and return a value | ✅ every task |

### Deliberate exclusions
Loops over `range(len(text))` (5.4, where position matters); `ord`/`chr`, `split`/`join` (5.4); lists; nested loops.
`islower`/`isupper`/`index` (worksheet Q16) are named in the demo and left as a lookup.

---

## 3. Lesson Goal

**A `for` loop visits every character of a string once; a counter that starts before the loop counts what matches, and
`+=` builds a new string one character at a time. Methods such as `startswith` and `isdigit` answer yes/no questions.**

---

## 4. Core Mental Models

```python
def count_char(text, letter):
    count = 0                      # set ONCE, before the loop
    for character in text:         # character is a different letter each time
        if character == letter:
            count += 1
    return count
```

```python
new_text = ""
for character in "We play on the computer":
    if character >= "a" and character <= "e":    # a comparison of two one-letter strings
        new_text = new_text + character
print(new_text)                                   # eaece  (the capital W and the letters after "e" are skipped)
```

- `for character in text:` — the loop variable holds a one-letter string; its name is free (the Ministry writes `ot`).
- `print(letter * 3, end="")` keeps the next print on the same line; a plain `print()` afterwards ends the line.
- `startswith(s, start, end)` and `endswith(s, start, end)` look only between the two places.
- `isdigit()` is `False` for `"1.9.2027"` (the dots are not digits) and for `""`.

---

# 5. Lab Rhythm

Starter: [`Traverse_Starter.py`](Traverse_Starter.py). Reference: [`Traverse_Reference.py`](Traverse_Reference.py).

| Clock | Activity |
|---|---|
| 0–8 | **Demo (5 min) + predict:** `lower()` / `upper()` (7.1 slides 29–31), `startswith`, `endswith`, `isalpha`, `isdigit` (slides 32–36). Predict `"1.9.2027".isdigit()` and `"2027".isdigit()`; `"Piano And Drums".upper()` |
| 8–18 | **Task 1:** predict/run worksheet Q14, then `is_year(text)` |
| 18–26 | **Demo (6 min) — `for` over a string** (8.0 slides 8–10): run the comma-printing code, **predict** the output of the "letters a–e" code and complete the sentence `num of ____ is:` |
| 26–32 | **Warm-up bug:** the counter that restarts |
| 32–42 | **Task 2:** `count_char` — Ministry exercise 1 |
| 42–52 | **Task 3:** `triple_print`, then `triple` — exercise 2 |
| 52–64 | **Task 4:** `count_cohen_a` and `count_cohen_b` — exercise 3 |
| 64–74 | **Task 5:** `keep_a_to_e` — the slide-9 code as a function |
| 74–84 | **If time:** `count_words` — the slide-10 code; why two spaces in a row break it |
| 84–90 | Save and exit check |

---

# 6. Lab

## 0–8 — Demo: methods that answer a question

On `text = "I like to play drums"`: `text.startswith("I like")` is `True`; `text.startswith("play", 10, 17)` is `True`;
`text.startswith("to play", 10, 17)` is `False` (the checked part is `text[10:17]`, which is `"play dr"`;
`"to play"` begins at place 7); `text.endswith("drums")` is `True`. Letter case matters: `"I Like"` is not `"I like"`.

## 8–18 — Task 1: `is_year(text)`

First predict and run the three `startswith` lines from the demo. Then write `is_year(text)`: `True` only when the text is
digits only **and** has four characters. `"2027"` → `True`, `"1.9.2027"` → `False`, `"20x7"` → `False`, `"99"` → `False`.
Ask: what would a program checking an AI answer's *date* need to check beyond this? (The year could be four digits and
still wrong.)

## 18–26 — Demo: `for` over a string

```python
def ex(text):
    for ot in text:
        print(ot, end=",")
```

`ex("sometimes")` prints `s,o,m,e,t,i,m,e,s,`. Predict the other two slides: `"We play on the computer"` →
`eaece`; `"We are learning to program"` prints the sentence and `num of words is: 5` (spaces + 1).

## 26–32 — Warm-up: the counter that restarts

```python
def count_letter(text, letter):
    for character in text:
        count = 0
        if character == letter:
            count += 1
    return count

print(count_letter("sometimes you win sometimes you learn", "e"))   # should be 5
```

Predict, then run: `0`. The `count = 0` line is inside the loop, so the counter restarts for every character; at the
end it is the answer for the *last* character only. Fix: move `count = 0` above the loop. (If the last character happens
to match, the answer is `1` — equally wrong.)

## 32–42 — Task 2: `count_char(text, letter)` (Ministry exercise 1)

Write it again as `count_char`, with a `for` loop and **without** `count()`. The sentence above with `"e"` gives `5`. Check against `text.count("e")`.

## 42–52 — Task 3: `triple_print(text)` and `triple(text)` (Ministry exercise 2)

`triple_print("Learn")` prints `LLLeeeaaarrrnnn` on one line (`end=""`, then a `print()` at the end). Then `triple(text)`
builds the same text with `+=` and **returns** it — which one is easier to test? (The returning one.)

## 52–64 — Task 4: `count_cohen_a(number)`, `count_cohen_b(number)` (Ministry exercise 3)

Each function reads `number` surnames with `input()` and returns how many contain `cohen` (any letter case). Version a: use
`count`. Version b: without `count` — use `in`. **Use invented surnames only; never type the name of a real student.**

## 64–74 — Task 5: `keep_a_to_e(text)`

Return a new string with only the characters between `"a"` and `"e"`. `"We play on the computer"` → `"eaece"`.

## 74–84 — If time: `count_words(text)`

Spaces plus one. `"We are learning to program"` → `5`; `"two  spaces"` → `3` (a double space counts twice) — what real text breaks this, and what would fix it? (Discuss; the fix, `split`, comes in 5.4.)

## 84–90 — Save and exit check

Save As `G8_U5_M3_Traverse_<Name>.py`. Exit check (on paper):

1. `"2027".isdigit()` is…
2. `"Python".startswith("py")` is…
3. After `for ch in "abc": print(ch * 2, end="")`, the screen shows…
4. In a counting loop, where does `count = 0` go?

**Answers:** `True`; `False`; `aabbcc`; before the loop.

### Tool Note – Thonny
Use **Step over** on the loop to see `character` change one letter at a time in the Variables view; this makes the
restarting counter visible.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `count = 0` can sit anywhere | It is set once, before the loop; inside the loop it restarts every turn |
| `startswith("play", 10, 17)` checks the whole text | Only the places from 10 up to (not including) 17 |
| `isdigit()` accepts `"1.9.2027"` | The dots are not digits → `False` |
| `isdigit()` on `""` is `True` | It is `False` for an empty string |
| `print(x, end="")` also removes the final newline later | Add a plain `print()` when the line should end |
| A loop changes the original string | A string never changes; the loop builds a new one |

---

# 8. Assessment Evidence (formative)

- The three read-the-code predictions written before running
- The warm-up explained (why `0`, why moving one line fixes it)
- `is_year`, `count_char`, `triple`, `count_cohen_b`, `keep_a_to_e` passing their test inputs
- Exit check
