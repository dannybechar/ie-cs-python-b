# Unit 8.3 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Project Planning, Data, Bias

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Teachable Machine and a camera (see Tool Note); this meeting handles real photographs —
read the Photography Safety note before class
**Source of inspiration:** `python_b_unit08_classification_complete_unit.md`, meeting 3 — its own clock table, the
category definitions (`fist`/`ok`), the diversity matrix, the collection plan, the pre-training data audit
questions, the test-set plan, the four bias experiments, the experiment log and the targeted-improvement steps kept
nearly unchanged, including its full photography privacy and consent rules.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Teachable Machine**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 8.1 | classification, features, decision boundary, a naive rule-based classifier | 45 / 45 |
| 8.2 | the ML process; training vs. test; first Teachable Machine try | 45 / 45 |
| **8.3 (this)** | **project planning, 100+ images per category, bias experiments** | 45 / 45 |
| 8.4 | accuracy, export, loading the model in Python | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 20) | Covered here |
|---|---|
| Goal 8: build an image classifier in Teachable Machine | ✅ the training step |
| Goal 9: plan a diverse image collection | ✅ the diversity matrix, collection plan |
| Goal 13: identify a visual bias and propose a concrete data change | ✅ the bias experiments |

### Deliberate exclusions
Accuracy computation (8.4), model export and Python loading (8.4).

---

## 3. Photography Safety (read before class)

- Photograph **hands only** — faces are never required.
- Get consent before photographing anyone else.
- No names, ID documents, personal screens, or other private information visible in the background.
- Store images per school policy; delete them when no longer needed.
- Never publish a link to the model or image collection without permission.
- Confirm the chosen hand gestures are culturally appropriate for the class.

---

## 4. Lesson Goal

**A category needs an agreed labeling rule decided before collection; a diverse image set (not an exhaustive one)
prevents a category from being identifiable by one incidental factor alone.**

---

## 5. Core Mental Models

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

- The goal isn't photographing every combination — it's preventing a category from being guessable by one
  incidental factor (a fixed background, one hand, one lighting setup) alone.
- Before training: at least 100 images per category, similar counts across categories, several separate shooting
  bursts (not one continuous take), shared backgrounds/lighting across **both** categories, and external test
  images set aside from the very start.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | Present the project's goal and the photography safety rules (§3) |
| 8–20 | Define the two categories and their labeling rule; agree **now** how to label an ambiguous case, and never change the definition mid-collection without documenting it |
| 20–32 | The diversity matrix (above) |
| 32–45 | The collection plan; the pre-training audit questions: does one category share one background? Does one hand appear in only one category? Are the counts similar? Any blurry or mislabeled images? Did a test image slip into training? Can you guess the category from the background alone? |

---

# 7. Second 45 Minutes — Lab

Starter: [`DataPlan_Starter.py`](DataPlan_Starter.py). Reference: [`DataPlan_Reference.py`](DataPlan_Reference.py).

## 45–55 — Collecting (groups, subject to Tool Note)

100+ images per category, following the diversity matrix and the collection plan above.

### Tool Note – Teachable Machine
Needs a browser, camera permission, and network access. If a live shoot isn't possible, use a teacher-prepared,
approved image set instead — every downstream step (training, testing, bias experiments) works the same way.

## 55–63 — Warm-up: balanced, according to the wrong direction

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

Predict a warning (`fist` is only 20% of the data — clearly under-represented), run, get `"Balanced enough"` — the
condition checks for a **high** share, not a low one. Fix: flag either category when its share drifts too far from
an even split (e.g., under 40% or over 60%).

## 63–73 — Task 1: `check_variety(labels, counts, minimum)`

Warns, by name, about any category (in this case: a diversity factor like "dark background") whose count is below
`minimum`; tallies the warnings; prints a clean "every category meets the minimum" if there were none. Test on
`labels = ["bright background", "dark background", "side light", "new user"]`, `counts = [40, 5, 15, 3]`,
`minimum = 10`.

## 73–80 — Task 2: `count_covered(required, tested)`

How many of the `required` bias-experiment conditions also appear in `tested` — a simple checklist-coverage count,
reusing the `in`-over-a-list pattern from Unit 7's search. Test on
`required = ["background", "lighting", "user", "angle"]`, `tested = ["lighting", "angle"]` → `2`.

## 80–90 — Bias experiments + exit check

Run at least one of the four controlled experiments (background, lighting, user, angle — changing one factor at a
time) and log it: image, true label, prediction, confidence, factor tested, conclusion.

Save As `G8_U8_M3_DataPlan_<Name>.py`.

1. What is the desired feature in this project?
2. Name two possible incidental features.
3. How do you keep an external test set truly external?
4. If the model fails on a dark background, what data change would you try?

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| More images always means more diversity | 100 nearly identical images from one continuous take add little diversity |
| A unique background per category is a shortcut, not a problem | It's exactly the kind of incidental feature that causes hidden bias |
| The category definition can be adjusted quietly if collection gets hard | Any change must be documented and applied consistently, not made silently mid-collection |
| One failed image proves the whole model is broken | It's evidence for a hypothesis — test more images before concluding anything |
| Fixing a bias means starting the data collection over | Usually a targeted addition (more examples of the failing condition, in both categories) is enough |

---

# 9. Assessment Evidence (formative)

- The category definitions with an explicit rule for ambiguous cases
- The pre-training audit questions answered honestly about the actual collected set
- The warm-up's inverted condition explained, not just fixed
- `check_variety()` and `count_covered()` both passing their tests
- At least one completed bias-experiment log row with a stated conclusion
- Exit check
