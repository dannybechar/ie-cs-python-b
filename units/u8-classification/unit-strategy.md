# Unit 8 — Classification

**8h = 4 Theory + 4 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 8 (pp. 19–21); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked 8 Nov 2026 to the Ministry teaching materials (files 16.0–19.1; the worksheets 16.2, 17.2, 18.2, 19.2 and 19.3 were not delivered);
awaiting re-approval. The v1 build (approved earlier) came from `Downloads\python-b-codex\python_b_unit08_classification_complete_unit.md`, used `keras_Model.h5` and a
mock model, and ordered the topics differently. Decks: superseded, new NotebookLM decks pending.

## Official topics and hours

Unit totals from the master table (4 theory / 4 practice = 360 minutes), matching the chapter's own table (intro + naive classifier 1/1, the ML process + Teachable Machine 1/1, the project's
four hours 2/2).

| Topic | Planned in | Ministry files | Minutes (T / P) | Status |
|---|---|---|---:|---|
| Classification by rules, features, the separating line; `classify_fruit` | 8.1 (45 T + 45 P) | 16.0, 16.1, 16.2.0 | 45 / 45 | 🔶 |
| Training set and test set, challenging cases, bias, first Teachable Machine try | 8.2 (45 T + 45 P) | 17.0, 17.0.1, 17.1 | 45 / 45 | 🔶 |
| Accuracy; the fist / OK project; saving the model | 8.3 (45 T + 45 P) | 18.0, 18.1 + the two image archives | 45 / 45 | 🔶 |
| The trained model inside Python (`TFSMLayer`), confidence, "act only above 85%" | 8.4 (45 T + 45 P) | 19.0, 19.1 | 45 / 45 | 🔶 |
| **Total** | | | **180 / 180** | |

Chapter goals (source §1, thirteen in all):

1. Define a classification problem, category, feature and feature space → 8.1
2. Explain a decision boundary between categories → 8.1
3. Choose relevant, distinguishing features for a classification task → 8.1
4. Implement a rule-based classifier with compound conditions → 8.1
5. Identify edge cases where rigid rules fail → 8.1
6. Describe the ML process stages: collect, label, train, test, improve → 8.2
7. Distinguish a training set from a test set; avoid leakage between them → 8.2
8. Build an image classifier in Teachable Machine → 8.2–8.3
9. Plan a diverse image collection (background, lighting, angle, user traits) → 8.3
10. Calculate accuracy (successes / attempts) → 8.3–8.4
11. Distinguish a single prediction's confidence from a test set's accuracy → 8.2–8.4
12. Export a model and integrate its loading and prediction code in Python → 8.3–8.4
13. Identify a visual bias and propose a concrete data change → 8.2–8.4

## Unit 8.1 — Knowledge + Lab: Classification by Rules, Features, a Separating Line
- classification (dog or bagel), the two ways to teach a computer (rules vs data); the Louvre classic / modern classifier with a trace table; features: relevant and distinguishing (cat vs dog);
  two features, the plane and a separating line (`y = mx + b`); `classify_fruit(softness, color)` and why rules do not scale.
- lab: warm-up bug (the painting from exactly 1860 falls in the gap), Spotify-style playlists by year and by length, choosing features, `classify_fruit` and its edge cases (the unripe banana, softness 2),
  why "mood" is hard.

## Unit 8.2 — Knowledge + Lab: Training Set and Test Set, Challenging Cases, Bias
- the two stages of machine learning (training moves the line, the test does not), challenging cases, bias (glasses, skin color), responsibility, hand gestures and sign language, a live Teachable Machine demo (17.0.1 guide).
- lab: warm-up bug (list equality is not a leak check), a first quick model with a deliberate background shortcut, a log table, the 17.1 discussion questions including "no category fits", `describe_trial`, `count_correct`.

## Unit 8.3 — Knowledge + Lab: Accuracy and the Fist / OK Project
- accuracy = successes / attempts (the four-picture walk-through), classification in daily life, project planning (category rule, diversity matrix, audit, privacy), the supplied training pictures (155 fist, 114 ok)
  plus the students' own, the 7 hidden test pictures, **saving `converted_savedmodel.zip`**.
- lab: warm-up bug (inverted balance check), `calculate_accuracy(successes, attempts)`, `check_variety`, the project with one controlled bias experiment, accuracy on the 7 test pictures, export.

## Unit 8.4 — Knowledge + Lab: The Trained Model in Python (unit checkpoint)
- the exported ZIP (`model.savedmodel` + `labels.txt`), why code + model, the Ministry code as a black box (`TFSMLayer`, `preprocess_image`, `argmax`; edit only the three paths), confidence 99% vs 73%, act only above 85%.
- lab: warm-up bug (the label is `1 ok`, not `ok`), `report`, `decide`, `evaluate` (accuracy on 7 test pictures), the model report. Real model: `Ministry_Model_Code.py`; a clearly-labelled stand-in runs without TensorFlow.

