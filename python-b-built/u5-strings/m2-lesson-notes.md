# Unit 5.2 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Slicing — Start, End, Step

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** Lab + Lab (30 min guided practice, then 60 min lab)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit05_strings_complete_unit.md`, meeting 2 — its own clock table, the
`text[start:end:step]` anatomy, the "why isn't the end included" explanation, the negative-index example, the step
examples (including reversal), the prediction table, the header/body extraction task, the character-vs-slice
demonstration, the masked-ID challenge (with its own privacy caveat) and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | indices, `+`/`*`/`in`, core methods, immutability | 45 / 45 |
| **5.2 (this)** | **slicing: start, end, step** | 0 / 90 |
| 5.3 | dynamic slicing + traversal | 0 / 90 |
| 5.4 | string algorithms + the "Smart Text Checker" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 13–14) | Covered here |
|---|---|
| Goal 5: slicing of the form `[start:end:step]` | ✅ every task |
| Goal 10: apply string skills to prompts and AI-generated text | ✅ the header/body extraction task |

### Deliberate exclusions
Dynamic bounds computed from `find()` (5.3), character loops (5.3).

---

## 3. Lesson Goal

**`text[start:end:step]` returns characters from `start` up to but not including `end`, stepping by `step`; missing
bounds copy from the beginning or run to the end.**

---

## 4. Core Mental Models

```python
part = text[start:end:step]
```

```python
word = "PROMPT"
print(word[0:3])   # PRO
print(word[3:])    # MPT  - missing end runs to the end
print(word[:3])    # PRO  - missing start runs from the beginning
print(word[:])     # PROMPT - both missing: the whole string
print(word[::-1])  # TPMORP - step -1: reversed
```

- A plain slice `text[a:b]` (step 1) is `b - a` characters long — the excluded end makes this arithmetic exact.
- `word[2]` returns one **character**; `word[2:3]` returns a one-character **slice** — equal in value, different in
  kind (a single value vs. a string of length one).

---

# 5. Guided Practice (0–30)

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** positive and negative indices |
| 8–22 | **Need:** pulling a title, a short code, or a file extension out of a longer piece of text — why a single index isn't enough |
| 22–38 | Syntax: `start`, `end` (excluded), missing bounds; `word[0:3]`, `word[3:6]`, `word[:3]`, `word[3:]`, `word[:]` on `"PROMPT"`; then negative bounds on `"answer.txt"` (`[-3:]` → `txt`, `[:-4]` → `answer`) |
| 38–52 | **Prediction table (pairs, on `"ARTIFICIAL"`):** `text[0:3]`, `text[3:7]`, `text[:4]`, `text[-3:]`, `text[::2]`, `text[::-1]` — write before checking |
| 52–65 | Step: `text[::2]`, `text[1::2]`, `text[::-1]` on `"0123456789"` |
| 65–90 | *(rolls into the lab — see below)* |

The prediction table (38–52):

<div dir="rtl">

| ביטוי | תוצאה |
|---|---|
| `text[0:3]` | `ART` |
| `text[3:7]` | `IFIC` |
| `text[:4]` | `ARTI` |
| `text[-3:]` | `IAL` |
| `text[::2]` | `ATFCA` |
| `text[::-1]` | `LAICIFITRA` |

</div>

---

# 6. Lab (30–90)

Starter: [`Slicer_Starter.py`](Slicer_Starter.py). Reference: [`Slicer_Reference.py`](Slicer_Reference.py).

## 30–39 — Warm-up: one character, not a substring

```python
filename = "answer.txt"
extension = filename[-3]
print(extension)
```

Predict `txt`, run, get `t` — `filename[-3]` is a single character (the third from the end), not a slice. Fix:
`filename[-3:]` → `txt`.

## 39–55 — Task 1: three slicing functions

On `answer = "TITLE: Safe AI\nBODY: Check important facts."`, write and test:

- `first_six(text)` — the first six characters
- `last_ten(text)` — the last ten characters
- `reversed_text(text)` — the whole text, reversed

```text
TITLE:
ant facts.
.stcaf tnatropmi kcehC :YDOB
IA efaS :ELTIT
```

## 55–68 — Task 2: `mask_id(demo_id)`

Returns `"****"` followed by the last 4 characters. Test on `"CLASSROOM-2026-ABCD"` → `****ABCD`.

> [!WARNING]
> This is a **fake demonstration ID**, not a real API key. A real key is never printed at all — not even masked.

## 68–90 — Save, share, and exit check

Save As `G8_U5_M2_Slicer_<Name>.py`. Swap with a partner: they give you a slice expression to evaluate by hand
before running it.

For `word = "PYTHON"`:

1. `word[1:4]`?
2. `word[-2:]`?
3. `word[::2]`?
4. `word[::-1]`?

**Answers:** `YTH`, `ON`, `PTO`, `NOHTYP`.

### Tool Note – Thonny
Select an expression in the editor and use Thonny's **evaluate selection** (or paste it into the Shell) to check a
slice by hand before running the whole file.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The end index of a slice is included | It's always excluded — that's what makes `end - start` the length |
| A single index and a one-length slice are the same kind of value | Both equal the same character(s), but one is a character, the other a string |
| Step `0` is a valid slice step | It raises `ValueError` — step must be non-zero |
| You can assign to `text[0]` to change a character | Strings are immutable — build a new string instead |
| Slicing needs a trace table only for beginners | Sketching indices first catches most slicing mistakes, at any level |

---

# 8. Assessment Evidence (formative)

- The `"ARTIFICIAL"` prediction table filled before checking
- The warm-up's character-vs-slice distinction explained, not just fixed
- `first_six`, `last_ten`, `reversed_text` passing the given text
- `mask_id()` correct, with the real-key warning acknowledged
- The partner slice-evaluation exchange and the exit check
