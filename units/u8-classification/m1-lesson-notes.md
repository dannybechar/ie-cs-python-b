# Lessons 16.0–16.2 — Classification

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: Classification by Rules — Features and a Separating Line

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry teaching materials **16.0** (teacher emphases), **16.1** (deck, 68 slides: dog or bagel, the Louvre
classifier, good features, two features and a separating line, `classify_fruit`) and **16.2.0** (teacher solution of worksheet 16.2: Spotify
playlists, choosing features, `classify_fruit`, an edge case) and the **worksheet 16.2** itself (now delivered, `Classwork 16.2`; the lab follows its
five questions, the fruit-function exercise and the "advanced features" ideas). The v1 build (from `python_b_unit08_…_complete_unit.md`) is kept only where the Ministry is silent: the
relevant-vs-distinguishing language, the weather classifier (now "if time") and the "a boundary is a developer's decision" idea.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (lessons 4.1–4.6) and lists (lessons 9.1–9.5, 12.0–14.5) — the Ministry code uses `def`, parallel lists, `append` and `range(len(...))`.

---

## 1. Position in the classification block (lessons 16.0–19.1)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **Lessons 16.0–16.2 (this)** | **classification by rules, features, a separating line** | 45 / 45 |
| Lessons 17.0–17.1 | training set and test set, challenging cases, bias, first Teachable Machine try | 45 / 45 |
| Lessons 18.0–18.1 | accuracy, the fist / OK project, export | 45 / 45 |
| Lessons 19.0–19.1 | the trained model inside Python, confidence | 45 / 45 |

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
Training and test sets, Teachable Machine (lessons 17.0–17.1), accuracy (lessons 18.0–18.1), model code (lessons 19.0–19.1). No nested loops, no lists of lists, no comprehensions.

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

# 6. Second 45 Minutes — Lab (worksheet 16.2 with its teacher solution 16.2.0)

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

## 53–61 — Task 1: a playlist classifier (16.2 Q1–2)

Official data: `years = [2008, 2022, 2015, 1999]`, `songs = ["Halo", "As It Was", "Shape of You", "All Star"]` (the worksheet gives the finished
`classifier()` with split year 2015; our brief asks the students to write it, the Ministry gives it ready: use the Ministry version on the board if the class is slow).
**Q1:** the students **choose their own split year** (examples 2010, 2020), predict with the trace table (columns `i`, `songs[i]`, `years[i]`, condition True / False, the two lists),
run and check. **Q2:** add two songs they like to both lists (the starter already has the Ministry's additions `Believer` 2017 and `Michelle` 2026).
The worksheet's two list names are `classic` / `modern`; our starter uses `nostalgia` / `hits` (accept both).

Trace table, split year 2020 (the Ministry solution's example):

| i | songs[i] | years[i] | condition | classic | modern |
|---|---|---|---|---|---|
| 0 | Halo | 2008 | True | ["Halo"] | [] |
| 1 | As It Was | 2022 | False | ["Halo"] | ["As It Was"] |
| 2 | Shape of You | 2015 | True | ["Halo", "Shape of You"] | ["As It Was"] |
| 3 | All Star | 1999 | True | ["Halo", "Shape of You", "All Star"] | ["As It Was"] |

Real output on all six songs (`task1_songs`, Python 3.14):

```text
split 2015:  nostalgia: ['Halo', 'All Star']   hits: ['As It Was', 'Shape of You', 'Believer', 'Michelle']
split 2020:  nostalgia: ['Halo', 'Shape of You', 'All Star', 'Believer']   hits: ['As It Was', 'Michelle']
```

## 61–67 — Task 2: another feature (16.2 Q3–4)

Q3: which other feature could Spotify use (length, singer, tempo, genre, mood)? Q4: classify the songs by one of the suggested features with **two parallel lists**
and an empty list per category. Our model: length, short under 200 seconds, long otherwise (`lengths = [180, 240, 150, 310, 200, 199]`; the lengths are made up for practice,
the Ministry's own example uses `[180, 240, 150, 310]` with placeholder titles):

```text
short: ['Halo', 'Shape of You', 'Michelle']
long: ['As It Was', 'All Star', 'Believer']
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

## 82–86 — Task 5: think, no code (16.2 Q5)

A programmer writes: *if the song's speed is above 120 it is "happy", otherwise "sad"*. Find a song or style where it fails (a fast, sad rock song; a slow, happy
lullaby) and explain why a year is easier to turn into an `if` than a mood. **If time — the Ministry's "advanced features":** another classifier of the student's choice. Ministry ideas:
**vehicles** (number of wheels, where it travels, speed, engine, handlebar or round steering wheel), **animals** (mammal / bird / fish by number of legs, body covering, color, way of moving),
**geometric shapes** (number of sides, sum of angles) or their own idea; a sample vehicle classifier is `task_if_time_vehicles` in the reference. Our own extra, the v1 weather classifier
`classify_activity` (reference file, two edge cases), stays as a second option.

## 86–90 — Save and exit check

Save As `G8_U8_M1_Classifier_<Name>.py`.

1. What is a feature, and what makes it a good one?
2. What is a separating line?
3. Why is an unripe banana an edge case for the fruit rule?
4. Why can't we write `if/else` rules for every picture in the world?

### Wording and language notes (worksheet 16.2 vs our files)
- **Student-facing Hebrew says "פעולה" (as the Ministry does), never "פונקציה"**; the brief says so in its reference box.
- The Ministry is itself inconsistent about the unknown fruit: the deck prints `"לא ידוע"`, the worksheet text says `"פרי לא מוכר"`, the teacher key adds emoji. We print English strings
  (`apple`, `banana`, `unknown fruit`); the outputs for `(1, "green")`, `(4, "yellow")`, `(3, "purple")` match the key. Hebrew return strings are an acceptable variant.
- Q1 of the second exercise ("choose two features") and the three test calls: the worksheet leaves two calls blank (`classify_fruit(________)`); the key fills them with `(4, "yellow")` and `(3, "purple")`.
- Ministry pictures of 16.1 (dog or bagel, cat/dog scatter, eye colour and ear axis) are in the deck; the teacher sources them from the deck itself.

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
