# Unit 6 — Advanced Language Model

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 10.0–11.3.0 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Every code file now uses the **real**
> `paraphrase-multilingual-MiniLM-L12-v2` model through `sentence-transformers` (the old classroom mock and its invented scores are
> gone). The teacher installs the library and downloads the model **once, at school, before 6.1**; every file was run with the real
> model on Python 3.14. The worksheets use `def` (Unit 3 comes first in the schedule). The three NotebookLM decks are **superseded** —
> new NotebookLM prep folders are ready (`unit6-m1-slides` … `unit6-m3-slides`, 17 / 16 / 13 slides).

## Unit 6.1 — Advanced Language Model

**Topic:** Tokens, Tokenization and IDs

90 minutes: 45 knowledge + 45 lab · **the Semantle demo → old models and their limits → tokens and IDs (real tokenizer) → playground**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Tokenizer_Starter.py`](Tokenizer_Starter.py) | `convert_tokens_to_ids(sentence)` warm-up bug, Tasks 1–4 (info, tokens, count, playground) |
| Teacher | [`Tokenizer_Reference.py`](Tokenizer_Reference.py) | Solutions, one function per task; the old toy tokenizer is an extension |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — pending a new NotebookLM deck |

## Unit 6.2 — Advanced Language Model

**Topic:** The Context Window, the Meaning Map, Self-Attention

90 minutes: 45 knowledge + 45 lab · **the meaning map → self-attention → the context window → `calculate_similarity`**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Meanings_Starter.py`](Meanings_Starter.py) | Spelling-comparison warm-up bug, the `calculate_similarity` fill-in, the verdict program, spelling vs meaning, the playground |
| Teacher | [`Meanings_Reference.py`](Meanings_Reference.py) | Solutions (real scores) |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — pending a new NotebookLM deck |

## Unit 6.3 — Advanced Language Model

**Topic:** Semantic Similarity + the "Semantle" Project — unit checkpoint

90 minutes: Lab + Lab · **the basic game → the attempts counter → percent, 20-emoji thermometer, messages**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including the project rubric |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Semantle_Starter.py`](Semantle_Starter.py) | Swapped-thermometer-symbols warm-up bug, the project brief |
| Teacher | [`Semantle_Reference.py`](Semantle_Reference.py) | Solutions, run with the real model (`basic_game`, `game_with_attempts`, `semantle_game`, `semantle_game_safe`) |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | **Superseded** deck of the v1 build (11 slides) — pending a new NotebookLM deck |
