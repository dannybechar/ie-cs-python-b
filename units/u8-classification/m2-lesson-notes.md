# Unit 8.2 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Training Set and Test Set, Challenging Cases, Bias — a First Teachable Machine Model

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Teachable Machine (web, a camera or uploaded images — see Tool Note)
**Source of inspiration:** Ministry teaching materials **17.0** (teacher emphases and answers to the discussion questions), **17.0.1** (teacher helper deck:
Teachable Machine, 30 slides, mostly screenshots), **17.1** (deck, 53 slides: training and test, challenging cases, bias, hand gestures, sign
language, demo). Worksheet **17.2** is still missing ⚠️ (never invented): the hands-on lab below is rebuilt from 17.0 and 17.1 (two hand-gesture categories, train, test,
the discussion questions) and flagged as an assumption. The v1 build is kept for the data-leakage idea, the background-bias experiment,
`describe_trial` and `count_correct`. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Teachable Machine**.
**Prerequisite:** functions (Unit 3) and lists (Unit 7).

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | classification by rules, features, a separating line | 45 / 45 |
| **8.2 (this)** | **training set and test set, challenging cases, bias, first Teachable Machine try** | 45 / 45 |
| 8.3 | accuracy, the fist / OK project, export | 45 / 45 |
| 8.4 | the trained model inside Python, confidence | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 19–20) | Covered here |
|---|---|
| Goal 6: the ML process stages | ✅ training → test → back to training (17.1 pp. 5–30) |
| Goal 7: distinguish training from test; avoid leakage | ✅ 17.1 and the `has_leak` warm-up |
| Goal 8: build an image classifier in Teachable Machine | ✅ first, deliberately quick model (17.0.1 guide) |
| Goal 11: confidence vs accuracy | ✅ "confidently wrong" (the pen / pencil slides) |
| Goal 13: identify a visual bias | ✅ glasses, skin color, the background shortcut |

### Deliberate exclusions
Accuracy as a number (8.3), the 100-image project and export (8.3), model code (8.4). A **sign-language recognition** example is shown, not built.

---

## 3. Lesson Goal

**A model learns from a training set and is judged on a separate test set of examples it has never seen. It learns every pattern that repeats in the
pictures — also the wrong ones (a background, the lighting) — and it must always pick one of its categories, even when none fits.**

---

## 4. Core Mental Models

```text
training:  examples + an "answer sheet"  →  the computer moves the line after each mistake
test:      NEW examples + the answer sheet →  the line does not move; the computer only scores itself
score not good enough?  →  more and better training, a new test, and again
```

- **Training set:** the examples (pictures) the computer learns from, each with the right answer. **Test set:** new examples it has never seen, used only to check.
- **Data leakage** (our addition): if the same picture is in both sets, the score is flattering and says nothing about new pictures.
- **Challenging cases:** a cat photographed from the back, in a dark room. If the training pictures were all from the front, the model has never seen them.
  More varied training means a better test.
- **Bias:** results that lean in one direction because the data are not varied enough (training faces with no glasses and no dark skin).
- The model decides what to learn. We give examples; it may learn the shape of the hand **and** the wall behind it, the lighting, even who held the camera.
- **No category fits?** The model still picks one of the categories it knows (17.0 p. 3).
- Confidence belongs to one prediction; it can be high and wrong.

Real output of the lab functions ([`TrainTest_Reference.py`](TrainTest_Reference.py), Python 3.14):

```text
has_leak(["img1", "img2", "img3"], ["img2", "img9"])  -> True
has_leak(["img1", "img2", "img3"], ["img7", "img9"])  -> False
fist -> fist (confidence 0.91) - correct
ok -> fist (confidence 0.55) - WRONG
count_correct(...) -> 4
best_label(["fist", "ok"], [0.62, 0.38]) -> fist
```

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 17.1, helper deck 17.0.1)

| Clock | Activity |
|---|---|
| 0–3 | **Recap** (17.1 p. 3): classification, the Louvre, cats and dogs by two features. "For many pictures we need many examples" |
| 3–18 | **Training and test** (pp. 4–32): the two stages are what we call *machine learning*. **Training:** the computer places the training pictures on the plane, tries a line, and moves it after every mistake (it has an "answer sheet"). **Test:** new pictures; the line does **not** move; "2 of 3". Not good enough? Back to training. Our addition: the same image in both sets = a leak. Glimpse: real models have far more than 2 features and curved lines (p. 31) |
| 18–26 | **Challenging cases** (pp. 33–37): "our cat" trained on front and side pictures; *predict-first:* will it recognize a picture from the back, or in a dark room? (question only, then the answer). *How do we improve training?* — more variety of angles and light |
| 26–35 | **Bias** (pp. 38–44): face training pictures without glasses (will it recognize the person with glasses?) and without dark skin; the definition; *what is our responsibility as programmers?* (a model is as biased as its data) |
| 35–39 | **What do we classify today?** (pp. 45–47): two hand gestures — like / dislike, point / victory, fist / OK (next meeting: fist and OK). A real example: sign-language recognition (a Google competition in 2023 with 1,165 participants) — and of course sign language has far more than 2 categories |
| 39–45 | **Teachable Machine live demo** (17.0.1): new image project, the three-part screen, rename a category, add a category, add pictures by holding the webcam button or by upload, train, test and read the confidence. Show the trap (17.0.1 pp. 20–25): a model trained on pen and pencil pictures says "pen" with high confidence for a pencil (hints: look at how it was trained, and at the **background**), and a "marker" category trained on a **single** picture also gets called "pen". |

