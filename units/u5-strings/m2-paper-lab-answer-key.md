# Unit 5.2 paper lab — answer key and rubric

For [`m2-paper-lab-worksheet-he.md`](m2-paper-lab-worksheet-he.md): **one sheet, two sides, two challenging questions with four sub-questions each**
(א–ד, each continues the previous one). On each side the question is in a box on the right and a large empty box for the handwritten code is on
the left. Students write by hand first, then type the code in Thonny ([`PaperLab2_Starter.py`](PaperLab2_Starter.py)), check, and correct in
another colour; they hand in the **paper** at the end of the 45 minutes (about 22 minutes per question).
Every answer below was run from the full solutions [`PaperLab2_Q1_Solution.py`](PaperLab2_Q1_Solution.py) and
[`PaperLab2_Q2_Solution.py`](PaperLab2_Q2_Solution.py). **No functions:** the class has not learned `def` yet. New tools of this lab: slicing,
`find` (also with a start place), `count`, `replace` (also with a count, and with `""`); loops are only the 5.1 kind
(`while`, `for i in range(len(text))`).
Print with `python tools/problem_sheet_docx.py m2-paper-lab-worksheet-he.md out.docx 1` (one question per side).

## Answers

**Question 1** — `file = "holiday_photo_2026.jpg"`

```python
# a
dot = file.find(".")
print("Name:", file[:dot])
print("Extension:", file[dot + 1:])
# b
count = file.count("_")
print("Underscores:", count)
print("First at:", file.find("_"))
# c
print(file.replace("_", " "))
print(file.replace("_", "-", 1))
# d
if count == 0:
    print("No underscore")
else:
    for i in range(len(file)):
        if file[i] == "_":
            print("Underscore at", i)
```

Output: `Name: holiday_photo_2026`, `Extension: jpg`, `Underscores: 2`, `First at: 7`, `holiday photo 2026.jpg`, `holiday-photo_2026.jpg`,
`Underscore at 7`, `Underscore at 13`. With a name that has no `_` the program prints `No underscore`.

**Question 2**

```python
# a
code = input("Code: ")
while code.count("-") != 2:
    print("Need exactly 2 dashes")
    code = input("Code: ")
# b
first = code.find("-")
second = code.find("-", first + 1)
part1 = code[:first]
part2 = code[first + 1:second]
part3 = code[second + 1:]
print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)
# c
print(part3 + "/" + part2 + "/" + part1)
print(code.replace("-", ""))
# d
print(part1 + "-" + "*" * len(part2) + "-" + part3)
print("Mirror:", code[::-1])
```

`7340-ABCD`, then `7340-ABCD-2026` → the message once, then `Part 1: 7340`, `Part 2: ABCD`, `Part 3: 2026`, `2026/ABCD/7340`, `7340ABCD2026`,
`7340-****-2026`, `Mirror: 6202-DCBA-0437`.

Accept equivalent code: the place of the dot kept in any variable; `file[dot + 1:]` or `file[dot + 1:len(file)]`; a `while` loop with a place
counter instead of `for`; in 1ד `if "_" in file` / `else` instead of testing the count; in 2ב the second dash found by
`code[first + 1:].find("-") + first + 1` instead of the start place; in 2ד a loop that builds the stars instead of `"*" * len(part2)`.
`split`, `join` and `rfind` are not taught in this lesson — do not expect them.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per sub-question**. A value that is built but never printed: −1 once per question.
A later sub-question that continues correctly from a wrong earlier one is graded on its own logic.

| Sub-question | Points | Full marks for |
|---|---:|---|
| 1א | 12 | `file.find(".")` stored (4); `file[:dot]` (4); `file[dot + 1:]` (4). `file[dot:]` (the extension with the dot): max 10 |
| 1ב | 10 | `file.count("_")` (5); `file.find("_")` (5) |
| 1ג | 14 | `file.replace("_", " ")` printed (6); `file.replace("_", "-", 1)` with the count `1` (8). `replace` without printing or without keeping the result: 0 for that line |
| 1ד | 14 | the test of the count against 0 and a message (4); a loop over the places `range(len(file))` (4); `file[i] == "_"` (3); printing the place `i` (3) |
| 2א | 10 | the first input before the loop (2); `while code.count("-") != 2` (4); a message and a **new input inside** the loop (4). An `if` instead of `while`: max 4 |
| 2ב | 14 | the first dash `code.find("-")` (3); the second dash searched with a start place `first + 1` (5); `code[:first]` (2); `code[first + 1:second]` (2); `code[second + 1:]` (2). A second `find("-")` without a start returns the first place again: max 6 |
| 2ג | 12 | the parts joined in reverse order with `"/"` between them (6); `code.replace("-", "")` printed (6) |
| 2ד | 14 | `"*" * len(part2)` (5); the three parts and the dashes joined with `+` (5); `code[::-1]` printed with the label (4) |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of slicing, `find`, `count` and `replace` |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit the `end` place of a slice (not included) and keeping the result of `replace` |
| below 56 | Needs support before the next lesson |

### Marking sheet (one row per student — keep it outside the repository)

| Student | 1א /12 | 1ב /10 | 1ג /14 | 1ד /14 | 2א /10 | 2ב /14 | 2ג /12 | 2ד /14 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| 1א the extension is `.jpg` | `file[dot:]` instead of `file[dot + 1:]` |
| 1א the name still ends with `.` | `file[:dot + 1]`: the `end` place is not included, so `file[:dot]` is right |
| 1ג prints the original file name | `file.replace(...)` without `print` or without `file = ...`: replace gives back a new string |
| 1ג every underscore is replaced in the second line | the count `1` is missing |
| 1ד prints the places from 0 to the end | the `if file[i] == "_"` test is missing inside the loop |
| 2א asks only once | `if` instead of `while` |
| 2ב `Part 2` is empty or wrong | the second `find` has no start place, so it finds the first dash again |
| 2ב `Part 2: -ABCD` | `code[first:second]` — the dash is included; start at `first + 1` |
| 2ג prints `7340/ABCD/2026` | the parts joined in the original order instead of reversed |
| 2ג the dashes are still there | `code.replace("-", "")` was not printed or kept, or an `" "` was typed instead of `""` |
| 2ד the stars are 3 or 5 instead of 4 | a typed number instead of `len(part2)` (accept it if the answer is right for this code only) |
