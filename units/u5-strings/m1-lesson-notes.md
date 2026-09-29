# Unit 5.1 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: A String Is an Ordered Sequence

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit05_strings_complete_unit.md`, meeting 1 — its own clock table, the "how
does Python see this text" hook, the empty-string note, the five-letter positive/negative index table, the
operators section (with the `in` case-sensitivity note), the core-methods block and its immutability demo, the two
practice tasks and the header challenge, the common-mistakes list and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **5.1 (this)** | **indices, `+`/`*`/`in`, core methods, immutability** | 45 / 45 |
| 5.2 | slicing: start, end, step | 0 / 90 |
| 5.3 | dynamic slicing + traversal | 0 / 90 |
| 5.4 | string algorithms + the "Smart Text Checker" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 13) | Covered here |
|---|---|
| Goal 1: a string is an ordered sequence of characters | ✅ hook, index table |
| Goal 2: the empty string; `+`, `*`, `in` | ✅ |
| Goal 3: access by positive or negative index | ✅ index table |
| Goal 4: why the first index is `0` | ✅ |
| Goal 6: `len`, `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` | ✅ (`isalpha`/`isnumeric` previewed here, taught in depth in 5.3) |

### Deliberate exclusions
Slicing (5.2), traversal with a loop (5.3), building new strings from filtered characters (5.3–5.4).

---

## 3. Lesson Goal

**A string is an ordered sequence of characters, indexed from `0`; its methods return a new string and never change
the original.**

---

## 4. Core Mental Models

```python
word = "ROBOT"
#        R  O  B  O  T
# index: 0  1  2  3  4
#       -5 -4 -3 -2 -1

print(word[0])    # R
print(word[-1])   # T - the last character, without needing len(word) - 1
```

```python
name = "python"
name.upper()          # returns "PYTHON" but throws it away - name is unchanged
print(name)             # python
name = name.upper()     # only reassigning keeps the new string
print(name)              # PYTHON
```

- The last valid index is always `len(text) - 1`; `text[len(text)]` is one past the end.
- `in` is case-sensitive; normalize with `.lower()` on both sides when case shouldn't matter.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Hook:** `ai_answer = "Take a short break and drink water."` — `type()`, `len()`, `ai_answer[0]`. What type is it? What does `len` count? What's the first character? |
| 8–20 | The empty string `""` — it exists, holds no characters, and is a useful starting value for building text later; a five-letter index table (`ROBOT`), positive and negative, both directions; the classic off-by-one: `word[5]` on a 5-character word |
| 20–35 | Operators: `+`, `*`, `"art" in "artificial"` vs. `"ART" in "artificial"` — predict all four, then check; normalizing with `.lower()` before an `in` check |
| 35–48 | Core methods on `"  AI can help, but AI can be wrong.  "` after `.strip()`: `upper`, `lower`, `startswith`, `endswith`, `count`, `find`, `replace` — predict each result first; then the immutability demo (`name.upper()` alone vs. `name = name.upper()`) |
| 48–63 | **Predict (alone, then check):** length, first/last character, a case-insensitive `in` check, and a count, all on `"Explain loops"` |
| 63–78 | *(rolls into the lab — see below)* |
| 78–90 | The lab missions, then exit check |

The prediction (48–63):

```python
prompt = "Explain loops"
print(len(prompt))
print(prompt[0])
print(prompt[-1])
print("loop" in prompt.lower())
print(prompt.count("o"))
```

```text
13
E
s
True
2
```

---

# 6. Second 45 Minutes — Lab

Starter: [`Checker_Starter.py`](Checker_Starter.py). Reference: [`Checker_Reference.py`](Checker_Reference.py).

## 63–71 — Warm-up: the method that didn't change anything

```python
text = "python"
text.upper()
print(text)
```

Predict, then run: still `python`, not `PYTHON`. `upper()` returns a new string; nothing was done with it. Fix:
`text = text.upper()` → `PYTHON`.

## 71–81 — Task 1: a prompt checker

Read a prompt with `input()` and print: its length, whether it's empty, whether it contains `"password"` (any
case), and whether it ends with `"?"`.

## 81–86 — Task 2: `header_check(answer)`

Returns `"Structured answer"` when `answer` starts with `"SUMMARY:"`, otherwise `"Missing title"`. Test on
`"SUMMARY: Python loops repeat instructions."` and on the same sentence without the header.

## 86–90 — Save and exit check

Save As `G8_U5_M1_Checker_<Name>.py`. For `text = "MODEL"`, complete:

1. `text[1]` is…
2. `text[-1]` is…
3. `len(text)` is…
4. `"del" in text.lower()` is…

**Answers:** `O`, `L`, `5`, `True`.

### Tool Note – Thonny
Hover a string in the **Variables** view to see it with its quotes — useful for spotting a stray leading or
trailing space that `.strip()` would remove.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An index equal to the string's length is valid | The last valid index is `len(text) - 1` |
| `in` ignores letter case | It's case-sensitive; normalize with `.lower()` first if needed |
| `upper()` / `replace()` change the original variable | They return a new string; reassign to keep it |
| `find()` returns `True`/`False` | It returns an index, or `-1` when nothing matches |
| Counting words is the same as `len()` | `len()` counts characters, including spaces and punctuation |

---

# 8. Assessment Evidence (formative)

- The index table filled in both directions before running any code
- The `"Explain loops"` prediction, all five lines, before running
- The warm-up explained (why nothing changed, not just the one-line fix)
- The prompt checker and `header_check()` passing their test inputs
- Exit check
