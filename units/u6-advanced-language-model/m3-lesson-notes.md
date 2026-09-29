# Unit 6.3 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Semantic Similarity + the "Semantle" Project (Unit Checkpoint)

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** Lab + Lab (20 min guided practice, then 70 min lab, including the capstone project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny; a multilingual embeddings model for the live version (see Tool Note)
**Source of inspiration:** `python_b_unit06_advanced_language_models_complete_unit.md`, meeting 3 — its own clock
table, the model-loading example, `calculate_similarity`, the display-score and percent functions, the meter
function with its two worked examples, the full game skeleton and solution, the seven-case test table, the peer
checklist and closing reflection kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the embeddings model**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | tokens, tokenization, token IDs, a learning tokenizer | 45 / 45 |
| 6.2 | context window, the meaning map, self-attention | 45 / 45 |
| **6.3 (this)** | **semantic similarity + the "Semantle" project** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 16) | Covered here |
|---|---|
| Goal 8: install and import a multilingual embeddings model for local use | ✅ (framed for the live version; see Tool Note and `unit-strategy.md`) |
| Goal 9: implement `calculate_similarity(text_a, text_b)` returning a numeric score | ✅ Task 1 |
| Goal 10: a game with a guess loop, an attempt counter, a percent display, a graphical meter | ✅ the project |
| Goal 11: a similarity score is not a probability, a truth, or human understanding | ✅ discussion, exit check |

### Deliberate exclusions
Any new AI concept — this meeting applies 6.1–6.2's ideas in code, it doesn't introduce new theory.

---

## 3. Lesson Goal

**Load an embeddings model once, outside any function or loop; a similarity function takes two strings and returns
a number; a percent display is a game readout, not a probability.**

---

## 4. Core Mental Models

```text
שתי מחרוזות
    ↓
שני embeddings
    ↓
cosine similarity
    ↓
מספר מוחזר לתוכנית הראשית
```

```python
def calculate_similarity(text_a, text_b):
    ...
    return float(score)          # always a plain number, not a tensor or a raw model object


def score_for_display(raw_score):
    return max(0.0, min(1.0, raw_score))   # cosine similarity CAN be negative - clamp before displaying


def create_meter(raw_score):
    display_score = score_for_display(raw_score)
    filled = int(display_score * 10)
    empty = 10 - filled
    return "🟩" * filled + "⬜" * empty      # always exactly 10 characters long
```

- The model loads **once**. Loading it inside a function or a loop wastes time and memory on every call.
- A win is decided by matching the secret word exactly — never by score alone (a very high score is still a guess,
  not a match).

---

# 5. Guided Practice (0–20)

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** embeddings, closeness, cosine similarity (conceptual) |
| 8–20 | **Demo (live, or classroom mode — see Tool Note):** load the model once, encode a pair of strings, compute and print a similarity score for a few pairs; no fixed order across pairs should be assumed — record results and explain them cautiously |

---

# 6. Lab (20–90)

Starter: [`Semantle_Starter.py`](Semantle_Starter.py). Reference: [`Semantle_Reference.py`](Semantle_Reference.py).
Classroom mode by default — `calculate_similarity()` uses the rule-based stand-in from 6.2 (`meaning_score_demo`),
so nothing here needs a download to build and test (Tool Note below).

## 20–28 — Warm-up: the meter's colors are swapped

```python
def create_meter(raw_score):
    display_score = score_for_display(raw_score)
    filled = int(display_score * 10)
    empty = 10 - filled
    return "⬜" * filled + "🟩" * empty


print(create_meter(0.70))
print(create_meter(0.20))
```

Predict `🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜` for `0.70` (7 green, 3 white); run and compare — the colors are backwards. Fix: swap
which symbol multiplies `filled` and which multiplies `empty`.

## 28–40 — Task 1: completing `calculate_similarity`

In classroom mode, `calculate_similarity(text_a, text_b)` should return `meaning_score_demo(text_a, text_b)`. Fill
it in and confirm the meter and percent both react correctly to a close pair and a far pair.

## 40–75 — Task 2 (project): the "Semantle" guessing game — unit checkpoint

`secret_word = "מוזיקה"`, an attempt counter starting at `0`, a `playing` flag. While playing, read a guess:
`"quit"` ends the game; a guess under 2 characters prints a correction and does **not** count as an attempt;
otherwise the attempt counter grows by one, the similarity score and its percent are computed and shown with the
meter, and an exact match to the secret word ends the game with the attempt count.

## 75–85 — Testing, using all seven of the source's own cases

<div dir="rtl">

| מקרה | קלט | תוצאה צפויה |
|---|---|---|
| ניצחון | מילת היעד המדויקת | המשחק מסתיים ומספר הניסיונות מוצג |
| יציאה | `quit` | המשחק מסתיים בלי לחשב דמיון |
| קלט ריק | Enter | הודעת תיקון; המונה אינו גדל |
| תו יחיד | אות אחת | הודעת תיקון; המונה אינו גדל |
| מילה קרובה | מילה מאותו תחום | מתקבל ציון ומד מתאים |
| מילה רחוקה | מילה מתחום אחר | ציון נמוך יותר, אך לא מובטח |
| שפה אחרת | תרגום של מושג | בודקים איך המודל הרב-לשוני מתנהג (רק בהרצה חיה עם המודל האמיתי) |

</div>

## 85–90 — Peer review and closing reflection

Checklist: is the model (or in classroom mode, the stand-in) used the same way every time, not reloaded per call?
does the function take two strings and return a `float`? does the counter only grow on a valid guess? is the meter
always exactly 10 characters? can `quit` end the game? is a win decided by the word itself, not the score?

Exit check:

1. Why load the model only once?
2. What does `calculate_similarity` return?
3. Why clamp the score before building the meter?
4. Why is a win decided by the word, not just a high score?

### Tool Note – the embeddings model
For a real run: `pip install -U sentence-transformers`, then load
`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` once, well before class — the first download is large.
Cache it locally and test it once beforehand; keep the classroom-mode fallback ready in case the connection fails
during the lesson. Do not enter any real personal or sensitive text, even though the computation runs locally.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Loading the model inside the function is simpler | It reloads on every single call — load once, outside any function or loop |
| A returned tensor or model object is fine to use directly | Convert to a plain `float` before returning, so the calling code gets a normal number |
| The percent shown is the probability the guess is right | It's a display value derived from a clamped similarity score — not a probability |
| A very high score should end the game by itself | A win is decided by matching the exact secret word |
| The meter's length can vary with the score | It's always exactly 10 characters — only the split between filled and empty changes |

---

# 8. Assessment Evidence (formative)

- The warm-up's swapped colors explained against the two worked examples (0.70, 0.20)
- `calculate_similarity()` correctly wired to the classroom-mode stand-in
- **Unit 6 checkpoint — "Semantle"**, scored against the source's 20-point rubric: loading the model once 2, the
  similarity function 4, the game loop 3, the attempt counter 2, score display 3, input handling 2, testing 2,
  conceptual explanation 2. Bands: 18–20 complete, efficient, tested and precisely explained · 14–17 works, one
  small flaw in display, testing, or explanation · 10–13 partial, the similarity function or loop needs a fix ·
  0–9 needs support separating into functions, the counter, or the similarity computation.
- All seven test cases run and matched against the table above (the cross-language case discussed conceptually if
  no live model is available)
- The peer review and closing reflection
