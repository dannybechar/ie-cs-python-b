# Unit 8.1 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Classification by Rules — Features and a Separating Line

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry teaching materials **16.0** (teacher emphases), **16.1** (deck, 68 slides: dog or bagel, the Louvre
classifier, good features, two features and a separating line, `classify_fruit`) and **16.2.0** (teacher solution of worksheet 16.2: Spotify
playlists, choosing features, `classify_fruit`, an edge case). The worksheet 16.2 itself was **not delivered**; its tasks are rebuilt from
the teacher solution. The v1 build (from `python_b_unit08_…_complete_unit.md`) is kept only where the Ministry is silent: the
relevant-vs-distinguishing language, the weather classifier (now "if time") and the "a boundary is a developer's decision" idea.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3) and lists (Unit 7) — the Ministry code uses `def`, parallel lists, `append` and `range(len(...))`.

---

## 1. Position in Unit 8

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **8.1 (this)** | **classification by rules, features, a separating line** | 45 / 45 |
| 8.2 | training set and test set, challenging cases, bias, first Teachable Machine try | 45 / 45 |
| 8.3 | accuracy, the fist / OK project, export | 45 / 45 |
| 8.4 | the trained model inside Python, confidence | 45 / 45 |

The Ministry's four meetings are 16 (this), 17, 18 and 19, in the same order.

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 19) | Covered here |
|---|---|
| Goal 1: define a classification problem, category, feature, feature space | ✅ deck 16.1 pp. 10–13, 28; the two-feature plane |
| Goal 2: explain a decision boundary | ✅ the separating line (16.1 pp. 34–50) |
| Goal 3: choose relevant, distinguishing features | ✅ cat / dog features (pp. 29–33), worksheet Task 3 |
| Goal 4: a rule-based classifier with compound conditions | ✅ Louvre, `classify_fruit` |
| Goal 5: identify edge cases where rigid rules fail | ✅ the 1860 gap, the unripe banana, softness 2, "happy" songs |

### Deliberate exclusions
Training and test sets, Teachable Machine (8.2), accuracy (8.3), model code (8.4). No nested loops, no lists of lists, no comprehensions.

---

## 3. Lesson Goal

**Classification assigns an example to one of a fixed set of categories using its features. A rule-based classifier is code a person wrote
rule by rule — it works for a few simple categories and breaks on edge cases — and a separating line is a choice the designer makes.**

---

## 4. Core Mental Models

```python
def classify_fruit(softness, color):
    if softness < 2 and color in ["red", "green", "yellow"]:
        return "apple"
    elif softness > 2 and color in ["yellow", "green"]:
        return "banana"
    else:
        return "unknown fruit"
```

- **Classification** = dividing items into categories by shared features. A **feature** is a detail that helps describe and recognize something.
- A good feature is **relevant** (connected to the category) and **distinguishing** (it differs between categories). The number of ears is
  relevant to "an animal" but useless for cat vs dog: both have two.
- One feature is often not enough; two features give a **plane**, and a **separating line** (`y = m·x + b`, as in math class) puts
  one category on each side. Real models use many more features and curves.
- A rule-based classifier is classical code. It cannot grow to 50 fruits, and it cannot read a camera picture of millions of pixels.

Real output of the teacher demos in [`Classifier_Reference.py`](Classifier_Reference.py) (run on Python 3.14):

```text
demo_louvre():
classic: ['Mona Lisa']
modern: ['Starry Night', 'Water Lilies', 'The Scream']

demo_line():
one feature - ears:  cats [5, 4, 2] dogs [5, 2, 1, 3]
one feature - eyes:  cats [3, 4, 5] dogs [1, 3, 4, 2]
cat 5 3 -> cat
cat 4 4 -> cat
cat 2 5 -> cat
dog 5 1 -> dog
dog 2 3 -> dog
dog 1 4 -> dog
dog 3 2 -> dog
```

The numbers are invented for the demo (ear stand-up 1–5, eye darkness 1–5): neither feature alone separates the animals, but
`ears + eyes > 6` does — that is the separating line.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 16.1)

| Clock | Activity |
|---|---|
| 0–4 | **Recap + warm-up** (pp. 3–9): "dog or bagel?" — three picture pairs, raise the left or right hand. *How did we know? Would a computer?* |
| 4–10 | **Definition and discussion** (pp. 10–12): classification = dividing items into categories by shared features. Where do we classify in daily life (music, games, clothes, who gets the message)? Where does AI classify (medicine, photos, spam)? |
| 10–14 | **Two ways to teach a computer to classify** (p. 13): rules written by a person (today) vs learning from data (next meetings) |
| 14–26 | **Code example 1 — the Louvre** (pp. 14–26): sort paintings into classic (before 1860) and modern. Build the loop with the class (two parallel lists, two empty lists, `append`) and **fill a trace table** for `years = [1889, 1519, 1906, 1893]` (`demo_louvre`). *Predict-first, question only:* **what happens to a painting made in exactly 1860?** The answer is the lab warm-up. |
| 26–38 | **Features** (pp. 28–50): what is a feature (cat in a picture: fur, 4 legs, pointed ears…); is "number of ears" good for cat vs dog? (no: both 2) → good features are relevant and distinguishing. Then **two features and a line**: eye color alone cannot separate, so add ear stand-up and draw the line on the plane (`demo_line`). Mention `y = mx + b`. |
| 38–45 | **Code example 2 — fruit** (pp. 51–65): apple vs banana by softness (1–5) and color; complete the skeleton `classify_fruit(softness, color)` with the class; call it and print. Discussion: *what if there are 50 fruit types? what if the input is a camera picture?* → the bridge to machine learning, "next week". |

