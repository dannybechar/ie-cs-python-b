# Unit 2.2 — AI2 Year Opening

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: How Does a Computer See Without Eyes? Quick, Draw!, Data and the Road Ahead

**Status:** Built, awaiting teacher approval 🔶  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Quick, Draw! and its data page (web), Ministry worksheet 3.2 (Classroom); Thonny only for the if-time block  
**Source of inspiration:** the Ministry deck **3.1** (slides 35–50: Quick, Draw! with three volunteers, its rules, the summary questions, the programmers' role, "AI changes the world", consumers to creators with the language-model code teaser, the year's road map, the summary and "with great technology comes great responsibility") and the Ministry worksheet **3.2 "תרגול לפיצוח — איך מחשב רואה בלי עיניים?"** with the teacher's solution **3.2.0** (the whole lab: early recognition, the Data page, a failure, can a person recognise it, the Israeli stop sign, why biased data is dangerous, "guessing the future" from the stroke animation, the four fill-in sentences). **Changed from the previous version (Data, Bias and Responsibility):** the three stations, bias before and after training, cultural vs social bias, the improvement plan and the developer checklist are replaced by the Ministry worksheet and its model answers; the kettle failure is now the Ministry's own example. **Kept from the old version:** the dataset audit in Python (the kettle warm-up bug and `car_data_audit()`) — now only an "if time" block for fast finishers, because it turns the worksheet's question "is the dataset representative?" into numbers. **Changed from the Ministry:** the teaser code shows English strings and is labelled "no need to understand yet"; it is never run (no API key in any file; the API is Unit 4).  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Quick, Draw!** or **Tool Note – Thonny**.

---

## 1. Position in Unit 2

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 2.1 | AI or not? → definition → the revolutions → classic greeting in Python vs AI greeting | 45 / 45 |
| **2.2 (this)** | **Quick, Draw! → worksheet "איך מחשב רואה בלי עיניים?" → data and bias → consumers to creators, the year's road map, responsibility** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept / method (python-b-ai.pdf pp. 3, 8–9; Ministry deck 3.1, worksheet 3.2) | Covered here |
|---|---|
| Master table: data, responsibility and the danger of bias; "מצרכנים ליצרנים" | ✅ worksheet Q3, consumers to creators, summary |
| Goal 2: bias and how a biased or non-diverse dataset affects real decisions (hiring, autonomous car, medical) | ✅ worksheet Q3.2 and its model answer |
| Goal 3: why data diversity matters for a fair, accurate system | ✅ fill-in sentences 1–3 |
| Concepts: dataset, biased data, data diversity, pattern recognition | ✅ |
| Method 1: open with Quick, Draw! and a discussion | ✅ volunteers on the board |
| Method 2: the worksheet "איך מחשב רואה בלי עיניים?" and detective work in the drawings dataset | ✅ the lab |
| Method 3: discussion of ethics and the developer's responsibility | ✅ summary slide |
| Assessment 1: why the computer failed (e.g. no electric kettles in the dataset) | ✅ worksheet Q2 |
| Assessment 2: biased data leading to wrong, unfair or dangerous decisions | ✅ worksheet Q3.2 |
| Assessment 3: summary sentences on dataset size and diversity | ✅ fill-in sentences |

### Deliberate exclusions
Neural-network internals, fairness metrics, the API code (shown only as a teaser), any real personal data or photos of students.

---

## 3. Lesson Goal

**A model learns from the examples it was given: more examples and more varied examples make it more accurate and fair, examples that miss a group make it fail on that group — and the people who build it are responsible.**

---

## 4. Core Mental Models

