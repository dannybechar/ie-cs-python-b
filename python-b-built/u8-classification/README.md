# Unit 8 — Classification

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Staging note:** built in `python-b-built/`, not `units/` — see [`../README.md`](../README.md).
> **Model note:** `classify_image()` runs in classroom (mock) mode — no Teachable Machine model, TensorFlow/Keras
> install, or files required. Before teaching 8.4 live, the teacher exports a real model; see `unit-strategy.md`'s
> scope decisions. Units 8.2–8.3's Teachable Machine work is a browser + camera activity outside any code file.
> **Safety note:** Unit 8.3 involves photographing hands — read its lesson notes' Photography Safety section before
> that meeting.

## Unit 8.1 — Classification

**Topic:** Classification, Features, a Decision Boundary

90 minutes: 45 knowledge + 45 lab · **category, feature, feature space → decision boundary → a rule-based classifier**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Classifier_Starter.py`](Classifier_Starter.py) | Unnormalized-case warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`Classifier_Reference.py`](Classifier_Reference.py) | Solutions, one function per task |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Hebrew slide deck (15 slides, NotebookLM, patched) |

## Unit 8.2 — Classification

**Topic:** The ML Process + Teachable Machine

90 minutes: 45 knowledge + 45 lab · **the ML pipeline → training vs test → data leakage → confidence vs accuracy**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`TrainTest_Starter.py`](TrainTest_Starter.py) | List-equality warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`TrainTest_Reference.py`](TrainTest_Reference.py) | Solutions, one function per task |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Hebrew slide deck (12 slides, NotebookLM, patched) |

## Unit 8.3 — Classification

**Topic:** Project Planning, Data, Bias

90 minutes: 45 knowledge + 45 lab · **category definitions → diversity matrix → collection plan → bias experiments**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including full photography safety rules |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`DataPlan_Starter.py`](DataPlan_Starter.py) | Inverted-balance-check warm-up bug, stubs for Tasks 1–2 |
| Teacher | [`DataPlan_Reference.py`](DataPlan_Reference.py) | Solutions, one function per task |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | Hebrew slide deck (13 slides, NotebookLM, patched) |

## Unit 8.4 — Classification

**Topic:** Accuracy, Export, Loading the Model in Python — unit checkpoint

90 minutes: 45 knowledge + 45 lab · **calculate_accuracy → export → image preprocessing → the prediction pipeline**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including the project rubric |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Accuracy_Starter.py`](Accuracy_Starter.py) | Unstripped-label warm-up bug, the project brief |
| Teacher | [`Accuracy_Reference.py`](Accuracy_Reference.py) | Solutions (classroom mode), confirmed against the source's ≈85.7% example |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | Hebrew slide deck (13 slides, NotebookLM, patched) |