> The Ministry deck's own Louvre slides show the 1860 bug in the frontal part and a second version of the code with an indentation slip and
> a changed year (p. 17: `1900`, `paintings` not indented). We do **not** copy those: the frontal example avoids the boundary, and the boundary bug is
> the lab warm-up, so the students discover it themselves.

---

# 6. Second 45 Minutes — Lab (worksheet 16.2, rebuilt from the teacher solution 16.2.0)

Starter: [`Classifier_Starter.py`](Classifier_Starter.py). Reference: [`Classifier_Reference.py`](Classifier_Reference.py).
Brief: [`m1-lab-brief-he.md`](m1-lab-brief-he.md).

## 45–53 — Warm-up: the painting that vanished

```python
def classify_paintings():
    years = [1889, 1519, 1860, 1893]
    paintings = ["Starry Night", "Mona Lisa", "The Urchin", "The Scream"]
    classic = []
    modern = []
    for i in range(len(paintings)):
        if years[i] < 1860:
            classic.append(paintings[i])
        elif years[i] > 1860:
            modern.append(paintings[i])
    print("classic:", classic)
    print("modern:", modern)
```

Predict four paintings in the two lists, run:

```text
classic: ['Mona Lisa']
modern: ['Starry Night', 'The Scream']
```

`"The Urchin"` (1860) is neither `< 1860` nor `> 1860`. Fix: `elif years[i] >= 1860:` or a plain `else`. The cure for this whole family of bugs:
every example must land in a category, so check the boundary values.

## 53–61 — Task 1: a playlist classifier (16.2.0 Q1–2)

Two parallel lists (`songs`, `years`), two empty lists, a loop: songs before the split year go to `nostalgia`, the others to `hits`. Run with 2015, then
with 2020 (the Ministry lets the students choose the year):

```text
split 2015:  nostalgia: ['Song A', 'Song D']   hits: ['Song B', 'Song C', 'Song E', 'Song F']
split 2020:  nostalgia: ['Song A', 'Song C', 'Song D', 'Song E']   hits: ['Song B', 'Song F']
```

(`years = [2008, 2022, 2015, 1999, 2017, 2026]`, titles `Song A`…`Song F`; the Ministry solution uses real titles, we use placeholders.)
Add two songs of your own to both lists and check them.

## 61–67 — Task 2: another feature (16.2.0 Q3–4)

Which other feature could Spotify use (length, singer, tempo, genre, mood)? Classify the same songs by length: short under 200 seconds, long otherwise
(`lengths = [180, 240, 150, 310, 200, 199]`):

```text
short: ['Song A', 'Song C', 'Song F']
long: ['Song B', 'Song D', 'Song E']
```

## 67–72 — Task 3: choose features (on paper, 16.2.0 "Choosing features")

From the fruit list — color, purchase date, country of origin, softness (1–5), price per kilo — choose **two** that help tell apple from banana and
justify; then name one feature that is **not** good and why. Model answer: color (apples red/green/yellow, bananas yellow, then green) and softness are good
but neither is perfect alone (a rotten apple is soft, an unripe banana is hard); country, purchase date and price describe the shop or the day, not the fruit.

## 72–82 — Task 4: `classify_fruit` and its edge cases (16.2.0 "Classification function")

Write the function from the rules (apple: softness < 2 and red / green / yellow; banana: softness > 2 and yellow / green; else `"unknown fruit"`),
call it three times, then try to break it:

```text
classify_fruit(1, "green")   -> apple          (correct)
classify_fruit(4, "yellow")  -> banana         (correct)
classify_fruit(3, "purple")  -> unknown fruit  (correct)
classify_fruit(1, "green")   -> apple          (an UNRIPE BANANA is also hard and green: wrong)
classify_fruit(2, "yellow")  -> unknown fruit  (softness exactly 2 matches neither rule: the Louvre bug again)
```

Discuss: a boundary like "softness 2" is the designer's decision, not a fact of nature; every new rule creates new edge cases.

## 82–86 — Task 5: think, no code (16.2.0 Q5)

A programmer writes: *if the song's speed is above 120 it is "happy", otherwise "sad"*. Find a song or style where it fails (a fast, sad rock song; a slow, happy
lullaby) and explain why a year is easier to turn into an `if` than a mood. **If time:** the v1 weather classifier `classify_activity` (reference file) and its two edge cases.

## 86–90 — Save and exit check

Save As `G8_U8_M1_Classifier_<Name>.py`.

1. What is a feature, and what makes it a good one?
2. What is a separating line?
3. Why is an unripe banana an edge case for the fruit rule?
4. Why can't we write `if/else` rules for every picture in the world?

### Tool Note – Thonny
Use `print(...)` inside the loop (`print(i, years[i])`) to see which painting skips both branches. Run the same function twice with different split years to see the
effect of a changed boundary.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An easy-to-measure feature is automatically useful | It must also be relevant and distinguishing (number of ears for cat vs dog; price for apple vs banana) |
| `<` and `>` together cover every number | The boundary value falls in the gap: use `>=` or `else` and test it |
| A separating line is found in nature | It is a choice; a different line gives a different classification |
| More `if/elif` rules will eventually cover everything | Real data produces new edge cases faster than rules can be written; pictures have millions of pixels |
| This rule-based code is "AI" | A person wrote every rule; AI learns the rule from examples (next meetings) |

---

# 8. Assessment Evidence (formative)

- The Louvre trace table filled before running; the 1860 prediction explained in the warm-up
- Task 1 and Task 2 running with two split values; two songs added by the student
- Task 3 answer with reasons (relevant and distinguishing)
- Task 4: three calls plus the unripe-banana and softness-2 observations, in the student's words
- Exit check
