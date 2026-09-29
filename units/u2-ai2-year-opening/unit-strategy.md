# Unit 2 — AI2 Year Opening

**4h = 2 Theory + 2 Practice = 2 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 2 (pp. 8–9); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** ✅ complete — all 2 meetings built and approved by the teacher.
Inspired by the codex decks (`Downloads\python-b-codex\python_b_unit02_m01–m02_*.pptx`, the main source) and the teacher's
raw meetings (`Downloads\python-b-raw-meterials\ie-cs-python-b\U2_M1–M2`).

## Official topics and hours

Unit totals from the master table (2 theory / 2 practice). The chapter's own table (p. 9) lists one row — "תכנות קלאסי לעומת AI,
מהפכת ה-AI והתנסות ב-Quick, Draw!" — with garbled numbers; used only for topic order (hours rule, `CLAUDE.md`).
Minutes = hours × 45.
Status: ✅ built and approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry, master table p. 3) | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| מהפכת ה-AI — the AI revolution | 2.1 (hook) | part of 2.1 | ✅ |
| תכנות קלאסי לעומת AI — classical programming vs AI | 2.1 (45 T + 45 P) | 45 / 45 | ✅ |
| נתונים, אחריות והסכנה בהטיות — data, responsibility and bias | 2.2 (45 T + 45 P) | 45 / 45 | ✅ |
| "מצרכנים ליצרנים": the year's vision — building code that uses AI | 2.2 (closing) | part of 2.2 | ✅ |
| **Total** | | **90 / 90** | |

Chapter goals, concepts and methods (pp. 8–9):

- Goal 1: rule-based programming vs machine learning → 2.1 ✅
- Goal 2: define bias; how a biased or non-diverse dataset affects real decisions (hiring, autonomous car, medical) → 2.2 ✅
- Goal 3: why data diversity matters for a fair, accurate system → 2.2 ✅
- Concepts: machine learning vs rule-based, dataset, biased data, cultural and social bias, data diversity, pattern recognition → 2.1–2.2 ✅
- Method 1: open with Quick, Draw! and a discussion → 2.1 ✅
- Method 2: the worksheet "איך מחשב רואה בלי עיניים?" and detective work in the public drawings dataset → 2.1 lab (our brief is the worksheet) ✅
- Method 3: class discussion on ethics and bias in real systems and the developer's responsibility → 2.2 ✅
- Assessment 1: why the computer failed (e.g. no modern / electric kettles in the dataset) → 2.1 Task 3, 2.2 hook ✅
- Assessment 2: examples where biased data leads to wrong, unfair or dangerous decisions → 2.2 stations ✅
- Assessment 3: summary sentences on dataset size and diversity vs accuracy and fairness → 2.2 exit check ✅

## Unit 2.1 — Knowledge + Lab: Rules or Learning? (Quick, Draw!)
- where students already meet AI; who wrote the decision — a person or examples?
- classical: input + rules → output. Machine learning: labeled examples → training → model → a guess on new input.
- the kettle rule: rules break on drawings nobody planned for; mixed systems exist.
- lab: a rule-based Python demo, breaking the kettle rule, Quick, Draw! with a guess log, detective work in the dataset.

## Unit 2.2 — Knowledge + Lab: Data, Bias and Responsibility
- dataset, diversity, bias (a systematic gap — not only bad intent); where bias enters before and after training.
- three stations: hiring, a medical system, a self-driving car. Cultural vs social bias.
- lab: a dataset-audit program (shares in %, warnings), an improvement plan for one station, the year's vision.

### Scope decisions
- **Codex decks were the main source** (hook, two mechanisms, kettle rule, Quick, Draw! log, dataset facts, detective chain,
  kettle case, three stations, bias before / after training, dataset audit, cultural vs social bias, improvement plan,
  perspectives, developer checklist). Changed: "מפגש" labels removed; the codex 2.1 "design your own recognizer" block dropped
  (it repeats the 2.2 plan); the 1,000-face-photos audit replaced by the car dataset audit in Python — the lesson never
  handles faces or personal data.
- **Raw meetings:** kept the rule-based message flag (2.1 warm-up, labeled "rules, not AI"), the 9-outdoor / 1-indoor hook
  and the counts audit (2.2 lab, extended to three groups with a warning counter).
- **Worksheet:** the official worksheet "איך מחשב רואה בלי עיניים?" is in the Ministry's AI2 classroom (clarifications p. 5);
  our lab brief follows its method (observe → hypothesize → check). The teacher may hand out the Ministry sheet instead.
- **Not taught:** neural network internals, training mathematics, fairness metrics, precision / recall, AI APIs (Unit 4).
- **Web tools:** Quick, Draw! and its data page need internet; the offline fallback is printed drawing strips (teacher prep).
  No names or personal data are typed into any site.

## Exit criteria
The student explains the difference between rules written by a person and a model that learned from examples, defines
dataset, diversity and bias, gives a real example of how a non-diverse dataset leads to a wrong or unfair decision, and
names one responsibility of a developer before and one after launch.

## Enrichment
- 2.1: more Quick, Draw! categories with a hypothesis tested twice.
- 2.2: `car_data_audit()` with an empty dataset (0, 0, 0 → `ZeroDivisionError`) — how should an audit program guard against it?
