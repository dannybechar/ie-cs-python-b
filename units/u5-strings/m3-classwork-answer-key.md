# Unit 5.3 classwork — teacher's answer key

For [`m3-classwork-worksheet-he.md`](m3-classwork-worksheet-he.md). Every value below was produced by running
[`Classwork_Reference.py`](Classwork_Reference.py) on Python 3.14. Students' wording will differ; accept any correct reason.

## Part A — read and predict

| Item | Output | Notes |
|---|---|---|
| A1 | `s,o,m,e,t,i,m,e,s,` | one line, comma after every letter including the last (`end=","`); the empty `print()` ends the line |
| A2 | `eaece` | the condition keeps characters from `"a"` to `"e"`. `W` is rejected because a capital letter is *smaller* than `"a"`; `p` is rejected because it is *larger* than `"e"` |
| A3 | `We are learning to program` then `Number of words: 5` | `count` counts the **spaces** (4); a sentence of n words has n − 1 spaces, so words = spaces + 1. It breaks with two spaces in a row |

**A4 trace table**

| Round | ch | `ch == "a"`? | count at the end |
|---|---|---|---|
| 1 | b | False | 0 |
| 2 | a | True | 1 |
| 3 | n | False | 1 |
| 4 | a | True | 2 |
| 5 | n | False | 2 |
| 6 | a | True | 3 |

`a4()` returns `3`.

## Part B — functions

**B1.** Predicted and actual result: `0` (the right answer is `5`). `count = 0` runs at the start of **every** round, so the counter is
wiped; the final round's character is `n` (not `e`), so the last value is `0`. On an empty text the function would crash:
`UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`. Fix: move `count = 0` above the `for`.

```python
def count_char(text, letter):
    count = 0
    for ch in text:
        if ch == letter:
            count += 1
    return count
```

| B2 call | Result |
|---|---|
| `count_char("sometimes you win sometimes you learn", "e")` | 5 |
| `count_char("banana", "a")` | 3 |
| `count_char("banana", "x")` | 0 |
| `count_char("", "a")` | 0 |

**B3.**

```python
def triple(text):
    result = ""
    for ch in text:
        result += ch * 3
    return result
```

`triple("Learn")` → `LLLeeeaaarrrnnn`; `triple("")` → `""`. Why `result = ""` before the loop: it is the starting value;
inside the loop it would be emptied every round and only the last letter, tripled, would remain (`nnn`).

**B4.**

```python
def count_letters(text):
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count

def count_digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    return count
```

`count_letters(ai)` → `27`; `count_digits(ai)` → `5` (2, 0, 2, 4 and 3). `ai.count("5")` counts one specific
character; "any digit" means ten different characters (`0`–`9`), so a loop with `isdigit()` is shorter and clearer.

**B5.**

```python
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
```

`"Hello World"` → 3 · `"rhythm"` → 0 · `"AEIOU"` → 5.

## Part C — homework

```python
def only_digits(text):
    digits = ""
    for ch in text:
        if ch.isdigit():
            digits += ch
    return digits

def hide_digits(text):
    hidden = ""
    for ch in text:
        if ch.isdigit():
            hidden += "*"
        else:
            hidden += ch
    return hidden
```

`only_digits("In 2027 I turn 15")` → `"202715"` · `hide_digits("Room 12 floor 3")` → `"Room ** floor *"`.
Masking: numbers in a prompt may be private (an address, an ID); hide them before the text leaves the computer.

**C3.** On the AI answer: `count_char(answer, ".")` → 3 sentences · `count_char(answer, " ") + 1` → 17 words · `count_digits(answer)` → 2.
*Can check:* length, number of sentences and words, whether it contains digits, a required word. *Cannot judge:* whether
27 days is correct (one orbit takes about 27.3 days — check a reliable source), whether the source is trustworthy, whether it
answers the question. A model's answer is something to check, not the truth.

**C4 (challenge).** `count_each_vowel("Education is the key")` → `a: 1 e: 3 i: 2 o: 1 u: 1` (reference solution uses five counters and `elif`).

## Exit check (paper)

1. Before the loop, once — so it is not reset every round.
2. `aabbcc`.
3. `print(result)` shows the value on the screen and the function returns `None`; `return result` hands the value to the code that called the function so it can be stored or used.

## What to look for while circulating

| Sign | Likely cause |
|---|---|
| `0` where `5` is expected | counter inside the loop, or `return` inside the loop |
| `None` printed | `print` instead of `return` |
| `TypeError` on `result + 3` style code | forgot that `ch * 3` is repeating the letter, not adding |
| One tripled letter only | `result = ""` inside the loop |
| `count_vowels("AEIOU")` is `0` | no `.lower()` |

## Grading rubric (100 points + up to 10 bonus)

