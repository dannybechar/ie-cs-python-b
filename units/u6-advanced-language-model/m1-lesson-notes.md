# Unit 6.1 — Advanced Language Model

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Tokens, Tokenization and IDs

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny with `sentence-transformers` installed (or Google Colab, as the Ministry does) — see Tool Note
**Source of inspiration:** Ministry teaching materials **10.0** (teacher emphases), **10.1** (deck: tokens), **10.2** and **10.2.0**
(worksheet and teacher solution). The v1 build (from `python_b_unit06_…_complete_unit.md`) is kept only where the
Ministry is silent: the three-sentence hook, the controlled-experiment table, and our own toy tokenizer (now an
"if time" extension). See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the tokenizer library**.
**Prerequisite (precondition stated at the top):** Unit 3 (functions) is taught **before** this unit. The Ministry worksheet is written with `def`
(`print_sentence_info`, `tokens_sentence`; `count_tokens` is our addition), so `def`/`return`/parameters appear here only on that condition. If the class
has not learned `def`, give the three functions ready-made and let students only call them. No list is written by students in this meeting:
the printed token lists are only shown, like `split` in Unit 5 (lists proper start in Unit 7), and the playground calls one word per line instead of looping over a list.

---

## 1. Position in Unit 6

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **6.1 (this)** | **tokens, tokenization, token IDs — with the real tokenizer** | 45 / 45 |
| 6.2 | the meaning map, self-attention, the context window; `calculate_similarity` | 45 / 45 |
| 6.3 | the "Semantle" project (unit checkpoint) | 0 / 90 |

The Ministry fits the unit in **two** meetings (10.x tokens; 11.x meaning map and project). We keep three because the
master table gives 6 hours: 6.2 takes deck 11.1 and worksheet 11.2, 6.3 takes the project 11.3.

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 15) | Covered here |
|---|---|
| Goal 1: a token is a processing unit, not necessarily a whole word | ✅ deck 10.1 pp. 17–34, the quiz |
| Goal 2: a tokenizer converts text to tokens and numeric IDs | ✅ worksheet 10.2: `tokenize`, `convert_tokens_to_ids` |
| Goal 3: distinguish characters, words and tokens | ✅ `len`, `count(" ")` against the token count |

### Deliberate exclusions
Embeddings, the meaning map and attention (6.2), any similarity computation (6.2–6.3).

---

## 3. Lesson Goal

**A token is a model's own unit of text — a word, part of a word, a number, a space or a punctuation mark — and the
number of tokens depends on the tokenizer, the language and even the capital letters.**

---

## 4. Core Mental Models

```text
טקסט → טוקנייזר → טוקנים → מזהים מספריים → המודל
```

Real output of the worksheet's tokenizer (`paraphrase-multilingual-MiniLM-L12-v2`), checked on Python 3.14:

```text
"hello world"  → ['▁hell', 'o', '▁world']          → [33600, 31, 8999]
"שלום עולם"    → ['▁שלום', '▁עולם']                → [56976, 71107]
"The park is near the park" → ['▁The', '▁park', '▁is', '▁near', '▁the', '▁park'] → [581, 9201, 83, 43573, 70, 9201]
```

- The `▁` marks "a word starts here" (a space before it); it is part of the token.
- **The same token always gets the same ID** (`park` = 9201 twice) — the ID is an index into this tokenizer's vocabulary.
  A higher number does not mean "more important".
- `apple` is `[108787]` and `APPLE` is `['▁APP', 'LE']` = `[66440, 15300]`: capital letters change the tokens.
- **Vocabularies grow with every model (deck 10.1 p. 31):** a word that used to be split into several tokens becomes one token in a newer model.
  Example from the deck: the Hebrew word "אני" is **3 tokens in GPT-4** and **a single token in GPT-5**. Hebrew still "costs" almost twice
  English in the deck's quiz, but the gap narrows with each model. (We cannot run GPT here; MiniLM gives `['▁אני']` = 1 token. Say that the
  number is a property of a specific tokenizer.)
- The model's three stages (deck 10.1 p. 17): **tokens → meaning map → self-attention**. Today is stage one.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 10.1)

| Clock | Activity |
|---|---|
| 0–7 | **Hook — the Semantle demo** (10.1 pp. 2–7): the teacher plays the real game (the link is in the deck) and the class guesses. "By the end of next week you build this." Also the 10.0 requirement: **everyone has `sentence-transformers` installed** (Terminal or Colab) |
| 7–15 | **Old language models** (10.1 pp. 10–14): autocomplete, N-grams until 2014; three limits — poor memory, no flexibility (dog / puppy), double meaning ("mouse"). Predict first: *what would an autocomplete do with "mouse"?* |
| 15–22 | **Three stages** (p. 17) and the definition of a token (p. 20): a word, a part of a word, a number, a space, a punctuation mark; a fixed vocabulary. Prediction question (pp. 21–22): *how many tokens can Gemini hold at once?* — answered in 6.2 |
| 22–35 | **Token quiz** (pp. 23–33): students guess the number of tokens, then the teacher runs the sentence live and shows the tokens and IDs. Use *"nice to see you again!"*, *"It is a xylophone"*, *"I will definitly try"* (spelling mistakes cost tokens), *"כשהלכתי הביתה אתמול"* and the `park` pair (same ID twice) |
| 35–45 | **Name it and compare** (p. 34): the token count of your name; `apple` vs `APPLE`. Bridge to the lab: *the worksheet lets you do exactly this* |

