# Unit 2.2 — AI2 Year Opening

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Data, Bias and Responsibility — From Consumers to Creators

**Status:** Approved by the teacher  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny  
**Source of inspiration:** the codex deck `python_b_unit02_m02_data_bias_responsibility_delivery.pptx` (dataset / diversity / bias definitions, the kettle case, bias before and after training, the three stations — hiring, medical, self-driving car — with model answers, cultural vs social bias, the improvement plan and the hiring example, perspectives, the developer checklist, the summary sentences and the exit sentence kept; the 1,000-face-photos audit replaced by a car-dataset audit in Python so the lesson never handles faces or personal data; "מפגש" labels removed) and the teacher's raw `G8_Unit2_M2` (the 9-outdoor / 1-indoor hook and the counts audit kept, extended to three groups with shares and warnings)  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 2

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 2.1 | AI around us → rules vs learning from examples → the kettle rule → Quick, Draw! → dataset detectives | 45 / 45 |
| **2.2 (this)** | **dataset, diversity, bias → three real cases → dataset audit in Python → improvement plan → the year's vision** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept / method (python-b-ai.pdf pp. 3, 8–9) | Covered here |
|---|---|
| Master table: data, responsibility and the danger of bias; "מצרכנים ליצרנים" — the year's vision | ✅ |
| Goal 2: define bias; how a biased or non-diverse dataset affects real decisions (hiring software, autonomous car, medical system) | ✅ stations |
| Goal 3: why data diversity matters for a fair and accurate system | ✅ kettle case, audit, plan |
| Concepts: dataset, biased data, cultural and social bias, data diversity | ✅ |
| Method 3: class discussion of ethics and bias in real systems and the developer's responsibility | ✅ stations, checklist |
| Assessment 2: examples where biased data leads to wrong, unfair or dangerous decisions | ✅ stations |
| Assessment 3: summary sentences on dataset size and diversity vs accuracy and fairness | ✅ exit check |

### Deliberate exclusions
Fairness metrics, precision / recall, training code, collecting any real personal data or photos of students.

---

## 3. Lesson Goal

**A model can only be as good as the variety in its data: a systematic gap in the data (bias) becomes a systematic gap in its decisions — and the people who build it are responsible before and after launch.**

---

## 4. Core Mental Models

- **Dataset** — the examples used for learning or for testing. **Diversity** — how well they cover different people, places and situations.
- **Bias** — a systematic tendency to succeed more on some cases and less on others. It can come from ordinary collection choices, not only from bad intent.
- More of the same data is not diversity; an average score can hide a group that fails.
- Bias enters **before** training (a narrow goal, one source, inconsistent labels, missing rare cases) and **after** it (average-only testing, a new context, no monitoring).
- **Cultural bias:** objects, gestures and words look different in different places. **Social bias:** data from the past carries past unequal decisions — a model can repeat them.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–2 | Title: יחידה 2.2 – פתיחת שנת AI2 · "נתונים, הטיות ואחריות" |
| 2–6 | **Hook (pairs):** a model learned "bottle" from 10 photos — 9 outdoors, 1 indoors. What could go wrong? |
| 6–8 | Answer: it may fail indoors — the data barely showed that situation |
| 8–14 | Dataset, diversity, bias (above); "more photos" ≠ "more kinds of photos" |
| 14–18 | **Predict (pairs):** a model trained mostly on silver kettles with black handles — how will it do on a tall electric kettle, a painted clay kettle, a round black kettle, a partial drawing that shows only the spout? Give a reason for each |
| 18–20 | Answer: more risk the further a case is from the repeated examples — a gap in representation; the fix is planned variety, tested group by group |
| 20–24 | Where bias enters: before and after training (two columns) |
| 24–32 | **Three stations (groups, one station each):** find the decision, who could be hurt, and the missing check — hiring software trained on past employees · a medical system tested mostly on one population · a self-driving car trained mostly by day in clear weather |
| 32–36 | Answers: compare results by group; widen the data and measure each population; test night, rain and glare — and act when a gap appears |
| 36–40 | Cultural vs social bias (neutral examples first: kettle styles, hand gestures) |
| 40–45 | The developer's checklist: before launch (clear goal, minimal permitted data, representation, edge tests) · after launch (monitor gaps, report errors, human review and appeal, fix or stop); the lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Audit_Starter.py`](Audit_Starter.py). Reference: [`Audit_Reference.py`](Audit_Reference.py).

