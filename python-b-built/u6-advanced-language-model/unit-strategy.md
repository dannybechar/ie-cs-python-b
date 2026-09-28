# Unit 6 — Advanced Language Model

**6h = 2 Theory + 4 Practice = 3 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 6 (pp. 15–16); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 built from the codex material only — **staged in `python-b-built/`, not yet in `units/`.**
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit06_advanced_language_models_complete_unit.md` —
one detailed document covering all three meetings, including its own exact 90-minute clock tables and meeting split.

## Official topics and hours

Unit totals from the master table (2 theory / 4 practice), matching the chapter's own table exactly (tokens 1/2,
meaning-map + attention + project 1/2, total 2/4 — for once both agree).

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| Tokens, tokenization, token IDs; a simple learning tokenizer | 6.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| Context window, the meaning map, self-attention | 6.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| Semantic similarity + the "Semantle" project | 6.3 (0 T + 90 P) | 0 / 90 | 🔶 |
| **Total** | | **90 / 180** | |

Chapter goals (source §1, eleven in all):

1. A token is a model's processing unit, not necessarily a whole word → 6.1
2. A tokenizer converts text to tokens and to numeric IDs from the model's own vocabulary → 6.1
3. Distinguish characters, words and tokens → 6.1
4. Explain the context window and why it's limited in tokens → 6.2
5. Describe an embedding as a numeric vector of learned meaning features → 6.2
6. Vector closeness can estimate semantic similarity → 6.2–6.3
7. Explain, conceptually, how self-attention uses context to update a word's representation in a sentence → 6.2
8. Install and import a multilingual embeddings model for local use → 6.3
9. Implement `calculate_similarity(text_a, text_b)` returning a numeric score → 6.3
10. Build a game with a guess loop, an attempt counter, a percent display and a graphical closeness meter → 6.3
11. Explain that a similarity score is not a probability, a truth or human understanding → every meeting

## Unit 6.1 — Knowledge + Lab: Tokens, Tokenization and IDs
- token vs. character vs. word; a token isn't necessarily a whole word; the pipeline text → tokenizer → tokens →
  numeric IDs → model.
- a teacher-led demo with a real tokenizer (a downloaded library — see Tool Note) shows the concept; students build
  and extend their **own** small learning tokenizer, explicitly not a stand-in for a real model's vocabulary.
- controlled experiments changing one factor at a time (case, punctuation, a space, language, word length) and
  documenting hypothesis → result → conclusion.
- lab: a missing-final-flush warm-up bug, extending the tokenizer to mark spaces, a token-counting function used
  for the experiments.

## Unit 6.2 — Knowledge + Lab: The Context Window, the Meaning Map, Self-Attention
- the context window: what fills it (system instructions, prior turns, the current message, supplied documents,
  the response being generated) and what happens when it's exceeded — not human memory, no guarantee of correct use.
- spelling similarity vs. semantic similarity; embeddings as high-dimensional vectors, a 2D class map as a
  simplified illustration only; cosine similarity at a conceptual level (no formula).
- self-attention, conceptually: the same spelling (`bank`) gets a different contextual representation depending on
  surrounding words; never described as human-like thought or understanding.
- lab: a spelling-vs-meaning warm-up bug, comparing a rule-based "meaning" stand-in against a simple spelling-overlap
  function on word pairs that expose the difference.

## Unit 6.3 — Lab + Lab: Semantic Similarity + the "Semantle" Project (unit checkpoint)
- loading a real embeddings model **once**, outside any function or loop; `calculate_similarity` returning a
  `float`; clamping a score to `[0, 1]` for display only (raw cosine similarity can be negative); a percent is a
  **display value**, not a probability.
- a character-repeated closeness meter, always exactly 10 characters long.
- the guessing-game loop: an attempt counter that only grows on a valid guess, `quit` to exit, a win decided by
  matching the target word, not by score alone.
- lab: a swapped-meter-colors warm-up bug (checked against the source's own two worked examples), completing
  `calculate_similarity`, then the "Semantle" game itself — the unit's capstone.

### Scope decisions
- **The source document is the only material and is unusually complete** — clock tables (verified to sum to 90 for
  each meeting), worked code, common mistakes, a no-model fallback, a project rubric and closing summary questions.
  Followed closely; adapted into the house lesson-notes/lab-brief split and warm-up-bug convention.
- **The real embeddings model is not used in the built/verified code, by design.** The source itself gives exactly
  this fallback — `calculate_similarity_demo`, "not an AI model … only to allow practicing the game" — and warns
  the first download is large and must happen before class, with a no-internet alternative ready. Every code file
  here defaults to **classroom (mock) mode**: `calculate_similarity()` uses the source's own rule-based stand-in
  (renamed `meaning_score_demo`, reused unchanged in 6.2 and 6.3), so files run and are verifiable with plain
  `python`, no download or internet required. The real `sentence-transformers` call is a clearly marked, commented
  block, ready to fill in once the teacher has installed and cached the model. This mirrors Unit 4's `ask_ai()`
  pattern exactly.
- **6.1's teacher demo with a real HuggingFace tokenizer** (`AutoTokenizer`) is kept in the lesson notes as an
  **optional live demonstration**, not something students run or that the built code depends on — the source frames
  it the same way ("a demonstration tool … students focus on the output, not the structure"). The graded student
  work is entirely the hand-written `simple_tokenize`, which needs no download at all.
- **Not taught:** the cosine-similarity formula, attention math (Q/K/V, positional encoding), embedding training,
  transformer architecture details — the source's own depth boundaries, matching `docs/annual-strategy.md` §7.
- **Not taught yet:** lists (Unit 7) — `calculate_similarity`'s real version returns a tensor that would normally be
  indexed as a two-item collection; the source's own code already isolates that behind `.item()`/indexing the
  teacher demo provides, so no list syntax is required from students here.

## Exit criteria
The student distinguishes characters, words and tokens; explains the context window and why it's measured in
tokens; describes an embedding as a learned vector and cosine similarity as a direction-based estimate of semantic
closeness; explains self-attention conceptually as context updating a word's representation; and builds a working
similarity-based guessing game while correctly stating that its score is not a probability or a fact.

## Checkpoint
6.3's "Semantle" project is the unit's capstone, with the source's own 20-point rubric (loading the model once 2,
the similarity function 4, the game loop 3, the attempt counter 2, score display 3, input handling 2, testing 2,
conceptual explanation 2) — see the lesson notes for the full rubric and performance bands. Verified here (in
classroom mode) against all seven of the source's own test cases (win, quit, empty input, single character, a
close word, a far word, and — noted, not separately re-verified — a cross-language guess).

## Enrichment
From the source: let the player choose the secret word without revealing it to another player; a personal-best by
attempt count; comparing a Hebrew guess to an English translation; feedback messages across more score bands
without ever showing the target word; comparing two different embedding models' scores carefully; keeping a
text record of the best guess so far without using a list.