- **Dataset** — the examples a system learns from. **Diversity** — how well they cover different people, places and situations. **Biased data** — examples that represent only one culture or one kind of person.
- Quick, Draw! keeps the **whole movement of the hand** (the order of the strokes), not just the finished picture — so it can "guess the future" before you finish.
- A system compares a new drawing with similar drawings in its data; it does not understand the object. A person can think of "something similar"; the system cannot go beyond its data.
- **Consumers → creators:** this year the students stop only using AI and start building code that uses it.
- **With great technology comes great responsibility:** data is the fuel of AI; the more diverse the examples, the more accurate and fair the AI is for everyone.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: יחידה 2.2 – פתיחת שנת AI2 · "איך מחשב רואה בלי עיניים?" |
| 1–3 | Recap of 2.1: AI learns from examples; data is the fuel. Today: see how, and what we build this year |
| 3–5 | Meet Quick, Draw! (a game by Google's engineers; an AI that learned to recognise drawings from many examples; the goal: make it recognise your drawing as fast as possible) |
| 5–18 | **Quick, Draw! on the board:** 3 volunteers, 2 rounds each (6 rounds). The class writes on the board how long each recognition took. **Audience task:** at which moment did the AI recognise the drawing — was there a line that helped? |
| 18–22 | **Summary questions (pairs, then class; answers after):** At which stage did the game succeed? When did it not? Did it ever recognise before you finished (explained in the worksheet)? AI does not follow a fixed "rule book" — it learns from many examples; the data is the fuel; do the examples matter? (worksheet) |
| 22–24 | Preview of the Data page: the game's drawings are public — we will investigate them in the lab |
| 24–26 | **Predict (pairs):** what is the programmers' role in our world? (solving problems with technology; once with fixed rules, now with AI inside the code too) |
| 26–29 | AI changes the world: learning, climate, environment, health, social. Optional: the Ministry's short video of an original social-field initiative (deck slide 44) |
| 29–32 | **Consumers → creators:** most of us use Gemini, ChatGPT or Copilot as consumers; this year we build with AI |
| 32–36 | **Teaser:** the Ministry's code that asks a language model for the greeting (below). "No need to understand it — we will, later this year." It is **not run**; no API key |
| 36–45 | **The year's road map:** Python — functions, strings, lists; AI — language model, classification, recommender systems; bringing AI into code (API). Projects: a day planner, a guessing game, a hand-gesture recognition system. The worksheet mission |

The teaser (Ministry deck slide 46, English strings; compiles, does not run without a key — `WRITE_YOUR_API_KEY_HERE` is a placeholder):

```python
from google import genai

# API settings
client = genai.Client(api_key="WRITE_YOUR_API_KEY_HERE")
# input from the user
sender = input("Who is wishing? (grandson/granddaughter): ")
hobbies = input("What does Grandma Sarah love? ")
style = input("Which style? (moving/rhymes/funny): ")
# build the prompt
prompt = ("Write a birthday greeting for Grandma Sarah in a " + style + " style.\n"
          "The sender is her " + sender + " and her hobbies are " + hobbies + ".\n"
          "Weave the hobbies in naturally.")
# send the prompt to the language model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt)
# print the result
print(response.text)
```

Say: the program we wrote in 2.1 had every line written by us; here the sentence is written by the model — and we decide how it helps. Check the model name against the current Gemini list before Unit 4.

---

# 6. Second 45 Minutes — Lab

The lab is the Ministry worksheet 3.2 (the teacher assigns it in Classroom); our brief [`m2-lab-brief-he.md`](m2-lab-brief-he.md) follows it step by step; the model answers below are the Ministry's (3.2.0). Optional code for fast finishers: [`Audit_Starter.py`](Audit_Starter.py), [`Audit_Reference.py`](Audit_Reference.py).

## 45–50 — Two rounds of Quick, Draw! (each student)

Goal: get the system to recognise the drawing within 20 seconds. The game is in English; the browser can translate it (automatic translation is not always accurate). No sign-in, no names.

## 50–58 — Question 1: early recognition and The Data

a) An object recognised in a short time — which part of the drawing helped? (Model: a watermelon — a half-circle arc and a second arc for thickness, like a smile; recognised after the second arc.) b) On **The Data** page (objects sorted A–B): how many drawings of the object are there? (watermelon: 124,481 in the Ministry's example); is there a common viewing direction; how does yours resemble and differ? Conclusion "recognised quickly because …" (many people drew a half watermelon). c) Find a drawing that does not fit the object (an upside-down arc) and flag it with **Flag as inappropriate** — removing it from the data prevents mistakes.

## 58–66 — Question 2: a failure

a) Play until the system fails on an object you drew clearly (Model: a kettle that looks like an electric kettle). b) Look at the data of that object: (Model: the data has traditional kettles with a spout, the kind put on the stove that whistles — today's electric kettles are missing, so the data does not represent "kettle" well). c) Could a person recognise it? (Model: yes — told "not a vase, not a jug" a person tries a similar meaning; the system looks for similarity to the drawings in its data and here they do not represent it).

## 66–75 — Question 3: are the drawings representative?

Search "Stop sign", "Bread" or "house". Does the data represent how these look **in Israel**? (Model: the Israeli stop sign has a drawing of a hand; in the data every example says STOP in English and no hand appears.) Then: an AI system with a real impact (an autonomous car, hiring software, a medical robot) — what can happen if its data represents only one culture or one kind of people? (Models: hiring software that learned only from men's résumés may not hire women; a car may not stop at the Israeli stop sign; a medical system trained on one group may detect diseases worse in women, children, older people or people of other origin. The AI learns from the examples it is given; if they are not diverse, its decisions may be inaccurate, unfair and sometimes dangerous.)

## 75–81 — Question 4: guessing the future

a) Why does the computer recognise drawings before you finish? b) Detective: on the Data page (e.g. apple) hover over a drawing (without clicking) — it "comes alive"; the system saved the whole hand movement. How does the animation help it guess? (Model: it saves not only what was drawn but how — the order of strokes and the movement of the hand — it recognises patterns from earlier drawings and can guess the object before the picture is complete.)

