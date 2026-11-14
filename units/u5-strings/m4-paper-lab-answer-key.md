# Lessons 8.2–8.7 paper lab — answer key and rubric

For [`m4-paper-lab-worksheet-he.md`](m4-paper-lab-worksheet-he.md): **one sheet, two sides, five separate questions**, each with its **own string and its own task**; the questions do not
continue each other. Side one has questions 1 (indices) and 2 (a `while` input check); side two has 3 (`count` and initials with a loop), 4 (a shift cipher with `ord`/`chr`) and 5 (a number code with dashes and a total). The font is enlarged (1.25 × the usual size).
**Every question has a "כלים לשימוש" box listing the methods and expressions to use** (not the solution): Q1 `len`, `[0]`, `[-1]`, `[len // 2]`; Q2 `input`, `while len(...) < 4`, `[0].upper()`; Q3 `count(" ")`, `range(1, len)`, `[i - 1] == " "`, `.upper()`; Q4 `for ch in`, `isalpha`, `ord`, `chr`, `+=`; Q5 `for ch in`, `ord(ch) - 96`, `str`, `!= ""`, `+=`. In each row the question is in a box on the right and a large empty
box for the handwritten code is on the left. Students write by hand first, then type the code in Thonny ([`PaperLab4_Starter.py`](PaperLab4_Starter.py)), check, and correct in another colour;
they hand in the **paper** at the end of the 45 minutes (about 9 minutes per question).
Every answer below was run from the solution files `PaperLab4_Q1_Solution.py` … `PaperLab4_Q5_Solution.py` (one per question; question 2 needs typed input). **No functions:** the class has not learned `def` yet.
Print with `python tools/problem_sheet_docx.py m4-paper-lab-worksheet-he.md out.docx 2,3 1.25 8.0` (two questions on the first side, three on the second; font ×1.25; writing box 8 cm).
New in Lessons 8.2–8.7 and needed here: `ord`, `chr`, `range(len(...))` with `text[i - 1]`. `split`/`join` are **not** used on this sheet.

## Answers

**Question 1** — `city = "jerusalem"`

```python
city = "jerusalem"

print("First:", city[0])
print("Last:", city[-1])
print("Length:", len(city))
print("Middle:", city[len(city) // 2])
```

Results: `j`, `m`, `9`, `s` (place 4).

**Question 2** — no given string (the user types `ab`, then `pixel7`)

```python
username = input("Username: ")
while len(username) < 4:
    print("Too short, try again")
    username = input("Username: ")
print("Hello", username[0].upper())
print("Length:", len(username))
```

Results: `Too short, try again` once, then `Hello P`, `Length: 6`.

**Question 3** — `band = "red hot chili peppers"`

```python
band = "red hot chili peppers"

words = band.count(" ") + 1
initials = band[0].upper()
for i in range(1, len(band)):
    if band[i - 1] == " ":
        initials += band[i].upper()
print("Words:", words)
print("Initials:", initials)
```

Results: `Words: 4`, `Initials: RHCP`.

**Question 4** — `text = "hello world"`

```python
text = "hello world"

coded = ""
for ch in text:
    if ch.isalpha():
        coded += chr(ord(ch) + 2)
    else:
        coded += ch
print("Coded:", coded)
```

Results: `Coded: jgnnq yqtnf`.

**Question 5** — `word = "snow"`

```python
word = "snow"

numbers = ""
total = 0
for ch in word:
    place = ord(ch) - 96
    if numbers != "":
        numbers += "-"
    numbers += str(place)
    total += place
print("Number code:", numbers)
print("Total:", total)
```

Results: `Number code: 19-14-15-23`, `Total: 71`.

Accept equivalent code: `+=` or `x = x + …`; `city[len(city) - 1]` for `city[-1]`; `len(city) // 2` or `int(len(city) / 2)`; a `while` loop with an index instead of `for`/`range`;
for question 3 `len(band.split(" "))` is **not** expected (`split` is shown only, not tested) but is accepted for full marks; for question 5 a trailing-dash version that removes the last character
(`numbers[:-1]`), and `ord(ch) - ord("a") + 1` for `ord(ch) - 96`. Question 4 has no wrap-around by design (no letter of the example reaches `z`); a student who adds the
`if code > ord("z")` check from the live lesson gets the same answer and full marks.

