# Unit 8.3 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Accuracy and the Classification Project — Fist or OK

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab (mostly the project)
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Teachable Machine and a camera (see Tool Note); this meeting handles real photographs — read the Photography Safety note before class
**Source of inspiration:** Ministry teaching materials **18.0** (teacher emphases) and **18.1** (deck, 39 slides: accuracy, everyday classification, the
project, saving the model), plus the two image archives `תמונות לאימון` (269 AI-generated pictures: `fist/` 155, `ok/` 114) and `תמונות למבחן` (7 test
images, `תמונה1`–`תמונה7`). Worksheet **18.2** was **not delivered**: the lab below follows 18.0 / 18.1 (import the supplied training pictures, add your own, train, test on the
teacher's 7 images, **save the model**). The v1 build is kept for the category-definition rule, the diversity matrix, the pre-training audit, the
bias experiments, the privacy rules, `check_variety` and `check_balance`. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Teachable Machine**.
**Prerequisite:** functions (Unit 3) and lists (Unit 7).

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | classification by rules, features, a separating line | 45 / 45 |
| 8.2 | training set and test set, challenging cases, bias, first Teachable Machine try | 45 / 45 |
| **8.3 (this)** | **accuracy, the fist / OK project, export** | 45 / 45 |
| 8.4 | the trained model inside Python, confidence | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 20) | Covered here |
|---|---|
| Goal 8: build an image classifier in Teachable Machine | ✅ the project with the supplied pictures plus your own |
| Goal 9: plan a diverse image collection | ✅ category rule, diversity matrix, collection plan, audit |
| Goal 10: calculate accuracy | ✅ accuracy = successes / attempts (18.1 pp. 7–19), `calculate_accuracy` |
| Goal 11: confidence vs accuracy | ✅ one prediction vs the whole test set |
| Goal 13: identify a visual bias and propose a concrete data change | ✅ the bias experiment, the unbalanced supplied set |

### Deliberate exclusions
Loading the model in Python (8.4). A confusion matrix, precision and recall are not taught.

---

## 3. Photography Safety (read before class)

- Photograph **hands only** — faces are never required.
- Get consent before photographing anyone else.
- No names, ID documents, personal screens or other private information visible in the background.
- Store images per school policy; delete them when no longer needed.
- Never publish a link to the model or an image collection without permission.
- Confirm the chosen hand gestures are culturally appropriate for the class.
- The supplied training pictures are AI-generated (no real people). **Never copy them, or any student picture, into this repository.**

---

## 4. Lesson Goal

**Accuracy = successes ÷ attempts (× 100 for a score). A good project is judged on a test set the model has never seen, and a diverse training set — not just many pictures — is what makes it
succeed on them.**

---

## 5. Core Mental Models

```python
def calculate_accuracy(successes, attempts):
    if attempts == 0:
        return 0
    return successes / attempts * 100
```

```text
4 test pictures, 2 classified correctly, 2 not:   accuracy = 2 / 4 = 0.5   score = 0.5 * 100 = 50
```

<div dir="rtl">

| קטגוריה 1 — `fist` | קטגוריה 2 — `ok` |
|---|---|
| כל האצבעות מקופלות לכף היד | האגודל והאצבע המורה יוצרים עיגול; שאר האצבעות מורמות |

| גורם | וריאציות לדוגמה |
|---|---|
| רקע | בהיר, כהה, צבעוני, כיתה |
| תאורה | חזקה, חלשה, אור צד |
| זווית | ישרה, מעט ימינה, מעט שמאלה, הטיה |
| מרחק | קרוב, בינוני, רחוק |
| יד | ימין ושמאל |
| שרוול/כפפה | צבעים וסגנונות שונים |

</div>

