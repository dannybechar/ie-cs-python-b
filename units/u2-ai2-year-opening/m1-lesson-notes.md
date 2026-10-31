# Unit 2.1 — AI2 Year Opening

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: AI or Not? A Greeting for Grandma Sarah — Classic Code vs AI

**Status:** Built, awaiting teacher approval 🔶  
**Duration:** 90 minutes  
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab  
**Minutes (theory / practice):** 45 / 45  
**Current tool:** Thonny, a chatbot in the browser (teacher demo)  
**Source of inspiration:** the Ministry deck **3.1 "שיעור פתיחה לשנה ב AI2"** (slides 1–34 and 48; the main source): the "AI or not?" image warm-up (slides 2–7), the six-product quiz "Is there AI inside?" with its answers (12–18), the shared-feature discussion and the definition of AI (19–20), the four revolutions and "why now: brain + power + fuel" (21–24), the question "landing on the moon vs writing a greeting" (25–26), and the greeting for Grandma Sarah — classic Python in three steps (print, then input and if, then the hobby), then an AI-written greeting and the comparison table (27–33). Slides 35–47 (Quick, Draw!, the programmers' role, consumers to creators, the road map) are in 2.2. **Changed from the previous version (Rules or Learning?):** the codex and raw material are replaced by the Ministry flow; the kettle rule, the rule-based message flag and the Quick, Draw! guess log are gone from 2.1 (Quick, Draw! and the kettle failure now live in 2.2 with the Ministry worksheet). The greeting program is the lab. **Changed from the Ministry:** the code prints English strings (a gendered Hebrew verb does not translate, so the `if` branch picks a sign-off line instead; English also keeps Thonny's console left-to-right); the AI greeting is shown in a chatbot, not through code (the API arrives in Unit 4).  
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny** or **Tool Note – Chatbot**.

---

## 1. Position in Unit 2

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **2.1 (this)** | **AI or not? → definition → the revolutions → classic greeting in Python vs AI greeting** | 45 / 45 |
| 2.2 | Quick, Draw! → worksheet "איך מחשב רואה בלי עיניים?" → data and bias → consumers to creators, the year's road map, responsibility | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal / concept / method (python-b-ai.pdf pp. 3, 8–9; Ministry deck 3.1) | Covered here |
|---|---|
| Master table: the AI revolution; classical programming vs AI | ✅ revolutions, why now, greeting in both ways |
| Goal 1: rule-based programming vs machine learning | ✅ comparison table, the lab |
| Concepts: machine learning vs rule-based, pattern recognition | ✅ quiz, definition |
| Method 1: open with a discussion (here: the "AI or not?" warm-up and quiz) | ✅ |

### Deliberate exclusions
Neural-network internals, training mathematics, the language-model API (Unit 4), Quick, Draw! (2.2). Python stays at Unit 1 level: `print`, `input`, `if`/`else`, `+` on strings, `int()`.

---

## 3. Lesson Goal

**Classic code does exactly what a person wrote, so the same input always gives the same output. An AI system learns from examples and builds a new answer each time — and its answer is something to check.**

---

## 4. Core Mental Models

<div dir="rtl">

| תכנות קלאסי | בינה מלאכותית |
|---|---|
| פועל לפי חוקים קבועים מראש, התוצאות צפויות | לומדת מדוגמאות ויוצרת תשובות חדשות בכל פעם |
| אותו קלט ← אותה ברכה | אותו קלט ← ברכה שונה בכל הרצה |
| המחשב מבצע את מה שנכתב לו | המחשב מנסח בעצמו לפי ההגדרות שקיבל |

</div>

