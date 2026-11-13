# Lessons 19.0–19.1 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Connecting the Trained Model to Python — Confidence and Acting on It (Unit Checkpoint)

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny with TensorFlow installed, **or Google Colab as the Ministry does** (19.1 p. 31 points to a Colab notebook, 19.3) — see Tool Note
**Source of inspiration:** Ministry teaching materials **19.0** (teacher emphases) and **19.1** (deck, 33 slides: the exported ZIP, why connect a model to code, the
code as a black box, confidence). The worksheets **19.2** and **19.3** (the Colab notebook) are still missing ⚠️ (never invented); the lab follows 19.0 / 19.1: extract the ZIP, find the three paths, edit
only them, run on test pictures. The v1 `keras_Model.h5` / `load_model` flow and its mock are **replaced** by the Ministry's `converted_savedmodel.zip` and `TFSMLayer`; a small
clearly-labelled stand-in is kept so the lab functions can be verified and run without TensorFlow. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the exported model**.
**Prerequisite:** functions (lessons 4.1–4.6), lists (lessons 9.1–9.5, 12.0–14.5), the saved `converted_savedmodel.zip` from lessons 18.0–18.1.

---

## 1. Position in the classification block (lessons 16.0–19.1)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 16.0–16.2 | classification by rules, features, a separating line | 45 / 45 |
| Lessons 17.0–17.1 | training set and test set, challenging cases, bias, first Teachable Machine try | 45 / 45 |
| Lessons 18.0–18.1 | accuracy, the fist / OK project, export | 45 / 45 |
| **Lessons 19.0–19.1 (this)** | **the trained model inside Python, confidence, acting only when sure** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 20–21) | Covered here |
|---|---|
| Goal 10: calculate accuracy | ✅ `evaluate`: accuracy over the 7 test pictures |
| Goal 11: confidence vs accuracy | ✅ 99% vs 73%, "act only above 85%" |
| Goal 12: export a model and integrate loading and prediction in Python | ✅ the Ministry code, run on the students' own model |
| Goal 13: identify a visual bias | ✅ the OK drawing that was classified as a fist |

### Deliberate exclusions
How TensorFlow loads a model, what a tensor is, why `/ 255.0`: the Ministry treats the code as a **black box** ("we are not going to be scared of long code"), and so do we.

---

## 3. Lesson Goal

**A trained model only decides which category a picture belongs to; a Python program turns that decision into action. The program prepares the picture the same way every time,
reads the label and the confidence, and acts only when the confidence is high enough.**

---

## 4. Core Mental Models

The Ministry code ([`Ministry_Model_Code.py`](Ministry_Model_Code.py), deck 19.1 pp. 15–24) is read as four blocks:

| Block | What it does | Students edit it? |
|---|---|---|
| `import` lines | bring in `tensorflow`, `numpy`, `PIL` | no |
| `load_labels(labels_path)` | reads the category names from the text file | no |
| `preprocess_image(image_path, target_size)` | opens the picture, `convert("RGB")`, resizes to 224 × 224, divides by `255.0`, adds the batch dimension (`expand_dims`) | no |
| `main()` | loads the model with `tf.keras.layers.TFSMLayer(model_path, call_endpoint="serving_default")`, processes the picture, takes the highest score (`argmax`), looks up the label, prints label and confidence | **only** `model_path`, `labels_path`, `image_path` |

- The exported archive: `converted_savedmodel.zip` is a ZIP ("a magic box packing files") — extract it (right-click, *Extract All*) to get the folder **`model.savedmodel`** and **`labels.txt`**.
  It is the model's "backpack": everything it needs to decide.
- A model alone only says which category; **code** lets it matter: a camera or satellite picture → the model's category → check category and confidence → act (the forest-fire alert, 19.1 p. 10).
- **Confidence level:** a good model not only says "OK" but says it with a high confidence. Example: category `OK`, confidence 0.99 → we can act. Another picture: the sign is OK but the model
  answered with confidence 0.73 and the wrong category (maybe it was never trained on drawings, or only on fists in drawings) → go back to the training data, and in the program **require
  a high confidence (for example above 85%) before acting**.
- `labels.txt` lines are `<number> <name>`, for example `0 fist` and `1 ok`: the label printed by the Ministry code is `1 ok`. **This was checked on a made-up stand-in file in the same format,
  not on a real Teachable Machine export — confirm on your own export before class** (see the open question in the report).

Real output of the lab functions ([`Model_Reference.py`](Model_Reference.py), the **stand-in** model, Python 3.14):

