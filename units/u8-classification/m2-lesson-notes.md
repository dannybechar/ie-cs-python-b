# Unit 8.2 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: The ML Process + Teachable Machine

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Teachable Machine (web, needs a camera — see Tool Note)
**Source of inspiration:** `python_b_unit08_classification_complete_unit.md`, meeting 2 — its own clock table, the
ML-process pipeline diagram, the train/test comparison table, the "quick, deliberately unbalanced" first experiment,
the background-bias experiment, the confidence-vs-accuracy distinction and the reflection questions kept nearly
unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Teachable Machine**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | classification, features, decision boundary, a naive rule-based classifier | 45 / 45 |
| **8.2 (this)** | **the ML process; training vs. test; first Teachable Machine try** | 45 / 45 |
| 8.3 | project planning, 100+ images per category, bias experiments | 45 / 45 |
| 8.4 | accuracy, export, loading the model in Python | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 19–20) | Covered here |
|---|---|
| Goal 6: the ML process stages | ✅ pipeline diagram |
| Goal 7: distinguish training from test; avoid leakage | ✅ every task |
| Goal 8: build an image classifier in Teachable Machine | ✅ the first experiment |
| Goal 11: confidence vs. accuracy | ✅ closing discussion |
| Goal 13: identify a visual bias | ✅ the background experiment |

### Deliberate exclusions
Full project planning and 100+ image collections (8.3), accuracy computation in code (8.4).

---

## 3. Lesson Goal

**A model learns from a training set and is judged on a separate test set — if the same example appears in both,
the measurement is optimistic and doesn't test real generalization.**

---

## 4. Core Mental Models

```text
הגדרת בעיה → הגדרת קטגוריות → איסוף ותיוג נתוני אימון → אימון המודל →
בדיקה על נתונים חדשים → חישוב מדד וניתוח טעויות → שיפור הנתונים או התכנון
```

- **Training set**: what the model learns from. **Test set**: held out, never used for training, checked against a
  known true label.
- **Confidence** belongs to one prediction; **accuracy** summarizes performance over a whole test set — a model can
  be confidently wrong on a single image.
- A quick first model isn't meant to be good — it's meant to **reveal** what incidental pattern (background,
  lighting) the model might have latched onto instead of the intended feature.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** rules vs. learning from examples |
| 10–24 | The ML process pipeline (above), stage by stage |
| 24–34 | Training set vs. test set; what data leakage is and why it makes a measurement meaningless |
| 34–45 | **First experiment, live:** open Teachable Machine, `Image Project`, two temporary categories (e.g., `left`/`right`, or two objects), collect a handful of images quickly, train, test immediately on a different background/lighting — the goal is to **discover** a shortcut the model may have learned, not to build a good model yet |

### Tool Note – Teachable Machine
Needs a browser, camera permission, and network access to `teachablemachine.withgoogle.com`. If unavailable,
substitute a teacher-prepared set of sample images and walk the process on the board instead of live.

---

# 6. Second 45 Minutes — Lab

Starter: [`TrainTest_Starter.py`](TrainTest_Starter.py). Reference: [`TrainTest_Reference.py`](TrainTest_Reference.py).

## 45–53 — Background-bias experiment (continuing from the Teachable Machine demo)

Category A photographed only against a blue background; category B only against yellow. After training, swap the
backgrounds without changing the object. Research question: did the model learn the object, or the background?

## 53–61 — Warm-up: a leak that wasn't caught

```python
def has_leak(train_ids, test_ids):
    return train_ids == test_ids


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))
```

Predict `True` (`"img2"` is in both), run, get `False` — comparing the two *whole lists* for equality is not the
same as checking whether any single item overlaps. Fix: loop over `test_ids` and check `in train_ids`.

## 61–71 — Task 1: `describe_trial(true_label, predicted, confidence)`

Returns one readable line: `"<true_label> -> <predicted> (confidence <confidence>) - correct"` or `"... - WRONG"`.
Test on `("fist", "fist", 0.91)` and on `("ok", "fist", 0.55)`.

## 71–81 — Task 2: `count_correct(true_labels, predicted_labels)`

How many positions match between the two (same-length) lists. Test on
`["fist", "ok", "fist", "ok", "ok"]` / `["fist", "ok", "ok", "ok", "ok"]` → `4`.

## 81–90 — Reflection + save + exit check

Reflection: which feature did you *want* the model to learn? Which incidental feature might it have learned
instead? What experiment separated the two? What would you change in data collection?

Save As `G8_U8_M2_TrainTest_<Name>.py`.

1. Why is a separate test set needed?
2. What is data leakage between training and test?
3. How can a background become an unwanted feature?
4. What's the difference between confidence and accuracy?

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Testing only on training images checks the model properly | It can't reveal whether the model generalizes to new examples |
| Comparing two whole lists checks for any shared item | It only checks if the lists are identical — check membership per item instead |
| A high confidence score proves a prediction is correct | It's the model's own certainty estimate, not a guarantee |
| One shortcut background is harmless if accuracy still looks fine | A hidden shortcut can fail badly the moment conditions change |
| Changing several factors in one experiment isolates the cause | Change one factor at a time, or you can't tell which one mattered |

---

# 8. Assessment Evidence (formative)

- The ML process stages named in order, in the student's own words
- The background-bias experiment: a stated hypothesis and what the swapped-background test showed
- The warm-up's list-equality bug explained (why it misses real leaks), not just fixed
- `describe_trial()` and `count_correct()` both passing their tests
- The reflection questions answered with a concrete proposed data change
