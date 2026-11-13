# Lessons 11.1–11.2 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: The Meaning Map, Self-Attention and the Similarity Function

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny with `sentence-transformers` installed (or Colab) — see Tool Note
**Source of inspiration:** Ministry **11.1** (deck: meaning map and self-attention, 28 slides), **11.2** and **11.2.0**
(worksheet #1, "preparation for the Semantle hackathon", and its teacher solution). Kept from v1: the context-window
"suitcase" activity, the spelling-vs-meaning comparison (now with real scores), the `bank` example. See
[`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite (precondition stated at the top):** the functions block (lessons 4.1–4.6) is taught **before** this unit — the worksheet defines `calculate_similarity`
(`def` with two parameters and `return`). The Ministry hands the function over with blanks to fill; if `def` is not yet taught, hand it over
complete and let students only call it. The only list-like syntax students meet is the "copy the form" call `model.encode([word])` (the
library wants a list; lists proper are the lists block (lessons 9.1–9.5, 12.0–14.5)) — students copy it exactly and are not asked to build lists.
**Official naming caveat:** the Ministry calls the result `score_distance` and its comments say "distance", but a **higher** score means
**closer** (1 = same meaning). We keep the official name (so files match the worksheet) and say it aloud: it is a closeness score, not a distance.

---

## 1. Position in the advanced-language-model block (lessons 10.0–11.3)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 10.0–10.2 | tokens, tokenization, token IDs | 45 / 45 |
| **Lessons 11.1–11.2 (this)** | **meaning map, self-attention, context window, `calculate_similarity`** | 45 / 45 |
| Lesson 11.3 | the "Semantle" project | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 15–16) | Covered here |
|---|---|
| Goal 4: the context window and why it is limited in tokens | ✅ the suitcase; 2M tokens (11.1 pp. 22–24) |
| Goal 5: an embedding as a numeric vector of learned meaning features | ✅ the map (11.1 pp. 8–13) |
| Goal 6: vector closeness estimates semantic similarity | ✅ `util.cos_sim` in the worksheet |
| Goal 7: self-attention, conceptually | ✅ "mouse" and the listening window (11.1 pp. 13–21) |
| Goal 9: implement `calculate_similarity` returning a number | ✅ worksheet task 2 |
| Goal 11: a similarity score is not a probability, a truth, or understanding | ✅ closing discussion |

### Deliberate exclusions
The cosine formula, attention mathematics, training. The project itself (lesson 11.3).

---

## 3. Lesson Goal

**A model gives every token a fixed address on a "meaning map" — close addresses, close meanings; self-attention lets the
neighbouring words move a word's address; and one function, `calculate_similarity`, measures the closeness of two words.**

---

## 4. Core Mental Models

```python
meaning_pos1 = model.encode(["dog"])        # the word's address on the map
meaning_pos2 = model.encode(["cat"])
score = util.cos_sim(meaning_pos1, meaning_pos2).item()   # 0.30 here; closer to 1 = closer in meaning
```

- The 2D map on the board is a simplified drawing. A real map has hundreds of dimensions (11.1 p. 8).
- A token's map position is **fixed**. "mouse" (animal or computer?) is the same point until self-attention lets the
  words around it move it (11.1 pp. 13–21).
- Closeness of **spelling** and closeness of **meaning** are independent — and the model is not perfect either.
- A score is the model's estimate of closeness, not a probability and not the truth.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 11.1)

| Clock | Activity |
|---|---|
| 0–8 | **Recap and "watch" quiz** (pp. 5–6): tokens and IDs from lessons 10.0–10.2 |
| 8–23 | **The meaning map** (pp. 8–13): a token is a fixed point; groups; **students place** "four", "orange" and "mouse" on the board map; disputed placements explained |
| 23–38 | **Self-attention** (pp. 13–21): "mouse" cannot have only one point; each word "listens" to the previous words (the 4-word window) and moves on the map. Predict first: *where does "mouse" go after "I clicked the…"?* |
| 38–45 | **How much can a model hold?** (pp. 22–24): Gemini's window is about 2M tokens. **Official equivalents (11.1 p. 24):** 1.5M English words (≈ 20 thick books) · 800K Hebrew words (≈ 11 thick books) · 60,000 lines of code · 22 hours of audio · 2 hours of video ("audio and video can enter a language model too — but we won't learn that now"). Footnote for stage 2: here a token is treated roughly as a word. The **suitcase** (v1 activity, 5 min): six of ten cards fit — a bigger window is not memory and does not guarantee the details are used. Short "AI tips" (pp. 25–27): (1) tokens — spelling mistakes waste tokens, and Hebrew costs more than English in a long chat; (2) meaning map — "you are a physics professor" sends the chat to a very different area of the map than "you are a 5-year-old"; (3) self-attention — give the chat as many examples, links and documents as you can, so it can be accurate |

### Tool Note – Thonny
Same setup as lessons 10.0–10.2 (`pip install sentence-transformers`, model downloaded once at school). Print Hebrew directly in the Shell.

---

# 6. Second 45 Minutes — Lab (worksheet 11.2)

Starter: [`Meanings_Starter.py`](Meanings_Starter.py). Reference: [`Meanings_Reference.py`](Meanings_Reference.py).
Brief: [`m2-lab-brief-he.md`](m2-lab-brief-he.md). The Ministry's task 1 (set up the environment) is done in lessons 10.0–10.2 — skip it.

## 45–52 — Warm-up: measuring the wrong thing

```python
def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character == word_b:      # <- the bug
            count += 1
    return count


print(shared_letters("מזוודה", "מוזיקה"))
```

Predict a positive number (the words share letters), run, get `0`: one character can never equal the **whole** second word.
Fix: `character in word_b` → **5**.

## 52–62 — Task 1: complete `calculate_similarity` (worksheet task 2 a–b)

The starter gives the function with `___` blanks: `meaning_pos1 = model.encode([word1])`, `meaning_pos2 = model.encode([word2])`,
`score_distance = util.cos_sim(meaning_pos1, meaning_pos2).item()`, `return score_distance`. Why must the function
**return** the score and not print it? (lesson 11.3 uses it inside a loop.)

## 62–70 — Task 2: the verdict program (worksheet task 3)

Read two words, print the score, then: `>= 0.5` → "המילים האלו קרובות במשמעות!"; between `0.3` and `0.5` → "יש קשר מסוים";
`<= 0.3` → "המילים האלו מעולמות שונים לחלוטין". (The reference uses `>= 0.5`, `> 0.3`, else — the worksheet says "less than
or equal 0.3" for the last case.) `dog`/`cat` = 0.303 → "יש קשר מסוים"; `dog`/`dog` = 1.0.

## 70–78 — Task 3: spelling or meaning? (kept from v1, with real scores)

<div dir="rtl">

| מילה | תווים משותפים עם "מוזיקה" | ציון המודל |
|---|---:|---:|
| פסנתר | 0 | 0.56 |
| שיר | 1 | 0.86 |
| כדורגל | 1 | 0.48 |
| מזוודה | 5 | 0.55 |

</div>

`שיר` is very close, `פסנתר` shares no letters yet is close. **Honest point:** `מזוודה` (suitcase) scores 0.55, almost as high as
`פסנתר` — a score is an estimate and the model is not perfect; never read it as the truth. (The v1 mock table said 0.82 / 0.76 /
0.19 / 0.35 — invented numbers; they are gone.)

## 78–87 — Task 4: the playground (worksheet "מעבדת ניסויים" — the Ministry's "מגרש משחקים")

Teacher emphasis (10.0): let students experiment freely and independently with the playground corners ("the language test", "the opposites test"); this also practises critical thinking about what the slides taught. Ask after each: *is the model right? how do you know?*

Real results, rounded — yours may differ by a little with the model version:

| Experiment | Pair | Score |
|---|---|---:|
| language test | `computer` / `מחשב` | 0.994 |
| opposites | `happy` / `sad` | 0.614 (opposites are **close**: they appear in the same sentences) |
| unrelated | `london` / `monkey` | 0.172 (searching all pairs of a 16-word list found −0.002: `spoon` / `orbit` — students get 10 tries, so they will not match it) |
| brands | `McDonald's` / `Burger King` | 0.641 |

## 87–90 — Save and exit check

Save As `G8_U6_M2_Meanings_<Name>.py`. Exit check: 1. What is the meaning map? 2. Why isn't "mouse" enough without self-attention?
3. What does `calculate_similarity` return, and what does 1 mean? 4. Why is a score not a probability?

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An embedding is a point on a 2D map | A real one has hundreds of dimensions; the map is only a drawing |
| Spelling closeness implies meaning closeness | They are independent (`פסנתר` has 0 shared letters, score 0.56) |
| Opposites get a low score | They are used in the same contexts, so they are often **close** (`happy`/`sad` 0.61) |
| A high score is the truth | It is an estimate; `מזוודה` / `מוזיקה` is 0.55 |
| Self-attention means the model understands like a person | It is a context-dependent representation, never human-like thought |
| A bigger context window means perfect memory | It only bounds what fits |

---

# 8. Assessment Evidence (formative)

- The map activity: where "four", "orange" and "mouse" were placed, and one disputed placement explained
- The warm-up bug explained (character vs whole word)
- `calculate_similarity` completed and returning a number; the verdict program on three pairs
- The spelling-vs-meaning table with a written conclusion; two playground results with a conclusion
- Exit check
