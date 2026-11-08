# Unit 8 — Classification

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

8 academic hours = 4 meetings = 360 minutes (180 theory / 180 practice).

> **Reworked 8 Nov 2026 to the Ministry materials** (files 16.0–19.1 — see
> [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)). Worksheets 16.2, 17.2, 18.2, 19.2 and 19.3 were not delivered; their labs are rebuilt from the decks, the teacher notes
> and the teacher solution 16.2.0 (the unit strategy lists what is assumed). The model code is now the Ministry's `converted_savedmodel.zip` + `TFSMLayer` code (`Ministry_Model_Code.py`,
> **not run here: it needs TensorFlow and a live run with a real exported model before class**); the lab functions run on a clearly-labelled **stand-in** `classify_image()` with fixed answers.
> The four NotebookLM decks are **superseded** — new prep folders are ready (`unit8-m1-slides` … `unit8-m4-slides`).
>
> **Safety note:** Units 8.2 and 8.3 involve photographing hands — read the Photography Safety section of the 8.3 lesson notes before 8.2. Never put the Ministry image archives or student pictures in this repository.

## Unit 8.1 — Classification

**Topic:** Classification by Rules, Features, a Separating Line

90 minutes: 45 knowledge + 45 lab · **dog or bagel → the Louvre classifier → features and a separating line → `classify_fruit` and its edge cases**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Classifier_Starter.py`](Classifier_Starter.py) | Louvre 1860 warm-up bug, stubs for Tasks 1–5 |
| Teacher | [`Classifier_Reference.py`](Classifier_Reference.py) | Solutions, one function per task, plus the two teacher demos |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | **Superseded** deck of the v1 build (15 slides) — pending a new NotebookLM deck |

## Unit 8.2 — Classification

**Topic:** Training Set and Test Set, Challenging Cases, Bias — a First Teachable Machine Model

90 minutes: 45 knowledge + 45 lab · **training moves the line, the test does not → challenging cases → bias → Teachable Machine hands-on**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`TrainTest_Starter.py`](TrainTest_Starter.py) | List-equality warm-up bug, stubs for Tasks 1–2 and the if-time task |
| Teacher | [`TrainTest_Reference.py`](TrainTest_Reference.py) | Solutions, one function per task |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | **Superseded** deck of the v1 build (12 slides) — pending a new NotebookLM deck |

## Unit 8.3 — Classification

**Topic:** Accuracy and the Classification Project — Fist or OK

90 minutes: 45 knowledge + 45 lab · **accuracy = successes / attempts → project planning → the supplied pictures + your own → the 7 test pictures → saving the model**

| For | File | What it is |
|---|---|---|
| Teacher | [`m3-lesson-notes.md`](m3-lesson-notes.md) | Lesson plan, including the full photography safety rules |
| Student | [`m3-lab-brief-he.md`](m3-lab-brief-he.md) | Hebrew lab brief |
| Student | [`DataPlan_Starter.py`](DataPlan_Starter.py) | Inverted-balance-check warm-up bug, stubs for `calculate_accuracy` and `check_variety` |
| Teacher | [`DataPlan_Reference.py`](DataPlan_Reference.py) | Solutions, one function per task |
| Teacher | [`m3-slides-he.pdf`](m3-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — pending a new NotebookLM deck |

## Unit 8.4 — Classification

**Topic:** Connecting the Trained Model to Python — Confidence and Acting on It (unit checkpoint)

90 minutes: 45 knowledge + 45 lab · **the exported ZIP → code + model → the Ministry code as a black box → confidence → act only above 85%**

| For | File | What it is |
|---|---|---|
| Teacher | [`m4-lesson-notes.md`](m4-lesson-notes.md) | Lesson plan, including the 20-point project rubric |
| Student | [`m4-lab-brief-he.md`](m4-lab-brief-he.md) | Hebrew lab brief |
| Student | [`Model_Starter.py`](Model_Starter.py) | `1 ok` label warm-up bug, stand-in `classify_image()`, stubs for Tasks 1–3 |
| Student | [`labels_standin.txt`](labels_standin.txt) | A made-up `labels.txt` in the Teachable Machine format, for the stand-in |
| Teacher | [`Model_Reference.py`](Model_Reference.py) | Solutions (stand-in model), verified: accuracy 85.7% on the seven made-up pictures |
| Teacher | [`Ministry_Model_Code.py`](Ministry_Model_Code.py) | The Ministry's real `TFSMLayer` code + our `classify_image()` wrapper — **needs a live run with TensorFlow** |
| Teacher | [`m4-slides-he.pdf`](m4-slides-he.pdf) | **Superseded** deck of the v1 build (13 slides) — pending a new NotebookLM deck |