- **Shared feature of every product that contains AI** (the Ministry's discussion): it learns from examples (data) and improves over time.
- **Definition (slide 20):** AI is the ability of a computer to do things that usually require human abilities — learning, thinking, decision-making — in conditions that were not defined in advance.
- **Why now:** brain (programs that imitate how the human brain works) + power (computers became much faster) + fuel (huge amounts of data on the internet).
- Safety: a chatbot's greeting is a **draft to check** — is it true about this grandmother, is it respectful, did it invent a fact?

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–1 | Title: יחידה 2.1 – פתיחת שנת AI2 · "בינה מלאכותית או לא?" |
| 1–6 | **Warm-up "AI or not?" (whole class, hands):** four pairs of similar images (Ministry deck, slides 3–6); the left image made by AI → raise the left hand, the right → the right hand; reveal each answer. Punchline (slide 7): half the pictures were photographed, half were made by a computer that never left the room — how did it learn what a dog looks like? "We will learn that this year." |
| 6–13 | **Quiz — is there AI inside? (pairs, thumbs up or down per product, then reveal):** calculator · text autocorrect · Netflix recommendations · voice assistant · automatic mall door · license-plate recognition in a parking lot |
| 13–15 | Reveal the answers with reasons (table in the brief): the calculator and the automatic door follow fixed rules; the other four learn from data |
| 15–19 | **Discussion (pairs, then class):** what do all the products with AI share? (they learn from examples — data — and get better over time). Then the definition of AI |
| 19–22 | The four revolutions (steam, electricity, computers, AI) — "how would your life look if you were born before each?"; **predict:** how long did it take Netflix to reach 1 million subscribers? ChatGPT? (3.5 years; 5 days) |
| 22–25 | Why now: brain + power + fuel |
| 25–27 | **The big question (pairs):** a computer landed a spacecraft on the moon in 1969 but could not write an original greeting for Grandma Sarah — what is the difference between the two tasks? (one has exact rules that can be written down; the other has none) |
| 27–30 | **Live code 1:** the greeting in two `print` lines. Predict: what happens each time you run it? (the same two lines) |
| 30–33 | **Live code 2:** `input` + `if`/`else` — who is wishing? Predict the output for "grandson" and for "granddaughter" |
| 33–37 | **Live code 3:** the hobby question joined with `+`. Predict: run it twice with the same answers — the same greeting? Yes — "the same as last year's birthday". The computer only does what we wrote |
| 37–41 | **The AI greeting (teacher demo in a chatbot, not code):** ask for a birthday greeting for Grandma Sarah, add a style (funny, rhymes or moving), her hobby and who is wishing. Run the same request twice — different greetings. Students find one thing in the text that must be checked |
| 41–45 | Comparison table (classic vs AI); the lab mission |

---

# 6. Second 45 Minutes — Lab

Starter: [`Greeting_Starter.py`](Greeting_Starter.py). Reference: [`Greeting_Reference.py`](Greeting_Reference.py).

## 45–50 — Warm-up bug: the card that says "friend"

```python
def birthday_card():
    friend = input("Friend's name: ")
    print("Happy birthday, friend!")
```

Typed `Dana` → `Happy birthday, friend!`. The word `friend` is inside the quotes, so it is text, not the variable. Fix: `print("Happy birthday, " + friend + "!")`. Say it: a variable name inside quotes is just letters.

## 50–58 — Task 1: `greeting_1()`

Two `print` lines: `Happy birthday, Grandma Sarah!` and `I wish you health and happiness!`. Run it three times. Change one word. Who decided what the program says? (the person who typed it)

## 58–69 — Task 2: `greeting_2()`

Ask `Who is wishing? (grandson/granddaughter): `, print the first line, then a last line that depends on the answer. Tests: `grandson` → `Your grandson wishes you health and happiness!` · `granddaughter` → `Your granddaughter wishes you health and happiness!`. (The Ministry version branches on a gendered Hebrew verb; in English the sign-off line carries the difference.)

## 69–80 — Task 3: `greeting_3()`

Add a question about the hobby and use the answer in one line with `+`. Test: `grandson`, `hiking` → the middle line `I wish you lots of joy with hiking!`. Run twice with the same answers: identical output — **classic code never surprises**.

## 80–85 — If time (choose one)

- `greeting_4()`: ask for her age (`int`) and add a line when she is 80 or older.
- Pairs: ask a chatbot for a greeting with the same facts (no real names — only "Grandma Sarah"), twice. Write one difference between the two answers and one sentence in them that you would want to check.

## 85–90 — Save and exit check

Save: `File › Save As` → `G8_U2_M1_Greeting_<Name>.py`. Exit check (in the brief): 1) a program that always gives the same greeting for the same answers — classic or AI? 2) one thing a chatbot's greeting needs checking for; 3) why is the calculator not AI while the autocorrect is?

### Tool Note – Thonny
Remove the `#` from one call at the bottom for each task and put it back on the previous one.

### Tool Note – Chatbot
Use the chatbot the school allows. Never type a real person's name or personal details; the model's text is a draft that a person checks.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Every smart-looking program is AI | A calculator and an automatic door follow fixed rules |
| Code with `input` and `if` that "adapts" is AI | It has only the branches a person wrote; the same input gives the same output |
| AI is magic that thinks like a person | It learned patterns from many examples and produces new text each time |
| The chatbot's greeting is correct because it sounds good | It may invent facts or fit badly — check it |
| AI appeared suddenly | Brain, power and fuel came together over decades |

---

# 8. Assessment Evidence (formative)

- Quiz answers with a reason for each of the six products
- `greeting_1`–`greeting_3` run with the listed tests; the warm-up fixed
- A sentence on what differs between the classic and the AI greeting
- Exit check
