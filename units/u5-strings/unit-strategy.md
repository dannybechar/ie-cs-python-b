# Unit 5 — Strings

**8h = 2 Theory + 6 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 5 (pp. 13–15) for goals and hours (master table, p. 3);
**what is taught and with which exercises comes from the Ministry's teaching materials** — see
[`../../docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md): deck 7.1 and worksheet 7.2 (strings, part A), decks 8.0 / 8.1,
worksheet 8.2 and summary 8.7 (strings with loops). Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked from the Ministry materials — all 4 meetings built, awaiting teacher approval.
The first version (approved earlier) was built from `python_b_unit05_strings_complete_unit.md` and planned **45 / 315** minutes;
the official split is **90 / 270**, so the unit is now two Knowledge + Lab meetings (5.1, 5.2) and two Lab + Lab (5.3, 5.4).
The old slide decks stay in the folder, marked superseded in the README, until the new NotebookLM decks are reviewed.

## Official topics and hours

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| What a string is, quotes, indices (positive and negative), `len`, `+`, `*`, `int`/`str` | 5.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| Slicing `[start:end:jump]`, `count`, `replace`, `in`, `find` | 5.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| `lower`/`upper`, `startswith`/`endswith`, `isalpha`/`isdigit`; `for` over a string, counting, building with `+=` | 5.3 (90 P) | 0 / 90 | 🔶 |
| Exercises 4–7, `ord`/`chr` cipher, `split`/`join` (shown), worksheet 8.2, checkpoint | 5.4 (90 P) | 0 / 90 | 🔶 |
| **Total** | | **90 / 270** | |

Chapter goals (ten in all — the official numbering):

1. A string is an ordered sequence of characters → 5.1
2. The empty string and the operators `+`, `*`, `in` → 5.1, 5.2
3. A character by a positive or negative index → 5.1
4. Why the first index is `0` → 5.1
5. Slicing `[start:end:step]` (the Ministry says *jump*) → 5.2
6. `len`, `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric` (the Ministry uses `isdigit`), `replace` → 5.1–5.3
7. Traverse with `for`, and with `range(len(text))` when the place matters → 5.3, 5.4
8. Counting, searching, validation and text-cleaning algorithms → 5.3, 5.4
9. Functions that take a string and return a value → 5.3, 5.4
10. Apply string skills to prompts and AI text → framing in every meeting; closing discussion in 5.4

## Unit 5.1 — Knowledge + Lab: A String Is an Ordered Sequence
- 7.1 slides 2–13; worksheet 7.2 Q1–4. Quotes, `str` vs `int`, indices both ways on `"think big be bold show your color"`,
  `len`, `+`, `*`, `int()`/`str()`.
- lab: the `word[len(word)]` warm-up, predict-and-check, `add_as_numbers`, `join_as_text`, `show_edges`, `first_and_last`.

## Unit 5.2 — Knowledge + Lab: Slicing and Searching
- 7.1 slides 14–28; worksheet 7.2 Q5–11, 13, 15. `[start:end:jump]`, `count`, `replace` (with a count), `in`, `find`.
- lab: the discarded `upper()` warm-up, slices from outputs, `count_the`, `replace_first_three`, `has_yes`, `looks_like_email`.

## Unit 5.3 — Lab + Lab: Methods and the `for` Loop over a String
- 7.1 slides 29–38; worksheet Q12, Q14, Q16; 8.0 / 8.1 slides 7–15 (exercises 1–3). `lower`/`upper`,
  `startswith`/`endswith` (with start and end), `isalpha`/`isdigit`; `for ot in text`, `end=""`, counters, `+=`.
- lab: the counter-reset warm-up, `is_year`, `count_char`, `triple_print`/`triple`, `count_cohen_a`/`_b`, `keep_a_to_e`, `count_words`.

## Unit 5.4 — Lab + Lab: String Algorithms, a Secret Code, and the Checkpoint
- 8.0 / 8.1 exercises 4–7, the ASCII enrichment and cipher, `split`/`join` (8.1 slides 20–23); worksheet 8.2; summary 8.7.
- lab: the `or "e"` warm-up, `first_and_last_word`, `initials`, `count_is`, `print_vowels`, `next_letters`, `dash_words`;
  **checkpoint:** `middle`, `edges`, `alternate_case`.

### Scope decisions
- **Ministry materials are the source of truth** (teacher's decision, 31 Oct 2026). Allowed here because the Ministry teaches them:
  `+=`, `end=""`, `ord`/`chr`, `split`/`join`. `isdigit` replaces `isnumeric` in the lessons (same result for digit characters).
- **`split`/`join` are shown and printed only** — the result is a list; no indexing, looping or changing it (Unit 7 revisits them).
- **Not taught:** lists as a topic, nested loops, dictionaries, tuples, comprehensions, regular expressions, `index()` beyond a sentence.
- **The "Smart Text Checker" project was dropped**: its building blocks (counting loops, `startswith`, building a string) now
  come straight from the Ministry exercises, and the checkpoint is three worksheet-8.2 functions. The "what a program can and
  cannot check about AI text" discussion is kept as the framing for goal 10 (no new AI content in this unit).
- **Ministry text fixed, not copied:** the exercise-1 solution's `print(count = ', count)`; the cipher solution's stray `print('a')`;
  worksheet Q2's broken quotes; worksheet Q7's index-parity hint (gives different capitals than the printed example);
  Q6 (the word `it` vs the characters `it`).
- Exercise functions take a string and return a value (program goal 9); the Ministry's `input`-based `ex()` is kept
  only for exercise 3.
- No real students' names: the surname exercise (#3) uses invented surnames.

## Exit criteria
The student explains a string as an ordered sequence, reads and writes positive and negative indices and `[start:end:jump]`
slices (the end place excluded), uses `count`, `replace`, `in`, `find`, `startswith`/`endswith` and the `is…` methods,
walks over a string with `for`, counts and builds strings, writes small functions that take a string and return a value,
and says what a text check can and cannot tell about an AI-generated answer.

## Checkpoint
5.4: `middle`, `edges`, `alternate_case` (worksheet 8.2 Q3, Q4, Q7), written alone, scored out of 10 (see the 5.4 lesson notes).

## Enrichment
Worksheet 8.2 Q2, Q5, Q6, Q8 (all solved in `Cipher_Reference.py`); a decoder for the next-letter cipher; Ministry
"Python Master" interactive strings component (6.3 in the Ministry classroom).