> **Numbers differ by tokenizer.** The Ministry deck's quiz answers (6, 6, 5, 10 tokens) were made with a different
> tokenizer than the worksheet's. With the worksheet's MiniLM tokenizer, run live, the same four sentences give
> **6, 7, 5, 5**. Always run the quiz sentences yourself and show your own numbers; tell the class that another tokenizer
> gives other numbers — that is part of the lesson. Hebrew was about twice as expensive as English in the Ministry's
> quiz (deck p. 31); with MiniLM it costs more too, but less (5 vs 4 tokens for "I walked home yesterday", 8 vs 6 in the worksheet pair), so quote the numbers you measure, not a general rule.

### The Ministry's introduction (worksheet 10.2, read aloud before the lab)
`sentence-transformers` is a **toolbox** for running AI models that turn human language into mathematical calculations. At the heart of the project is
the model `paraphrase-multilingual`, a multilingual "brain" trained on billions of sentences to understand Hebrew and English on **one shared meaning map**.
Before the model works, the **tokenizer** (the translator) splits our text into small units called tokens and gives each one a number from a ready-made
dictionary; that lets the model measure the "distance of meaning" between the guesses and the secret word (the project of 6.3).

### Tool Note – the tokenizer library
`pip install sentence-transformers`, then the first run downloads the model (hundreds of MB): **do it once at school, before
class**, on every computer (or use Colab as in the Ministry deck: `!pip install -U sentence-transformers`). Check at
home that `SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")` loads. On Windows a harmless symlink warning
appears. No outside text, names or personal data go into the model.

---

# 6. Second 45 Minutes — Lab (worksheet 10.2)

Starter: [`Tokenizer_Starter.py`](Tokenizer_Starter.py). Reference: [`Tokenizer_Reference.py`](Tokenizer_Reference.py).
Brief: [`m1-lab-brief-he.md`](m1-lab-brief-he.md).

## 45–52 — Warm-up: the IDs come out as one number

```python
def tokens_sentence(sentence):
    tokens = tokenizer.tokenize(sentence)
    print("tokens:", tokens)
    token_ids = tokenizer.convert_tokens_to_ids(sentence)   # <- the bug
    print("token_ids:", token_ids)
    return tokens
```

Predict a list of eight numbers, run, get `token_ids: 3`. `convert_tokens_to_ids` expects the **list of tokens**; given
the whole sentence as a string it treats it as one unknown token (ID 3). Fix: `convert_tokens_to_ids(tokens)`.

## 52–60 — Task 1: characters and spaces

`print_sentence_info(sentence)`: the length in characters and the number of spaces. For
`"אני אוהב ללמוד פייתון בבית הספר"`: **31** characters, **5** spaces, and **8 tokens** — characters, words and tokens are three different counts.

## 60–66 — Task 2: look at the tokens

`tokens_sentence` on the same sentence. Which tokens are whole words and which are parts (`פי`, `ית`, `ון`)? Expected tokens:
`['▁אני', '▁אוהב', '▁ללמוד', '▁פי', 'ית', 'ון', '▁בבית', '▁הספר']`.

## 66–70 — Task 3: `count_tokens`

`count_tokens(text)` returns `len(tokenizer.tokenize(text))`. `count_tokens("hello world")` = 3, `count_tokens("שלום עולם")` = 2.

## 70–84 — Task 4: the playground (explore; no need to solve everything)

| Experiment | What to try | Real result (MiniLM) |
|---|---|---|
| 1. my name | English vs Hebrew | `Danny Bechar` 3 tokens, `דן בכר` 4; the Ministry teacher solution: `עפרי` = **2** tokens (checked: `['▁ע', 'פרי']`) |
| 2. **challenge:** in 10 tries find a Hebrew sentence with **fewer** tokens than the same sentence in English | one pair per try | the Ministry answer: `hello world` = 3, `שלום עולם` = 2 (checked: 3 and 2). The long pair `אני אוהב ללמוד פייתון בבית הספר` vs `I love learning Python at school` goes the other way: 8 vs 6 — a good discussion |
| 3. a 5-letter word that breaks the most | 10 tries; write down your record | Ministry example: `ארצנו` = 3 tokens (checked: `['▁א', 'רצ', 'נו']`); `qxzjw` and `פצצצץ` = 5 tokens (one per letter, record); `Mississippi` = 1 |
| 4. capital letters | `apple` vs `APPLE` | `[108787]` vs `[66440, 15300]` |

Conclusion to write: *the number of tokens is not the number of words, and it changes with language, spelling and capital letters.*

## 84–90 — Extension, save, exit check

- **If time:** `simple_tokenize` — our own toy tokenizer (in the reference, with its old flush-the-last-token fix). Compare its output with the real one; it has no vocabulary and no IDs.
- Save As `G8_U6_M1_Tokenizer_<Name>.py`.
- Exit check: 1. A token can be… 2. A token ID is… 3. Why can't you guess the token count from the word count? 4. Why does `apple` differ from `APPLE`?

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Every token is a word | A token can be a word, part of a word, a number, a space or a punctuation mark |
| A higher token ID means a more important word | It's an index into a vocabulary — the number carries no meaning by itself |
| The same text gets the same IDs in every model | Different tokenizers, different vocabularies and counts (see the Ministry quiz vs the worksheet) |
| Hebrew costs exactly twice the tokens of English | It depends on the tokenizer: about 2x in the Ministry deck, about 1.3x with MiniLM |
| Capital letters don't matter | `apple` and `APPLE` are different tokens with different IDs |

---

# 8. Assessment Evidence (formative)

- The warm-up bug explained (what `convert_tokens_to_ids` expects), not just fixed
- `print_sentence_info`, `tokens_sentence` and `count_tokens` working on the sample sentence
- At least two playground experiments recorded as prediction → result → conclusion
- Exit check
