# Unit 5.4 paper lab — answer key and rubric

For [`m4-paper-lab-worksheet-he.md`](m4-paper-lab-worksheet-he.md): **one sheet, two sides, two challenging questions with four sub-questions each**
(א–ד, each continues the previous one). On each side the question is in a box on the right and a large empty box for the handwritten code is on
the left. Students write by hand first, then type the code in Thonny ([`PaperLab4_Starter.py`](PaperLab4_Starter.py)), check, and correct in
another colour; they hand in the **paper** at the end of the 45 minutes (about 22 minutes per question).
Every answer below was run from the full solutions [`PaperLab4_Q1_Solution.py`](PaperLab4_Q1_Solution.py) and
[`PaperLab4_Q2_Solution.py`](PaperLab4_Q2_Solution.py). **No functions:** the class has not learned `def` yet.
Print with `python tools/problem_sheet_docx.py m4-paper-lab-worksheet-he.md out.docx 1` (one question per side).
New in 5.4 and needed here: `ord`, `chr`, `range(len(...))` with `text[i - 1]`. `split`/`join` are **not** used on this sheet.

## Answers

**Question 1** — `title = "moon light sonata"` (17 characters, 3 words)

```python
# a
print("First:", title[0])
print("Last:", title[-1])
print("Length:", len(title))
print("Middle:", title[len(title) // 2])
# b
words = title.count(" ") + 1
print("Words:", words)
# c
initials = title[0].upper()
for i in range(1, len(title)):
    if title[i - 1] == " ":
        initials += title[i].upper()
print("Initials:", initials)
# d
fixed = ""
for i in range(len(title)):
    if i == 0 or title[i - 1] == " ":
        fixed += title[i].upper()
    else:
        fixed += title[i]
print("Fixed title:", fixed)
print("Short name:", initials + str(words))
```

Results: `m`, `a`, `17`, `h` (place 8); `Words: 3`; `Initials: MLS`; `Fixed title: Moon Light Sonata`, `Short name: MLS3`.
Common trap: `initials + words` fails (`str` + `int`); needs `str(words)`.

**Question 2** — `word = "bike"`

```python
# a
print("Number of first letter:", ord(word[0]))
print("Next letter:", chr(ord(word[0]) + 1))
# b
secret = ""
for ch in word:
    secret += chr(ord(ch) + 3)
print("Secret word:", secret)
# c
numbers = ""
for ch in word:
    if numbers != "":
        numbers += "-"
    numbers += str(ord(ch) - 96)
print("Number code:", numbers)
# d
decoded = ""
for ch in secret:
    decoded += chr(ord(ch) - 3)
print("Decoded:", decoded)
if decoded == word:
    print("The code works")
else:
    print("The code is broken")
```

Results: `98`, `c`; `elnh`; `2-9-11-5`; `bike`, "The code works". Every letter of `bike` shifted by 3 stays inside `a`–`z`, so no wrap-around is needed
(the live lesson handles `z`; here a word with `x`, `y` or `z` would give `{`, `|`, `}`).

Accept equivalent code: `+=` or `x = x + …`; `code[len(code) - 1]` for `code[-1]`; `len(title) // 2` or `int(len(title) / 2)`; a `while` loop with an index instead of
`for`/`range`; `title[i - 1] == " "` replaced by `title[i] != " " and title[i - 1] == " "`; for 1ב `len(title.split(" "))` is **not** expected
(`split` is shown only, not tested) but is accepted for full marks; for 2ג a trailing-dash version that removes the last character
(`numbers[:-1]`) is accepted; `ord(ch) - ord("a") + 1` for `ord(ch) - 96`; for the number code a first-iteration check using `i == 0` with `range(len(word))`.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per sub-question**. A value that is built but never printed: −1 once per question.
A later sub-question that continues correctly from a wrong earlier one is graded on its own logic.

| Sub-question | Points | Full marks for |
|---|---:|---|
| 1א | 10 | `title[0]` (2); `title[-1]` or `title[len(title) - 1]` (2); `len(title)` (2); the middle at `len(title) // 2` (4). `len(title) / 2` is a float and raises `TypeError`: max 6 |
| 1ב | 8 | `title.count(" ")` (4); plus one (2); printed (2). The number of spaces printed as the words: max 4 |
| 1ג | 16 | `initials` starts with the first letter, in capitals (4); `range(1, len(title))` or a loop that does not read before place 0 (3); the test `title[i - 1] == " "` (5); the letter added with `upper()` and `+=` (2); printed after the loop (2). Using the space itself instead of the letter after it: max 8 |
| 1ד | 16 | `fixed = ""` before the loop (2); the first place handled (`i == 0`) (3); the letter after a space in capitals (4); every other letter added unchanged (3); `str(words)` in the short name (2); both printed (2). Without the first place the result is `moon Light Sonata`: max 12 |
| 2א | 8 | `ord(word[0])` (4); `chr(ord(word[0]) + 1)` (4). `word[0] + 1` raises `TypeError`: max 1 |
| 2ב | 16 | `secret = ""` before the loop (2); `for ch in word` (3); `ord(ch) + 3` (4); converted back with `chr` (4); `+=` and printed after the loop (3). `secret += ord(ch) + 3` raises `TypeError`: max 8 |
| 2ג | 18 | `numbers = ""` before the loop (2); `ord(ch) - 96` (4); `str(...)` before adding (4); the dash only between numbers (6); printed after the loop (2). A dash after every number (`2-9-11-5-`): max 12 |
| 2ד | 8 | the same loop over `secret` with `- 3` (4); the comparison with `word` (2); both messages printed (2). Decoding with `+ 3` prints `hoqk`: max 2 |

Total: 10 + 8 + 16 + 16 + 8 + 16 + 18 + 8 = 100.

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of indices, loops over places, `ord`/`chr` and building a new string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `chr`/`ord` as a pair and the counter or the empty string set before the loop |
| below 56 | Needs support before the unit test |

### Marking sheet (one row per student — keep it outside the repository)

| Student | 1א /10 | 1ב /8 | 1ג /16 | 1ד /16 | 2א /8 | 2ב /16 | 2ג /18 | 2ד /8 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| 1א `TypeError ... must be integers, not 'float'` | `len(title) / 2` instead of `//` |
| 1ב prints `2` | forgot the `+ 1` (spaces are one fewer than words) |
| 1ג the initials are `LS` | the first word was missed: nothing comes before place 0, so the first letter must be added separately |
| 1ג the initials contain spaces | the space itself was added instead of the next letter |
| 1ד `moon Light Sonata` | the place 0 was not handled |
| 1ד `TypeError` on the last line | `initials + words` without `str(words)` |
| 2א `TypeError: can only concatenate str` | `word[0] + 1`: a letter is not a number, needs `ord` |
| 2ב `TypeError` inside the loop | `secret += ord(ch) + 3`: the number was not turned back with `chr` |
| 2ג `TypeError` | `numbers += ord(ch) - 96` without `str(...)` |
| 2ג `2-9-11-5-` | a dash added after every number; ask: "what is different about the first number?" |
| 2ד prints `hoqk` / "The code is broken" | decoded with `+ 3`, or compared with `secret` |
