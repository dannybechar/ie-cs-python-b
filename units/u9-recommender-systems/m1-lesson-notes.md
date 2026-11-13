# Lessons 20.0–20.1 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: The Feed Riddle, Two Kinds of Recommender, the Culinary Twin, the Survey

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Google Forms for the real survey (see Tool Note)
**Source of inspiration:** Ministry teaching materials **20.0** (teacher emphases, p. 1–2) and **20.1** (deck "הכרות עם מערכות המלצה",
42 slides): the viewing-habits discussion, the YouTube-feed riddle, regular algorithm vs AI, content-based vs user-based (signals; the
ice-cream seller), the "culinary twin" class game, the two-step project and the Google Forms survey. The worksheet **20.2** (the Google
Classroom survey activity) was **not delivered**: the survey steps below are our own, built from 20.1 pp. 37–39 and the 20.0 rule about
V / X / 0. The v1 build is kept where the Ministry is silent: the four-scenario classification drill, the survey privacy rules and the
pre-publish checklist. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Google Forms**.
**Prerequisite:** functions (lessons 4.1–4.6) and lists (lessons 9.1–9.5, 12.0–14.5) are done before the recommender-systems block (lessons 20.0–22.1); the code uses `def`, strings and flat lists only.

---

## 1. Position in the recommender-systems block (lessons 20.0–22.1)

The Ministry fits the unit in **three** meetings (20, 21, 22); we keep **four** because the master table gives 8 hours. Lessons 20.0–20.1 = deck 20.1,
Lesson 21.1 = first half of 21.1, lessons 21.1–21.2 = second half of 21.1 plus the code, lessons 22.0–22.1 = 22.1.

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **Lessons 20.0–20.1 (this)** | **the feed riddle, content-based vs user-based, the culinary twin, the survey (V / X / 0)** | 45 / 45 |
| Lesson 21.1 | the participants × items table, counting similarity points, the twin | 45 / 45 |
| Lessons 21.1–21.2 | recommend what the twin liked, the project (checkpoint) | 45 / 45 |
| Lessons 22.0–22.1 | the dangers: fake and fact, the business model, the cave, three traps, controls | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 21–22) | Covered here |
|---|---|
| Goal 1: why digital services use recommender systems | ✅ feed, where we meet them, the riddle |
| Goal 2: content-based vs user-based recommendation | ✅ signals, the ice-cream seller, the classification drill |
| Goal 3–4: preferences as data; a shared answer, why "don't know" is excluded | ✅ the culinary-twin game, the V / X / 0 scale |
| Goal 14: privacy limits on data collection | ✅ the survey rules |

### Deliberate exclusions
Note: 20.0 says the unit has "two meetings" but lists three (survey, code, dangers); the Ministry's three lessons (20, 21, 22) become our four meetings (see the unit strategy). Left to later meetings: the table and the similarity count (lesson 21.1), the recommendation code (lessons 21.1–21.2), the traps and ethics (lessons 22.0–22.1).

---

## 3. Lesson Goal

**A recommender does not read minds: it learns from our behaviour (content-based) or from people who behave like us (user-based). To let a
program compare people, everybody answers on one closed scale — `V` liked, `X` disliked, `0` don't know.**

---

## 4. Core Mental Models

```text
content-based: what I liked before -> features / signals of the item -> similar items
user-based:    my answers -> people with similar answers (the "twin") -> what they liked and I don't know
```

- **Signals** a content-based system collects (20.1 p. 23, the five of the slide): **likes** (a like = I like it), **comments** (it made me want to say what I think),
  **star ratings** (how interested I was), **long watch time** (otherwise I would have left after seconds), **sharing** (it was worth discussing with friends).
  The slide's question: *what data do recommenders collect?* — the answer: "in this way the system checks how much we liked the content". (Ours, added: what we search.)
- **The scale** (20.0 p. 1): `V` = liked, `X` = disliked, `0` = don't know. **Capital English letters only**, so the code can read them:
  `"v"` and `"V"` are different strings. A `0` is *not* an opinion: "don't know" gives the system nothing to compare.
- **Regular algorithm vs AI** (20.1 pp. 17–18): a regular algorithm follows fixed rules and gives everybody the same
  recommendation ("most orders: classic burger"); an AI model learns from data and predicts for **this** person.
- "Digital twin" is a teaching term: the participant whose answers are most like mine **on the data we collected**. It does not say the two
  people are alike, or that the twin's taste is right for me.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 20.1)