```text
label: ok
Gesture recognized: OK - opening the door
test_1_ok.png -> ok (99%)
test_4_ok_drawing.png -> fist (73%)
ACT: ok
NOT SURE: ask for another photo
test_1_ok.png -> correct
test_2_fist.png -> correct
test_3_fist_dark.png -> correct
test_4_ok_drawing.png -> WRONG (model said fist)
test_5_ok_side.png -> correct
test_6_fist_blurry.png -> correct
test_7_ok_far.png -> correct
Accuracy: 85.7 %
acted on 4 of 7 images; 4 were right
```

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 19.1)

| Clock | Activity |
|---|---|
| 0–3 | **Recap** (p. 3): the project we saved last time — fist or OK |
| 3–10 | **What did we download?** (pp. 4–7): the folder holds everything the model needs, like a backpack; what is a ZIP; demo: *Extract All*, look inside — the folder `model.savedmodel` and the file `labels.txt` |
| 10–16 | **Why connect a model to code?** (pp. 9–13): a model decides a category; a program acts. The forest-fire example: picture → category and confidence → alert; "without code: a classification; with code: a fire prevented". More: ripeness sorting, X-ray, recycling bins, climate pictures, driver fatigue |
| 16–32 | **The code, as a black box** (pp. 14–25): the four blocks (table above), line by line in plain words; **only the three paths change** (p. 22) — how to find the path of a folder or file. "Programmers in big companies work in teams on millions of lines; nobody writes it all" (19.1 p. 33, "programmers as in hi-tech": the hi-tech teamwork slide — say it aloud, it is the point of the black box) |
| 32–42 | **Reading the result** (pp. 26–30): the wanted result, the confidence level (99% → act), a second picture (the OK drawing): wrong category at 73% — *what went wrong?* (not trained on drawings? only fists?) → back to the data; and the rule in our program: **act only above 85%** |
| 42–45 | **Bridge to the lab** (p. 31): we connect the model we saved and finish the unit |

### Tool Note – the exported model
**Not verified in this repository** (no TensorFlow here; the stand-in file runs with plain Python): `Ministry_Model_Code.py` needs `tensorflow`, `numpy` and `pillow`, the extracted `model.savedmodel` folder
and `labels.txt`. The Ministry runs it in Google Colab (the 19.3 notebook is missing ⚠️). TensorFlow may not install on every Python version — **do a live run before class** with a model exported from
Teachable Machine (choose the Tensorflow tab, SavedModel option). Edit only the three paths at the top of the file. Teachable Machine export options and TensorFlow versions change over time.