**What is graded.** The handed-in paper worksheet: Parts A and B and the exit check (100 points). Part C is homework / early
finishers and earns **up to 10 bonus points; the grade is capped at 100**. The `.py` file is not graded (it is the
students' check tool).

**How to read the sheet.** The work cycle is *write on paper → run → compare → correct in another colour*, so:

- **Grade the final answer**, including corrections in another colour. A wrong *prediction* loses nothing, as long as
  a prediction was written. A missing prediction where the sheet asks for one costs **1 point** (A1–A3, B1).
- **Handwritten code:** grade the logic. A missing colon, bracket or quote is a slip: **−1 once per function**, not per line.
  Accept indentation that is roughly right if it is clear which lines belong to the loop.
- **Accept equivalent code:** `count = count + 1` or `+=`; `for i in range(len(text))` with `text[i]`; a `while` loop with an
  index; `ch == "a" or ch == "e" or …`; `ch in "aeiouAEIOU"` without `.lower()` (B5 — it is correct).
- **`print` instead of `return`** in a function that should return: −2 for that function (once).
- **Blank items** score 0. Partly-filled items get partial credit as in the table.

### Part A — read and predict (30)

| Item | Points | Full marks for |
|---|---:|---|
| A1 | 4 | `s,o,m,e,t,i,m,e,s,` on **one line** (2), a comma after **every** letter including the last (2) |
| A2 | 8 | output `eaece` (4); explanation: a capital letter is *smaller* than `"a"` (2) and `p` is *larger* than `"e"` (2). "Capitals don't count" with no comparison = 1 |
| A3 | 6 | both printed lines, `Number of words: 5` (2); the counter counts **spaces** (2); +1 because words = spaces + 1 (2) |
| A4 | 12 | 2 per round (6 rounds): character, True/False and counter value all right = 2, one cell wrong = 1. A counter written as the value *before* the round all the way down: max 6 |

### Part B — write functions (60)

| Item | Points | Full marks for |
|---|---:|---|
| B1 | 10 | actual result `0` written (2); explanation: `count = 0` runs **every round**, so the counter is reset (4); fix: move `count = 0` above the `for` (4) |
| B2 | 12 | `count = 0` before the loop (3), `for ch in text` (2), `if ch == letter` (2), counter + 1 inside the `if` (2), `return count` **after** the loop (2), the 4 "actual" cells filled (1). Uses `text.count(...)`: max 2 |
| B3 | 12 | `result = ""` before the loop (2), loop over `text` (2), `result += ch * 3` (or `ch + ch + ch`) (3), `return result` after the loop (2); explanation: inside the loop it would be emptied every round / only the last letter would stay (3) |
| B4 | 14 | `count_letters` with `isalpha()` (5) and `count_digits` with `isdigit()` (5) — counter before, test, +1, return; explanation: `count("5")` counts only the character `5`, a digit can be any of `0`–`9` (4) |
| B5 | 12 | counter + loop + return (4), `.lower()` on the text or the character, or both cases listed (4), `ch in "aeiou"` or an equivalent `or` chain (4). Works only for lowercase input: max 8 |

### Exit check (10)

| Item | Points | Full marks for |
|---|---:|---|
| 1 | 3 | before the loop, once (1) — so it is not reset every round (2) |
| 2 | 3 | `aabbcc` (one line, no spaces). `a a b b c c` or one pair per line: 1 |
| 3 | 4 | `print` shows the value on the screen (and the function returns `None`) (2); `return` hands the value back to the calling code to store or use (2) |

### Part C — bonus (up to 10, total capped at 100)

| Item | Points | Full marks for |
|---|---:|---|
| C1 | 2 | `only_digits` builds and returns the digit string |
| C2 | 3 | `hide_digits` with `if`/`else` (2); a reason: numbers may be private (address, ID, phone) and should not leave the computer (1) |
| C3 | 3 | the three results 3 / 17 / 2 (1); one thing the program **can** check (1); it **cannot** tell whether "27 days" is true — check a reliable source (1) |
| C4 | 2 | five counters, `if`/`elif`, the printed line `a: 1 e: 3 i: 2 o: 1 u: 1` |

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of string traversal |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit where the counter / `result = ""` goes and `return` vs `print` before 5.4 |
| below 56 | Needs support before 5.4 (the cipher and the unit checkpoint) |

### Marking sheet (one row per student — keep it outside the repository)

| Student | A1 /4 | A2 /8 | A3 /6 | A4 /12 | B1 /10 | B2 /12 | B3 /12 | B4 /14 | B5 /12 | Exit /10 | Bonus /10 | Total /100 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | | | | |

After grading, record **aggregates only** here (mean, median, range, strongest and weakest items, common errors), as
for the Unit 1 test.
