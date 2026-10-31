# Unit 5.4 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: String Algorithms, a Secret Code, and the Unit Checkpoint

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** Lab + Lab (short demo → task → short demo → task, ending with a checkpoint)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)):
decks **8.0 / 8.1** — exercises **#4, #5, #6, #7**, the ASCII enrichment (`ord`, `chr`, the circular next-letter cipher),
and the `split` / `join` slides (8.1 slides 20–23); worksheet **8.2** (questions 2–8); the one-page summary **8.7**.
**Changed from the previous version:** the whole "Smart Text Checker" project (normalize / counters / preview / hidden
digits / seven test cases / 20-point rubric) is replaced. Its ideas that the Ministry also teaches — counting with a loop,
building a string with `+=`, `startswith` — already appear in 5.3 and in exercises 4–7, so the project is no longer a
separate build; the checkpoint is now three functions from worksheet 8.2 (3, 4, 7), and the unit's "what a program can and
cannot tell about AI text" discussion stays as the closing five minutes. **Fixes to the Ministry text:** its
next-letter solution prints `"a"` with a plain `print` (a new line in the middle of the answer) and handles only `"z"`; the
course version builds the result with `+=` and returns it. Worksheet 8.2 Q7's hint (index parity) gives `"TrUsT YoUrSeLf"`,
not the printed `"TrUsT yOuRsElF"` — alternate by *letter*, not by index. Worksheet Q6 asks for the *word* `it`; counting the
characters `it` also finds `with`, `little` — the reference counts words.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | what a string is, indices (+/−), `len`, `+`, `*`, `int`/`str` | 45 / 45 |
| 5.2 | slicing, `count`, `replace`, `in`, `find` | 45 / 45 |
| 5.3 | `lower`/`upper`, `startswith`/`endswith`, `isalpha`/`isdigit`, `for` over a string | 0 / 90 |
| **5.4 (this)** | **exercises 4–7, `ord`/`chr` cipher, `split`/`join` (shown), worksheet 8.2, checkpoint** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 13–15) | Covered here |
|---|---|
| Goal 7: traverse with `for`, and with `range(len(text))` when the place matters | ✅ initials, `count_is_b`, the checkpoint |
| Goal 8: counting, searching, validation and text-cleaning algorithms | ✅ exercises 4–7, cipher, `alternate_case` |
| Goal 9: functions that take a string and return a value | ✅ every task |
| Goal 10: apply string skills to prompts and AI text | ✅ framing: the closing discussion and the cipher as a "text transformer" |
| Ministry additions (not in the program text): `ord`/`chr`, `split`/`join` | ✅ `ord`/`chr` practised; `split`/`join` **shown and printed only** |

### Deliberate exclusions
Lists as a topic: the result of `split` is printed and passed straight to `join`, never indexed, looped over or changed
(Unit 7 does that). No nested loops, no dictionaries, no comprehensions. The 8.2 Q8 challenge is solved with `find` and a
loop, not `split`.

---

## 3. Lesson Goal

**A text problem becomes a loop over the characters (or over the places) plus a counter, a remembered position, or a new
string built with `+=`; characters are numbers underneath (`ord`, `chr`), and a function takes a string and returns a value.**

---

## 4. Core Mental Models

| Task | Tool |
|---|---|
| count a letter, a substring | loop and counter, or `count` |
| the first word | `find(" ")` and a slice |
| the last word, a word that starts after a space | a loop that remembers a place, or looks at `text[index - 1]` |
| a word that is *the whole word* `it` | build the word letter by letter, compare at each space |
| change every letter | loop and `+=` into a new string |
| letter ↔ number | `ord("a")` is `97`; `chr(97)` is `"a"` |

```python
print(ord("a"), ord("b"), chr(100))      # 97 98 d
print(chr(ord("c") + 1))                  # d  - the next letter
text = "guitar piano drums"
print(text.split(" "))                    # ['guitar', 'piano', 'drums']  - a LIST, shown only
print("-".join(text.split(" ")))          # guitar-piano-drums
```

- Next-letter cipher: `z` has no "next" letter, so it wraps to `a` — a special case in the loop.
- `"is"` hides inside `this` and `his`: counting characters is not counting words.
- What a program can check about AI text: its **shape** (length, a title, digits, a spelling of a word). What it cannot: whether
  it is true, whether a source is reliable, whether the answer fits the reader.

---

# 5. Lab Rhythm

Starter: [`Cipher_Starter.py`](Cipher_Starter.py). Reference: [`Cipher_Reference.py`](Cipher_Reference.py).
If the class is slow, skip the second version of Tasks 3 and 4 (the version without `count`) — but not the checkpoint.

