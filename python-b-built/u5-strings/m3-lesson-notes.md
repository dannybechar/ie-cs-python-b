# Unit 5.3 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Dynamic Slicing + Traversal

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** Lab + Lab (25 min guided practice, then 65 min lab)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit05_strings_complete_unit.md`, meeting 3 — its own clock table, the
`find`-as-a-slice-boundary pattern (with the `-1` guard), the direct character loop vs. the index loop, the
character-type counting example, the returning `count_digits` function, the character-building
`keep_letters_and_spaces` example, all three practice tasks (`count_maybe`, `first_part`, `hide_digits`), the saved-
answer AI report task and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | indices, `+`/`*`/`in`, core methods, immutability | 45 / 45 |
| 5.2 | slicing: start, end, step | 0 / 90 |
| **5.3 (this)** | **dynamic slicing + traversal** | 0 / 90 |
| 5.4 | string algorithms + the "Smart Text Checker" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 14) | Covered here |
|---|---|
| Goal 5: slicing `[start:end:step]` (with a dynamic bound) | ✅ the `find`-as-boundary pattern |
| Goal 6: `find`, `isalpha`, `isnumeric` in depth | ✅ every task |
| Goal 7: traverse with `for` and with `range(len(text))` when the index is needed | ✅ guided practice, warm-up |
| Goal 8: counting, searching, validation and text-cleaning algorithms | ✅ every task |
| Goal 9: split a solution into functions that take a string and return a value | ✅ every task |

### Deliberate exclusions
Combining several functions into one report (5.4), the full "Smart Text Checker" project (5.4).

---

## 3. Lesson Goal

**Use `find()`'s result as a slice boundary only after checking it isn't `-1`; loop directly over characters when
only the character matters, and over `range(len(text))` only when the position matters too.**

---

## 4. Core Mental Models

```python
record = "topic=loops;level=beginner"
separator = record.find(";")
if separator == -1:
    print("Separator not found")
else:
    print(record[:separator])         # topic=loops
    print(record[separator + 1:])       # level=beginner
```

```python
for character in text:                 # the character itself matters
    ...

for index in range(len(text)):          # the position matters too
    print(index, text[index])
```

- `find()` returns an index, or `-1` when nothing matches — **always** check before slicing with it.
- `range(len(text))`, never `range(len(text) + 1)` — the last valid index is `len(text) - 1`.

---

# 5. Guided Practice (0–25)

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** short slices and the excluded-end mistake |
| 10–25 | **Dynamic slicing:** `record.find(";")` used as a slice boundary; what happens when the separator isn't found — the `-1` guard, live on `"topic=loops"` with no `;` |

---

# 6. Lab (25–90)

Starter: [`Scan_Starter.py`](Scan_Starter.py). Reference: [`Scan_Reference.py`](Scan_Reference.py).

## 25–34 — Warm-up: one index too far

```python
text = "AI 2026"
for index in range(len(text) + 1):
    print(index, text[index])
```

Run: `IndexError: string index out of range` after the last real character. `+ 1` pushes one index past the end.
Fix: `range(len(text))` → seven clean lines, index `0` through `6`.

Then compare the two traversal styles side by side: `for character in text: print(character)` (the character
matters, not its position) vs. the fixed loop above (both the position and the character matter).

## 34–46 — Task 1: `count_maybe(text)`

Returns how many times `"maybe"` appears, ignoring case. Normalize once with `.lower()`, then `.count()` — don't
loop character by character for this one. Test: `"Maybe it works. MAYBE verify it."` → `2`.

## 46–58 — Task 2: `first_part(text)`

Returns everything before the first space; the whole text if there's no space (using the `find`-with-`-1`-guard
pattern from guided practice). Test: `"smart assistant"` → `smart`; `"Python"` → `Python`.

## 58–75 — Task 3: `hide_digits(text)`

Returns the text with every digit replaced by `#`, built one character at a time — not one `.replace()` call per
digit. Test: `"Room 12 at 09:30"` → `Room ## at ##:##`.

## 75–86 — Applying it to saved AI text

On `ai_answer = "Maybe the answer is 42. Verify important facts."`, produce: length, digit count (reuse
`count_digits` from guided practice or write it fresh), whether `"maybe"` appears, whether the text ends with a
period, and a 10-character preview (`ai_answer[:10]`).

## 86–90 — Save and exit check

Save As `G8_U5_M3_Scan_<Name>.py`.

1. When is `for character in text` the better choice?
2. When do you actually need `range(len(text))`?
3. What does `find()` return when the text isn't found?
4. Why is it better for a text-analysis function to `return` its result than to `print` it?

### Tool Note – Thonny
An `IndexError` traceback names the exact line and the index that failed — use it to find the off-by-one directly,
rather than re-reading the whole loop.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `find()` returns `True`/`False` when nothing is found | It returns `-1` — always compare to `-1`, not to `False` |
| `range(len(text) + 1)` "just to be safe" | It's always one too far; the last valid index is `len(text) - 1` |
| Index loops are needed even when only the character matters | A direct `for character in text` is simpler whenever position is irrelevant |
| Modifying the string being looped over is safe | Strings are immutable — build a **new** string in a separate variable instead |
| `.replace()` is the right tool for "replace every digit" | A loop with `isnumeric()` handles it in one pass without repeating the call per digit |

---

# 8. Assessment Evidence (formative)

- The warm-up's `IndexError` explained by index, not just patched
- `count_maybe()`, `first_part()`, `hide_digits()` all passing their test inputs
- The saved-AI-answer report producing all five values correctly
- Exit check