| Clock | Activity |
|---|---|
| 0–3 | **Title + plan.** Riddle, two kinds of recommender, a class game, then our own survey |
| 3–6 | **Viewing habits** (20.1 p. 3, discussion): *what is the last series or film you watched? how did you get to know it?* Write the answers on the board in **two columns**: heard from friends / saw something similar before. Then reveal: from friends = like a **user-based** system; similar content = like a **content-based** system. Then: *would YouTube's home page look the same on every phone? why not?* |
| 6–10 | **What is a feed** (pp. 5–13): *why is YouTube's home page different from person to person?* YouTube does not read minds, it learns from behaviour: what we watched, clicked, liked, where we stayed longer. **Definition (p. 6):** a recommender is a smart (AI) tool that predicts our preferences and gives personalised content without our searching. The stream is the *feed* ("to feed"); it is different for everyone. Where we meet it: video, music, shopping, social networks (show your own screens, never a student's) |
| 10–14 | **The riddle** (pp. 14–15, question only): three people, three YouTube home pages, who owns which? Pairs, one minute, finger vote |
| 14–17 | **The riddle answered:** what clues did you use? (words in the titles = interests) — the system uses the same clues |
| 17–21 | **Regular algorithm vs AI** (pp. 17–18): same rule for everybody vs a prediction for me; call back the grandma greeting from the AI2 year-opening block (lessons 3.0–3.2) |
| 21–25 | **Method 1 — content-based** (pp. 21–23): similar items to what I liked; the signals it collects |
| 25–29 | **Method 2 — user-based** (pp. 25–26): the ice-cream seller who has seen others with the same taste: "strawberry and banana? add chocolate sauce" |
| 29–32 | **Classify** (question only, pairs): four sentences — content-based or user-based? |
| 32–34 | **Answers** |
| 34–43 | **Class game: the culinary twin** (rules and a five-food example 3 min, the 12 foods 6 min) (pp. 28–31): a volunteer answers V / X / 0 on 12 foods; every student scores against the volunteer: **a point only when the answers are identical and not 0**. Most points = the culinary twin |
| 43–45 | **Recommend** (p. 32): is there a food the twin liked and the volunteer does not know? That is the recommendation. "This is how a recommender works." **In reality** (p. 33): companies like Netflix keep huge tables and compare us with millions of users to find a whole group with a similar taste, not one twin. Bridge: *next we build one in Python* — **the project in two stages** (pp. 35–36): (1) choose a topic and run a survey among family and friends; (2) program a system that takes a user's data, finds the most similar survey participant and recommends accordingly. Summary (p. 40): apps do not read minds — every like, comment and watch time is a clue; method 1 = content already liked, method 2 = users with a similar taste |

**Classification drill (question only, then answers):**

<div dir="rtl">

| תרחיש | הגישה |
|---|---|
| "אהבת שיר קצבי; הנה שיר קצבי נוסף" | מבוססת תוכן |
| "אנשים שאהבו את אותם שלושה משחקים אהבו גם משחק רביעי" | מבוססת משתמשים |
| "הסרט דומה בז'אנר ובבמאי לסרט שאהבת" | מבוססת תוכן |
| "משתמש בעל דירוגים דומים לשלך נתן לפריט 'אהבתי'" | מבוססת משתמשים |

</div>

