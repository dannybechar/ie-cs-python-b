# Strings quiz Q1 (lessons 7.1–8.7) — answer key

**Status:** Built, awaiting teacher approval 🔶
**Given:** Sun 29 Nov 2026 (P2), 25 minutes, paper, no computer. Student sheet: [`strings-quiz-he.md`](../assessment/strings-quiz-he.md). Practice version for the students (Mashov): [`strings-quiz-mock-he.md`](../assessment/strings-quiz-mock-he.md) with [answers](L04-string-algorithms-and-cipher-quiz-mock-answers.md).
**Solutions (run, Python 3.14):** [`StringsQuiz_Solution.py`](solutions/StringsQuiz_Solution.py). Plain code only: no functions, no lists. Scope = the מיקוד chapter 5 (`startswith`, `endswith`, `isalpha`, `isnumeric` are not examined).

## Answers and points (100)

| Q | Part | Answer | Pts |
|---|---|---|---:|
| 1a | `word = "pineapple"` | `nea` · `pple` · `pep` · `4` · `True` · `bineabble` | 3 each = 18 |
| 1b | `a + " cream"` not saved | prints `ice`; strings do not change, the sum was calculated and thrown away | output 3 + reason 3 |
| 2a | `range(len(s) + 1)` | `IndexError` (string index out of range) — 4; fix `range(len(s))` — 4 | 8 |
| 2b | `count` before `lower` | prints `0` — 4; fix `text.lower().count("ana")` (or lower the string first) — 4 | 8 |
| 3 | date | see code below; 6 points per printed line | 30 |
| 4a | count `l` / `L` | `for ch in text` with `ch.lower() == "l"` and a counter; prints `L count: 3` | 10 |
| 4b | reverse with a loop | `rev = ch + rev` (the new letter goes in front); prints `Reversed: lleW sgnirtS nraeL` | 10 |
| 4c | places of `l` / `L` | `for i in range(len(text))` with `text[i].lower() == "l"`; prints 0, 16, 17 | 10 |

### Q3 model answer

```python
date = "25/11/2026"
print("Day:", date[:date.find("/")])
print("Year:", date[-4:])
print("With dashes:", date.replace("/", "-"))
print("Slashes:", date.count("/"))
print("Has 11:", "11" in date)
```

Accept: `date[0:2]` for the day only if the student says why it works (the line is worth 3, not 6, because it ignores `find` — the quiz asks to find the first slash); `date[6:]` or `date[len(date) - 4:]` for the year; an `if "11" in date: print("Has 11: True")`; building the dashes with a loop (full marks if correct).

### Q4 model answers

```python
count = 0
for ch in text:
    if ch.lower() == "l":
        count += 1
print("L count:", count)

rev = ""
for ch in text:
    rev = ch + rev
print("Reversed:", rev)

for i in range(len(text)):
    if text[i].lower() == "l":
        print("Place:", i)
```

Accept for 4a: `ch == "l" or ch == "L"`, `ch in "lL"`. A count with `text.lower().count("l")` earns 4 of 10 (the question asks for a loop). For 4b: `rev = rev + ch` gives `Learn Strings Well` (not reversed): 5 of 10; `range(len(text) - 1, -1, -1)` with `rev += text[i]` is correct (full marks). For 4c: a counter of the places is not what is asked.

## Rubric notes

- Grade the final answer. A handwriting slip (colon, quote) costs nothing; a value built and never printed: −1. Plain code without `def` gets full marks.
- Q3 and Q4: the printed text must match the expected output; a missing label (`Day:`) costs 1 per line.
- A wrong prediction in 1a costs only that row.

## Grading scale and marking sheet

90–100 excellent · 75–89 good · 60–74 fair · below 60: reteach slides 1–4 of the exam-review deck. Record only aggregates in the repo (never names).

| Q1 /24 | Q2 /16 | Q3 /30 | Q4 /30 | Total /100 |
|---|---|---|---|---|
| | | | | |

## What to look for

- **Q1b / Q2b:** students who believe a method changes the string in place (the `replace` / `upper` / `+` habit) — the single most examined idea of the block.
- **Q2a / Q4c:** index equal to the length.
- **Q3:** `find` result used as the slice end gives the right day, but for `Rest` style tasks `+ 1` is needed; here only the day is cut, so `date[:place]` is right.
- **Q4b:** `rev += ch` (not reversed) and `rev = ch + rev` confusion.
