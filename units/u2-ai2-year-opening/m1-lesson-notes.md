# Unit 2.1 — AI2 Year Opening

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Rules or Learning? — Classical Programming vs Machine Learning (Quick, Draw!)

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny, Quick, Draw! (web)  
**Source of inspiration:** the codex deck `python_b_unit02_m01_ai_vs_rules_delivery.pptx` ("who wrote the decision?" sort, two mechanisms, the kettle rule, the learning pipeline, Quick, Draw! with privacy rules and an offline fallback, the guess log, the failure-analysis example, the dataset facts, the detective chain, the exit sentence kept; its "design your own recognizer" block dropped — 2.2 builds a fuller plan; "מפגש" labels removed) and the teacher's raw `G8_Unit2_M1` (the rule-based message flag kept as the warm-up, with its "rules, not AI" label; its "mixed system" boundary case kept)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny** or **Tool Note – Quick, Draw!**.

---

## 1. Position in Unit 2

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **2.1 (this)** | **AI around us → rules vs learning from examples → the kettle rule → Quick, Draw! → dataset detectives** | 45 / 45 |
| 2.2 | dataset, diversity, bias → three real cases → dataset audit in Python → improvement plan → the year's vision | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept / method (python-b-ai.pdf pp. 3, 8–9) | Covered here |
|---|---|
| Master table: the AI revolution; classical programming vs AI | ✅ hook, two mechanisms |
| Goal 1: classical programming (fixed rules written by a developer) vs machine learning (a model that learns patterns from examples) | ✅ sort, mechanisms, kettle rule |
| Concepts: machine learning, rule-based, dataset, pattern recognition | ✅ |
| Method 1: open with Quick, Draw! and a discussion of how the computer guesses in real time | ✅ Task 2 |
| Method 2: the worksheet "איך מחשב רואה בלי עיניים?" and detective work in the public drawings dataset | ✅ guess log, Task 3 |
| Assessment 1: why recognition failed (e.g. no modern / electric kettles in the dataset) | ✅ Task 1, Task 3 |

### Deliberate exclusions
Neural networks, training mathematics, bias as a formal concept (2.2), APIs (Unit 4).

---

## 3. Lesson Goal

**In classical code a person writes the rules; in machine learning a model finds patterns in many examples — so what it can recognize depends on the examples it saw.**

---

## 4. Core Mental Models

<div dir="rtl">

| תכנות קלאסי | למידת מכונה |
|---|---|
| קלט ← חוקים שאדם כתב ← פלט | דוגמאות מתויגות ← אימון ← מודל ← ניחוש על קלט חדש |
| קל להסביר איזה חוק הופעל | ההצלחה תלויה בדוגמאות |
| מתאים לבעיות חד-משמעיות | מתאים לזיהוי של דברים מגוונים (ציורים, קול, תמונות) |

</div>

- In both, **people** choose the goal, the data and the tests.
- A decision alone does not make a program AI; many real systems mix learned parts and written rules.
- A model's guess is a probability, not a fact — it can be confidently wrong.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 2.1 – פתיחת שנת AI2 · "חוקים או למידה?" |
| 2–6 | **Hook — the AI revolution (pairs):** list three places you met AI this week |
| 6–10 | **Who wrote the decision? (vote, then pairs):** a tax calculator with a fixed formula · a spam filter that adapts to new messages · a traffic light on a fixed schedule · a system that recognizes a hand drawing |
| 10–12 | Answer: rules — the calculator, the traffic light; learning from examples — the spam filter, the drawing |
| 12–18 | Two mechanisms (table above); people choose goals, data and tests |
| 18–22 | **Predict (pairs):** which kettle drawings will this rule miss? |
| 22–24 | Answer: an electric kettle, a kettle drawn from the side, one without a clear handle — more `if`s never cover every way to draw |
| 24–30 | Learning from examples: many labeled drawings → training finds repeating patterns → a model → a guess on a drawing it never saw |
| 30–34 | Boundary: a mixed system (a learned spam score plus a written "block list" rule); "a decision" is not enough to call it AI |
| 34–40 | Quick, Draw! and its dataset: about 50 million drawings in 345 categories from players around the world; each drawing is saved as strokes over time, with its category and whether it was recognized. Privacy: no names or personal details |
| 40–45 | The guess log (observation → hypothesis → test) · the lab missions |

