# Unit 8.1 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Classification, Features, a Decision Boundary

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit08_classification_complete_unit.md`, meeting 1 — its own clock table, the
sort-without-a-rule hook, the key-concepts table, the song-feature evaluation table, the one-dimensional boundary
example, the rule-based fruit classifier with its edge cases, the rules-vs-learning comparison table, both practice
drills and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **8.1 (this)** | **classification, features, decision boundary, a naive rule-based classifier** | 45 / 45 |
| 8.2 | the ML process; training vs. test; first Teachable Machine try | 45 / 45 |
| 8.3 | project planning, 100+ images per category, bias experiments | 45 / 45 |
| 8.4 | accuracy, export, loading the model in Python | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 19) | Covered here |
|---|---|
| Goal 1: define a classification problem, category, feature, feature space | ✅ hook, concepts |
| Goal 2: explain a decision boundary | ✅ the song-year example |
| Goal 3: choose relevant, distinguishing features | ✅ the song-feature table |
| Goal 4: a rule-based classifier with compound conditions | ✅ every task |
| Goal 5: identify edge cases where rigid rules fail | ✅ the fruit edge cases, Task 1 |

### Deliberate exclusions
The ML process and Teachable Machine (8.2), accuracy computation (8.4).

---

## 3. Lesson Goal

**Classification assigns an example to one of a fixed set of categories, using its features; a decision boundary is
a choice the system's designer makes, not a fact discovered in nature.**

---

## 4. Core Mental Models

```python
def classify_song(year):
    if year <= 2010:
        return "old"
    else:
        return "new"
```

```python
def classify_fruit(color, shape, hardness):
    color = color.lower()
    shape = shape.lower()
    hardness = hardness.lower()

    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"
```

- A good feature is both **relevant** (connected to the category) and **distinguishing** (actually varies between
  categories) — an album cover's color is neither.
- More `if`/`elif` branches never fully solve a rigid rule system: the real world keeps producing new edge cases
  (a green, hard banana; a yellow apple) that no one wrote a rule for yet.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Hook:** sort a set of objects into two groups on the table, without revealing the rule — others guess it |
| 8–20 | Key concepts: classification, class/label, feature, feature space, decision boundary, edge case |
| 20–32 | **Feature evaluation (pairs):** is song release year, album cover color, title length, or recording date relevant and distinguishing for `old` vs. `new`? |
| 32–45 | The one-dimensional boundary (`classify_song`, above) and the rule-based fruit classifier — walk through its four test cases together |

---

# 6. Second 45 Minutes — Lab

Starter: [`Classifier_Starter.py`](Classifier_Starter.py). Reference: [`Classifier_Reference.py`](Classifier_Reference.py).

## 45–53 — Discuss: the fruit classifier's edge cases

How would you classify a green, hard banana? A yellow apple? Can you keep writing rules forever? What's the cost of
a large rule system?

## 53–61 — Warm-up: the case that didn't match

```python
def classify_fruit(color, shape, hardness):
    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"


print(classify_fruit("Yellow", "Long", "Soft"))
```

Predict `banana`, run, get `unknown` — the input's capitalization doesn't match the lowercase strings the rules
compare against. Fix: normalize with `.lower()` on every input first.

## 61–72 — Task 1: a weather-based classifier

Write `classify_activity(temperature, raining, strong_wind)`, returning `"indoor"` or `"outdoor"`: rain or strong
wind means indoor; otherwise, a temperature between 18 and 30 (inclusive) means outdoor, anything else indoor. Then
find **two** edge cases where the decision feels wrong or incomplete, and name the missing feature each time (e.g.,
humidity, or how light the rain actually is).

## 72–84 — Task 2: trace before running

```python
def classify_level(score, attempts):
    if score >= 80 and attempts <= 3:
        return "advanced"
    elif score >= 50:
        return "intermediate"
    else:
        return "beginner"
```

Trace `(90, 2)`, `(90, 6)`, `(55, 8)`, `(40, 1)` on paper before running.

```text
advanced
intermediate
intermediate
beginner
```

## 84–90 — Save and exit check

Save As `G8_U8_M1_Classifier_<Name>.py`.

1. What is a feature?
2. What is a decision boundary?
3. Give an example of an incidental feature.
4. Why is a green banana an edge case for a simple color-based classifier?

### Tool Note – Thonny
Print each input's value right before a comparison (e.g., `print(repr(color))`) to catch a case-sensitivity bug
like the warm-up's — `repr()` shows the exact characters, including any you might have missed.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An easy-to-measure feature is automatically useful | It's only useful if it's also relevant and distinguishing |
| Color alone is always enough to classify a fruit | It's necessary but not sufficient — shape and hardness matter too, and even they can fail |
| A rule-based system is itself "learning AI" | It's classical code — a person wrote every rule explicitly |
| A learned model never needs rules, data, or human decisions | Every model still depends on human choices about goals, data, and evaluation |
| More `if`/`elif` branches eventually cover every real case | The world keeps producing new edge cases faster than rules can be written for them |

---

# 8. Assessment Evidence (formative)

- The feature-evaluation table (relevant/distinguishing) completed with reasons
- The fruit classifier's four test cases predicted before running
- The warm-up bug explained (case sensitivity), not just fixed
- `classify_activity()` with two genuine edge cases and their missing features named
- The `classify_level()` trace matching all four expected outputs
- Exit check
