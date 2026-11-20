# Lessons 8.2–8.7 — Strings: exam-review lesson and lab (teacher guide and answer key)

**Status:** Built, awaiting teacher approval 🔶
**Purpose:** close the strings block (lessons 7.1–8.7) with exactly what the Ministry's מיקוד for the mafmar (17 Mar 2027, chapter 5) requires, and prepare the class for **Quiz Q1** a week later (Sun 29 Nov, plan P2). It replaces the countdown and live-problem editions for P1; those stay in the repo as optional extra practice.
**Duration:** 90 minutes: **45 minutes deck** (5 slides, 9 minutes each, teacher copies each code block into Thonny and runs it) + **45 minutes paper lab** (5 questions, then Thonny check).
**No functions, no lists:** plain code only.

## Scope (from the מיקוד, chapter 5)

On the exam: the empty string · `+` and `*` · `in` · indexing and slicing `[]` `[::]` · `len`, `find`, `upper`, `lower`, `count`, `replace` · bounded loops, with the difference between index and content (`for i in range(len(st))` and `for ch in st`).
**Not on the exam (the מיקוד says so):** `startswith`, `endswith`, `isalpha`, `isnumeric`. Also left out of this lesson: `ord`, `chr`, `split`, `join` (Ministry extras, never examined). The class has seen some of these in 8.0–8.1; do not quiz them.

## Deck (5 slides, source [`…-exam-review-source-slides.md`](L04-string-algorithms-and-cipher-exam-review-source-slides.md), PDF [`exam-review-slides-he.pdf`](../lessons/L04-string-algorithms-and-cipher/exam-review-slides-he.pdf))

| # | Slide | Min | Run in Thonny | Question to ask |
|---|---|---:|---|---|
| 1 | What the exam covers: empty string, `+ * in`, index, slice | 9 | `+`, `*`, `in`, `len("")` | `len("")`? `"ha" * 0`? (0, empty string) |
| 2 | Index and slicing | 9 | `[0] [-1] [1:4] [:3] [2:] [::2] [::-1]`; then show `word[6]` crash | `word[3:3]`? (empty string) |
| 3 | The five methods | 9 | `len upper find lower+count replace` and `print(song)` | `song` after `replace`? (unchanged) |
| 4 | Two loops: content vs place | 9 | `cat` both ways, then doubles in `balloon` | why `len(word) - 1`? (`word[i + 1]` would fail on the last place) |
| 5 | One program that joins everything | 9 | the full program; type `Learn AI With Me` | why `low` and not `text`? (capital `E`, `A`, `I` would not match) |

Tell the class: slides 1–4 are the Q1 material; slide 5 shows how an exam answer looks.

## Lab (paper, 45 minutes; sheet [`exam-review-lab-he.md`](../lessons/L04-string-algorithms-and-cipher/exam-review-lab-he.md); starter [`ExamReview_Starter.py`](../exercises/ExamReview_Starter.py))

Students write by hand, type into Thonny to check, correct in another colour, hand in the paper. Print: `python tools/problem_sheet_docx.py exam-review-lab-he.md out.docx 2,3 1.05 7.0` (2 + 3 questions per side). Estimated time for the average student: about 45 minutes; the last question is the one to cut if the class is slow (grade out of 80 in that case and scale).

| Q | Task | Skills | Solution | Points |
|---|---|---|---|---:|
| 1 | Find the bug: `word[len(word)]` raises `IndexError: string index out of range`; fix | index, `len`, `-1` | [`ExamReview_Q1_Solution.py`](solutions/ExamReview_Q1_Solution.py) | 15 (error named 5, fix 10) |
| 2 | E-mail: name before `@`, domain after, `upper`, `in` | `find`, slicing, `upper`, `in` | [`ExamReview_Q2_Solution.py`](solutions/ExamReview_Q2_Solution.py) | 20 |
| 3 | Count `python` ignoring case, `replace`, `len` | `lower`, `count`, `replace`, `len` | [`ExamReview_Q3_Solution.py`](solutions/ExamReview_Q3_Solution.py) | 20 |
| 4 | Count vowels and build the text without them | `for ch`, `in "aeiou"`, `+=`, counter | [`ExamReview_Q4_Solution.py`](solutions/ExamReview_Q4_Solution.py) | 25 |
| 5 | Doubles in `committee`; even places with a loop, compare with `[::2]` | `for i in range(len(...))`, `i % 2`, slicing | [`ExamReview_Q5_Solution.py`](solutions/ExamReview_Q5_Solution.py) | 20 |

Expected outputs are printed on the sheet and were produced by running the solution files (Python 3.14).

### Accepted variants

- **Q1:** `word[len(word) - 1]` or `word[-1]`. Naming the error as `IndexError` (or "index out of range") earns the 5 points.
- **Q2:** `email[:email.find("@")]`; the domain may use `email[at + 1:]` or `email[email.find("@") + 1:]`. Printing `True`/`False` with `print("Has school:", "school" in email)`; an `if` that prints the same text is fine.
- **Q3:** `sentence.lower().count("python")`. Counting without `lower` gives 1: lose the points for the count only. The new length 33 must come from `len` of the new string.
- **Q4:** `for ch in text` with `ch.lower() in "aeiou"` or `ch in "aeiouAEIOU"`. A `+=` string built correctly with spaces kept. Counting with `text.count("a") + …` for the vowels is accepted if the new text is still built with the loop.
- **Q5:** `range(len(word) - 1)` for the doubles; the second part may use `range(0, len(word), 2)` instead of `i % 2` (accept it). Printing `Same: True` requires comparing the two strings with `==`.

### Common errors to look for while circulating

- Index equal to the length (Q1); using `find` result as a slice end without `+ 1` for the domain (Q2: slicing from `at` instead of `at + 1` gives `@school.org`).
- `count` before `lower` (Q3); forgetting that `replace` returns a new string (printing `sentence`, still with `easy`).
- `if ch == "a" or "e" …` (the `or` bug from 8.2–8.7) in Q4 — remind them of the `in "aeiou"` tool.
- `range(len(word))` in the doubles check: `IndexError` at the last place (Q5).

### Grading

100 points as above. Grade the final answer including corrections in another colour; a wrong prediction loses nothing; a plain-code answer needs no `def`; a value built but never printed: −1. Scale: 90–100 excellent · 75–89 good · 60–74 fair · below 60 reteach before Quiz Q1. Record only aggregates in the repo.

### Marking sheet (no names)

| Q1 /15 | Q2 /20 | Q3 /20 | Q4 /25 | Q5 /20 | Total /100 |
|---|---|---|---|---|---|
| | | | | | |

## Quiz Q1 (Sun 29 Nov)

Not built yet. Suggested shape: 15 minutes, five short items on exactly the slide 1–4 skills (one trace of a slice, one `find`/`count`/`replace` output, one index-vs-content loop, one write-the-code). The lab questions above are the practice for it.
