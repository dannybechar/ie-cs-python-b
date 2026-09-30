# Unit 8 — Classification

**8h = 4 Theory + 4 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 8 (pp. 19–21); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 4 meetings built and approved by the teacher.
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit08_classification_complete_unit.md` —
one detailed document covering all four meetings, including its own exact 90-minute clock tables and meeting split.

## Official topics and hours

Unit totals from the master table (4 theory / 4 practice), matching the chapter's own table exactly (intro + naive
classifier 1/1, the ML process + Teachable Machine 1/1, the project's four hours 2/2, total 4/4 — for once both
agree, same as Unit 4 and Unit 6).

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| Classification, features, the decision boundary; a naive rule-based classifier | 8.1 (45 T + 45 P) | 45 / 45 | ✅ |
| The ML process; training vs. test; first Teachable Machine try | 8.2 (45 T + 45 P) | 45 / 45 | ✅ |
| Project planning, 100+ images per category, bias experiments | 8.3 (45 T + 45 P) | 45 / 45 | ✅ |
| Accuracy, export, loading the model in Python | 8.4 (45 T + 45 P) | 45 / 45 | ✅ |
| **Total** | | **180 / 180** | |

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
10. Calculate accuracy from parallel lists of true labels and predictions → 8.4
11. Distinguish a single prediction's confidence from a test set's accuracy → 8.2, 8.4
12. Export a model and integrate its loading and prediction code in Python → 8.4
13. Identify a visual bias and propose a concrete data change → 8.2–8.3

## Unit 8.1 — Knowledge + Lab: Classification, Features, a Decision Boundary
- classification, class/label, feature, feature space, decision boundary, edge case; sorting objects into two groups
  before naming the rule.
- a relevant vs. distinguishing vs. incidental feature (the song year/album color/title length example); a
  one-dimensional boundary (`year <= 2010`) as a developer's decision, not a natural fact.
- a rule-based fruit classifier with compound conditions; where it fails (a green, hard banana; a yellow apple);
  why "add more rules" doesn't scale.
- lab: an unnormalized-case warm-up bug, a weather-based rule-based classifier with two found edge cases, a
  trace-before-run drill.

## Unit 8.2 — Knowledge + Lab: The ML Process + Teachable Machine
- the pipeline: define the problem → define categories → collect and label training data → train → test on new
  data → measure and analyze errors → improve the data or design.
- training set vs. test set; **data leakage** — if the same image appears in both, the measurement is optimistic and
  doesn't test real generalization.
- a first, deliberately quick and unbalanced Teachable Machine experiment: two temporary categories, a small
  collection, immediate testing under a different background/lighting — the point is to **discover** how incidental
  correlations creep in, not to build a good model yet.
- confidence (one prediction's score) vs. accuracy (the test set's overall correct rate) — a model can be
  confidently wrong.
- lab: a whole-list-equality warm-up bug for leak detection, a trial-description function, a match-counting function.

## Unit 8.3 — Knowledge + Lab: Project Planning, Data, Bias
- defining the two project categories (`fist`, `ok`) with an agreed labeling rule for ambiguous cases, decided
  **before** photographing, never changed mid-collection without documenting it.
- a diversity matrix (background, lighting, angle, distance, hand, sleeve/glove, users) — not exhaustive coverage,
  but enough variation that no category is identifiable by one incidental factor alone.
- a collection plan: 100+ images per category, similar counts across categories, several separate shooting bursts,
  shared backgrounds/lighting across both categories, external test images held aside from the start.
- controlled bias experiments changing one factor at a time (background, lighting, user, angle) and logging
  truth/prediction/confidence/factor/conclusion.
- lab: an inverted balance-check warm-up bug, a per-category diversity-count checker, a checklist-coverage counter
  for which bias experiments were actually run.

## Unit 8.4 — Knowledge + Lab: Accuracy, Export, Loading the Model (unit checkpoint)
- computing accuracy from two parallel lists (`correct / total × 100`), guarding empty and mismatched-length input.
- why accuracy alone isn't the whole story: a small test set is noisy, one category can hide behind a good overall
  average, accuracy doesn't explain *why* an error happened.
- exporting a Keras model and its `labels.txt`; the image-processing steps before prediction (RGB, resize to
  224×224, normalize, batch of 1, `predict`, `argmax`, map the index back to a label) — and the real-world trap of
  unstripped label text making a correct prediction look wrong.
- lab: a real-world stripped-vs-unstripped label warm-up bug, confirming accuracy on the source's own 7-item
  example (≈85.7%), then the checkpoint: a classroom-mode `classify_image` wired into a full test-set prediction and
  accuracy report.

### Scope decisions
- **The source document is the only material and is unusually complete** — clock tables (verified to sum to 90 for
  each meeting), worked code, a full privacy/safety section for photographing hands, a project rubric and closing
  summary questions. Followed closely; adapted into the house lesson-notes/lab-brief split and warm-up-bug
  convention.
- **No Teachable Machine training, no TensorFlow/Keras model, and no photography happens in the built/verified
  code, by design.** Units 8.2–8.3's hands-on model-building work is inherently a browser + camera activity outside
  any code file's scope — the lesson notes describe it in full but it isn't something to "run" here. Unit 8.4's
  `classify_image()` defaults to **classroom (mock) mode**: it guesses a label from the file name instead of loading
  a real exported model, so the file runs and is verifiable with plain `python`, no installed packages or model
  files required. The real Keras/PIL/NumPy loading and preprocessing code (taken directly from the source, which
  itself is taken from Teachable Machine's official export snippet) is a clearly marked, commented block, ready to
  fill in once the teacher has an exported model to test with. This mirrors Units 4 and 6's `ask_ai()` /
  `calculate_similarity()` pattern exactly.
- **Photography safety, verbatim from the source, belongs in the lesson notes, not the code.** Hands only, no faces
  needed; consent before photographing another person; no names, documents, personal screens or private information
  in the background; images handled per school policy and deleted when no longer needed; no publishing a model or
  image collection link without permission; gestures checked for cultural appropriateness. These rules are stated
  in full in 8.3's lesson notes and are non-negotiable regardless of how the meeting is taught.
- **Not taught:** a confusion matrix, precision/recall/F1, loss functions, gradient descent, or building a
  classifier "from scratch" (all explicitly out of scope per `docs/annual-strategy.md` §7); these appear only as
  named **enrichment** ideas below, never as required content.

## Exit criteria
The student defines a classification problem in terms of categories and features, implements a rule-based
classifier and finds its edge cases, describes the ML process and why training and test data must stay separate,
plans a diverse image collection and runs at least one controlled bias experiment, computes accuracy from parallel
lists, and integrates a model-loading/prediction pipeline into a Python program — while correctly distinguishing
confidence from accuracy throughout.

## Checkpoint
8.4's classification project (fist vs. OK) is the unit's capstone, with the source's own 20-point rubric (problem
definition 2, data planning 4, test set 3, accuracy calculation 3, bias testing 3, loading in Python 3, critical
explanation 2) — see the lesson notes for the full rubric and performance bands. The accuracy function and the
prediction pipeline are verified here in classroom mode; the live Teachable Machine model, its export, and a real
run in Thonny are the teacher's separate, hands-on step before class (see Tool Notes throughout).

## Enrichment
From the source: accuracy computed separately per category; counting errors by which shooting condition caused
them; comparing a first model to an improved one on the same test set; adding a confidence threshold below which
the program returns `"uncertain"` (and discussing the cost of that threshold); a four-counter confusion matrix for
two categories; testing how training-set size affects results without changing the test set.
