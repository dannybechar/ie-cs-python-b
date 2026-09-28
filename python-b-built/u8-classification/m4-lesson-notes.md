# Unit 8.4 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Accuracy, Export, Loading the Model in Python (Unit Checkpoint)

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; for a live run, TensorFlow/Keras + Pillow + NumPy and an exported model (see Tool Note)
**Source of inspiration:** `python_b_unit08_classification_complete_unit.md`, meeting 4 — its own clock table, the
manual accuracy calculation, `calculate_accuracy`, the accuracy-isn't-enough discussion, the Teachable Machine
export steps, the official Keras loading/prediction snippet, the image-preprocessing steps, the test-set prediction
loop, the label-text-mismatch warning, the model report and the seven-case test table kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the exported model**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | classification, features, decision boundary, a naive rule-based classifier | 45 / 45 |
| 8.2 | the ML process; training vs. test; first Teachable Machine try | 45 / 45 |
| 8.3 | project planning, 100+ images per category, bias experiments | 45 / 45 |
| **8.4 (this)** | **accuracy, export, loading the model in Python** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 20–21) | Covered here |
|---|---|
| Goal 10: calculate accuracy from parallel lists | ✅ warm-up, every task |
| Goal 11: confidence vs. accuracy | ✅ recap, discussion |
| Goal 12: export a model and integrate loading/prediction in Python | ✅ the checkpoint |

### Deliberate exclusions
Any new classification concept — this meeting completes the pipeline in code.

---

## 3. Lesson Goal

**Accuracy is the fraction of correct predictions over a whole test set; a real prediction pipeline converts an
image the same way every time — RGB, resized, normalized — before asking the model for its best guess.**

---

## 4. Core Mental Models

```python
def calculate_accuracy(actual, predicted):
    if len(actual) == 0 or len(actual) != len(predicted):
        return 0
    correct = 0
    for index in range(len(actual)):
        if actual[index].strip() == predicted[index].strip():
            correct += 1
    return correct / len(actual) * 100
```

Image processing before a prediction, in order: open and convert to RGB → resize/fit to `224×224` (what the model
expects) → convert to a numeric array → normalize pixel values → wrap in a batch of size 1 → run `predict` →
`argmax` picks the highest-scoring index → map that index to a category name.

- Accuracy alone doesn't explain *why* an error happened — that needs looking at which conditions the wrong
  predictions share.
- A `labels.txt` line often carries a trailing space, a newline, or a leading number — `.strip()` it before
  comparing, or a **correct** prediction can look wrong.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** test set, confidence vs. accuracy |
| 10–25 | **Manual calculation:** 6 of 7 predictions correct → `accuracy = 6 / 7 × 100 ≈ 85.7%`; then a true/predicted table filled by hand |
| 25–38 | Building `calculate_accuracy(actual, predicted)` in Python, guarding an empty or mismatched-length input |
| 38–45 | Why accuracy alone isn't the whole story: a small test set is noisy, a good overall number can hide a failing category, accuracy doesn't explain *why* an error happened |

---

# 6. Second 45 Minutes — Lab

Starter: [`Accuracy_Starter.py`](Accuracy_Starter.py). Reference: [`Accuracy_Reference.py`](Accuracy_Reference.py).

## 45–53 — Warm-up: a "wrong" prediction that was actually right

```python
def calculate_accuracy(actual, predicted):
    if len(actual) == 0 or len(actual) != len(predicted):
        return 0
    correct = 0
    for index in range(len(actual)):
        if actual[index] == predicted[index]:
            correct += 1
    return correct / len(actual) * 100


actual_labels = ["fist", "ok", "fist"]
predicted_labels = ["fist", "ok ", "fist"]   # a trailing space, as read from a real labels.txt line
print(calculate_accuracy(actual_labels, predicted_labels))
```

Predict `100.0` (all three actually match), run, get `66.7` — `"ok "` (with a trailing space) never equals `"ok"`.
Fix: `.strip()` both sides before comparing.

## 53–59 — Confirm on the full official example

```python
actual_full = ["fist", "ok", "fist", "ok", "ok", "fist", "ok"]
predicted_full = ["fist", "ok", "ok", "ok", "ok", "fist", "ok"]
print(round(calculate_accuracy(actual_full, predicted_full), 1))
```

Expect `≈85.7`, matching the hand calculation from guided practice.

## 59–67 — Export and image processing (teacher-led, or classroom mode — see Tool Note)

Export from Teachable Machine (`Export Model` → the Keras/TensorFlow option → download → keep `keras_Model.h5` and
`labels.txt` together). Walk through what image processing does and why each step matters (§4 above).

## 67–83 — Task (project — the checkpoint): loading and predicting

Complete `classify_image(image_path)` — in **classroom mode** (`MOCK_MODE = True`, no download needed): lowercase
`image_path`; if it contains `"fist"`, return `("fist", 0.9)`; if it contains `"ok"`, return `("ok", 0.9)`;
otherwise `("unknown", 0.5)`. Then write `predict_test_set(test_images, actual_labels)`: call `classify_image` on
each path, print the path, prediction and confidence, collect the predicted labels, and finish by printing the
overall accuracy with `calculate_accuracy`.

```text
test_images/fist_1.jpg
Prediction: fist
Confidence: 0.9
...
Accuracy: 100.0 %
```

## 83–90 — Model report + exit check

Each group reports: the classification goal and categories; the desired feature; at least two incidental features
tested; training counts per category; the test set description; overall accuracy; one example error and its
confidence; one data change made in response; one remaining limitation.

1. How do you calculate accuracy?
2. What's the difference between confidence and accuracy?
3. Why normalize the image before predicting?
4. What failure did you find, and what data change might reduce it?

### Tool Note – the exported model
For a real run: `pip install tensorflow keras pillow numpy`, place `keras_Model.h5` and `labels.txt` together with
the test images, set `MOCK_MODE = False` in the reference file, and fill in the commented loading/prediction block
(it's the source's own code, taken from Teachable Machine's official export snippet). Test it once, isolated,
before class — export tools and TensorFlow/Keras versions change over time.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A trailing space or extra number in a label is harmless | It silently breaks an exact-match comparison — always `.strip()` labels read from a file |
| High overall accuracy means there's no bias left | It can hide a category or condition that fails consistently |
| Any image size works for prediction | The model expects one exact size (here, `224×224`) — mismatched input breaks or misleads it |
| `confidence` and `accuracy` measure the same thing | One is per-prediction certainty; the other summarizes a whole test set |
| Seven test images prove a model is "good" | State the sample size explicitly — it's a small, informative check, not a full guarantee |

---

# 8. Assessment Evidence (formative)

- The manual accuracy calculation matching the Python function's result
- The warm-up's stripped-vs-unstripped bug explained, not just fixed
- `calculate_accuracy()` confirmed against the official ≈85.7% example
- **Unit 8 checkpoint** — scored against the source's 20-point rubric: problem definition 2, data planning 4, test
  set 3, accuracy calculation 3, bias testing 3, loading in Python 3, critical explanation 2. Bands: 18–20 full
  process, diverse data, correct measurement, critical analysis · 14–17 working model, one small gap in diversity,
  measurement, or documentation · 10–13 an early model; missing a clean train/test split or bias check · 0–9 needs
  support with problem definition, collection, measurement, or loading.
- The classroom-mode prediction pipeline running end-to-end and producing a correct accuracy
- The model report and exit check
