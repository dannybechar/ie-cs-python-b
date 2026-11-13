# Unit 5.4 paper lab — answer key and rubric

For [`m4-paper-lab-worksheet-he.md`](m4-paper-lab-worksheet-he.md): **one sheet, two sides, eight separate questions** (four per side), each with its **own string and its own
task**; the questions do not continue each other and can be solved in any order. Side one (questions 1–4) is the lighter side: indices, `count`, `ord`/`chr` and a `while` input
check. Side two (questions 5–8) uses a loop over a string: initials, counting, a shift cipher and a number code. In each row the question is in a box on the right and a large empty
box for the handwritten code is on the left. Students write by hand first, then type the code in Thonny ([`PaperLab4_Starter.py`](PaperLab4_Starter.py)), check, and correct in another colour;
they hand in the **paper** at the end of the 45 minutes (about 20 minutes for side one, 25 for side two; the final question of each side can be left for homework only if the teacher says so).
Every answer below was run from the solution files `PaperLab4_Q1_Solution.py` … `PaperLab4_Q8_Solution.py` (one per question; question 4 needs typed input). **No functions:** the class has not learned `def` yet.
Print with `python tools/problem_sheet_docx.py m4-paper-lab-worksheet-he.md out.docx 4` (four questions per side).
New in 5.4 and needed here: `ord`, `chr`, `range(len(...))` with `text[i - 1]`. `split`/`join` are **not** used on this sheet.

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

**Question 2** — `sentence = "the quick brown fox jumps"`

```python
sentence = "the quick brown fox jumps"

words = sentence.count(" ") + 1
print("Words:", words)
if words > 4:
    print("Long sentence")
else:
    print("Short sentence")
```

Results: `Words: 5`, `Long sentence`.

**Question 3** — `letter = "m"`

```python
letter = "m"

print("Number:", ord(letter))
print("Previous:", chr(ord(letter) - 1))
print("Next:", chr(ord(letter) + 1))
print("Place in alphabet:", ord(letter) - 96)
```

Results: `109`, `l`, `n`, `13`.

**Question 4** — no given string (the user types `ab`, then `pixel7`)

```python
username = input("Username: ")
while len(username) < 4:
    print("Too short, try again")
    username = input("Username: ")
print("Hello", username[0].upper())
print("Length:", len(username))
```

Results: `Too short, try again` once, then `Hello P`, `Length: 6`.

**Question 5** — `band = "red hot chili peppers"`

```python
band = "red hot chili peppers"

initials = band[0].upper()
for i in range(1, len(band)):
    if band[i - 1] == " ":
        initials += band[i].upper()
print("Initials:", initials)
```

Results: `Initials: RHCP`.

**Question 6** — `word = "education"`

```python
word = "education"

vowels = 0
for ch in word:
    if ch in "aeiou":
        vowels += 1
print("Vowels:", vowels)
print("Consonants:", len(word) - vowels)
```

Results: `Vowels: 5`, `Consonants: 4`.

**Question 7** — `text = "hello world"`

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

**Question 8** — `word = "snow"`

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
for question 2 `len(sentence.split(" "))` is **not** expected (`split` is shown only, not tested) but is accepted for full marks; for question 6 `ch == "a" or ch == "e" …` instead of `ch in "aeiou"`;
for question 8 a trailing-dash version that removes the last character (`numbers[:-1]`); `ord(ch) - ord("a") + 1` for `ord(ch) - 96`; for question 5 `title()`-style shortcuts are not available (not taught).
Question 7 has no wrap-around by design (no letter after `u` in the example reaches `z`); a student who adds the `if code > ord("z")` check from the live lesson gets the same answer and full marks.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per question**. A value that is built but never printed: −1 once per question.

| Question | Points | Full marks for |
|---|---:|---|
| 1 | 8 | `city[0]` (2); `city[-1]` or `city[len(city) - 1]` (2); `len(city)` (2); the middle at `len(city) // 2` (2). `len(city) / 2` is a float and raises `TypeError`: max 6 |
| 2 | 8 | `sentence.count(" ")` (3); plus one (2); the comparison with 4 and both messages (3). The number of spaces printed as the words: max 4 |
| 3 | 10 | `ord(letter)` (2); `chr(ord(letter) - 1)` (2); `chr(ord(letter) + 1)` (3); `ord(letter) - 96` (3). `letter + 1` raises `TypeError`: max 1 for that line |
| 4 | 10 | `input` before the loop (2); `while len(username) < 4` (3); `input` again inside the loop with the message (2); `username[0].upper()` (2); the length printed (1). A loop that never asks again (an `if`): max 4 |
| 5 | 14 | `initials` starts with the first letter, in capitals (3); `range(1, len(band))` or a loop that does not read before place 0 (3); the test `band[i - 1] == " "` (4); the letter added with `upper()` and `+=` (2); printed after the loop (2). Using the space itself instead of the letter after it: max 7 |
| 6 | 14 | a counter set to 0 before the loop (2); `for ch in word` (3); the test for a vowel (4); `+= 1` inside the `if` (2); consonants as `len(word) - vowels` or a second counter (2); both printed (1). `word.count("a")` for one vowel only: max 4 |
| 7 | 18 | `coded = ""` before the loop (2); `for ch in text` (3); `ch.isalpha()` or a test against the space (3); `ord(ch) + 2` converted back with `chr` (5); the else adds the character unchanged (3); printed after the loop (2). `coded += ord(ch) + 2` raises `TypeError`: max 8. Shifting the space too (`jgnnq"yqtnf`): max 12 |
| 8 | 18 | `numbers = ""` and `total = 0` before the loop (3); the place `ord(ch) - 96` (4); `str(...)` before adding (3); the dash only between numbers (5); the total added up (2); both printed (1). A dash after every number (`19-14-15-23-`): max 13 |

Total: 8 + 8 + 10 + 10 + 14 + 14 + 18 + 18 = 100.

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of indices, loops over places, `ord`/`chr` and building a new string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `chr`/`ord` as a pair and the counter or the empty string set before the loop |
| below 56 | Needs support before the unit test |

### Marking sheet (one row per student — keep it outside the repository)

| Student | Q1 /8 | Q2 /8 | Q3 /10 | Q4 /10 | Q5 /14 | Q6 /14 | Q7 /18 | Q8 /18 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| Q1 `TypeError ... must be integers, not 'float'` | `len(city) / 2` instead of `//` |
| Q2 prints `4` | forgot the `+ 1` (spaces are one fewer than words) |
| Q3 `TypeError: can only concatenate str` | `letter + 1`: a letter is not a number, needs `ord` |
| Q3 prints `Place in alphabet: 109` | forgot `- 96` |
| Q4 the loop never runs again after a short name | an `if` instead of `while`, or no second `input` inside the loop |
| Q5 the initials are `HCP` | the first word was missed: nothing comes before place 0, so the first letter must be added separately |
| Q5 the initials contain spaces | the space itself was added instead of the next letter |
| Q6 vowels print `0` | the counter is reset inside the loop, or the test `ch == "aeiou"` compares with the whole string |
| Q7 `TypeError` inside the loop | `coded += ord(ch) + 2`: the number was not turned back with `chr` |
| Q7 the space becomes `"` | the space was shifted too: needs `isalpha()` |
| Q8 `TypeError` | `numbers += ord(ch) - 96` without `str(...)` |
| Q8 `19-14-15-23-` | a dash added after every number; ask: "what is different about the first number?" |