The kettle rule (18–24):

```python
if circles == 1 and lines >= 2:
    print("kettle")
else:
    print("not kettle")
```

---

# 6. Second 45 Minutes — Lab

Starter: [`Rules_Starter.py`](Rules_Starter.py). Reference: [`Rules_Reference.py`](Rules_Reference.py).

## 45–51 — Warm-up: a rule you can point to

```python
# Warm-up: this is classical code - rules written by a person, not AI.
# Predict the output for 180 / yes, 180 / no and 100 / yes, then run and check.


def flag_message():
    message_length = int(input("Message length: "))
    has_link = input("Contains a link? (yes/no): ") == "yes"
    if message_length > 150 and has_link:
        print("Flag message")
    else:
        print("Allow message")
```

180 / yes → `Flag message` · 180 / no → `Allow message` · 100 / yes → `Allow message`. Change 150 to 100; 120 / yes → `Flag message`. Ask: did the program learn anything? (No — a person changed a rule.) No warm-up bug in this meeting: the point is that every result can be traced to one written line.

## 51–57 — Task 1: break the kettle rule

Run `kettle_rule()` and look for two failures:

<div dir="rtl">

| ציור | עיגולים | קווים ישרים | פלט | נכון? |
|---|---|---|---|---|
| קומקום מסורתי | 1 | 3 | kettle | כן |
| קומקום חשמלי גבוה | 0 | 6 | not kettle | לא — קומקום שהוחמץ |
| תמרור על עמוד | 1 | 2 | kettle | לא — "קומקום" מזויף |

</div>

Ask: add a condition that fixes one of them — what does it break? (Assessment 1: rules miss what nobody planned for.)

## 57–69 — Task 2: Quick, Draw! with a guess log (pairs)

One draws, one logs; swap after three drawings; six drawings in all. For each drawing: what was asked · when the right guess came · wrong guesses before it · what might have confused the model · one change to test next time.
Model entry (show it): *observation* — it guessed "cup" instead of "kettle"; *hypothesis* — the handle came before the spout, so it looked like a cup; *test* — draw again, spout first; *temporary conclusion* — stroke order may matter.

### Tool Note – Quick, Draw!
`quickdraw.withgoogle.com` → "Let's Draw!". No sign-in is needed; don't type any names. If the site is blocked, use the printed drawing strips: students guess at which stroke the object becomes recognizable.

## 69–81 — Task 3: dataset detectives

`quickdraw.withgoogle.com/data` → choose a category (kettle recommended — the official example). Compare drawings that were recognized with ones that were not: two patterns in the recognized ones, one feature of the missed ones, one careful hypothesis.
Example chain: recognized kettles have a clear spout and handle; some missed ones are tall electric kettles with no long spout → hypothesis: the dataset (or what the model learned) represents traditional kettles better → test: count successes by kettle type over more drawings. One drawing proves nothing.

## 81–85 — Share

Each pair reads one hypothesis and the test that would check it.

## 85–90 — Exit check

1. Complete: "When a model makes a mistake on a new drawing, the first thing to check is …" (e.g. whether similar examples were in the data it learned from)
2. Rules or learned from examples: a program that gives a discount to anyone over 65 · an app that recognizes songs from a short recording? (rules · learned)
3. Why doesn't adding more `if`s make the kettle rule reliable? (people draw in endless ways — rules only cover what their writer imagined)

### Tool Note – Thonny
Only one call at the bottom of the file is active; remove the `#` from `kettle_rule()` and add it to `flag_message()` for Task 1.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Every program that decides is AI | A program that follows written rules is classical code |
| AI means there are no rules anywhere | Many systems mix learned models and written rules |
| A model learns by itself, without people | People choose the goal, the examples and the tests |
| A fast right guess means the computer understands the object | It matched patterns from examples; it can be confidently wrong |
| A big dataset covers everything | Size helps; variety and quality must be checked separately |
| One failed drawing proves the dataset is biased | It gives a hypothesis to test on more examples |

---

# 8. Assessment Evidence (formative)

- The "who wrote the decision" sort with reasons
- Two failures of the kettle rule and why more rules don't solve it (official assessment 1)
- A guess log with observation → hypothesis → test for at least three drawings
- One dataset hypothesis with a planned check (method 2)
- Exit check
