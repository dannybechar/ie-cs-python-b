# Lessons 16.0–19.1 — Classification

Python B, Grade 8 · 8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice, official master table). 4 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Lessons 16.0–16.2**<br>Classification by Rules — Features and a Separating Line<br>[md](lessons/L01-classification-by-rules.md) · [html](lessons/L01-classification-by-rules.html) · [slides PDF](lessons/L01-classification-by-rules/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 17.0–17.1**<br>Training Set and Test Set, Challenging Cases, Bias — a First Teachable Machine Model<br>[md](lessons/L02-training-and-test.md) · [html](lessons/L02-training-and-test.html) · [slides PDF](lessons/L02-training-and-test/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 3 | **Lessons 18.0–18.1**<br>Accuracy and the Classification Project — Fist or OK<br>[md](lessons/L03-accuracy-and-project.md) · [html](lessons/L03-accuracy-and-project.html) · [slides PDF](lessons/L03-accuracy-and-project/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 4 | **Lessons 19.0–19.1**<br>Connecting the Trained Model to Python — Confidence and Acting on It (Unit Checkpoint)<br>[md](lessons/L04-connecting-the-model.md) · [html](lessons/L04-connecting-the-model.html) · [slides PDF](lessons/L04-connecting-the-model/slides-he.pdf) | 45 / 45 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-classification-by-rules-notes.md`](teacher/L01-classification-by-rules-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-training-and-test-notes.md`](teacher/L02-training-and-test-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L03-accuracy-and-project-notes.md`](teacher/L03-accuracy-and-project-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L04-connecting-the-model-notes.md`](teacher/L04-connecting-the-model-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (6 files) |

## Status and open checks

- 0 of 4 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 16.0–19.1 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Worksheet 16.2 is delivered (the lessons 16.0–16.2 lab follows it); worksheets 17.2, 18.2, 19.2 and 19.3 (Colab) are still missing ⚠️ and their labs are rebuilt from the decks and the teacher notes
> (the unit strategy lists what is assumed). The model code is now the Ministry's `converted_savedmodel.zip` + `TFSMLayer` code (`Ministry_Model_Code.py`,
> **not run here: it needs TensorFlow and a live run with a real exported model before class**); the lab functions run on a clearly-labelled **stand-in** `classify_image()` with fixed answers.
> The four NotebookLM decks are **superseded** — new prep folders are ready (`unit8-m1-slides` … `unit8-m4-slides`).
>
> **Safety note:** Lessons 17.0–17.1 and lessons 18.0–18.1 involve photographing hands — read the Photography Safety section of the lessons 18.0–18.1 lesson notes before lessons 17.0–17.1. Never put the Ministry image archives or student pictures in this repository.

### Lessons 16.0–16.2 — Classification

**Topic:** Classification by Rules, Features, a Separating Line

90 minutes: 45 knowledge + 45 lab · **dog or bagel → the Louvre classifier → features and a separating line → `classify_fruit` and its edge cases**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-classification-by-rules-notes.md`](teacher/L01-classification-by-rules-notes.md) | Lesson plan |
| Student | [`L01-classification-by-rules.md`](lessons/L01-classification-by-rules.md) | Hebrew lab brief |
| Student | [`Classifier_Starter.py`](exercises/Classifier_Starter.py) | Louvre 1860 warm-up bug, stubs for Tasks 1–5 |
| Teacher | [`Classifier_Reference.py`](teacher/solutions/Classifier_Reference.py) | Solutions, one function per task, plus the two teacher demos |
| Teacher | [`slides-he.pdf`](lessons/L01-classification-by-rules/slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lessons 17.0–17.1 — Classification

**Topic:** Training Set and Test Set, Challenging Cases, Bias — a First Teachable Machine Model

90 minutes: 45 knowledge + 45 lab · **training moves the line, the test does not → challenging cases → bias → Teachable Machine hands-on**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-training-and-test-notes.md`](teacher/L02-training-and-test-notes.md) | Lesson plan |
| Student | [`L02-training-and-test.md`](lessons/L02-training-and-test.md) | Hebrew lab brief |
| Student | [`TrainTest_Starter.py`](exercises/TrainTest_Starter.py) | List-equality warm-up bug, stubs for Tasks 1–2 and the if-time task |
| Teacher | [`TrainTest_Reference.py`](teacher/solutions/TrainTest_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L02-training-and-test/slides-he.pdf) | **Superseded** deck of the v1 build (12 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lessons 18.0–18.1 — Classification

**Topic:** Accuracy and the Classification Project — Fist or OK

90 minutes: 45 knowledge + 45 lab · **accuracy = successes / attempts → project planning → the supplied pictures + your own → the 7 test pictures → saving the model**

| For | File | What it is |
|---|---|---|
| Teacher | [`L03-accuracy-and-project-notes.md`](teacher/L03-accuracy-and-project-notes.md) | Lesson plan, including the full photography safety rules |
| Student | [`L03-accuracy-and-project.md`](lessons/L03-accuracy-and-project.md) | Hebrew lab brief |
| Student | [`DataPlan_Starter.py`](exercises/DataPlan_Starter.py) | Inverted-balance-check warm-up bug, stubs for `calculate_accuracy` and `check_variety` |
| Teacher | [`DataPlan_Reference.py`](teacher/solutions/DataPlan_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L03-accuracy-and-project/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — needs regeneration (NotebookLM prep folder refreshed) |

### Lessons 19.0–19.1 — Classification

**Topic:** Connecting the Trained Model to Python — Confidence and Acting on It (unit checkpoint)

90 minutes: 45 knowledge + 45 lab · **the exported ZIP → code + model → the Ministry code as a black box → confidence → act only above 85%**

| For | File | What it is |
|---|---|---|
| Teacher | [`L04-connecting-the-model-notes.md`](teacher/L04-connecting-the-model-notes.md) | Lesson plan, including the 20-point project rubric |
| Student | [`L04-connecting-the-model.md`](lessons/L04-connecting-the-model.md) | Hebrew lab brief |
| Student | [`Model_Starter.py`](exercises/Model_Starter.py) | `1 ok` label warm-up bug, stand-in `classify_image()`, stubs for Tasks 1–3 |
| Student | [`labels_standin.txt`](exercises/labels_standin.txt) | A made-up `labels.txt` in the Teachable Machine format, for the stand-in |
| Teacher | [`Model_Reference.py`](teacher/solutions/Model_Reference.py) | Solutions (stand-in model), verified: accuracy 85.7% on the seven made-up pictures |
| Teacher | [`Ministry_Model_Code.py`](teacher/solutions/Ministry_Model_Code.py) | The Ministry's real `TFSMLayer` code + our `classify_image()` wrapper — **needs a live run with TensorFlow (Python 3.14 may lack it: venv with an older Python or Colab; 19.3 Colab notebook missing ⚠️; checklist in the lessons 19.0–19.1 notes)** |
| Teacher | [`slides-he.pdf`](lessons/L04-connecting-the-model/slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — needs regeneration (NotebookLM prep folder refreshed) |