### Optional talk, additions from the Ministry files (17.0 "for the curious", 17.1 pp. 51–52)
- **The dog analogy (17.0):** teach a dog to tell apples from oranges: many pictures first (the training set), then new pictures it has never seen (the test set).
- **Three reasons to keep the sets apart (17.0):** (1) no self-deception — a model tested on its own training data looks good even if it learned nothing; (2) we measure **generalisation**,
  how it handles new data; (3) we improve the model by studying its mistakes on the test set.
- **Marker and unbalanced data (17.0.1 pp. 24–25):** a "marker" category trained on a single picture is called "pen" with high confidence — too little and too similar data is a bias too.
- **Video (17.1 p. 51):** "Noam, a research engineer at Google" — a video slide; the link was not delivered (`links.md` has nothing for 16–19), so show the slide or skip it ⚠️.
- **Next meeting (17.1 p. 52):** ask the class to bring coloured bristol boards, markers, gloves and anything that helps make different backgrounds and lighting for photographing hand signs.
- **Face-bias slides (17.1 pp. 39–41, glasses and dark skin) are discussion-only:** project them as a question about the data; **never** photograph or upload the faces of students or staff, not even as a demo.

### Tool Note – Teachable Machine
Needs a browser, camera permission and access to `teachablemachine.withgoogle.com`. The Ministry's advice (17.0): work in a room where the computers have working cameras,
at least one per pair; with no cameras, upload pictures (this takes longer: find them online or photograph with a phone); with one camera (the teacher's), do the hands-on
in plenary — "it's only the first lesson of a series". The teacher plays with the tool beforehand. **Privacy (full rules in the 8.3 notes):** hands only, never faces; no names or private screens in the background.

---

# 6. Second 45 Minutes — Lab (worksheet 17.2 — missing ⚠️; rebuilt from 17.0 / 17.1)

Starter: [`TrainTest_Starter.py`](TrainTest_Starter.py). Reference: [`TrainTest_Reference.py`](TrainTest_Reference.py).
Brief: [`m2-lab-brief-he.md`](m2-lab-brief-he.md).

## 45–51 — Warm-up: a leak that was not caught

```python
def has_leak(train_ids, test_ids):
    return train_ids == test_ids


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))
```

Predict `True` (`"img2"` is in both), run:

```text
False
```

Comparing the two whole lists for equality is not checking whether **any** item is in both. Fix: loop over `test_ids` and test `if test_id in train_ids`.

## 51–69 — The Teachable Machine experiment (pairs)

1. **Two categories** of hand gesture (for example fist and OK), 10–15 pictures each. For the first model, **photograph category A only against one background and category B only
   against another** (a bright wall and a dark notebook), then train.
2. **Test on new pictures**, and then swap the backgrounds without changing the hands. Fill the log table: the image, the true label, the prediction, the confidence, what was
   different. *Did the model learn the hand or the background?*
3. **Improve:** add pictures of both categories on both backgrounds and in different light, train again, and test the same swapped pictures again.

Do not export yet (8.3). If there is no camera, use a teacher-prepared approved picture set — the steps are the same.

## 69–75 — Discussion (17.0 and 17.1 p. 50, with the teacher's answers)

- What happens when the model "learns" (after *Train Model*)? It finds patterns that repeat in the pictures of each category and tunes itself to tell them apart.
- Which features does it learn, and who decided? We gave the examples; **the model** decided which features matter — including wrong ones (the wall, the light).
- How do we know it works? It classifies new pictures it did not train on correctly. One good test is not proof; many different conditions (background, light, angle, distance, photographer) is better.
  A model is never proven 100%; we estimate how far we can trust it.
- **If we show it a gesture that belongs to no category** (a peace sign), how will it classify it? It still chooses one of its categories — it has to choose among what it knows
  (`best_label` in the reference file shows it: scores `[0.62, 0.38]` give `fist`).

## 75–81 — Task 1: `describe_trial(true_label, predicted, confidence)`

Returns one line: `"<true_label> -> <predicted> (confidence <confidence>) - correct"` or `"... - WRONG"`. Test on `("fist", "fist", 0.91)` and `("ok", "fist", 0.55)`, then use it
on two real rows of your log table (91% is written 0.91).

## 81–86 — Task 2: `count_correct(true_labels, predicted_labels)`

Counts matching positions in two lists of equal length: `["fist", "ok", "fist", "ok", "ok"]` against `["fist", "ok", "ok", "ok", "ok"]` gives `4`.
**If time (homework):** `best_label(labels, scores)`.

## 86–90 — Save and exit check

Save As `G8_U8_M2_TrainTest_<Name>.py`.

1. Why is a separate test set needed?
2. What is data leakage between training and test?
3. How can a background become an unwanted feature?
4. A model says "fist" at 95% for a picture of a peace sign. What does that tell you?

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Testing on the training pictures proves the model works | It cannot show whether it generalizes to new pictures |
| Comparing two whole lists checks for a shared item | It only checks that the lists are identical — check membership item by item |
| A high confidence proves a prediction is right | It is the model's own certainty, not a guarantee (a pencil called "pen" with high confidence; a category with one picture) |
| The model learns "what a hand is" | It learns every repeating pattern: shapes, edges, colors, positions — and the background |
| A model that sees an unknown gesture says "unknown" | It must choose one of its categories |
| Many tests prove 100% | We only estimate how far to trust it |
| Bias is a computer being "unfair" on purpose | Biased data make a biased model; fixing the data is the programmer's responsibility |

---

# 8. Assessment Evidence (formative)

- The experiment log table (at least four rows) with a conclusion about the background shortcut
- The warm-up bug explained (list equality is not membership), not just fixed
- `describe_trial()` and `count_correct()` passing their tests, `describe_trial` used on two real rows
- Discussion answers in the student's words, including "no category fits"
- Exit check
