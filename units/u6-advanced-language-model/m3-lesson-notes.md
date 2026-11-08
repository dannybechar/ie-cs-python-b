# Unit 6.3 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: The "Semantle" Project (Unit Checkpoint)

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** Lab + Lab (10 min guided practice, then 80 min lab, including the capstone project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny with `sentence-transformers` installed (or Colab)
**Source of inspiration:** Ministry **11.3** and **11.3.0** (worksheet #2 and its teacher solution: the basic game, the attempts
counter, and the advanced features — percent, the emoji thermometer, welcome and victory messages). Kept from v1: the project
rubric, the `quit` / short-guess hardening (now optional), the "a win is decided by the word, not the score" rule, and the
seven test cases. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the embeddings model**.
**Prerequisite:** functions (Unit 3) and f-strings are **not** needed: the reference uses `calculate_similarity` as a given function
and builds messages with `+` and `str()`.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | tokens, tokenization, token IDs | 45 / 45 |
| 6.2 | meaning map, self-attention, `calculate_similarity` | 45 / 45 |
| **6.3 (this)** | **the "Semantle" project — unit checkpoint** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 16) | Covered here |
|---|---|
| Goal 8: install and use a multilingual embeddings model locally | ✅ done in 6.1; used here |
| Goal 9: `calculate_similarity` returning a numeric score | ✅ copied from 6.2 |
| Goal 10: a game with a guess loop, an attempt counter, a percent display, a graphical meter | ✅ the project |
| Goal 11: a score is not a probability, a truth or understanding | ✅ discussion, exit check |

### Deliberate exclusions
New AI concepts — this meeting applies 6.1–6.2 in code.

---

## 3. Lesson Goal

**Build a guessing game on top of one function: loop until the guess equals the secret word, show how close every guess was, and
count the attempts. A percent is a display value, not a probability.**

---

## 4. Core Mental Models

```python
secret_word = "אוקינוס"
guess = ""
while guess != secret_word:
    guess = input("הכניסו ניחוש: ")
    score = calculate_similarity(secret_word, guess)
    print(score)
```

- A win is decided by **matching the secret word**, never by the score (a very high score is still a guess: `ים` = 0.94).
- An exact match scores about 1.0 (the model prints `0.9999998`), so `round(score * 100)` gives 100%.
- A cosine score can be slightly negative, so clamp it before building the bar (`"❄️" * (20 - fires)` would otherwise exceed 20).
- The thermometer is always exactly 20 characters: `"🔥" * fires + "❄️" * (20 - fires)`.

---

# 5. Guided Practice (0–10)

| Clock | Activity |
|---|---|
| 0–10 | **Recap and demo:** the teacher shows the target output (the 4-guess run below); the class predicts what each stage adds. Real guesses for `אוקינוס`: `עכבר` 1%, `דג` 64%, `מים` 62%, `ים` 94%, `אוקינוס` 100% |

---

# 6. Lab (10–90)

Starter: [`Semantle_Starter.py`](Semantle_Starter.py). Reference: [`Semantle_Reference.py`](Semantle_Reference.py).
Brief: [`m3-lab-brief-he.md`](m3-lab-brief-he.md).

## 10–18 — Warm-up: the thermometer's symbols are swapped

```python
def make_thermometer(score):
    fires = round(20 * score)
    return "❄️" * fires + "🔥" * (20 - fires)

print(make_thermometer(0.70))
```

Predict 14 fires then 6 snowflakes, run, get the reverse. Fix: swap which symbol multiplies `fires` and which `20 - fires`.

## 18–25 — Task 1: copy `calculate_similarity` from 6.2

## 25–40 — Task 2: the basic game (worksheet 11.3, stage 3)

`secret_word`, a loop `while guess != secret_word`, print the score of every guess, print "סיום" at the end. Trap to discuss:
`guess` must exist before the loop (`guess = ""`).

## 40–48 — Task 3: the attempts counter (stage 4)

Count guesses and show them in the victory message. The Ministry starts at 1 and prints `attempts - 1`; the reference starts
at 0 and adds 1 before each guess — same result, fewer surprises.

## 48–75 — Task 4: the advanced features — **the unit checkpoint** (stages "advanced features")

1. the score as a percentage (`round(score * 100)` and a `%` sign);
2. the 20-emoji thermometer from the fixed warm-up function;
3. a welcome message and a victory message. Expected run:

```text
--------------------------------------------------
🎮 ברוכים הבאים למשחק סמנטעל! 🎮
המחשב בחר מילה סודית. נסו לנחש אותה.
בכל תור תקבלו ציון דמיון מ-0 (קר מאוד) עד 100 (לוהט!).
--------------------------------------------------
הכניסו ניחוש מספר 1: עכבר
📊 מדחום קירבה: [❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️] 1%
…
הכניסו ניחוש מספר 5: אוקינוס
📊 מדחום קירבה: [🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥] 100%

🏆 כל הכבוד! פיצחתם את המילה הסודית 'אוקינוס' ב-5 ניחושים!
```

## 75–85 — Testing, using the seven cases (the optional hardening)

<div dir="rtl">

| מקרה | קלט | תוצאה צפויה |
|---|---|---|
| ניצחון | המילה הסודית | המשחק מסתיים ומספר הניסיונות מוצג |
| יציאה | `quit` | המשחק מסתיים (רק בגרסה המוגנת) |
| קלט ריק | Enter | הודעת תיקון; המונה אינו גדל (גרסה מוגנת) |
| תו יחיד | אות אחת | הודעת תיקון; המונה אינו גדל (גרסה מוגנת) |
| מילה קרובה | `ים` | ציון גבוה, 94% |
| מילה רחוקה | `עכבר` | ציון נמוך, 1% |
| שפה אחרת | `ocean` | ציון גבוה מאוד (98%), אבל אין ניצחון — המילה שונה |

</div>

`semantle_game_safe` in the reference adds `quit` and the short-guess check. Without it, an empty guess still gets a score (0.38 for `אוקינוס`) — a good
question for the class.

## 85–90 — Peer review, save and exit check

Checklist: is the model loaded once, outside any loop? does the function take two words and return a number? does the loop end by
comparing the **word**? is the thermometer always 20 characters? Save As `G8_U6_M3_Semantle_<Name>.py`.
Exit check: 1. Why load the model only once? 2. Why is a win decided by the word, not the score? 3. Why is the percent not a
probability? 4. Why can `ים` score 94% and still not win?

### Tool Note – the embeddings model
`sentence-transformers` and the model are installed and downloaded once at school before the lesson (see 6.1). Verified with the
real model on Python 3.14 (8 Nov 2026): scores above are from that run. Do not enter personal or sensitive text.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Loading the model inside the loop is simpler | It reloads on every guess; load once, at the top |
| The percent is the probability the guess is right | It is a display value from a similarity score |
| A very high score should end the game | A win is decided by matching the secret word (`ים` = 94%) |
| The thermometer's length can vary | Always 20 characters; only the split changes |
| `guess` does not need a starting value | The loop condition reads it before the first `input` |

---

# 8. Assessment Evidence (formative)

- The warm-up's swapped symbols explained against two worked values (0.70 and 0.20)
- **Unit 6 checkpoint — "Semantle"**, scored against the 20-point rubric (kept from v1): loading the model once 2, the similarity
  function 4, the game loop 3, the attempt counter 2, score display 3 (percent + thermometer), input handling 2 (optional hardening),
  testing 2, conceptual explanation 2. Bands: 18–20 complete, efficient, tested and precisely explained · 14–17 works, one small
  flaw · 10–13 partial · 0–9 needs support.
- The test table run; the peer review; the exit check
