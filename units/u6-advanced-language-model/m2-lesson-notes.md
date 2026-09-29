# Unit 6.2 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: The Context Window, the Meaning Map, Self-Attention

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit06_advanced_language_models_complete_unit.md`, meeting 2 — its own clock
table, the "suitcase" context-window activity, the spelling-vs-meaning word comparison, the embedding definition and
class meaning-map activity, the conceptual cosine-similarity notes, the `bank`/`bank` self-attention example with
its "threads" activity, the polysemy comprehension exercise, the bias/limits discussion and the exit card kept
nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 6.1 | tokens, tokenization, token IDs, a learning tokenizer | 45 / 45 |
| **6.2 (this)** | **context window, the meaning map, self-attention** | 45 / 45 |
| 6.3 | semantic similarity + the "Semantle" project | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 15–16) | Covered here |
|---|---|
| Goal 4: the context window and why it's limited in tokens | ✅ the suitcase activity |
| Goal 5: an embedding as a numeric vector of learned meaning features | ✅ the meaning-map activity |
| Goal 6: vector closeness as an estimate of semantic similarity | ✅ cosine similarity, conceptually |
| Goal 7: self-attention, conceptually, updating a word's representation via context | ✅ the `bank` example, the threads activity |
| Goal 11: a similarity score is not a probability, a truth, or human understanding | ✅ closing discussion |

### Deliberate exclusions
The cosine-similarity formula, attention mathematics (Q/K/V, positional encoding), any code that computes a real
similarity score (6.3).

---

## 3. Lesson Goal

**An embedding is a learned numeric vector; vectors that are close together often represent related meanings — and
self-attention lets the same spelling take on a different contextual representation depending on the words around
it.**

---

## 4. Core Mental Models

```text
טקסט → מודל embedding → [0.12, -0.48, 0.77, ...]
```

- A 2D class map is a simplified illustration for talking about distance and direction — a real embedding has
  hundreds of dimensions, not two.
- Spelling closeness and meaning closeness are different things: `חתול`/`חתולה` are close in both; `חתול`/`כלב` are
  further apart in spelling but related in meaning (both pets).
- Self-attention gives each token a different contextual representation depending on the other tokens around it —
  the same word `bank` means something different next to `money` than next to `river`.
- A high similarity score reflects the model's and the metric's estimate — it is **not** a probability that an
  answer is correct.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** tokens and token IDs |
| 10–25 | **The "context suitcase" (groups):** ten information cards, a suitcase that holds only six — which are essential for the task? What's lost by leaving the rest out? Conclusion: a bigger context window isn't human memory and doesn't guarantee correct use of every detail |
| 25–38 | Spelling similarity vs. semantic similarity: `חתול`–`חתולה` vs. `חתול`–`כלב` vs. `חתול`–`מחשב` |
| 38–53 | **The "meaning map" (groups):** place word cards (cat, dog, tiger, car, bus, piano, guitar, song, apple, banana) close or far on paper by meaning, mark clusters, pick one disputed pair and explain the reasoning — no single map is "correct"; a model's map comes from its training data and task |
| 53–67 | Cosine similarity, conceptually — closer direction, higher score; not computed by hand here; a score is model- and metric-dependent, and a threshold that works for one task doesn't automatically fit another |
| 67–81 | Self-attention: `"She deposited money in the bank."` vs. `"They sat on the bank of the river."` — same spelling, different contextual meaning; the "threads" activity: cards for each word in a sentence, thick thread for a strong connection, thin for weak, then swap one word and see which threads change |
| 81–87 | Limits and bias: embeddings reflect their training data's patterns and gaps; under-represented languages and groups may get lower-quality representations; socially loaded words can reflect stereotypes; closeness in vector space is not a moral or scientific justification |
| 87–90 | Exit check |

---

# 6. Second 45 Minutes — Lab

Starter: [`Meanings_Starter.py`](Meanings_Starter.py). Reference: [`Meanings_Reference.py`](Meanings_Reference.py).

## Warm-up: measuring the wrong thing

```python
def shared_letters(word_a, word_b):
    count = 0
    for character in word_a:
        if character == word_b:
            count += 1
    return count


print(shared_letters("מזוודה", "מוזיקה"))
```

Predict a positive number (the two words do share several letters), run it, get `0` — comparing one character to
the **whole** second word can never match. Fix: `character in word_b`.

## Task: spelling score vs. a "meaning" stand-in

The file provides `meaning_score_demo(guess, target)` — explicitly **not** a real AI model, a rule-based stand-in
with a few fixed answers (all for the target word `מוזיקה`) and one default for everything else. For each word
below, print its spelling score against `מוזיקה` (fixed `shared_letters`) and its meaning score
(`meaning_score_demo`), then write one sentence explaining what the comparison shows:

<div dir="rtl">

| מילה | תווים משותפים עם "מוזיקה" | ציון "משמעות" (מדומה) |
|---|---:|---:|
| פסנתר | 0 | 0.82 |
| שיר | 1 | 0.76 |
| כדורגל | 1 | 0.19 |
| מזוודה | 5 | 0.35 |

</div>

`פסנתר` shares no letters with `מוזיקה` at all, yet scores close in "meaning" — spelling and meaning are
independent. `מזוודה` shares five letters (spelling looks close!) but has nothing to do with music — the demo
correctly falls back to its default score for it.

## Save and exit check

Save As `G8_U6_M2_Meanings_<Name>.py`.

1. The context window is measured in…
2. An embedding is…
3. Why isn't the board's meaning map the model's actual map?
4. How does self-attention help with a word that has more than one meaning?

### Tool Note – Thonny
Print the Hebrew strings directly in the Shell rather than in a message box — Thonny's Shell renders right-to-left
text correctly; some plugins and dialogs do not.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An embedding is literally a point on a 2D map | It's a vector with hundreds of dimensions — the map is only a simplified illustration |
| Spelling closeness implies meaning closeness | They're independent; `מזוודה`/`מוזיקה` share many letters but nothing else |
| Self-attention means the model "understands" a word like a person | It's a weighted, context-dependent representation — never describe it as human-like thought |
| A similarity score is a probability the guess is correct | It's a model- and metric-dependent estimate of closeness, nothing more |
| A bigger context window means the model remembers everything perfectly | It only bounds what fits in — it's not memory and gives no usage guarantee |

---

# 8. Assessment Evidence (formative)

- The context-suitcase activity: which six cards were kept, and why
- The meaning-map activity: one disputed placement explained
- The warm-up bug explained (character vs. whole-word comparison), not just fixed
- The four-word spelling-vs-meaning comparison completed with a written conclusion
- The polysemy/threads activity: at least one correctly identified disambiguating word
- Exit check