### Scope decisions
- **The Ministry materials are the source (8 Nov 2026).** 16.x, 17.x, 18.x and 19.x map one-to-one to our four meetings, in order: **8.1 = 16.0 / 16.1 / 16.2.0, 8.2 = 17.0 / 17.0.1 / 17.1, 8.3 = 18.0 / 18.1
  (+ the image archives), 8.4 = 19.0 / 19.1.** We keep our four meetings and 360 minutes (teacher's decision: hours from the master table).
- **Worksheets 16.2, 17.2, 18.2, 19.2 and 19.3 were not delivered.** 16.2's tasks are rebuilt from its teacher solution 16.2.0. The 17.2 / 18.2 / 19.2 labs are **assumed** from the teacher notes and decks
  (17.0: two hand-gesture categories, train, test, discussion; 18.0: import the supplied pictures, add your own, train, test on the 7 teacher pictures, save the model; 19.0: extract the ZIP, edit the paths, run).
  No Ministry content was invented for them; the notes say what is assumed. 19.3 (the Colab notebook) is missing.
- **`def` and lists are used** (Unit 8 follows Units 3 and 7), as the Ministry does. Still never: nested loops, lists of lists, tuples, sets, dictionaries, comprehensions, classes, default arguments.
  Our code returns a **list** `[label, confidence]` instead of a pair. The Ministry's own `load_labels` uses a list comprehension: it is part of the black-box file, never a student task.
- **The old `keras_Model.h5` / `load_model` flow and the mock-only design are replaced** by the Ministry's `converted_savedmodel.zip` and `tf.keras.layers.TFSMLayer(model_path, call_endpoint="serving_default")`,
  `preprocess_image` (RGB, 224 × 224, `/ 255.0`, `expand_dims`), `argmax` and the confidence. The real code is in `Ministry_Model_Code.py` (**not run here**: TensorFlow is not installed; its pre-processing
  and control flow were checked with a stub `tensorflow` module). A **stand-in** `classify_image()` (fixed answers for seven made-up picture names, no model, no photos) is kept in
  `Model_Starter.py` / `Model_Reference.py` so the lab functions can be verified and run without TensorFlow; `USE_REAL_MODEL = True` switches to the real code.
- **Ministry-deck bugs not copied:** the Louvre slides' second code version (p. 17: an unindented `paintings` line and `1900` for `1860`) and `__name__ _= "__main__"` in the model code (p. 15). The 1860 boundary
  bug itself is **kept as the 8.1 warm-up**, and the frontal Louvre trace uses data without an 1860 painting, so students discover the gap themselves. The Ministry's `classify_fruit` has the same kind of
  gap at `softness == 2`; we turn it into a discussion.
- **Added to the Ministry flow (kept from v1; the Ministry is silent):** the data-leakage idea (`has_leak`), the background-bias experiment, `describe_trial` / `count_correct`, the category-definition rule, the diversity
  matrix, the pre-training audit, controlled bias experiments, `check_balance` / `check_variety`, the photography privacy rules and the 20-point checkpoint rubric.
  **Dropped from v1:** `classify_fruit(color, shape, hardness)` with `.lower()` (replaced by the Ministry's two-feature function), the `classify_level` trace (the weather classifier stays as "if time"), the
  Keras-in-a-comment mock, `calculate_accuracy(actual, predicted)` over lists (accuracy is now `successes / attempts`, the Ministry's definition) and the `.strip()` label warm-up (replaced by the `1 ok` label bug).
- **Images:** the two archives (`תמונות לאימון`: 269 AI-generated pictures, 155 fist / 114 ok; `תמונות למבחן`: 7 test pictures) stay in the teacher's Drive. They are never copied into the repository; files refer to
  them by name. Our stand-in uses invented names (`test_1_ok.png` …), not the Ministry's.
- **Photography safety, kept from v1:** hands only, consent, no private information in the background, school storage policy, no publishing without permission (full text in the 8.3 notes; a short reminder in 8.2).
- **Needs a live run with the real service:** the Teachable Machine export and `Ministry_Model_Code.py` with TensorFlow (Thonny or Colab). TensorFlow may not install on the newest Python versions; the Ministry uses Colab.
- **Not taught:** a confusion matrix, precision / recall / F1, loss functions, gradient descent, building a classifier from scratch (out of scope per `docs/annual-strategy.md` §7); TensorFlow internals.

## Exit criteria
The student defines a classification problem in terms of categories and features, implements a rule-based classifier and finds its edge cases, describes the two stages of machine learning and why training and
test data must stay separate, plans a diverse image collection and runs at least one controlled bias experiment, computes accuracy as successes over attempts, and connects a trained model to a Python
program that acts only when the confidence is high enough — while correctly distinguishing confidence from accuracy throughout.

## Checkpoint
8.4's model report and `evaluate` on the 7 test pictures are the unit's capstone, with the 20-point rubric kept from v1 (problem definition 2, data planning 4, test set 3, accuracy calculation 3, bias testing 3,
loading in Python 3, critical explanation 2) — see the 8.4 lesson notes for the performance bands. The functions are verified here with the stand-in; the live Teachable Machine export and the real model
run are the teacher's separate, hands-on step before class.

## Enrichment
Accuracy computed separately per category; counting errors by which shooting condition caused them; comparing a first model to an improved one on the same test pictures; a confidence threshold that
returns `"uncertain"` and the cost of choosing it; testing how the training-set size affects results without changing the test set.
