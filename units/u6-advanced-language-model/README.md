# Lessons 10.0–11.3 — Advanced Language Model

Python B, Grade 8 · 6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice, official master table). 3 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief, HTML deck, PDFs, worksheets) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code and data files | [`exercises/`](exercises) |
| Plan a lesson, see solutions, answer keys, live-demo code (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | none yet: this repository has no per-unit `feedback/` folder |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the Ministry sources are indexed in [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (label · theme · Hebrew lab brief as `.md`, HTML deck, slide PDFs and worksheets) | Theory / practice min | Review status |
|---|---|---|---|
| 1 | **Lessons 10.0–10.2**<br>Tokens, Tokenization and IDs<br>[md](lessons/L01-tokens.md) · [html](lessons/L01-tokens.html) · [slides PDF](lessons/L01-tokens/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 11.1–11.2**<br>The Meaning Map, Self-Attention and the Similarity Function<br>[md](lessons/L02-meaning-map-and-similarity.md) · [html](lessons/L02-meaning-map-and-similarity.html) · [slides PDF](lessons/L02-meaning-map-and-similarity/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 3 | **Lesson 11.3**<br>The "Semantle" Project (Unit Checkpoint)<br>[md](lessons/L03-semantle.md) · [html](lessons/L03-semantle.html) · [slides PDF](lessons/L03-semantle/slides-he.pdf) | 0 / 90 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-tokens-notes.md`](teacher/L01-tokens-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-meaning-map-and-similarity-notes.md`](teacher/L02-meaning-map-and-similarity-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-semantle-notes.md`](teacher/L03-semantle-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (3 files) |

## Status and open checks

- 0 of 3 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 10.0–11.3.0 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Every code file now uses the **real**
> `paraphrase-multilingual-MiniLM-L12-v2` model through `sentence-transformers` (the old classroom mock and its invented scores are
> gone). The teacher installs the library and downloads the model **once, at school, before lessons 10.0–10.2**; every file was run with the real
> model on Python 3.14. The worksheets use `def` (precondition: the functions block (lessons 4.1–4.6) is taught **before** the advanced-language-model block (lessons 10.0–11.3); if not, the functions are handed out ready-made — stated at the top of each notes file). The lessons 10.0–10.2; 11.1–11.2; 11.3 files were patched on 13 Nov 2026 against the official program (GPT-4/GPT-5 token example, the "fewer tokens in Hebrew" challenge, the sentence-transformers intro, Gemini equivalents, emoji tip, `int()` vs `round()` table; the Semantle site link is still missing — the teacher adds it). The three NotebookLM decks are **superseded** —
> new NotebookLM prep folders are ready (`unit6-m1-slides` … `unit6-m3-slides`, 17 / 16 / 13 slides).

### Lessons 10.0–10.2 — Advanced Language Model

**Topic:** Tokens, Tokenization and IDs

90 minutes: 45 knowledge + 45 lab · **the Semantle demo → old models and their limits → tokens and IDs (real tokenizer) → playground**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-tokens-notes.md`](teacher/L01-tokens-notes.md) | Lesson plan |
| Student | [`L01-tokens.md`](lessons/L01-tokens.md) | Hebrew lab brief |
| Student | [`Tokenizer_Starter.py`](exercises/Tokenizer_Starter.py) | `convert_tokens_to_ids(sentence)` warm-up bug, Tasks 1–4 (info, tokens, count, playground) |
| Teacher | [`Tokenizer_Reference.py`](teacher/solutions/Tokenizer_Reference.py) | Solutions, one function per task; the old toy tokenizer is an extension |
| Teacher | [`slides-he.pdf`](lessons/L01-tokens/slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — needs regeneration (NotebookLM prep folder refreshed 13 Nov 2026) |

### Lessons 11.1–11.2 — Advanced Language Model

**Topic:** The Context Window, the Meaning Map, Self-Attention

90 minutes: 45 knowledge + 45 lab · **the meaning map → self-attention → the context window → `calculate_similarity`**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-meaning-map-and-similarity-notes.md`](teacher/L02-meaning-map-and-similarity-notes.md) | Lesson plan |
| Student | [`L02-meaning-map-and-similarity.md`](lessons/L02-meaning-map-and-similarity.md) | Hebrew lab brief |
| Student | [`Meanings_Starter.py`](exercises/Meanings_Starter.py) | Spelling-comparison warm-up bug, the `calculate_similarity` fill-in, the verdict program, spelling vs meaning, the playground |
| Teacher | [`Meanings_Reference.py`](teacher/solutions/Meanings_Reference.py) | Solutions (real scores) |
| Teacher | [`slides-he.pdf`](lessons/L02-meaning-map-and-similarity/slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — needs regeneration (NotebookLM prep folder refreshed 13 Nov 2026) |

### Lesson 11.3 — Advanced Language Model

**Topic:** Semantic Similarity + the "Semantle" Project — unit checkpoint

90 minutes: Lab + Lab · **the basic game → the attempts counter → percent, 20-emoji thermometer, messages**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-semantle-notes.md`](teacher/L03-semantle-notes.md) | Lesson plan, including the project rubric |
| Student | [`L03-semantle.md`](lessons/L03-semantle.md) | Hebrew lab brief |
| Student | [`Semantle_Starter.py`](exercises/Semantle_Starter.py) | Swapped-thermometer-symbols warm-up bug, the project brief |
| Teacher | [`Semantle_Reference.py`](teacher/solutions/Semantle_Reference.py) | Solutions, run with the real model (`basic_game`, `game_with_attempts`, `semantle_game`, `semantle_game_safe`) |
| Teacher | [`slides-he.pdf`](lessons/L03-semantle/slides-he.pdf) | **Superseded** deck of the v1 build (11 slides) — needs regeneration (NotebookLM prep folder refreshed 13 Nov 2026) |
