# Unit 5 — Strings

**8h = 2 Theory + 6 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 5 (pp. 13–15); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 built from the codex material only — **staged in `python-b-built/`, not yet in `units/`.**
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit05_strings_complete_unit.md` —
one detailed document covering all four meetings, including its own exact 90-minute clock tables and meeting split.

## Official topics and hours

Unit totals from the master table (2 theory / 6 practice). The chapter's own table (source §1, drawn from
`python-b-ai.pdf` p. 14) splits differently — string operations 1/1, slicing 1/2, traversal 1/2, totaling 3/5 —
used only for the order and weight of topics; the source document's own meeting plan already reconciles this with
the master table's 2/6, and that plan is followed directly below.

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| String as an ordered sequence; indices; `+`, `*`, `in`; core methods | 5.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| Slicing `[start:end:step]` | 5.2 (90 P) | 0 / 90 | 🔶 |
| Advanced slicing + traversal (character loop vs. index loop) | 5.3 (90 P) | 0 / 90 | 🔶 |
| String algorithms + the "Smart Text Checker" project | 5.4 (90 P) | 0 / 90 | 🔶 |
| **Total** | | **45 / 315** | |

Chapter goals (source §1, ten in all — the exact official numbering used throughout this unit's files):

1. Explain that a string is an ordered sequence of characters → 5.1
2. Use the empty string `""` and the operators `+`, `*`, `in` → 5.1
3. Access a character by a positive or negative index → 5.1
4. Explain why the first index is `0` → 5.1
5. Use slicing of the form `[start:end:step]` → 5.2–5.3
6. Use `len`, `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` → 5.1, 5.3
7. Traverse a string's characters with `for` and with `range(len(text))` when the index is needed → 5.3
8. Develop counting, searching, validation and text-cleaning algorithms → 5.3–5.4
9. Split a solution into functions that take a string and return a value → 5.3–5.4
10. Apply string skills to prompts and to AI-generated text → every meeting; capstone in 5.4

## Unit 5.1 — Knowledge + Lab: A String Is an Ordered Sequence
- the empty string; `len`; positive and negative indices (a five-letter table, both directions); the classic `word[5]`
  off-by-one on a five-character string.
- `+`, `*`, `in` (case-sensitive — normalize with `.lower()` first when that matters); `upper`, `lower`, `startswith`,
  `endswith`, `count`, `find`, `replace`; strings are immutable — a method returns a new string, it never changes the
  original.
- lab: a "the method didn't change my variable" warm-up, a prompt checker, a header-check function.

## Unit 5.2 — Lab + Lab: Slicing
- `text[start:end:step]`; `end` is never included (so a simple slice's length is `end - start`); missing bounds copy
  from the start or to the end; negative indices in a slice.
- step for skipping and for reversing (`[::-1]`); a single index (`word[2]`) returns a character, a slice of length
  one (`word[2:3]`) returns a one-character string — equal in value, different in kind.
- lab: an index-vs-slice warm-up bug, three slicing functions on a saved AI answer, a masked-ID challenge (a fake
  demonstration ID only — never a real key).

## Unit 5.3 — Lab + Lab: Dynamic Slicing + Traversal
- a slice bound computed from `find()`'s result; always check for `-1` before using it as a boundary.
- a direct character loop (`for character in text`) when only the character matters; an index loop
  (`for index in range(len(text))`) when the position matters too; never `range(len(text) + 1)`.
- counting character types; building a new string one character at a time (filtering, hiding digits).
- lab: an out-of-range warm-up, a case-insensitive counting task, a `find`-with-fallback task, a digit-hiding task.

## Unit 5.4 — Lab + Lab: String Algorithms + the "Smart Text Checker" (unit checkpoint)
- choosing the right tool per task: a method, a slice, or a loop.
- combining small, single-purpose, returning functions into one report.
- what a deterministic program can check about AI-generated text (structure, length, specific words, a header) and
  what it fundamentally cannot (truth, source reliability, fit to the reader, whether the model understood the
  request).
- lab: a copy-paste warm-up bug, then the capstone — `normalize`, `count_digits`, `count_letters`, `count_spaces`,
  `hide_digits`, `make_preview`, combined into one text report, tested on all seven of the source's own cases.

### Scope decisions
- **The source document is the only material and is extremely detailed** — an official meeting-by-meeting split that
  already reconciles the master table with the chapter's own hours table, full clock tables (verified to sum to 90
  for each meeting), worked code for every step, a project rubric, and closing summary questions. Followed closely;
  adapted into the house lesson-notes/lab-brief split and warm-up-bug convention. Where the source's own drills
  already are single, clean, runnable bugs (the immutability warm-up, the index-vs-slice mix-up, the off-by-one
  `range`, the copy-paste `count_letters` bug), they were kept as the warm-ups directly.
- The provisional outline in `docs/annual-strategy.md` guessed a four-meeting split by topic (indexing/operators;
  slicing; traversal; the text-processing program) before any Unit 5 source existed. The real source's own split is
  slightly different in its middle boundary (slicing spans 5.2 **and** the start of 5.3, traversal spans the rest of
  5.3 and all of 5.4) and is used here instead, since it is the document's own explicit, hour-accurate plan.
- **Not taught:** lists or list methods (Unit 7), dictionaries, regular expressions, tuples, f-string formatting
  beyond what Unit 4 already introduced.
- **AI framing, not new AI content.** Per the source's own note, this unit adds no new AI concept — prompts and model
  answers are simply treated as strings, preparing for tokens in Unit 6 without pre-empting it.

## Exit criteria
The student explains a string as an ordered sequence, uses positive/negative indexing and `[start:end:step]`
slicing correctly (including that `end` is excluded), chooses the right method/slice/loop for a text task, writes
small functions that take a string and return a result, and explains what a deterministic text check can and
cannot tell you about an AI-generated answer.

## Checkpoint
5.4's "Smart Text Checker" is the unit's capstone, with the source's own 20-point rubric (indices and slicing 3,
methods 3, loop and counters 4, building a string 3, modularity 3, testing 2, critical explanation 2) — see the
lesson notes for the full rubric and performance bands. Tested here against all seven of the source's own cases
(normal, empty, short, long, uppercase, digits, header).

## Enrichment
From the source: a palindrome check after basic normalization; finding every occurrence of a character using only
indices (no lists); collapsing repeated spaces to one; comparing two AI answers by length, digit count and warning
word count; a fixed-format report string ready to save or pass to another function.
