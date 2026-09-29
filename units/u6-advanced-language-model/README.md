# Unit 6 — Advanced Language Model

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

6 academic hours = 3 meetings = 270 minutes (90 theory / 180 practice).

> **Model note:** every file runs in classroom (mock) mode — `calculate_similarity()` uses a rule-based stand-in,
> no model download required. Before teaching 6.3 live, the teacher installs `sentence-transformers` and downloads
> the multilingual model once; see `unit-strategy.md`'s scope decisions.

## Unit 6.1 — Advanced Language Model

**Topic:** Tokens, Tokenization and IDs

90 minutes: 45 knowledge + 45 lab · **token vs word vs character → the pipeline → controlled experiments → a learning tokenizer**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Tokenizer_Starter.py`](Tokenizer_Starter.py) | Missing-final-flush warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`Tokenizer_Reference.py`](Tokenizer_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Hebrew slide deck (15 slides, NotebookLM, patched) |

## Unit 6.2 — Advanced Language Model

**Topic:** The Context Window, the Meaning Map, Self-Attention

90 minutes: 45 knowledge + 45 lab · **context window → spelling vs meaning → embeddings → self-attention**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Meanings_Starter.py`](Meanings_Starter.py) | Spelling-comparison warm-up bug, the spelling-vs-meaning task |
| Teacher | [`Meanings_Reference.py`](Meanings_Reference.py) | Solutions |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Hebrew slide deck (15 slides, NotebookLM, patched) |

## Unit 6.3 — Advanced Language Model

**Topic:** Semantic Similarity + the "Semantle" Project — unit checkpoint

90 minutes: Lab + Lab · **calculate_similarity → clamped display score → closeness meter → the guessing game**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including the project rubric |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Semantle_Starter.py`](Semantle_Starter.py) | Swapped-meter-colors warm-up bug, the project brief |
| Teacher | [`Semantle_Reference.py`](Semantle_Reference.py) | Solutions, all 7 official test cases verified (classroom mode) |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Hebrew slide deck (11 slides, NotebookLM, patched) |