**Differences between `Ministry_Model_Code.py` and the deck (19.1 pp. 15–24)** — say them out loud so a student comparing the slide with the file is not confused:
- The deck has the three paths **inside `main()`**; our file has them at the **top** (so `classify_image()` shares them and there is one place to edit). Same three lines, same names.
- The deck's `__name__ _= "__main__"` is a typo; ours is fixed. Official error, not copied.
- The deck prints Hebrew messages (`הקטגוריה אליה התמונה שייכת לפי המודל`, `רמת הביטחון של המודל`); ours prints the same two Hebrew messages. Comments are English.
- The deck's `main()` loads the model itself; so does ours. `classify_image()` (our addition) loads it **once, on its first call** — an earlier draft of the file loaded it twice at import; that is fixed.
- The file uses `with open`, a list comprehension, `.numpy()` and `if __name__` — all inside the black box, never a student task (the rulebook's documented exception).
- Option from 19.0: **an extra meeting** can be added if the students build a second classification project of their own (and if time remains at the end of the year). Not planned in our 4 meetings.

### Live-run checklist (before class, teacher) — nothing in this unit's real-model path has been run here
1. **TensorFlow may not exist for Python 3.14** (the installed version here). Use a Python that TensorFlow supports (check the TensorFlow release notes) in a venv, **or** Google Colab, as the Ministry does.
2. `pip install tensorflow pillow numpy` (Keras 3 is required for `TFSMLayer`); `import tensorflow as tf` works.
3. Export a model from Teachable Machine: *Export Model → Tensorflow → Savedmodel → Download*; extract `converted_savedmodel.zip` (Extract All): the folder `model.savedmodel` and `labels.txt`.
4. Put `Ministry_Model_Code.py` beside them; edit the three paths; run on one test picture. Expected: the label with its number (for example `1 ok`) and a confidence between 0 and 1.
5. Run `Model_Starter.py` with `USE_REAL_MODEL = True` and check that `classify_image()` returns `[label, confidence]`.
6. **Colab path:** the Ministry's 19.3 notebook (mounting Drive, uploading the zip, finding paths) is **missing ⚠️**. Do not invent it from memory in front of the class; try the upload-to-Colab route yourself first, or run locally.
7. Fall back to the stand-in (`USE_REAL_MODEL = False`) for the lab functions if any step fails; the unit still works.

---

# 6. Second 45 Minutes — Lab (worksheets 19.2 / 19.3 — missing ⚠️; rebuilt from 19.0 / 19.1)

Starter: [`Model_Starter.py`](Model_Starter.py) (with [`labels_standin.txt`](labels_standin.txt)). Reference: [`Model_Reference.py`](Model_Reference.py). The real model: [`Ministry_Model_Code.py`](Ministry_Model_Code.py).
Brief: [`m4-lab-brief-he.md`](m4-lab-brief-he.md).

A class **with** TensorFlow or Colab sets `USE_REAL_MODEL = True` and runs everything on its own model (the paths edited as in the deck). A class **without** keeps the stand-in
(`USE_REAL_MODEL = False`): it returns fixed answers for seven made-up picture names, so the same functions run on any computer.

## 45–51 — Warm-up: the OK sign that did not open the door

```python
result = classify_image("test_1_ok.png")
label = result[0]
confidence = result[1]
print("label:", label)
if label == "ok":
    print("Gesture recognized: OK - opening the door")
else:
    print("Not an OK sign - the door stays closed")
```

Predict `Gesture recognized: OK - opening the door`, run:

```text
label: 1 ok
Not an OK sign - the door stays closed
```

A line of `labels.txt` is `1 ok` — the number and the space belong to it. Fix: keep only what follows the first space
(`text[text.find(" ") + 1:]` — `find` gives `-1` when there is no space, so a bare `ok` stays whole).

## 51–61 — Task 1: edit the paths, `report(image_path)`

With the real model: set `model_path`, `labels_path`, `image_path` and run `Ministry_Model_Code.py` on one of the 7 test pictures. In both modes write
`report(image_path)`, which prints `test_1_ok.png -> ok (99%)` (use `round(confidence * 100)`). Run it on `"test_4_ok_drawing.png"`: `-> fist (73%)`.

## 61–71 — Task 2: `decide(label, confidence)`

Returns `"ACT: <label>"` when the confidence is at least `0.85`, otherwise `"NOT SURE: ask for another photo"`. Test: `("ok", 0.99)` → `ACT: ok`; `("fist", 0.73)` → `NOT SURE: ask for another photo`.

## 71–81 — Task 3: `evaluate(test_images, true_labels)` — the unit checkpoint

For each picture: classify, print `correct` or `WRONG (model said ...)`, count the successes, return the accuracy using `calculate_accuracy` (from lessons 18.0–18.1). In stand-in mode the 7 made-up names give
`Accuracy: 85.7 %` (6 of 7; the drawing is wrong). With the real model use `תמונה1`–`תמונה7` and the true labels the teacher gives.
**If time:** how many pictures would the program **act on** under the 85% rule, and were those right? (stand-in: 4 of 7, all 4 right.)

## 81–86 — Model report

Each group reports: the classification goal and the categories; the desired feature and two incidental features tested; the number of training pictures per category; the accuracy on the 7 test pictures;
one example of a mistake with its confidence; one data change you would make; one limitation that remains (what does the model do for a hand that is neither a fist nor OK?).

## 86–90 — Save and exit check

Save As `G8_U8_M4_Model_<Name>.py`.

1. What does a model alone do, and what does the code add?
2. Which three lines do you change to test your own picture?
3. What is the difference between accuracy and confidence?
4. Why act only above 85%?

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The label from `labels.txt` is just the name | The line is `<number> <name>`: strip the number before comparing |
| A prediction with high confidence is always right | It is the model's own certainty; the OK drawing at 73% shows the other side, and a wrong answer can be confident too |
| Seven test pictures prove a model is "good" | Report the sample size: a small, informative check |
| I must understand every line of the Ministry code | The deck treats it as a black box; understand the four blocks and edit only the three paths |
| The model decides what the program does | The program decides: it reads the category **and** the confidence and chooses to act or not |
| Accuracy and confidence are the same | One summarizes a test set; the other belongs to a single prediction |

---

# 8. Assessment Evidence (formative) — Classification checkpoint (lessons 16.0–19.1)

- The warm-up label bug explained, not just fixed
- `report`, `decide` and `evaluate` working, with the accuracy printed
- The model run on at least one test picture with the three paths edited (real model or stand-in)
- **Classification checkpoint (lessons 16.0–19.1)**, 20 points (the v1 rubric, kept): problem definition 2, data planning 4, test set 3, accuracy calculation 3, bias testing 3, loading in Python 3, critical explanation 2.
  Bands: 18–20 full process, diverse data, correct measurement, critical analysis · 14–17 working model, one small gap in diversity, measurement or documentation · 10–13 an early model; missing a clean
  train/test split or bias check · 0–9 needs support with problem definition, collection, measurement or loading.
- The model report and exit check