- The goal is not photographing every combination: it is preventing a category from being guessable by one incidental factor (a fixed background, one hand, one light).
- Before training: similar counts across categories, several separate shooting bursts (not one continuous take), shared backgrounds and lighting across **both** categories,
  and test images set aside from the very start (here: the teacher's 7 images, which the students do **not** see until the end).
- **The supplied set is not balanced:** 155 `fist` against 114 `ok` (fist is 57.6%). It still passes `check_balance` (40–60%), but the students can add `ok` pictures; the log of
  such a decision is part of the project.
- Real output of the lab functions ([`DataPlan_Reference.py`](DataPlan_Reference.py), Python 3.14):

```text
check_balance(20, 80)   -> Categories are not balanced - fist is 20.0 %
check_balance(48, 52)   -> Balanced enough
calculate_accuracy(2, 4)  -> 50.0        calculate_accuracy(6, 7) -> 85.7        calculate_accuracy(0, 0) -> 0
check_variety([...], [40, 5, 15, 3], 10) -> Warning: dark background has only 5 images
                                            Warning: new user has only 3 images
```

---

# 6. First 45 Minutes — Knowledge + Guided Practice (deck 18.1)

| Clock | Activity |
|---|---|
| 0–4 | **Recap** (pp. 3–6): we played with Teachable Machine; training makes the line, the test checks it on pictures it has not seen |
| 4–16 | **Accuracy** (pp. 7–19): how do we know the model is good? Count the successes out of the attempts. Walk the four test pictures one by one on the plane (1 / 1, 2 / 2, 2 / 3, 2 / 4). *Predict-first, question only:* how many pictures did we try, how many were right, how many wrong? (pp. 17–18, then the answer) → 2 / 4 = 0.5, × 100 = 50 |
| 16–22 | **Classification in daily life** (pp. 20–25): Google Lens, a car-park gate reading license plates, face filters, face unlock, photo albums by topic, finding disease in medical scans. "AI amplifies our abilities in whatever we do" |
| 22–25 | **Your idea** (p. 37): what could you build tomorrow morning with AI? (a sink that notices it is full, a bin that praises paper…) |
| 25–40 | **Planning our project** (v1 content, Ministry silent): the two categories and the **labeling rule for ambiguous cases, decided before shooting**; the diversity matrix; the collection plan; the supplied pictures and the privacy rules; the **audit before training** (does one category share one background? one hand? similar counts? blurry or mislabeled pictures? did a test picture slip into training? can you guess the category from the background alone?) |
| 40–45 | **Launch + saving the model** (pp. 26–33): the project brief; and the three export steps in advance — `Export Model`, the options marked in red in order, **check that `converted_savedmodel.zip` was downloaded** and send it to yourself (mail, Drive). **Mandatory** (18.0): without it the next meeting cannot start |

---

# 7. Second 45 Minutes — Lab (worksheet 18.2 — not delivered; rebuilt)

Starter: [`DataPlan_Starter.py`](DataPlan_Starter.py). Reference: [`DataPlan_Reference.py`](DataPlan_Reference.py).
Brief: [`m3-lab-brief-he.md`](m3-lab-brief-he.md).

## 45–50 — Warm-up: balanced, in the wrong direction

```python
def check_balance(fist_count, ok_count):
    total = fist_count + ok_count
    fist_share = fist_count / total * 100
    if fist_share > 50:
        print("fist is under-represented")
    else:
        print("Balanced enough")


check_balance(20, 80)
```

Predict a warning (fist is only 20%), run:

```text
Balanced enough
```

The condition looks at a **high** share, not a low one, and the message even says the opposite. Fix: flag either category when its share leaves an even split (under 40% or over 60%).

## 50–56 — Task 1: `calculate_accuracy(successes, attempts)`

Returns the percent; `0` when there were no attempts. Test: `(2, 4)` → `50.0`, `(6, 7)` → `85.7` (rounded). Keep it: it will be used on the real model's 7 test pictures at the end of this meeting.

## 56–62 — Task 2: `check_variety(labels, counts, minimum)`

Prints a warning for every factor below `minimum`, counts the warnings, prints a clean message if there were none. Test: `["bright background", "dark background", "side light", "new user"]`,
`[40, 5, 15, 3]`, minimum `10` → two warnings. (If the class is slow, Task 2 becomes homework; the export is **not** optional.)
**If time:** `count_covered(required, tested)` for the bias experiments, expected `2`.

## 62–84 — The project (groups)

1. Open an `Image Project` with two categories, `fist` and `ok`. Upload the supplied training pictures into the right categories (the archive `תמונות לאימון` from the Drive).
2. Add **your own** pictures (hands only), following the diversity matrix and the audit questions; check the balance; log what you changed.
3. Run **one controlled bias experiment** (change one factor — background, light, hand, or angle): log the picture, the true label, the prediction, the confidence, the factor and the conclusion.
4. Train. The teacher then hands out the **7 test pictures** (`תמונה1`–`תמונה7`) — the model has never seen them. Classify each one, count the successes, and compute the accuracy
   with Task 1's function (for example 6 of 7 gives 85.7).
5. **Save the model** (the three export steps) and check that `converted_savedmodel.zip` is on your computer. If there is no camera, use only the supplied and teacher-approved pictures.

### Tool Note – Teachable Machine
Needs a browser and network access. The export may take a few minutes. If no group finishes the bias experiment, run it together on the teacher's computer. The Ministry advises bringing colored card,
markers, gloves and pencils to build backgrounds and lighting for the shoot (18.0).

## 84–90 — Record and exit check

Write the accuracy and one example of a mistake with its confidence. Save As `G8_U8_M3_DataPlan_<Name>.py`.

1. How do you calculate accuracy?
2. What is the difference between accuracy and confidence?
3. Name one incidental feature your pictures might contain.
4. If the model fails on a dark background, what data change would you try?

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| More pictures always means more diversity | 100 nearly identical pictures from one continuous take add little |
| A unique background per category is harmless | It is exactly the kind of incidental feature that causes hidden bias |
| The category definition can be adjusted quietly | Any change must be documented and applied consistently |
| High accuracy on 7 pictures proves the model is good | It is a small, informative check; state the sample size |
| One failed picture breaks the whole model | It is evidence for a hypothesis; test more before concluding |
| Accuracy and confidence are the same number | One is a single prediction's certainty; the other summarizes a whole test set |
| A 50-50 split is required | The supplied set (155 / 114) is close enough; balance matters most for the factors the model could shortcut on |

---

# 9. Assessment Evidence (formative)

- The category definition with an explicit rule for ambiguous cases
- The audit questions answered about the actual collected set
- The warm-up's inverted condition explained, not just fixed
- `calculate_accuracy()` and `check_variety()` passing their tests
- One completed bias-experiment log row with a conclusion; the accuracy on the 7 test pictures
- The saved `converted_savedmodel.zip` (checked at the end of the lesson)
- Exit check
