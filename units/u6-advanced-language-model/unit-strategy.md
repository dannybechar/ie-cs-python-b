# Lessons 10.0–11.3 — Advanced Language Model

**6h = 2 Theory + 4 Practice = 3 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 6 (pp. 15–16); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked 8 Nov 2026 to the Ministry teaching materials (files 10.0–11.3.0); awaiting re-approval. The v1 build
(approved earlier) came from `Downloads\python-b-codex\python_b_unit06_advanced_language_models_complete_unit.md` and ran on a classroom mock;
the Ministry's materials use the real model, so code, notes and briefs were rewritten. Decks: superseded, new NotebookLM decks pending.

## Official topics and hours

Unit totals from the master table (2 theory / 4 practice), matching the chapter's own table exactly (tokens 1/2,
meaning-map + attention + project 1/2, total 2/4 — for once both agree).

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| Tokens, tokenization, token IDs (Ministry 10.0–10.2) | lessons 10.0–10.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| Meaning map, self-attention, context window, `calculate_similarity` (Ministry 11.1, 11.2) | lessons 11.1–11.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| The "Semantle" project (Ministry 11.3) | lesson 11.3 (0 T + 90 P) | 0 / 90 | 🔶 |
| **Total** | | **90 / 180** | |

Chapter goals (source §1, eleven in all):

1. A token is a model's processing unit, not necessarily a whole word → lessons 10.0–10.2
2. A tokenizer converts text to tokens and to numeric IDs from the model's own vocabulary → lessons 10.0–10.2
3. Distinguish characters, words and tokens → lessons 10.0–10.2
4. Explain the context window and why it's limited in tokens → lessons 11.1–11.2
5. Describe an embedding as a numeric vector of learned meaning features → lessons 11.1–11.2
6. Vector closeness can estimate semantic similarity → lessons 11.1–11.2; 11.3
7. Explain, conceptually, how self-attention uses context to update a word's representation in a sentence → lessons 11.1–11.2
8. Install and import a multilingual embeddings model for local use → lesson 11.3
9. Implement `calculate_similarity(text_a, text_b)` returning a numeric score → lesson 11.3
10. Build a game with a guess loop, an attempt counter, a percent display and a graphical closeness meter → lesson 11.3
11. Explain that a similarity score is not a probability, a truth or human understanding → every meeting

## Lessons 10.0–10.2 — Knowledge + Lab: Tokens, Tokenization and IDs
- token vs. character vs. word; a token isn't necessarily a whole word; the pipeline text → tokenizer → tokens →
  numeric IDs → model.
- a teacher-led demo with a real tokenizer (a downloaded library — see Tool Note) shows the concept; students build
  and extend their **own** small learning tokenizer, explicitly not a stand-in for a real model's vocabulary.
- controlled experiments changing one factor at a time (case, punctuation, a space, language, word length) and
  documenting hypothesis → result → conclusion.
- lab: a missing-final-flush warm-up bug, extending the tokenizer to mark spaces, a token-counting function used
  for the experiments.

## Lessons 11.1–11.2 — Knowledge + Lab: The Context Window, the Meaning Map, Self-Attention
- the context window: what fills it (system instructions, prior turns, the current message, supplied documents,
  the response being generated) and what happens when it's exceeded — not human memory, no guarantee of correct use.
- spelling similarity vs. semantic similarity; embeddings as high-dimensional vectors, a 2D class map as a
  simplified illustration only; cosine similarity at a conceptual level (no formula).
- self-attention, conceptually: the same spelling (`bank`) gets a different contextual representation depending on
  surrounding words; never described as human-like thought or understanding.
- lab: a spelling-vs-meaning warm-up bug, comparing a rule-based "meaning" stand-in against a simple spelling-overlap
  function on word pairs that expose the difference.

## Lesson 11.3 — Lab + Lab: Semantic Similarity + the "Semantle" Project (unit checkpoint)
- loading a real embeddings model **once**, outside any function or loop; `calculate_similarity` returning a
  `float`; clamping a score to `[0, 1]` for display only (raw cosine similarity can be negative); a percent is a
  **display value**, not a probability.
