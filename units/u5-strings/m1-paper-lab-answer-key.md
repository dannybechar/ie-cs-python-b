# Unit 5.1 paper lab — answer key and rubric

For [`m1-paper-lab-worksheet-he.md`](m1-paper-lab-worksheet-he.md): **one sheet, two sides, six short problems**. In each row the problem
is in a box on the right and an empty box for the handwritten code is next to it. Students write by hand first, then type the code in Thonny
([`PaperLab_Starter.py`](PaperLab_Starter.py)), check, and correct in another colour; they hand in the **paper** at the end of the 45 minutes.
Every answer below was run from [`PaperLab_Reference.py`](PaperLab_Reference.py). **No functions:** the class has not learned `def` yet.
Print the sheet with `python tools/problem_sheet_docx.py m1-paper-lab-worksheet-he.md out.docx 3` (3 problems per side).

## Answers

**Q1 — reverse a word** (`STAR` → `RATS`)

```python
word = "STAR"
result = ""
for i in range(len(word)):
    result = word[i] + result
print(result)
```

**Q2 — count a letter** (`BANANA`, `A` → `3`)

```python
count = 0
for i in range(len(word)):
    if word[i] == letter:
        count += 1
print(count)
```

**Q3 — dashes between the characters** (`STAR` → `S-T-A-R`)

```python
result = ""
for i in range(len(word)):
    if i > 0:
        result = result + "-"
    result = result + word[i]
print(result)
```

**Q4 — identity code** (`FALCON` → `FN-6`)

```python
print(word[0] + word[-1] + "-" + str(len(word)))
```

**Q5 — password** (`abc`, `planet` → `Too short`, then `Welcome`)

```python
password = input("Password: ")
while len(password) < 6:
    print("Too short")
    password = input("Password: ")
print("Welcome")
```

**Q6 — a name in a frame** (`LUNA`)

```python
name = input("Name: ")
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)
```

Accept equivalent code: `+=` or `x = x + …`; a `while` loop with an index; `word[len(word) - 1]` for `word[-1]`; `if i != 0` for `if i > 0`;
a stored length or `str(len(word))` inline.

## Grading rubric (100 points)

**What is graded:** the handed-in paper; the `.py` file is not graded. Grade the **final answer**, including corrections in another colour.
Handwritten code: grade the logic. A missing colon, bracket or quote: **−1 once per question**. The answer must be **printed**
(code that builds the right value but never prints it: −1 once).

| Q | Points | Full marks for |
|---|---:|---|
| 1 | 16 | `result = ""` before the loop (3); a loop over the places (3); the new character put **in front**: `word[i] + result` (7); `print` after the loop (3). `result + word[i]` gives `STAR`: max 9 |
| 2 | 16 | `count = 0` before the loop (3); a loop over the places (3); `word[i] == letter` (5); `count += 1` (3); `print` after the loop (2) |
| 3 | 17 | `result = ""` and a loop (4); the character added (4); a dash only **between** characters: `if i > 0` or an equivalent (6); `print` after the loop (3). A dash after every character (`S-T-A-R-`): max 11 |
| 4 | 17 | `word[0]` (4); `word[-1]` or `word[len(word) - 1]` (4); `"-"` (3); `str(len(word))` (4); joined with `+` and printed (2). Without `str(...)` (a `TypeError`): max 11 |
| 5 | 17 | the first input before the loop (3); `while len(password) < 6` (5); a message and a **new input inside** the loop (5); the final message after the loop (4). An `if` instead of `while`: max 8 |
| 6 | 17 | the input (2); `"*" * (len(name) + 4)` (6); the middle line with the spaces (5); the border printed twice (4) |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of strings, indices and loops over a string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit building a string in a loop and `str(...)` |
| below 56 | Needs support before the next lesson |

### Marking sheet (one row per student — keep it outside the repository)

| Student | Q1 /16 | Q2 /16 | Q3 /17 | Q4 /17 | Q5 /17 | Q6 /17 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| Q1 prints `STAR` | `result + word[i]` instead of `word[i] + result` |
| Q2 count always `0` | comparing `letter` with `word` instead of `word[i]` |
| Q3 `-S-T-A-R` or `S-T-A-R-` | the `if i > 0` check is missing, or the dash comes after the character |
| Q4 `TypeError` | `"-" + len(word)`: a number needs `str(...)` |
| Q5 asks only once | `if` instead of `while` |
| Q5 never ends | the new `input` is missing inside the loop |
| Q6 `* LUNA*` | a missing space in `"* " + name + " *"` |