**The riddle (our own text; the Ministry's deck uses three AI-generated people, which we do not copy).** Three fictional people and three
home pages; the class matches them.

<div dir="rtl">

| אדם | דף הבית של… |
|---|---|
| 1 — אוהב כדורגל וגיימינג | "גולים מהעונה", "טריקים במשחק כדורגל", "תקצירי הליגה" |
| 2 — מתכוננת לבגרות ואוהבת לבשל | "מתמטיקה לבגרות בקלות", "פסטה ב-10 דקות", "שיטות למידה" |
| 3 — מאלפת גורי כלבים | "אילוף גור בבית", "כלבים מצחיקים", "שירי פופ חדשים" |

</div>

Show the three lists scrambled (A, B, C); answer: A = 3, B = 1, C = 2 (the scrambled order is fixed in the slide source).

**The game, step by step.** Choose a volunteer (never push; use a food list and no personal topics). For each food the volunteer says
`V`, `X` or `0`; every student writes their own answer next to it and keeps a score (in the Ministry's game the answers are the words *like / dislike / didn't taste*; we use the letters `V` / `X` / `0` from the start so the game and the survey match). Point rules, which the Ministry states on slide 29
and which we repeat on the board: **(1)** both liked → point; both disliked → point; **(2)** different answers → no point; **(3)** a `0`
(by either of you) → no point, because "don't know" is not enough information. Count out loud who has the most; ties: both are twins, pick
one to recommend from. The twin offers a food they liked (`V`) that the volunteer answered `0`.

### Tool Note – the culinary-twin game
The Ministry shows the 12 foods on slide 30 (peach, beet, egg salad, fries, broccoli, cilantro, pasta, sushi, kohlrabi, steak, sweet potato
with tahini, pistachio ice cream). Our slide uses the same list; the teacher may change foods to the class's context. No names are written
on the board: students may raise a hand for "my score is N".

**The scoring table of p. 29 (five foods, a volunteer example; total 2 points):**

<div dir="rtl">

| אני | מתנדב | מאכל | נקודה? |
|---|---|---|---|
| אוהב | אוהב | פיצה | כן |
| לא אוהב | לא אוהב | ברוקולי | כן |
| לא אוהב | אוהב | סושי | לא |
| לא מכיר | אוהב | טאקו | לא |
| לא מכיר | לא מכיר | קיווי | לא |

</div>

Rule on the slide: a point only for a shared opinion (both like or both dislike); "don't know" = not enough information = no point. Students may count on fingers or step forward for each point.

---

# 6. Second 45 Minutes — Lab

Starter: [`SurveyData_Starter.py`](SurveyData_Starter.py). Reference: [`SurveyData_Reference.py`](SurveyData_Reference.py).
Brief: [`m1-lab-brief-he.md`](m1-lab-brief-he.md).

| Clock | Block |
|---|---|
| 45–50 | Warm-up bug: the last `else` of `describe_answer` |
| 50–58 | Task 1: `is_valid_answers(answers)` |
| 58–64 | Task 2: `count_known(answers)` |
| 64–80 | Build the survey in Google Forms (topic, 6–10 items, V / X / 0, privacy) |
| 80–86 | Pre-publish checklist, one pair checks another pair's form |
| 86–90 | Save and exit check |

## 45–50 — Warm-up: everything unknown becomes "don't know"

```python
def describe_answer(answer):
    if answer == "V":
        return "liked"
    elif answer == "X":
        return "disliked"
    else:
        return "don't know"


print(describe_answer("0"))
print(describe_answer("v"))
```

Predict `don't know` and `invalid answer`; run: **both** print `don't know`. The final `else` swallows every wrong answer — a small `v` typed
into the form is read as "don't know" and the person's opinion is lost silently. Fix: `elif answer == "0":` returns `don't know`,
and the `else` returns `invalid answer`. This is exactly why the Ministry insists on capital letters and why Task 1 checks the data.

## 50–58 — Task 1: `is_valid_answers(answers)`

`answers` is a string with one character per item (`"VX0XV"`). Return `True` only if **every** character is `V`, `X` or `0`.
Tests: `"VX0XV"` → `True`; `"VX0xV"` → `False` (small x); `"VX5XV"` → `False`.

## 58–64 — Task 2: `count_known(answers)`

How many characters are not `0`. `"VX0XV"` → `4`.

## 64–80 — Build the survey (pairs; Ministry 20.0, 20.1 pp. 36–39)

1. **Topic** — neutral and fun: music, series, games, trips, food, sports. Never health, politics, religion, family situation or anything personal.
2. **6–10 items** — names of things (songs, places, foods), unambiguous and spelled the same way everywhere.
3. **Every item has the same three options: `V` (liked), `X` (disliked), `0` (don't know).** Capital English letters, exactly these characters;
   write the legend once at the top of the form.
4. **Privacy (kept from v1):** an alias or a number instead of a name; no e-mail, phone, class or photo; say what the survey is for and that
   the answers are deleted when the unit ends; share only with friends and family who agree; the teacher looks at the form before it is sent.
5. In Forms the settings must not collect e-mail addresses and must not require sign-in.

## 80–86 — Pre-publish checklist

Same options everywhere? `0` clearly "don't know"? Item names clear and consistent? An alias question, and nothing that identifies a person?
Test the form yourself once and look at the response in the sheet: do you see exactly `V`, `X` or `0`?

## 86–90 — Save and exit check

Save As `G8_U9_M1_SurveyData_<Name>.py`.

1. In one sentence: what is the difference between content-based and user-based recommendation?
2. Why is a `0` not counted as a shared answer?
3. Name one privacy rule for the survey.

### Tool Note – Google Forms
One multiple-choice question per item with exactly three choices `V`, `X`, `0` (or a multiple-choice grid: rows = items, columns = the three
letters). Link responses to a sheet, then **File → Download → CSV**. The CSV header is `alias,item1,item2,…` — the sample
[`ratings.csv`](ratings.csv) has this shape. Before lesson 21.1 the teacher checks that every cell is `V`, `X` or `0` (the helper
[`CsvToLists_Teacher.py`](CsvToLists_Teacher.py) warns about bad cells). If Forms is unavailable, use the sample file.
**Wording difference to settle:** 20.1 p. 38 describes the survey options in words (*like / dislike / don't know*), while 20.0 requires the marks `V` / `X` / `0` in capital English letters. We assume the Forms options are literally `V`, `X`, `0` (with the legend); an alternative is words in the form that the teacher maps to the letters before lesson 21.1. The Ministry asks students to spread the survey among **family and friends** (20.1 p. 42): we keep that, with the privacy rules above.
The Ministry's worksheet 20.2 (not delivered) may give the exact form layout; follow it if it differs.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The app reads my mind | It learns from behaviour: what I watched, clicked, liked, how long I stayed |
| A regular algorithm and an AI recommend the same way | A fixed rule gives everyone the same; an AI predicts for the individual |
| `0` means "didn't like" | It means "don't know" — no information, never a shared opinion |
| `v` and `V` are the same | Different strings; the code only understands the agreed capital letters |
| The "digital twin" is a person like me | A data match on the items we collected — nothing more |
| A recommendation is a fact | It is a prediction from partial data |

---

# 8. Assessment Evidence (formative)

- The riddle explained from clues (which words showed which person)
- The four-scenario classification with reasons
- The culinary-twin game: each student's score explained point by point (why no point for `0`)
- The warm-up bug explained (`else` swallows `v`), not just fixed
- `is_valid_answers()` and `count_known()` passing their tests
- A survey design passing the checklist, with no identifying questions
- Exit check