## Challenge for early finishers (projected, solved in Thonny)

[`m4-challenge-he.pdf`](m4-challenge-he.pdf) — one slide, extra-large fonts. **The mirror cipher:** `a`↔`z`, `b`↔`y` …; capitals stay capitals, spaces and signs stay; apply it twice and check that the original comes back.
Solution: [`PaperLab4_Challenge_Solution.py`](PaperLab4_Challenge_Solution.py) (`Svool Dliow` / `Back: Hello World` / `Same: yes`). The key idea is that every pair has the same sum of numbers
(`ord("a") + ord("z")`), so the mirror of `ch` is that sum minus `ord(ch)`; the capitals use `ord("A") + ord("Z")`. Not graded; it may earn a bonus at the teacher's discretion (the rubric is capped at 100).

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per question**. A value that is built but never printed: −1 once per question.

| Question | Points | Full marks for |
|---|---:|---|
| 1 | 14 | `city[0]` (3); `city[-1]` or `city[len(city) - 1]` (3); `len(city)` (3); the middle at `len(city) // 2` (5). `len(city) / 2` is a float and raises `TypeError`: max 9 |
| 2 | 14 | `input` before the loop (3); `while len(username) < 4` (4); `input` again inside the loop with the message (3); `username[0].upper()` (3); the length printed (1). A loop that never asks again (an `if`): max 6 |
| 3 | 22 | words: `band.count(" ")` plus one (6); `initials` starts with the first letter, in capitals (3); `range(1, len(band))` or a loop that does not read before place 0 (3); the test `band[i - 1] == " "` (5); the letter added with `upper()` and `+=` (3); both printed after the loop (2). The number of spaces printed as the words: max 3 for the first part. Using the space itself instead of the letter after it: max 12 |
| 4 | 25 | `coded = ""` before the loop (3); `for ch in text` (4); `ch.isalpha()` or a test against the space (4); `ord(ch) + 2` converted back with `chr` (7); the else adds the character unchanged (4); printed after the loop (3). `coded += ord(ch) + 2` raises `TypeError`: max 11. Shifting the space too (`jgnnq"yqtnf`): max 17 |
| 5 | 25 | `numbers = ""` and `total = 0` before the loop (4); the place `ord(ch) - 96` (5); `str(...)` before adding (4); the dash only between numbers (7); the total added up (3); both printed (2). A dash after every number (`19-14-15-23-`): max 18 |

Total: 14 + 14 + 22 + 25 + 25 = 100.

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of indices, loops over places, `ord`/`chr` and building a new string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `chr`/`ord` as a pair and the counter or the empty string set before the loop |
| below 56 | Needs support before the unit test |

### Marking sheet (one row per student — keep it outside the repository)

| Student | Q1 /14 | Q2 /14 | Q3 /22 | Q4 /25 | Q5 /25 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|
| | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| Q1 `TypeError ... must be integers, not 'float'` | `len(city) / 2` instead of `//` |
| Q2 the loop never runs again after a short name | an `if` instead of `while`, or no second `input` inside the loop |
| Q3 prints `Words: 3` | forgot the `+ 1` (spaces are one fewer than words) |
| Q3 the initials are `HCP` | the first word was missed: nothing comes before place 0, so the first letter must be added separately |
| Q3 the initials contain spaces | the space itself was added instead of the next letter |
| Q4 `TypeError` inside the loop | `coded += ord(ch) + 2`: the number was not turned back with `chr` |
| Q4 the space becomes `"` | the space was shifted too: needs `isalpha()` |
| Q5 `TypeError` | `numbers += ord(ch) - 96` without `str(...)` |
| Q5 `19-14-15-23-` | a dash added after every number; ask: "what is different about the first number?" |
