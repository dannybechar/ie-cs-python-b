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
