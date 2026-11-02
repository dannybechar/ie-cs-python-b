# Unit 5.4 countdown edition — worksheet answer key and rubric

For [`m4-countdown-worksheet-he.md`](m4-countdown-worksheet-he.md). Every value below was produced by running
[`Worksheet_Reference.py`](Worksheet_Reference.py). Students' wording will differ; accept any correct reason.
The four countdown cases of the first half are ungraded; their solutions are in
[`Countdown_Reference.py`](Countdown_Reference.py) and on the reveal screen of the countdown page.

## Answers

**Q1 — the bug.** Prints `19` (the length of the text) instead of `8`. Python reads the condition as
`(character == "a") or "e" or …`; `"e"` on its own is a non-empty string, which counts as true, so **every** character
is counted. Fixed condition: `if character in "aeiou":` (or five full comparisons, `character == "a" or character == "e" or …`).

**Q2.**

```python
def middle(word):
    half = len(word) // 2
    if len(word) % 2 == 1:
        return word[half]
    return word[half - 1:half + 1]
```

`"robot"` → `b` · `"python"` → `th` · `"a"` → `a`.

**Q3.**

```python
def edges(text):
    if len(text) < 4:
        return "****"
    return text[:4] + text[-4:]
```

`"I like to play drums"` → `I lirums` · `"abc"` → `****` · `"abcd"` → `abcdabcd`. Why 4 characters and not 3 letters:
**a space is a character too** (`"I li"` is I, space, l, i).

**Q4.**

```python
def last_letters(text):
    result = ""
    for index in range(len(text)):
        if index == len(text) - 1 or text[index + 1] == " ":
            result += text[index]
    return result
```

`"I like to play drums"` → `Ieoys` · `"Hello"` → `o`. Why the end is checked first: on the last character there is no next
character, so `text[index + 1]` crashes with `IndexError: string index out of range`; `or` stops as soon as the first
part is true, so checking the end first protects the second part.

**Q5.**

```python
def alternate_case(text):
    result = ""
    upper_next = True
    for character in text:
        if character == " ":
            result += " "
        elif upper_next:
            result += character.upper()
            upper_next = False
        else:
            result += character.lower()
            upper_next = True
    return result
```

`"trust yourself"` → `TrUsT yOuRsElF` · `"ai"` → `Ai`. Why index parity is wrong: the space has an index too, so it uses up a
turn; after it the pattern flips and the second word starts with a capital (`TrUsT YoUrSeLf`). Accept any variable that
remembers whose turn it is (`True`/`False`, a counter of letters, `"upper"`/`"lower"`).

**If time.** `count_word_it("it is a little bit with it")` → `2` (reference: build the current word letter by letter, compare
at each space). `text.count("it")` counts the characters `it` anywhere, also inside `little`, `bit`, `with` → `5`.

**Exit check.** 1: `d`. 2: `3` — `count` finds the characters `is` inside `this` and `his` too. 3: `index += 1` (moving
to the next place); without it the condition never changes and the loop never ends.

## Grading rubric (100 points + up to 5 bonus, capped at 100)

**What is graded:** the handed-in paper worksheet. The `.py` file is not graded. Same reading rules as the 5.3 classwork:

- **Grade the final answer**, including corrections in another colour. A wrong prediction (Q1) loses nothing if one was written;
  a missing prediction costs 1 point.
- **Handwritten code:** grade the logic. A missing colon, bracket or quote: **−1 once per function**. Indentation that is
  roughly right is fine if it is clear which lines belong to the loop or the `if`.
- **Accept equivalent code:** `+=` or `x = x + …`; a `while` loop with an index instead of `for`; `text[len(text) - 4:]`
  instead of `text[-4:]`; in Q4, a `previous`/`next` variable or adding a space at the end of the text.
- **`print` instead of `return`:** −2 for that function (once).

| Item | Points | Full marks for |
|---|---:|---|
| Q1 | 15 | actual result `19` written (3); explanation: `"e"` alone counts as true, so every character is counted (6); a fixed condition that works (6). "The `or` is wrong" with no reason: 2 of the 6 |
| Q2 | 15 | `len(word) // 2` for the middle place (4); odd/even test with `% 2` (4); one letter for odd (3); the **two** middle letters for even, the right slice (4) |
| Q3 | 20 | the `< 4` test before slicing (4), returns `"****"` (2), `text[:4]` (4), `text[-4:]` (4), joined with `+` and returned (2); reason: a space is a character (4) |
| Q4 | 20 | loop over the places (3), `result = ""` before the loop (2), the "last in the word" test with both parts (6), `+=` the character (3), `return` after the loop (2); reason: no next character at the end / `IndexError` (4). Works for every word except the last: max 13 |
| Q5 | 20 | `result = ""` and a loop (3); a space is added unchanged (3); a variable that remembers whose turn it is, flipped only on letters (8); `upper()` / `lower()` (3); reason: the space takes a turn / index counts spaces (3). Index parity used in the code: max 11 |
| Exit check | 10 | 1: `d` (3) · 2: `3` with the reason (3) · 3: `index += 1` and "the loop never ends" (4) |
| If time (bonus) | 5 | a working `count_word_it` (3); why `count("it")` is wrong (2) |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of string algorithms |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit loops over places (`range(len(text))`) and "remember a state" variables |
| below 56 | Needs support before Unit 6 |

### Marking sheet (one row per student — keep it outside the repository)

| Student | Q1 /15 | Q2 /15 | Q3 /20 | Q4 /20 | Q5 /20 | Exit /10 | Bonus /5 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| Q1 fixed by adding brackets: `(character == "a" or "e")` | still always true — brackets don't change it |
| `middle("python")` → `h` | only the odd case written; or `word[half:half + 2]` (gives `ho`) |
| `edges("abc")` → `abcabc` | the `< 4` test is missing (slices never crash) |
| `IndexError` in Q4 | `text[index + 1]` tested before the end check |
| `TrUsT YoUrSeLf` | index parity instead of a turn variable |
