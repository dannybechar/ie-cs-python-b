# Unit 5.1 paper lab — answer key and rubric

For [`m1-paper-lab-worksheet-he.md`](m1-paper-lab-worksheet-he.md): **one sheet, two sides, two challenging questions with four sub-questions each**
(א–ד, each continues the previous one). On each side the question is in a box on the right and a large empty box for the handwritten code is on
the left. Students write by hand first, then type the code in Thonny ([`PaperLab_Starter.py`](PaperLab_Starter.py)), check, and correct in
another colour; they hand in the **paper** at the end of the 45 minutes (about 22 minutes per question).
Every answer below was run from [`PaperLab_Reference.py`](PaperLab_Reference.py). **No functions:** the class has not learned `def` yet.
Print with `python tools/problem_sheet_docx.py m1-paper-lab-worksheet-he.md out.docx 1` (one question per side).

## Answers

**Question 1** — `word = "BANANA"`

```python
# a
print("Length:", len(word))
print("First:", word[0])
print("Last:", word[-1])
# b
for i in range(len(word)):
    print(i, i - len(word), word[i])
# c
reversed_word = ""
for i in range(len(word)):
    reversed_word = word[i] + reversed_word
print("Reversed:", reversed_word)
if word == reversed_word:
    print("The word reads the same both ways")
# d
letter = input("Letter: ")
count = 0
for i in range(len(word)):
    if word[i] == letter:
        count += 1
if count > 0:
    print(letter, "appears", count, "times")
else:
    print(letter, "does not appear")
```

`BANANA` → `Reversed: ANANAB` (no same-both-ways message); `A` → 3 times; `Z` → does not appear. With `ANNA` the message is printed.

**Question 2**

```python
# a
username = input("Username: ")
while len(username) < 4 or len(username) > 10:
    print("Must be 4 to 10 characters")
    username = input("Username: ")
# b
print("Masked: " + username[0] + "*" * (len(username) - 1))
# c
age = int(input("Age: "))
while age < 1 or age > 120:
    print("Age must be 1 to 120")
    age = int(input("Age: "))
print("Next year you will be", age + 1)
# d
line1 = username
line2 = "Age: " + str(age)
width = len(line1)
if len(line2) > width:
    width = len(line2)
border = "*" * (width + 4)
gap1 = " " * (width - len(line1))
gap2 = " " * (width - len(line2))
print(border)
print("* " + line1 + gap1 + " *")
print("* " + line2 + gap2 + " *")
print(border)
```

`ab`, `falcon`, `200`, `12` → `Masked: f*****`, `Next year you will be 13`, and an 11-star frame with `* falcon  *` and `* Age: 12 *`.

Accept equivalent code: `+=` or `x = x + …`; a `while` loop with an index; `word[len(word) - 1]` for `word[-1]`; a flag or `if` / `else` for the
"does not appear" message; for the frame, any way that pads the shorter line with spaces.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per sub-question**. A value that is built but never printed: −1 once per question.
A later sub-question that continues correctly from a wrong earlier one is graded on its own logic.

| Sub-question | Points | Full marks for |
|---|---:|---|
| 1א | 8 | `len(word)` (3), `word[0]` (2), `word[-1]` or `word[len(word) - 1]` (3) |
| 1ב | 12 | a loop over the places (4); the place `i` (2); the place from the end `i - len(word)` (4); the character `word[i]` (2) |
| 1ג | 14 | `reversed_word = ""` before the loop (3); the character put **in front**: `word[i] + reversed_word` (6); printed (2); the comparison with the word and the message (3). The wrong order (`reversed_word + word[i]`) gives the same word: max 8 |
| 1ד | 16 | the input (2); `count = 0` before the loop (3); `word[i] == letter` (4); `count += 1` (3); a different message when the count is 0 (4) |
| 2א | 12 | the first input before the loop (2); `while` with both limits joined by `or` (6); a message and a **new input inside** the loop (4). An `if` instead of `while`: max 5 |
| 2ב | 8 | `username[0]` (3); `"*" * (len(username) - 1)` (4); joined and printed (1) |
| 2ג | 14 | `int(input(...))` (3); a `while` with `age < 1 or age > 120` (5); a new input inside (3); `age + 1` printed (3). `and` instead of `or`: max 6 |
| 2ד | 16 | the second line built with `"Age: " + str(age)` (4); the width from the longer line (4); the border `width + 4` printed twice (3); the shorter line padded with spaces (5). Without `str(...)` (a `TypeError`): max 12 |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of strings, indices, loops over a string and input checks |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit building a string in a loop and `while` with two limits |
| below 56 | Needs support before the next lesson |

### Marking sheet (one row per student — keep it outside the repository)

| Student | 1א /8 | 1ב /12 | 1ג /14 | 1ד /16 | 2א /12 | 2ב /8 | 2ג /14 | 2ד /16 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| 1ב the second number is also `i` | the place from the end is `i - len(word)`, not `-i` |
| 1ג prints `BANANA` | `reversed_word + word[i]` instead of `word[i] + reversed_word` |
| 1ד count always `0` | comparing `letter` with `word` instead of `word[i]` |
| 1ד prints "does not appear" for every letter | the message is inside the loop |
| 2א asks only once | `if` instead of `while`; or `and` instead of `or` (never true) |
| 2א never ends | the new `input` is missing inside the loop |
| 2ג `TypeError` / `ValueError` | `age + 1` on text: `int(...)` is missing |
| 2ד `TypeError` | `"Age: " + age`: a number needs `str(...)` |
| 2ד the right border does not line up | the shorter line is not padded to the width |