- a character-repeated closeness meter, always exactly 10 characters long.
- the guessing-game loop: an attempt counter that only grows on a valid guess, `quit` to exit, a win decided by
  matching the target word, not by score alone.
- lab: a swapped-meter-colors warm-up bug (checked against the source's own two worked examples), completing
  `calculate_similarity`, then the "Semantle" game itself — the unit's capstone.

### Scope decisions
- **The Ministry materials are the source (8 Nov 2026).** Deck 10.1, worksheets 10.2 / 11.2 / 11.3 and the teacher solutions set the
  topics, examples and code. The Ministry fits the unit in **two** meetings; we keep **three** (the master table gives 6 hours):
  Lessons 10.0–10.2 = 10.x, lessons 11.1–11.2 = 11.1 + 11.2, lesson 11.3 = 11.3. Our extra time goes to the real-model playground and the checkpoint rubric.
- **The real model is used everywhere; the classroom mock is gone.** The v1 `meaning_score_demo` returned invented scores
  (`כדורגל` 0.19, real 0.48), which taught wrong conclusions. All files use `sentence-transformers`
  (`paraphrase-multilingual-MiniLM-L12-v2`, `model.tokenizer`, `util.cos_sim`). The teacher installs the library and downloads the model
  once at school before lessons 10.0–10.2; every file was run with it on Python 3.14. A class with no internet can use Colab, as the Ministry does.
- **The Ministry deck's token quiz numbers differ from the worksheet's tokenizer** (10.1 says 6 / 6 / 5 / 10 tokens; the worksheet's MiniLM
  gives 6 / 7 / 5 / 5). The notes tell the teacher to run the quiz live and quote measured numbers.
- **Functions:** the Ministry worksheets use `def`; the advanced-language-model block (lessons 10.0–11.3) follows the functions block (lessons 4.1–4.6) in the schedule. If `def` is still untaught, give the functions
  ready-made. f-strings are not needed (the reference builds messages with `+` and `str()`).
- **Kept from v1:** the context "suitcase", the spelling-vs-meaning comparison, the 20-point project rubric, the `quit` / short-guess hardening
  (optional), our toy tokenizer (a lessons 10.0–10.2 extension), and "a win is decided by the word, not the score".
- **Not taught:** the cosine-similarity formula, attention math (Q/K/V, positional encoding), embedding training,
  transformer architecture details — the source's own depth boundaries, matching `docs/annual-strategy.md` §7.
- **Not taught yet:** lists (the lists block (lessons 9.1–9.5, 12.0–14.5)). `model.encode([word])` passes a one-item list literal; students copy that form without needing list
  syntax, and `.item()` is explained as "turns the result into a plain number".

## Exit criteria
The student distinguishes characters, words and tokens; explains the context window and why it's measured in
tokens; describes an embedding as a learned vector and cosine similarity as a direction-based estimate of semantic
closeness; explains self-attention conceptually as context updating a word's representation; and builds a working
similarity-based guessing game while correctly stating that its score is not a probability or a fact.

## Checkpoint
Lesson 11.3's "Semantle" project is the unit's capstone, with the source's own 20-point rubric (loading the model once 2,
the similarity function 4, the game loop 3, the attempt counter 2, score display 3, input handling 2, testing 2,
conceptual explanation 2) — see the lesson notes for the full rubric and performance bands. Verified here (in
classroom mode) against all seven of the source's own test cases (win, quit, empty input, single character, a
close word, a far word, and — noted, not separately re-verified — a cross-language guess).

## Enrichment
From the source: let the player choose the secret word without revealing it to another player; a personal-best by
attempt count; comparing a Hebrew guess to an English translation; feedback messages across more score bands
without ever showing the target word; comparing two different embedding models' scores carefully; keeping a
text record of the best guess so far without using a list.