## 45–52 — Warm-up: the audit that says "Balanced"

```python
# Warm-up: 5 of 50 kettle drawings are electric kettles. The program says "Balanced". Find the bug.


def kettle_audit():
    traditional = 45
    electric = 5
    total = traditional + electric
    electric_share = electric / total * 100
    print("Electric kettles:", electric_share, "%")
    if electric_share > 20:
        print("Under-represented")
    else:
        print("Balanced")
```

Output: `Electric kettles: 10.0 %` then `Balanced`. A group is under-represented when its share is **small** → `electric_share < 20` → `Under-represented`. The code counts a dataset — it is not a model.

## 52–64 — Task 1: `car_data_audit()`

Read the number of day, night and rain images; print each share in %; warn about every group under 20%; if there were no warnings, print `Every group is at least 20%` (a counter from Unit 1). Tests:

<div dir="rtl">

| יום | לילה | גשם | פלט |
|---|---|---|---|
| 800 | 150 | 50 | Day: 80.0 % · Night: 15.0 % · Rain: 5.0 % · two warnings (night, rain) |
| 400 | 300 | 300 | 40.0 / 30.0 / 30.0 · Every group is at least 20% |
| 600 | 200 | 200 | 60.0 / 20.0 / 20.0 · Every group is at least 20% (20 is not under 20) |

</div>

Ask: the first car scores 95% on its test set. Why can that still be dangerous? (the test is mostly daytime too — an average hides night and rain)

## 64–76 — Task 2: an improvement plan (groups, on paper)

Choose one station from the lesson. Five steps: who is affected by the decision · which examples are missing · a test by group or situation · what happens when a gap is found · how feedback arrives after launch. Model plan (hiring): affected — candidates and employers; missing — varied experience paths, not only past hires; test — compare pass rates between relevant groups; gap → stop using it, check the features, change the data; after launch — monitoring, records and a human appeal.

## 76–80 — Peer feedback

Each group reads its plan in one minute; listeners give one missing piece of evidence or one action.

## 80–84 — From consumers to creators

The year's vision: this year the class moves from using AI to building code with it — an app that calls a language model (Unit 4), the Semantle word game (Unit 6), an image classifier (Unit 8) and a recommender from the class survey (Unit 9). Every one of them will need today's questions: whose data, which gaps, who checks.

## 84–90 — Exit check — summary sentences (official assessment 3)

Complete each sentence and add an example:
1. A big dataset that is not diverse may … (fail on the cases it rarely saw)
2. A fairer model needs … (examples from every relevant group and situation, and a test for each group)
3. An accuracy score for everyone together may hide … (a group or situation where it fails)
4. A developer's responsibility continues after … (launch — monitoring, fixing, an appeal route)

### Tool Note – Thonny
`/` always gives a decimal number — the share prints as `10.0`, not `10`.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| More data always means better data | More of the same adds no variety |
| Bias always means someone meant to discriminate | It often comes from ordinary collection choices |
| High average accuracy proves the system is fair | The average can hide a group that fails |
| Past data is neutral truth | It can carry past unequal decisions |
| One good test proves the system works | Test every group and situation, and keep monitoring |
| The model is responsible for its mistakes | People and organizations are responsible |

---

# 8. Assessment Evidence (formative)

- Station answers: the decision, who could be hurt, the missing check (official assessment 2)
- `car_data_audit()` passing all three tests, with the reason 95% can still be dangerous
- A five-step improvement plan with one change after feedback
- The four summary sentences (official assessment 3)
