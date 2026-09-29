# Unit 5.4 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: String Algorithms + the "Smart Text Checker" (Unit Checkpoint)

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** Lab + Lab (20 min guided practice, then 70 min lab, including the capstone project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit05_strings_complete_unit.md`, meeting 4 — its own clock table, the
tool-choice recap table (method / slice / loop), the project brief, the choose-your-tool table, the student skeleton
and full solution (`normalize`, `count_digits`, `count_letters`, `count_spaces`, `hide_digits`, `make_preview`), the
report-as-a-string extension, the seven-case test table, the peer-review checklist, the "what the program can and
cannot check" boundary discussion and the closing summary questions kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | indices, `+`/`*`/`in`, core methods, immutability | 45 / 45 |
| 5.2 | slicing: start, end, step | 0 / 90 |
| 5.3 | dynamic slicing + traversal | 0 / 90 |
| **5.4 (this)** | **string algorithms + the "Smart Text Checker" checkpoint** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 14–15) | Covered here |
|---|---|
| Goal 8: counting, searching, validation and text-cleaning algorithms | ✅ the whole project |
| Goal 9: split a solution into functions that take a string and return a value | ✅ every function |
| Goal 10: apply string skills to prompts and AI-generated text | ✅ the project's subject matter |
| Assessment (source §4): a graded modular text-processing project | ✅ the checkpoint |

### Deliberate exclusions
Any new string method or slicing form; lists (Unit 7).

---

## 3. Lesson Goal

**A text-processing problem breaks into small, single-purpose functions — each takes a string and returns a
result — combined into one report; the right tool per task is a method, a slice, or a loop, never all three at once
out of habit.**

---

## 4. Core Mental Models

<div dir="rtl">

| משימה | כלי מתאים |
|---|---|
| המרה לאותיות קטנות | `lower` |
| הסרת רווחים חיצוניים | `strip` |
| קדימון | חיתוך |
| ספירת מילה קבועה | `count` לאחר נרמול |
| ספירת סוגי תווים | לולאה ומונים |
| הסתרת כל ספרה | לולאה ובניית מחרוזת |
| בדיקת כותרת | `startswith` |

</div>

- **What the program can check:** length and structure, specific characters and words, a header, digit or
  warning-word occurrences.
- **What it cannot check on its own:** whether a fact in an AI answer is true, whether a source is reliable, whether
  the recommendation fits this reader, whether the model actually understood the request.

---

# 5. Guided Practice (0–20)

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** matching a tool to a task (the table above) |
| 8–20 | **Planning:** break the project into functions; for each, decide its parameter(s) and its return value **before** writing any body |

---

# 6. Lab (20–90)

Starter: [`TextChecker_Starter.py`](TextChecker_Starter.py). Reference: [`TextChecker_Reference.py`](TextChecker_Reference.py).

## 20–33 — Warm-up: copy, paste, forget to change one line

```python
def count_letters(text):
    total = 0
    for character in text:
        if character.isnumeric():
            total += 1
    return total
```

Run `build_report("SUMMARY: Maybe 3 examples are enough.")` (given, unchanged) and check `Letters:` against the
text by eye — it's far too low. `count_letters` was copied from `count_digits` and the condition was never updated.
Fix: `character.isalpha()`.

## 33–75 — Task (project): "Smart Text Checker" — unit checkpoint

Pair work. Build a program that reads a prompt or AI answer and reports: a normalized version used internally
(stripped, lowercase — not printed on its own); total length; letter, digit and space counts; how many times
`"maybe"` appears (case-insensitive); whether the text starts with `"summary:"` after normalizing; a preview of up
to 40 characters, ending in `"..."` **only** when the text was actually cut; a version with every digit hidden as
`#`.

Build **bottom-up**: `normalize`, `count_digits`, `count_letters`, `count_spaces`, `hide_digits`, `make_preview` —
one function at a time, each tested alone, before assembling the report.

## 75–85 — Testing, using all seven of the source's own cases

<div dir="rtl">

| מקרה | קלט | נקודות לבדיקה |
|---|---|---|
| טקסט רגיל | `AI can help.` | אותיות, רווחים, ללא ספרות |
| מחרוזת ריקה | `""` | אין שגיאה וכל המונים אפס |
| טקסט קצר | `Hi` | הקדימון הוא הטקסט עצמו, בלי `...` |
| טקסט ארוך | יותר מ-40 תווים | הקדימון נחתך ומסתיים ב-`...` |
| אותיות גדולות | `MAYBE` | מזוהה לאחר `lower` |
| ספרות | `Room 12 at 09:30` | כל הספרות נספרות ומוסתרות |
| כותרת | `SUMMARY: ...` | `startswith` מחזירה `True` לאחר נרמול |

</div>

## 85–90 — Peer review, presentation and exit reflection

Each pair explains one algorithmic decision to another pair. Peer checklist: does every function do one clear job?
do functions use their parameter rather than a stray global? does every calculating function `return` its result?
does the preview work on short text too? is the empty string handled? are all digits counted? can they explain why
a structural report isn't a fact-check?

Exit card — two lines: one thing a program **can** check about an AI answer as a string; one thing it **cannot**
conclude from string operations alone.

### Tool Note – Thonny
Run each helper function alone in the Shell (`count_digits("Room 12")`) before wiring it into `build_report` — much
faster to isolate a bug in one function than inside the full report.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A copied function automatically fits its new name | Every condition inside must be checked, not assumed |
| Structural checks (length, headers, counts) prove a text is accurate | They only prove structure — truth needs human judgment and checking sources |
| A function should `print` its result to be "done" | A calculating function `return`s its value; printing happens once, in the report |
| The `"..."` should always be added to a preview | Only when the text was actually longer than the limit |
| A global variable is a shortcut worth taking here | Every helper takes text as a parameter — no hidden dependencies |

---

# 8. Assessment Evidence (formative)

- The warm-up's bug named specifically ("copied, condition never updated"), not just patched
- **Unit 5 checkpoint — "Smart Text Checker"**, scored against the source's 20-point rubric: indices and slicing 3,
  methods 3, loop and counters 4, building a string 3, modularity 3, testing 2, critical explanation 2. Bands:
  18–20 complete, modular, tested and well explained · 14–17 works, one small flaw in slicing, a check, or the
  explanation · 10–13 partial, missing a core function or an edge case · 0–9 needs support with indices, loops or
  return values.
- All seven test cases run and matched against the table above
- The peer review and the two-line exit reflection
