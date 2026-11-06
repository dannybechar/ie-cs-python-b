# Unit 5.3 paper lab — answer key and rubric

For [`m3-paper-lab-worksheet-he.md`](m3-paper-lab-worksheet-he.md): **one sheet, two sides, two challenging questions with four sub-questions each**
(א–ד, each continues the previous one). On each side the question is in a box on the right and a large empty box for the handwritten code is on
the left. Students write by hand first, then type the code in Thonny ([`PaperLab3_Starter.py`](PaperLab3_Starter.py)), check, and correct in
another colour; they hand in the **paper** at the end of the 45 minutes (about 22 minutes per question).
Every answer below was run from the full solutions [`PaperLab3_Q1_Solution.py`](PaperLab3_Q1_Solution.py) and
[`PaperLab3_Q2_Solution.py`](PaperLab3_Q2_Solution.py). **No functions:** the class has not learned `def` yet.
Print with `python tools/problem_sheet_docx.py m3-paper-lab-worksheet-he.md out.docx 1` (one question per side).
This lab is for the 5.3 live lesson ([`m3-live-problem-he.md`](m3-live-problem-he.md)); the earlier paper-classwork edition of 5.3
has its own worksheet and key ([`m3-classwork-answer-key.md`](m3-classwork-answer-key.md)).

## Answers

**Question 1** — `message = "Was it a car or a cat I saw?"`

```python
# a
print(message.upper())
print(message.lower())
print("Starts with was:", message.lower().startswith("was"))
print("Ends with a question mark:", message.endswith("?"))
# b
letters = 0
digits = 0
others = 0
for ch in message:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        others += 1
print("Letters:", letters)
print("Digits:", digits)
print("Others:", others)
# c
only_letters = ""
for ch in message:
    if ch.isalpha():
        only_letters += ch.lower()
print("Letters only:", only_letters)
# d
backwards = ""
for ch in only_letters:
    backwards = ch + backwards
print("Backwards:", backwards)
if only_letters == backwards:
    print("The message reads the same both ways")
else:
    print("The message does not read the same both ways")
```

Results: `Letters: 19`, `Digits: 0`, `Others: 9` (eight spaces and the `?`), `Letters only: wasitacaroracatisaw`, and the same string backwards, so the
message is printed. With `Meet me at 5 pm!` the letters-only string is `meetmeatpm` and the answer is "does not read the same".
Why `lower()` before `startswith("was")`: the message begins with a capital `W`, and `startswith` is case sensitive.

**Question 2** — `code = "TK-2027-AB"`

```python
# a
print("Starts with TK-:", code.startswith("TK-"))
print("Ends with a letter:", code[-1].isalpha())
print("Length:", len(code))
# b
print("Dashes:", code.count("-"))
first = code.find("-")
print("First dash at:", first)
# c
rest = code[first + 1:]
second = rest.find("-")
year = rest[:second]
print("Year:", year)
if year.isdigit() and len(year) == 4:
    print("Valid year")
else:
    print("Invalid year")
# d
cleaned = ""
digits = 0
for ch in code:
    if ch != "-":
        cleaned += ch.lower()
    if ch.isdigit():
        digits += 1
print("Cleaned:", cleaned)
print("Digits:", digits)
```

Results: `True`, `True`, `10`; `2` dashes, first at place `2`; `Year: 2027`, `Valid year`; `Cleaned: tk2027ab`, `Digits: 4`. With `TK-20x7-AB` the year is
`20x7` and "Invalid year" is printed (`isdigit()` is `False`).

Accept equivalent code: `+=` or `x = x + …`; `code[len(code) - 1]` for `code[-1]`; `code[:3] == "TK-"` instead of `startswith`; a `while` loop with an
index instead of `for ch in`; `if ch.isalpha()` written as `ch >= "a" and ch <= "z"` after `lower()`; for the year, `code[3:7]` is **not** accepted
as a general answer (it works only for this code) but earns half of the slice points; for the reversed string, `backwards + ch` is the wrong order.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per sub-question**. A value that is built but never printed: −1 once per question.
A later sub-question that continues correctly from a wrong earlier one is graded on its own logic.

| Sub-question | Points | Full marks for |
|---|---:|---|
| 1א | 10 | `upper()` and `lower()` printed (4); `lower()` **before** `startswith` (4); `endswith("?")` (2). `startswith("was")` on the original text prints `False`: max 6 |
| 1ב | 14 | three counters set to `0` **before** the loop (3); `for ch in message` (3); `isalpha()` and `isdigit()` as separate branches (4); everything else counted as "others" (2); the three results printed after the loop (2) |
| 1ג | 12 | `only_letters = ""` before the loop (2); only letters added (`isalpha`) (4); `lower()` on the added character (3); `+=` (1); printed after the loop (2) |
| 1ד | 14 | `backwards = ""` before the loop (2); the new character put **in front**: `ch + backwards` (6); the comparison with the letters-only string (3); the message and the print (3). Comparing `message` itself (spaces and capitals) prints "does not read the same": max 8 |
| 2א | 10 | `startswith("TK-")` (4); `code[-1].isalpha()` (4); `len(code)` (2) |
| 2ב | 12 | `code.count("-")` (4); `code.find("-")` (4); both printed (4) |
| 2ג | 14 | the part after the first dash: `code[first + 1:]` (4); the place of the second dash found in that part (4); the year cut with a slice up to that place (3); `isdigit()` **and** `len(...) == 4` (3) |
| 2ד | 14 | `cleaned = ""` and a loop over the characters (3); the dash skipped (4); `lower()` added (3); a digit counter set before the loop and printed after (4) |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of the string methods, `for` over a string, counters and building a new string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit the counter placement (before the loop) and building a string with `+=` |
| below 56 | Needs support before the next lesson |

### Marking sheet (one row per student — keep it outside the repository)

| Student | 1א /10 | 1ב /14 | 1ג /12 | 1ד /14 | 2א /10 | 2ב /12 | 2ג /14 | 2ד /14 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| 1א the `startswith` answer is `False` | `startswith("was")` on `message` (capital `W`): needs `message.lower()` |
| 1ב every count is `0` or `1` | the counters are set to `0` **inside** the loop |
| 1ב the digits count is wrong or missing | `else` used for digits, or `isdigit()` forgotten |
| 1ג the string still has spaces and `?` | the `if ch.isalpha()` test is missing |
| 1ד prints the message "does not read the same" | the comparison is with `message`, or the new character is added at the end (`backwards + ch`) |
| 2א prints `False` for the end | `code[-1]` replaced with `code[0]`; or `isdigit` instead of `isalpha` |
| 2ב the first dash is at `3` | counting from 1 instead of from 0 |
| 2ג `Year: 2027-AB` | the slice has no end, or `find` was not used on the part after the dash |
| 2ג "Invalid year" for `2027` | `len(year) == 4` written as `year == 4`, or `isdigit` called on the whole code |
| 2ד `Cleaned: TK2027AB` | `lower()` forgotten |
| 2ד `Digits` too high | the digit counter is inside the `if ch != "-"` branch of another loop, or counted twice |
