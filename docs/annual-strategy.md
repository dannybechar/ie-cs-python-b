# Grade 8 / AI + Python B — Annual Strategy

Source of truth: [`ministry-source/python-b-ai.pdf`](ministry-source/python-b-ai.pdf) — the Ministry program
**"בינה מלאכותית בשילוב מדעי המחשב — AI2 בשילוב אלגוריתמיקה באמצעות Python, חלק ב'"**
(published as `ai-Studies-Program-b.pdf` on meyda.education.gov.il).
Per-unit detail lives in each unit's own `unit-strategy.md` (written when the unit is built) — see
[`../course-map.md`](../course-map.md) for the full list.

## 1. Document Status and Sources

1. **`python-b-ai.pdf`** — the authority for units, topics, performance objectives, teaching methods,
   assessment and hours. Master syllabus table pp. 3–4; one chapter per unit on pp. 5–23.
2. **Ministry circular תשפ"ז** ([`ministry-circular-tashpaz-he.pdf`](ministry-source/ministry-circular-tashpaz-he.pdf), p. 2) —
   this program is Grade 8 alternative A; the Ministry exam (בחינת מפמ"ר) is set for **May 2027**; printed notes are allowed,
   calculators are not (p. 3).
3. **Clarifications תשפ"ז** ([`clarifications-tashpaz-he.pdf`](ministry-source/clarifications-tashpaz-he.pdf), p. 3) —
   compared with the old Python B, the new program drops the cyber chapter, the ciphers and **nested loops**, and moves
   tuple / set / queue / list of lists to Part C.
4. [`python-b-ai-working-edition-en.pdf`](ministry-source/python-b-ai-working-edition-en.pdf) — an unofficial English
   synthesis. Reference only; where it differs from the official PDF, the official PDF wins.
5. The teacher's raw materials (`Downloads\python-b-raw-meterials\`: a year strategy, the annual work plan, and six built
   meetings 1.1–1.3, 2.1–2.2, 3.1) are **inspiration only**.