## 81–86 — Fill in the sentences

1) A bigger dataset → easier to **learn / recognise** objects from the real world. 2) More diverse examples (countries and cultures) → more **accurate** and fairer for everyone. 3) "Bad fuel" (examples that fit only one culture) → wrong or **biased** results. 4) The game keeps the **order and movement of the strokes**, so it guesses before we finish.

Fast finishers: [`Audit_Starter.py`](Audit_Starter.py) — fix the warm-up bug (`>` should be `<`), then write `car_data_audit()`.

## 86–88 — Summary and responsibility (teacher)

The revolution is here: AI is already around us. AI is a computer's ability to learn from data, recognise patterns and improve — not only follow fixed rules. This year: from consumers to creators. **With great technology comes great responsibility: data is the fuel of AI; the more diverse the examples, the more accurate and fair the AI is for everyone.**

## 88–90 — Exit check

In the brief (three questions).

### Tool Note – Quick, Draw!
`quickdraw.withgoogle.com` (the game) and its data page (`/data`). If a site is blocked, the teacher shows it on the board and students work from the teacher's screenshots; the worksheet's answers then come from what the class sees together.

### Tool Note – Thonny
Only for the if-time audit: one call at the bottom of the file is active at a time.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The computer saw my drawing like a person | It compared strokes with patterns from many drawings |
| Recognising early means it read my mind | It learned how most people start that drawing |
| More drawings always means a better system | More **and more varied** drawings; a data set can be big and still miss kettles or the Israeli stop sign |
| A failure means my drawing was bad | The data may not represent my kind of drawing |
| Bias only means someone meant harm | Data from one culture is enough to make the system fail on others |
| The AI is responsible for its mistakes | The people who build it and choose its data are |

---

# 8. Assessment Evidence (formative)

- Quick, Draw! times on the board and the answer to "when did it recognise?"
- The completed worksheet 3.2 (questions 1–4 and the four fill-in sentences)
- One example of biased data causing a wrong, unfair or dangerous decision (official assessment 2)
- Exit check
