# Unit 6.1 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Tokens, Tokenization and IDs

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; optionally a downloaded tokenizer library for the teacher demo (see Tool Note)
**Source of inspiration:** `python_b_unit06_advanced_language_models_complete_unit.md`, meeting 1 — its own clock
table, the three-sentence comparison hook, the token pipeline diagram, the real-tokenizer teacher demo, the
controlled-experiment table, the learning tokenizer's own trace table, the space-marking extension exercise and
the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the tokenizer library**.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **6.1 (this)** | **tokens, tokenization, token IDs, a learning tokenizer** | 45 / 45 |
| 6.2 | context window, the meaning map, self-attention | 45 / 45 |
| 6.3 | semantic similarity + the "Semantle" project | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 15) | Covered here |
|---|---|
| Goal 1: a token is a processing unit, not necessarily a whole word | ✅ hook, pipeline |
| Goal 2: a tokenizer converts text to tokens and numeric IDs | ✅ teacher demo |
| Goal 3: distinguish characters, words and tokens | ✅ the three-sentence comparison |

### Deliberate exclusions
Context window (6.2), embeddings and attention (6.2), any similarity computation (6.3).

---

## 3. Lesson Goal

**A token is a model's own unit of text — not necessarily a whole word — and different tokenizers can split the
same text differently.**

---

## 4. Core Mental Models

```text
טקסט → טוקנייזר → טוקנים → מזהים מספריים → המודל
```

```text
"unbelievable!" → ["un", "believ", "able", "!"] → [418, 9201, 642, 12]
```

(A conceptual example — the actual split and numbers depend entirely on which tokenizer is used.)

- A token ID is just an index into one particular tokenizer's vocabulary; a higher number does not mean "more
  important" or "more meaningful."
- The number of tokens in a text cannot be predicted from its character or word count alone — it depends on the
  tokenizer.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Hook:** compare `"AI helps."`, `"Artificial intelligence can help."`, and a Hebrew sentence with similar meaning — which has more characters? More words by spaces? Can you know the token count without knowing the tokenizer? (No.) |
| 8–20 | Character, word, token, token ID — the four concepts, with the pipeline diagram |
| 20–32 | **Teacher demo** (real tokenizer, if available — see Tool Note): tokenizing a sentence, showing tokens, IDs and the token count; otherwise walk the conceptual `"unbelievable!"` example |
| 32–48 | **Controlled experiments (pairs):** change **one** factor at a time and predict first — case (`hello`/`Hello`), punctuation (`hello`/`hello!`), a space (`icecream`/`ice cream`), a number (`2026`/`20 26`), language (a short English sentence vs. its Hebrew translation), word length |
| 48–61 | Record each experiment: hypothesis → result → conclusion, on a worksheet |
| 61–90 | *(rolls into the lab — see below)* |

### Tool Note – the tokenizer library
The real-tokenizer demo needs `pip install transformers` and a downloaded model (the same multilingual model used
in 6.3 — download it once, well before class). If unavailable, run the demo conceptually on the board using the
`"unbelievable!"` example, and let the lab's `simple_tokenize` carry the hands-on part entirely.

---

# 6. Second 45 Minutes — Lab

Starter: [`Tokenizer_Starter.py`](Tokenizer_Starter.py). Reference: [`Tokenizer_Reference.py`](Tokenizer_Reference.py).
This meeting's own learning tokenizer is **not** a stand-in for a real model's vocabulary — say so explicitly (see
Misconceptions below).

## 61–70 — Warm-up: the last token gets lost

```python
def simple_tokenize(text):
    result = ""
    current = ""
    for character in text:
        if character.isalpha() or character.isnumeric():
            current += character.lower()
        else:
            if current != "":
                result += "[" + current + "]"
                current = ""
            if character != " ":
                result += "[" + character + "]"
    return result


print(simple_tokenize("AI helps"))
```

Predict `[ai][helps]`, run, get only `[ai]` — the loop only flushes `current` when it hits a non-letter character;
if the text ends mid-word, that last piece never gets flushed. Fix: add the same flush **after** the loop.

## 70–82 — Task 1: marking spaces as their own token

Write `simple_tokenize_with_spaces(text)` — every space becomes its own `[SPACE]` token instead of being dropped.
Test on `"AI helps"` → `[ai][SPACE][helps]`.

## 82–87 — Task 2: counting tokens

Write `token_count(text)` — how many tokens `simple_tokenize` produced (count the `"["` characters in its result).
Use it on a few of the guided-practice experiment pairs and compare the counts.

```text
hello    -> 1
hello!   -> 2
ice cream -> 2
icecream  -> 1
```

## 87–90 — Save and exit check

Save As `G8_U6_M1_Tokenizer_<Name>.py`.

1. A token can be…
2. A token ID is…
3. Why can't you always guess the token count from the word count?
4. Name one limitation of the simple tokenizer built today.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Every token is a word | A token can be a word, part of a word, a punctuation mark, or something else |
| A higher token ID means a more important word | It's just an index into a vocabulary list — the number carries no meaning by itself |
| The same text always gets the same IDs in every model | Different tokenizers, different vocabularies, different results |
| Comparing two languages' token counts tells you about model quality | It only reflects tokenization for that text — no broader conclusion follows from one experiment |
| Today's simple tokenizer works like a real model's tokenizer | It's a learning tool: no trained vocabulary, no real IDs, no subword rules |

---

# 8. Assessment Evidence (formative)

- At least one controlled experiment recorded as hypothesis → result → conclusion
- The token vs. word vs. character distinction stated in the student's own words
- The warm-up bug explained (why the *last* token specifically was lost)
- `simple_tokenize_with_spaces()` and `token_count()` passing their tests
- Exit check
