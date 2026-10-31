# Unit 2 — AI2 Year Opening

**4h = 2 Theory + 2 Practice = 2 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 2 (pp. 8–9); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md). Teaching materials: [`../../docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).

**Build status:** 🔶 reworked from the Ministry teaching materials — both meetings built, awaiting teacher approval.
Main sources: the Ministry deck 3.1 "שיעור פתיחה לשנה ב AI2" (50 slides), the worksheet 3.2 "איך מחשב רואה בלי עיניים?" and the teacher solution 3.2.0.
The earlier version (codex decks, raw meetings, "Rules or Learning?" and "Data, Bias and Responsibility") is superseded.

## Official topics and hours

Unit totals from the master table (2 theory / 2 practice). The chapter's own table (p. 9) lists one row — "תכנות קלאסי לעומת AI,
מהפכת ה-AI והתנסות ב-Quick, Draw!" — with garbled numbers; used only for topic order (hours rule, `CLAUDE.md`).
Minutes = hours × 45.
Status: ✅ built and approved · 🔶 built, awaiting approval · ⏳ planned, not built · ⚠️ gap to resolve.

| Topic (Ministry, master table p. 3) | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| מהפכת ה-AI — the AI revolution (images, quiz, definition, four revolutions, why now) | 2.1 (first half) | part of 2.1 | 🔶 |
| תכנות קלאסי לעומת AI — classical programming vs AI (greeting for Grandma Sarah) | 2.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| התנסות ב-Quick, Draw! ונתונים — experience with Quick, Draw!, data and bias (worksheet 3.2) | 2.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| "מצרכנים ליצרנים": the year's road map and responsibility | 2.2 (second half of the theory, summary) | part of 2.2 | 🔶 |
| **Total** | | **90 / 90** | |

Chapter goals, concepts and methods (pp. 8–9):

- Goal 1: rule-based programming vs machine learning → 2.1 (the greeting both ways) 🔶
- Goal 2: define bias; how a biased or non-diverse dataset affects real decisions → 2.2 (worksheet Q3) 🔶
- Goal 3: why data diversity matters for a fair, accurate system → 2.2 (fill-in sentences) 🔶
- Concepts: machine learning vs rule-based, dataset, biased data, data diversity, pattern recognition → 2.1–2.2 🔶
- Method 1: open with Quick, Draw! and a discussion → 2.2 (volunteers on the board); 2.1 opens with the "AI or not?" warm-up and quiz 🔶
- Method 2: the worksheet "איך מחשב רואה בלי עיניים?" → 2.2 lab (the Ministry worksheet itself) 🔶
- Method 3: discussion on ethics and the developer's responsibility → 2.2 summary 🔶
- Assessment 1: why the computer failed (no electric kettles in the data) → 2.2 worksheet Q2 🔶
- Assessment 2: biased data leading to wrong, unfair or dangerous decisions → 2.2 worksheet Q3.2 🔶
- Assessment 3: summary sentences on dataset size and diversity → 2.2 fill-in sentences 🔶

## Unit 2.1 — Knowledge + Lab: AI or Not? A Greeting for Grandma Sarah
- Warm-up "AI or not?" (image pairs), quiz "is there AI inside?" (6 products), the shared feature, the definition of AI.
- The four revolutions and why now (brain + power + fuel); the moon vs the greeting question.
- The greeting in classic Python (`print` → `input`/`if` → hobby with `+`: always the same output) vs an AI greeting in a chatbot (not through code); comparison table.
- Lab: the students write the classic greeting step by step (warm-up bug: a variable name inside quotes).

## Unit 2.2 — Knowledge + Lab: How Does a Computer See Without Eyes?
- Quick, Draw! with three volunteers on the board; summary questions; what AI changes; consumers to creators with the API code teaser (not run).
- The year's road map: functions, strings, lists, language model, classification, recommender systems, API; projects.
- Lab: the Ministry worksheet 3.2 (early recognition, The Data, a failure, representativeness — the Israeli stop sign, why biased data is dangerous, guessing the future from the stroke animation, four fill-in sentences); responsibility; exit check.
- If time: the dataset audit in Python (`Audit_*`), kept from the previous version.

### Scope decisions
- **The Ministry flow wins.** Removed from the previous version: the kettle rule and the rule-based message flag (2.1), the Quick, Draw! guess log and dataset-detective chain (replaced by the worksheet), the three stations, bias before / after training, cultural vs social bias, the improvement plan and the developer checklist (2.2). Kept: the dataset audit as an if-time block.
- **Python stays at Unit 1 level** (`print`, `input`, `if`/`else`, `+` on strings, `int()`); the greeting uses English strings so the console stays left-to-right and the `if` chooses a sign-off line (the Ministry's Hebrew branch relies on a gendered verb).
- **AI greeting through a chatbot only.** The `genai` code appears once, as the Ministry's teaser ("no need to understand yet"), is never run, and holds only a placeholder instead of a key; the API itself is Unit 4.
- **Not taught:** neural-network internals, training mathematics, fairness metrics.
- **Web tools:** Quick, Draw! and its data page need internet; if blocked, the teacher shows them on the board. No names or personal data are typed into any site.

## Exit criteria
The student tells a product with AI from one without (and why), defines AI in a sentence, writes a classic greeting program with `input`, `if` and `+` and explains why it always gives the same output for the same input, explains why Quick, Draw! recognised or failed on a drawing using the data, gives one example of biased data causing a wrong, unfair or dangerous decision, and names the year's road map.

## Enrichment
- 2.1: `greeting_4()` (an age rule); a chatbot greeting asked twice, with a list of the facts to check.
- 2.2: `car_data_audit()` with an empty dataset (0, 0, 0 → `ZeroDivisionError`) — how should an audit program guard against it?