**Hours rule (teacher's decision, 2026-09-28):** the master table on pp. 3–4 is the authority (21 theory + 39 practice = 60).
The per-chapter hours tables disagree with it for four units — Unit 1 (2 / 4), Unit 3 (1 / 5), Unit 5 (3 / 5),
Unit 7 (4 / 6) — and are not used for the theory/practice split. They are still used for the *order and weight of topics*
inside a unit.

## 2. Annual Framework

- Total: **60 academic hours** of 45 minutes = **2,700 minutes**
- Operating structure: **30 double meetings of 90 minutes**
- Official split: **21 theory hours + 39 practice hours**
- A **Knowledge + Lab** meeting is 45 theory / 45 practice; a **Lab + Lab** meeting is 0 / 90.
  Each unit has as many Knowledge + Lab meetings as it has theory hours; the rest are Lab + Lab.

## 3. Annual Structure by Unit

| # | Unit | Hours | Theory / Practice | Meetings | K+L / L+L |
|---|---|---:|---:|---:|---:|
| 1 | Python A Review | 6 | 1 / 5 | 3 | 1 / 2 |
| 2 | AI2 Year Opening | 4 | 2 / 2 | 2 | 2 / 0 |
| 3 | Functions | 6 | 2 / 4 | 3 | 2 / 1 |
| 4 | Bringing AI into Code (API) | 4 | 1 / 3 | 2 | 1 / 1 |
| 5 | Strings | 8 | 2 / 6 | 4 | 2 / 2 |
| 6 | Advanced Language Model | 6 | 2 / 4 | 3 | 2 / 1 |
| 7 | Lists | 10 | 3 / 7 | 5 | 3 / 2 |
| 8 | Classification | 8 | 4 / 4 | 4 | 4 / 0 |
| 9 | Recommender Systems | 8 | 4 / 4 | 4 | 4 / 0 |
|  | **TOTAL** | **60** | **21 / 39** | **30** | **21 / 9** |

## 4. Two Tracks, One Course

The program's rationale (p. 2): AI is not a separate unit — every programming building block gets an AI counterpart.

| Programming track | AI track |
|---|---|
| Python A review (Unit 1) | Classical rules vs learning from data (Unit 2) |
| Functions with `return` (Unit 3) | A wrapper function around an AI service (Unit 4) |
| Strings (Unit 5) | Tokens, meaning and context (Unit 6) |
| Lists (Unit 7) | Rule-based and learned classifiers (Unit 8); a list-based recommender (Unit 9) |

The year-long habit on both tracks: **a classical algorithm is transparent and fixed; an AI system is probabilistic and
learns from data** — so its output is checked, not trusted, and its builder is responsible for bias, privacy and copyright.

## 5. Provisional Meeting Outline

What each meeting covers, from each chapter's goals, teaching methods and per-topic table. It is refined — and may be
reordered inside a unit — when the unit is built and its `unit-strategy.md` is written.

| Meeting | Structure | Content (official page) |
|---|---|---|
| 1.1 | K+L | Compound conditions (`and`, `or`, `not`), `if` / `elif` / `else`, input validation (pp. 5–6) |
| 1.2 | L+L | Counted loops: `for` with `range(n)` and `range(start, stop, step)`; counters and totals (pp. 6–7) |
| 1.3 | L+L | Conditional loops: `while`, the stop condition, loops that never end; integrated review (p. 7) |
| 2.1 | K+L | The AI revolution; classical programming vs machine learning; Quick, Draw! and the worksheet "איך מחשב רואה בלי עיניים?" (p. 8) |
| 2.2 | K+L | Data, bias and responsibility: biased datasets in hiring, cars and medicine; "מצרכנים ליצרנים" (pp. 8–9) |
| 3.1 | K+L | Functions without / with parameters, no `return` (review); the black box, "what" vs "how" (p. 10) |
| 3.2 | K+L | Functions that return a value; `print` vs `return`; local and `global` variables (p. 10) |
| 3.3 | L+L | Bottom-up design: solving a problem with small returning functions (pp. 10–11) |
| 4.1 | K+L | API as a "waiter" between the code and the model; importing a library; a safe API key; a wrapper function that returns the model's answer (pp. 11–12) |
| 4.2 | L+L | Dynamic prompts with f-strings; a `while` loop that collects input and one call outside it; validation with `len` and `in`; prompt chaining; the "יום מאוזן" mini-project (pp. 12–13) |
| 5.1 | K+L | The empty string, `+`, `*`, `in`, indexing and `len`; position vs content (p. 13) |
| 5.2 | K+L | String methods: `find`, `upper`, `lower`, `count`, `startswith`, `endswith`, `isalpha`, `isnumeric`, `replace` (pp. 13–14) |
| 5.3 | L+L | Slicing `[start:end:step]` (p. 14) |
| 5.4 | L+L | Traversal: `for i in range(len(st))` vs `for ch in st`; a small text-processing program (pp. 3–4, 14) |
| 6.1 | K+L | Tokens, tokenization and token IDs; the context window; the tokenizer worksheet (pp. 15–16) |
| 6.2 | K+L | The semantic map (embeddings), self-attention, semantic distance (pp. 15–16) |
| 6.3 | L+L | The "סמנטעל" (Semantle) game: `calculate_similarity`, an attempt counter, percentages, an emoji thermometer (p. 16) |
| 7.1 | K+L | What a list is; access, update, concatenation, `len`, `in` (pp. 17–18) |
| 7.2 | K+L | List operations: `append`, `insert`, `remove`, `pop`, `index`, `count`, `sort`, `reverse`, `split`, `join` (p. 18) |
| 7.3 | K+L | The summation pattern (p. 18) |
| 7.4 | L+L | The sequential-search pattern (p. 18) |
| 7.5 | L+L | An integrated list problem solved with black-box functions (pp. 17–18) |
| 8.1 | K+L | Classification, good features and the decision boundary; a naive rule-based classifier in Python (apple / banana, songs by year) (pp. 19–21) |
| 8.2 | K+L | The machine-learning process: training vs test; first try of Teachable Machine; background and lighting bias (pp. 19–21) |
| 8.3 | K+L | Planned project (fist vs OK): challenge cases, 100+ images per class, planning against bias (pp. 20–21) |
| 8.4 | K+L | Testing on 7 outside images, accuracy, export the model and load it in Python (pp. 20–21) |
| 9.1 | K+L | Content-based vs user-based recommendation; design the class survey in Google Forms (pp. 21–23) |
| 9.2 | K+L | Similarity score between users' rating lists (parallel lists, loops, conditions) (pp. 22–23) |
| 9.3 | K+L | The digital twin: recommend an item the user has not seen that the twin liked; the main program (pp. 22–23) |
| 9.4 | K+L | Filter bubbles, echo chambers and the attention economy; the "בונים בועה ב-5 דקות" experiment (pp. 22–23) |

## 6. Default 90-Minute Lesson Pattern

Same rhythm as Python A: never more than 10–15 minutes of teacher talk before students act.

**Knowledge + Lab — first 45 minutes:** hook / predict → concept → live example → predict / trace → guided try.
**Second 45 minutes (and both halves of Lab + Lab):** warm-up bug → short demo → task → short demo → task → save → exit check.
Lab + Lab meetings hold the longer builds: the Unit 1 integrated review, the "יום מאוזן" and Semantle projects, the
list project, and (in Units 8–9, which are all Knowledge + Lab) the project steps spread over several meetings.

## 7. Depth Boundaries

What the official chapters do **not** require, so we don't teach it:

- **Python:** no nested loops (clarifications, p. 3); no tuples, sets, dictionaries, list comprehensions or lists of lists
  (moved to Part C); no default or keyword arguments; no classes.
- **AI:** no transformer, attention or embedding mathematics; no training mathematics, gradients or loss functions;
  no precision / recall / F1 / confusion matrix; no production back-end or HTTP internals.
- **Given code, not taught code:** where the program says students "integrate given code" — loading a Teachable Machine model
  (p. 19), reading the survey's CSV (p. 22), the embedding library's call (p. 15) — the library call is provided in the starter
  and students write the logic around it.

## 8. Tools and Safety (to settle before the unit is built)

| Unit | Needs | Decision for the teacher |
|---|---|---|
| 2 | Quick, Draw! (web) | Offline fallback if the site is blocked |
| 4 | An approved language-model API (the program's methods name Gemini, p. 12) and a key | Which service; teacher-held key, never in student code, screenshots or the repo |
| 6 | A multilingual embedding library installed in Thonny | Which library, and whether the lab computers can install it |
| 8 | Teachable Machine (web, camera) and a Python library to load the exported model | Which export format; a no-camera alternative |
| 9 | Google Forms / Sheets and a CSV export | Survey topic; no personal data in the survey |

## 9. Assessment

The Ministry exam (בחינת מפמ"ר) at the end of the year, set for **May 2027** (circular, p. 2). Its structure for the new
program has not been published — we don't guess it. Evidence is collected inside the 60 hours, following each chapter's
"דרכי הערכה": tracing and predicting code, identifying an algorithm's goal, writing and running solutions, and — for the AI
units — worksheets, experiment logs, a working project (יום מאוזן, Semantle, the classifier, the recommender) and a written
explanation of bias or limits.

## 10. Grade 8 Exit Profile

At the end of the year a student can:

1. Write compound conditions, `if` / `elif` / `else` and input validation.
2. Choose between a `for` loop and a `while` loop and explain why a loop stops.
3. Write functions with and without parameters and with and without `return`, and use a returned value.
4. Tell local from global variables.
5. Call a language-model API through a wrapper function with a dynamic prompt, keeping the key safe.
6. Process text with indexing, slicing, string methods and traversal.
7. Explain tokens, the context window, the semantic map and self-attention at a conceptual level.
8. Use lists and their operations, and implement the summation and sequential-search patterns.
9. Explain classification, features, the decision boundary, training vs test and accuracy — and build a rule-based classifier.
10. Explain content-based and user-based recommendation and implement a similarity score and a recommendation.
11. Name the bias, privacy and copyright risks of an AI system and who is responsible for them.
12. Explain their own code and the reasoning behind it.