| Clock | Activity |
|---|---|
| 0–5 | **Recap with the Ministry summary (8.7):** the one-page list of string operations. "Which tool?" quick-fire: say a task, class points to the tool in the table |
| 5–11 | **Warm-up bug:** `if character == "a" or "e" or …` |
| 11–19 | **Task 1:** first and last word (#4) |
| 19–27 | **Task 2:** initials (#5) |
| 27–36 | **Task 3:** count `"is"` with and without `count` (#6) |
| 36–47 | **Task 4:** count the vowels with and without `count` (#7) |
| 47–52 | **Demo:** `ord`, `chr`, the numbers behind letters (8.0 slides 22–25) |
| 52–63 | **Task 5:** the next-letter cipher |
| 63–70 | **Demo + Task 6:** `split` and `join` — shown and printed only |
| 70–85 | **Checkpoint:** `middle`, `edges`, `alternate_case` (worksheet 8.2 Q3, Q4, Q7) |
| 85–90 | Save, exit check, and the "what a program cannot check" discussion |

---

# 6. Lab

## 5–11 — Warm-up: the `or` that is always true

```python
def count_vowels(text):
    total = 0
    for character in text:
        if character == "a" or "e" or "i" or "o" or "u":
            total += 1
    return total

print(count_vowels("sometimes you learn"))   # should be 8
```

Predict, run: `19` — every character is counted (`"e"` on its own is a non-empty string, so it is true). Python reads
`(character == "a") or "e" or …`. Fix: `if character in "aeiou":` (or five full comparisons joined with `or`).

## 11–19 — Task 1: `first_and_last_word(text)` (Ministry exercise 4)

`"Cats and dogs are great friends"` → `"Cats friends"`. Hint: `find(" ")` for the first space; a loop that remembers the
latest space for the last word. A one-word text returns itself.

## 19–27 — Task 2: `initials(text)` (Ministry exercise 5)

`"American Standard Code Information Interchange"` → `"ASCII"`. Hint: the first letter, then every letter whose previous
character is a space (`text[index - 1] == " "`, a loop over `range(1, len(text))`).

## 27–36 — Task 3: `count_is_a(text)`, `count_is_b(text)` (Ministry exercise 6)

How many times does `"is"` appear? a: with `count`. b: without — a loop over `range(len(text) - 1)` that compares
`text[index:index + 2]` with `"is"`. `"this is his list"` → `4` (not 1: `this`, `is`, `his`, `list`).

## 36–47 — Task 4: `print_vowels(text)` (Ministry exercise 7)

Print the number of `a`, `e`, `i`, `o`, `u`, each on its own line (`a: 1`). Version a uses `count`; version b walks once with five
counters (`a = 0` … `u = 0`) and `if` / `elif`. `"sometimes you learn"` → `a: 1, e: 3, i: 1, o: 2, u: 1`.

## 47–52 — Demo: letters are numbers

Run `for ch in "Hello": print(ord(ch), end=",")` → `72,101,108,108,111,`. Show the ASCII table (8.0 slide 24), then
`chr(97)`, `chr(ord("c") + 1)`. Predict first: what is `ord("A")`? (65.) Why are capitals different from small letters?

## 52–63 — Task 5: `next_letters(text)`

Every letter becomes the next one in the alphabet; `z` becomes `a`; spaces stay. `"abcd"` → `"bcde"`, `"zoo"` → `"app"`,
`"i like python"` → `"j mjlf qzuipo"`. Use only lower-case text. Link: this is a (very weak) cipher — the program
changes the *shape* of a message and anyone can undo it, so it protects nothing.

## 63–70 — Demo + Task 6: `split` and `join`

`"guitar piano drums".split(" ")` gives a **list** `['guitar', 'piano', 'drums']` — *only print it for now*: lists get their
own unit (Unit 7). `"-".join(that_list)` glues it back with a separator. Task: `dash_words(text)` returns the text with every
space replaced by `-`, using `"-".join(text.split(" "))`. Compare with `text.replace(" ", "-")` — same result; when would
`split` be the better tool? (When you want the pieces, not only a different separator — next time.)

## 70–85 — Checkpoint (worksheet 8.2 Q3, Q4, Q7)

Students work alone, no help from the board. Each function takes a string and returns a value.

- `middle(word)` — the middle letter; two letters for an even length. `"robot"` → `"b"`, `"python"` → `"th"`.
- `edges(text)` — the first 4 and the last 4 characters; `"****"` when the text has fewer than 4. `"I like to play drums"` → `"I lirums"`.
- `alternate_case(text)` — letters alternate UPPER / lower; a space stays and is not counted. `"trust yourself"` → `"TrUsT yOuRsElF"`.

Scoring (10 points): each function 3 points (returns, not prints: 1; correct on a normal input: 1; correct on an edge: 1), plus 1 for a
sensible name and layout. Enrichment / homework from worksheet 8.2: Q2 (`C*s`), Q5 (last letters), Q6 (the word `it`), Q8 (challenge).

## 85–90 — Save and exit

Save As `G8_U5_M4_Cipher_<Name>.py`. Exit card, two lines: one thing a program **can** check about an AI answer *as a string*,
and one thing it **cannot** tell you from string operations alone. (Examples: can — it starts with a title, has no digits, is
under 100 characters; cannot — whether the facts are true, whether a source exists.)

### Tool Note – Thonny
Run each function alone in the **Shell** first (`initials("American Standard Code Information Interchange")`) — much faster to
find a mistake in one function than in a whole file.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `x == "a" or "e"` means "a or e" | Each side of `or` is a full condition: `x == "a" or x == "e"`, or `x in "ae"` |
| `count("is")` counts the word `is` | It counts the characters `is` anywhere, including inside `this` |
| `split` returns a string | It returns a **list**; we only print it here |
| `ord("a")` gives a letter | It gives a number; `chr` goes the other way |
| The cipher keeps a message secret | Anyone can shift back; it is a puzzle, not protection |
| A function should `print` its result | A calculating function `return`s; printing happens outside |

---

# 8. Assessment Evidence (formative)

- The warm-up explained (why `or "e"` is always true)
- Exercises 4–7 passing their test inputs; `next_letters` passing all three
- **Unit 5 checkpoint** — `middle`, `edges`, `alternate_case`, scored out of 10 as above
- The two-line exit reflection on what a program can and cannot check
