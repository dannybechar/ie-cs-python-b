# Unit 5.1 paper lab — answer key and rubric

For [`m1-paper-lab-worksheet-he.md`](m1-paper-lab-worksheet-he.md) (45 minutes, handwritten, handed in at the end of the lab).
Every value below was produced by running [`PaperLab_Reference.py`](PaperLab_Reference.py). **No functions:** the class has not
learned `def` yet; every answer is plain code. The same cycle as the 5.3 and 5.4 worksheets: paper first, then Thonny
([`PaperLab_Starter.py`](PaperLab_Starter.py) has Questions 1–2 ready to run), corrections in another colour, the **paper** is graded.

Timing: Q1 6 · Q2 6 · Q3 10 · Q4 10 · Q5 10 · exit check 3 = 45 minutes. The "if time" block is a bonus.

## Answers

**Q1.** Prints:

```text
0 S
1 TS
2 ATS
3 RATS
RATS
```

The program builds the word **backwards**: each new letter is put in front of what was built so far.

**Q2.** Prints `0 S`, `1 T`, `2 A`, `3 R`, then stops with `IndexError: string index out of range`. For `i = 4` the program asks for
`word[4]`, but the last place of a 4-letter word is 3 (`len(word) - 1`); `range(len(word) + 1)` goes one too far.
Fix: `for i in range(len(word)):`.

**Q3.**

```python
callsign = input("Callsign: ")
while len(callsign) < 4:
    print("Too short, try again")
    callsign = input("Callsign: ")
first = callsign[0]
last = callsign[-1]
print("First:", first)
print("Last:", last)
print("Length:", len(callsign))
print("Code: " + first + last + "-" + str(len(callsign)))
```

`ox`, `FALCON` → asks twice; `First: F`, `Last: N`, `Length: 6`, `Code: FN-6`. `callsign[-1]` or `callsign[len(callsign) - 1]` are both fine.

**Q4.**

```python
message = input("Message: ")
letter = input("Letter: ")
stars = ""
count = 0
for i in range(len(message)):
    if i > 0:
        stars = stars + "*"
    stars = stars + message[i]
    if message[i] == letter:
        count += 1
print(stars)
print(letter, "appears", count, "times")
```

`BANANA`, `A` → `B*A*N*A*N*A` and `A appears 3 times`. The `*` is not added before the first character. A lower-case `a` is a different
character: it counts `0`.

**Q5.**

```python
name = input("Name: ")
age = int(input("Age: "))
while age < 1 or age > 120:
    print("Age must be 1 to 120")
    age = int(input("Age: "))
border = "*" * (len(name) + 4)
print(border)
print("* " + name + " *")
print(border)
print("Seat: " + name[0] + str(age))
print("Next year:", age + 1)
```

`LUNA`, `200`, `12` → the message once, then an 8-star frame, `* LUNA *`, `Seat: L12`, `Next year: 13`.

**Exit check** (`text = "PLANET"`): `P` · `E` · `6` · `IndexError: string index out of range` (the last place is `len(text) - 1`, which is `T`).

**If time.** Build the reversed message (`backwards = message[i] + backwards` in the loop) and `if message == backwards:` print
`Same both ways` → `ANNA` yes, `BANANA` no.

## Grading rubric (100 points + 5 bonus, capped at 100)

**What is graded:** the handed-in paper. The `.py` file is not graded. Same reading rules as the 5.3 and 5.4 worksheets:

- **Grade the final answer**, including corrections in another colour. A wrong prediction (Q1, Q2) loses nothing if one was written; a missing prediction costs 1 point.
- **Handwritten code:** grade the logic. A missing colon, bracket or quote: **−1 once per question**. Indentation that is roughly right is fine if it is clear which lines belong to the loop or the `if`.
- **Accept equivalent code:** `+=` or `x = x + …`; `while` with an index instead of `for`; `str(len(x))` or a stored length; `if i != 0` for `if i > 0`; a `*` added after each character and the last one removed is **not** accepted unless it works for the whole message.
- **The answer must be printed:** code that builds the right value but never prints it: −1 for that question (once).

| Item | Points | Full marks for |
|---|---:|---|
| Q1 | 12 | the four lines plus the last `RATS` written correctly (8); "builds the word backwards" (4) |
| Q2 | 14 | prediction (3); the error and the value `i = 4` (4); why: the last place is `len(word) - 1`, the loop goes one too far (4); `range(len(word))` (3) |
| Q3 | 22 | input before the loop (2); `while len(...) < 4` with a message and a new input inside (6); `[0]` and `[-1]` (4); length printed (2); the code joined with `+`, a dash and `str(...)` (6); prints (2). Without `str(...)`: max 16 |
| Q4 | 22 | loop over the places (3); `stars = ""` and `count = 0` before the loop (3); no `*` before the first character (4); builds `stars` (3); `if message[i] == letter` and `count += 1` (6); both results printed (3) |
| Q5 | 22 | age check with `while` and `or` (6) and a new input inside (2); `int(...)` on the age (2); frame width `len(name) + 4` (3); the three frame lines (3); the seat with `str(age)` (3); next year `age + 1` (3) |
| Exit check | 8 | 2 points per value; for the fourth, the error name or "error, out of range" |
| If time (bonus) | 5 | a reversed string built in a loop (3); the comparison and the print (2) |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of strings, indices and loops over a string |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit places (`range(len(text))`), building a string, and `str(...)` |
| below 56 | Needs support before the next lesson |

### Marking sheet (one row per student — keep it outside the repository)

| Student | Q1 /12 | Q2 /14 | Q3 /22 | Q4 /22 | Q5 /22 | Exit /8 | Bonus /5 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors).

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| Q1 prints `STAR` or `RATS` on each line | a different order of `word[i] + result`; trace with the table |
| Q2 "the loop is fine" | not seeing that `range(len(word) + 1)` reaches `4` |
| Q3 `TypeError` on the code line | `"-" + len(callsign)`: a number must go through `str(...)` |
| Q3 asks only once | `if` instead of `while` |
| Q4 `*` at the start (`*B*A…`) | the `if i > 0` check is missing |
| Q4 count always `0` | comparing `letter` with `message` instead of `message[i]` |
| Q5 `* LUNA*` | a missing space in `"* " + name + " *"` |
| Q5 `ValueError` | `int(...)` on text that is not digits — not part of this lab, tell them to type digits |
