# Unit 9.4 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: The Trap of Recommendations — Fact or Fake, the Cave, Three Traps, Controls

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; a private/incognito browser window for the live demo (see Tool Note) — this meeting has its own safety rules, read them before class
**Source of inspiration:** Ministry deck **22.1** ("מלכודת ההמלצות", 45 slides) and the teacher emphases in **20.0** p. 2 (the broken "shared
reality", the business model "who is the product", technological responsibility, the Micha Goodman video and the podcast episode 150 as
preparation). The teacher notes **22.0** and the worksheet **22.2** (the student "build a bubble" activity) were **not delivered**; the student
activity below is our own (a pair experiment, live or by cards, plus the code simulation of v1, redesigned). From v1 we keep: the experiment
safety rules, the offline card simulation as a fallback, observation vs interpretation, the feed-control toolkit, the responsibility card,
and the idea that our own code decisions (one twin, a tie-break rule) have consequences. See
[`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – the live demo**.
**Prerequisite:** `def`, `return`, flat lists, `append`, `not in` (Units 3, 5, 7).

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | feed riddle, content-based vs user-based, culinary twin, survey | 45 / 45 |
| 9.2 | the table, similarity points | 45 / 45 |
| 9.3 | the twin, the recommendation, the project | 45 / 45 |
| **9.4 (this)** | **fact or fake, the business model, the cave, three traps, controls; a toy bubble in code** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 23) | Covered here |
|---|---|
| Goal 11: define filter bubble, echo chamber, addiction engineering (the attention economy) | ✅ the three traps, the business model |
| Goal 12: how behavioural signals shape recommendations | ✅ the incognito demo, the toy simulation |
| Goal 13: practical tools for feed control | ✅ controls toolkit, pros and cons |
| Goal 14: ethical limits — privacy, consent, bias | ✅ safety rules, the responsibility card, the shared-reality discussion |

### Deliberate exclusions
New recommender code (finished in 9.3). The simulation is a toy, not a model of any real platform.

### What is official and what is ours
Official (22.1, 20.0): the fact-or-fake quiz, the business model, the incognito demo, the cave, the three traps, polarisation, the controls, pros and cons.
**Ours, enrichment (the Ministry's 22.2 is a browser activity, not code):** the Bubble code (`simulate_feed_round`, `run_bubble_experiment`,
`count_different`, with invented numbers), the offline card fallback, the observation/interpretation table, the responsibility card.
**⚠️ unverified against official 22.2 (and 22.0):** neither file was delivered, so the student activity in the lab is our reconstruction of "build a
bubble"; if 22.2 differs, follow it and keep the code simulation as an optional extension. Note for the record: 20.0 says "two meetings" but
describes three (survey, code, dangers); the unit follows the three described, split into our four.

---

## 3. Experiment Safety (read before class)

- The teacher runs the live demo on **one** machine, with a signed-out private window and a neutral topic.
- Students who run it themselves (only if the school allows): teacher-approved neutral topics, no sign-in, no likes, comments or subscriptions.
- Never search for harmful, extreme, violent or dangerous content "to test the algorithm".
- Private / incognito mode reduces linkage with an account and old history (this is why the Ministry requires it: old history would hide the change); it does **not** make browsing anonymous.
- Stop and tell the teacher if inappropriate content appears.
- The goal is critical observation, not watch time. Close the window at the end.
- If live browsing is not suitable, use the **offline card simulation** (Option B below): same idea, no account, no network.

---

## 4. Lesson Goal

**Feeds are built to keep our attention, not to inform us. Three traps follow: the filter bubble (what we are shown narrows), the echo
chamber (what we hear back is our own opinion) and addiction engineering (the next surprise keeps us scrolling). We can notice them and
act: tell the app, search on our own, follow other views.**

---

## 5. Core Mental Models

<div dir="rtl">

| מושג | משמעות | דימוי מהמערה |
|---|---|---|
| בועת סינון (Filter Bubble) | האלגוריתם מראה בעיקר מה שכבר מכירים ואוהבים | "הצללים הם כל העולם" |
| תיבת תהודה (Echo Chamber) | שומעים בחזרה רק את הדעה שלנו ומאבדים את היכולת להטיל ספק | הד בתוך מערה |
| הנדסת התמכרות | הפתעה בלתי צפויה בכל גלילה שומרת אותנו מול המסך | הצללים מרתקים את האסירים |

</div>

- **The business model:** a free app earns from ads. Time on screen and data about us = more targeted ads = more money. "If you do not pay
  for the product, you are the product."  The chain, as on 22.1 p. 35 (five steps): **(1) data collection** — the system tracks every click and watch time;
  **(2)** the AI learns what keeps us on the screen; **(3) maximising screen time** (pushing extreme or addictive content) — filter bubble and echo chamber;
  **(4) exposure to ads** (you see ads); **(5) profit** for the company. The slide's heading: "the business model: if you do not pay for the product, you are the product".
- **Plato's cave** (22.1 pp. 20–24): prisoners = us, chains = the algorithms, shadows = the feed, shadow-makers = the companies, the blinding
  light = truths that are hard to accept.
- **Observation vs interpretation:** "related videos increased" is an observation; "the app wants to trap me" is a claim the short demo cannot prove.
- **A shared reality** (20.0 p. 2): if everyone sees a different feed, people stop agreeing about the facts, and trust in debate weakens.

---

# 6. First 45 Minutes — Knowledge + Guided Practice (deck 22.1)

| Clock | Activity |
|---|---|
| 0–2 | **Title and recap** (pp. 2–3): recommenders help us, but do they have downsides? |
| 2–6 | **Fact or fake?** (pp. 5–13; question only): five posts, show fact or fake with the fingers |
| 6–9 | **Answers**, with the lesson that the algorithm does not check truth — it sees what keeps people watching |
| 9–14 | **The business model** (pp. 15–17, 35): "who is the product?" and the five-step chain |
| 14–20 | **Live demo: building a bubble in five steps** (p. 18): the exact script of 22.1 p. 18, **on the teacher's computer**: (1) open an incognito window in the browser (Ctrl + Shift + N) (2) go to YouTube — *which videos appear on the home page?* (3) search for videos about jazz music (4) watch two videos, half a minute each (5) click the home icon to return to YouTube's home page — *which videos appear now?* Offline fallback: cards (Option B) |
| 20–24 | **Observe and interpret:** what changed (observation) and why might it have (interpretation)? What can we *not* claim? |
| 24–26 | **Plato's cave** (pp. 20–23, question only): who are the prisoners? what are the shadows? |
| 26–29 | **The cave answered** (p. 24, table) |
| 29–33 | **The three traps** (pp. 26–33): filter bubble, echo chamber, addiction engineering — a table, with the "surprise machine" example |
| 33–36 | **Predict** (pp. 36–37, question only): a graph of how the two US political camps see each other: what happened to the slope in 2014? |
| 36–41 | **Answer and caution, then why it matters:** the slope grows steeper. Ministry claim: in 2014 the platforms moved to AI recommendation. *Correlation is not proof* — many things changed. A shared reality (pp. 38–39) |
| 41–45 | **What can we do?** (pp. 41–43): the four controls of p. 42, in the Ministry's words — use the "not interested" button (tell the app when it is wrong; it retrains it); search proactively (do not wait for what the feed throws at you); ask questions (why did this video jump out now? who gains?); "burst the bubble" (follow creators who think differently). Closing line: the feed pulls you one way, but your head is yours — check, ask, think for yourself. (Ours, added: look at the source before sharing.) Then pros (personalisation, convenience, more interest in content) and cons (a non-diverse feed — "filter bubble", privacy harm from data collection, influence on opinions and behaviour), p. 43 |

**Fact or fake — five posts (ours, based on 22.1 pp. 7–13; fictional people only):**

<div dir="rtl">

| # | הפוסט | תשובה |
|---|---|---|
| 1 | "קוד קופון סודי: עגלת בגדים שלמה בחינם! לחצו לפני שיתקנו את הבאג" | פייק — קליקבייט (פיתיון ללחיצה) |
| 2 | אתר חדשות מוכר מפרסם: "מחקר חדש: נמצאו סימנים למים על מאדים" | אמת — מקור אמין שבודק עובדות |
| 3 | סרטון בטיקטוק: "דחוף! משרד החינוך קיצר את החופש הגדול בחודש" | פייק — שמועה שמייצרת לחץ ותגובות |
| 4 | סרטון קצר: "מסמך סודי: הממשלה תשתיל שבבי מעקב בכל האזרחים עד 2035" | פייק — משחק על פחד מפרטיות |
| 5 | כתבה מתחת לשורת החיפוש: "ארגון הבריאות העולמי מפיץ חיסון נגד מלריה לילדים" | אמת — המערכת זיהתה עניין בבריאות |

</div>

**Official wording to keep on the slides (22.1):** agenda (p. 4): behind the scenes of the algorithm, ancient illusions (philosophy), build a bubble, digital control, fake or fact. *Clickbait* (p. 5): an exaggerated headline on purpose so that we click (Click = pressing, Bait = lure). *Fake News* (p. 5): wrong or invented information. Why would the feed show exaggerated or false things? (p. 14) — "no free gifts" (p. 15): apps earn billions, their aim is to keep us on the screen as long as possible; more screen time and data about us = more ads matched to us = more money. Extreme content sticks (p. 17). The surprise machine and dopamine (p. 32; a popular explanation, see the strategy). The flat-earth story (p. 34): many young people online believe the world is a flat disc and that NASA hides it — one example of extreme suspicion that causes a deep crisis of trust in science, medicine and state institutions. Closing (p. 44): be critical users, get out of the filter bubble, take command of your screen.

The Ministry deck's Elon Musk item (a made-up quote of a real person) is not used. The 2020 US election slide (p. 39) names a political camp's
beliefs; we teach the principle instead: *a debate needs agreement on what happened.* Ask the teacher before using named examples.

**The polarisation graph** (22.1 pp. 36–37; the slide text gives **no numbers** and does not name a source — it says only that the graph is from
the USA and shows people of both political camps coming to view the other side very negatively). The figures below are **approximate, estimated
by us from the slide's chart image** (the chart looks like the Pew Research Center series on "very unfavorable" views of the other party, but
that attribution is **unverified**): check them against the real source before quoting them to students, or show the chart without numbers
and ask only about the slope.

<div dir="rtl">

| שנה | מחנה א׳ לגבי ב׳ | מחנה ב׳ לגבי א׳ |
|---|---:|---:|
| 1994 | 17% | 16% |
| 2014 | 43% | 38% |
| 2022 | 62% | 54% |

</div>

Approximate growth per year, from these estimates: about 1.1–1.3 percentage points before 2014 and 2.0–2.4 after (the two camps). The slope is steeper; **whether the recommenders caused it is not
shown by the graph.**

### Option B — offline card simulation (fallback)
The teacher prepares cards of four topics. In round 0 the student draws five cards: one of the chosen topic and four others. After
every round the student "watches" a card of the chosen topic, and the next hand has one more card of that topic (never more than 4 of 5).
Five rounds; fill the observation table. This is the same rule as the code in the lab.

### Tool Note – the live demo
The demo needs a browser and the safety rules in section 3. If YouTube is not suitable for the school, use Option B: it shows the same pattern and collects no data.
Ministry 22.2 (not delivered) presumably holds the student version of the five steps — follow it if you have it.

---

# 7. Second 45 Minutes — Lab

Starter: [`Bubble_Starter.py`](Bubble_Starter.py). Reference: [`Bubble_Reference.py`](Bubble_Reference.py).
Brief: [`m4-lab-brief-he.md`](m4-lab-brief-he.md).

| Clock | Block |
|---|---|
| 45–55 | Pairs: build a bubble (live, if allowed, or cards) and fill the observation table |
| 55–62 | Warm-up bug: `count_related` |
| 62–72 | Task 1: `simulate_feed_round` |
| 72–80 | Task 2: `run_bubble_experiment` (+ Task 3 if time) |
| 80–86 | Controls and the responsibility card |
| 86–90 | Save and exit check |

## 45–55 — The experiment and the observation table

<div dir="rtl">

| סיבוב | מה עשינו | כמה מתוך 5 קשורים לנושא | מה ראינו (תצפית) | הסבר אפשרי (פרשנות) |
|---:|---|---:|---|---|
| 0 | לפני צפייה | | | |
| 1 | צפייה ראשונה | | | |
| 2 | צפייה שנייה | | | |
| 3 | צפייה שלישית | | | |

</div>

## 55–62 — Warm-up: counted the wrong direction

```python
def count_related(feed, topic):
    count = 0
    for card in feed:
        if card != topic:
            count += 1
    return count


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))
```

Predict `3`, run: **`2`** — `!=` counts the cards that are *not* the topic. Fix: `==`.

## 62–72 — Task 1: `simulate_feed_round(topic, other_topics, round_number)`

A toy feed of 5 cards: `related = round_number + 1` cards of `topic` (at most 4), the remaining slots filled from `other_topics` one after the other,
wrapping around. With `["cooking", "sports", "art"]`:

```text
round 0 -> ['space', 'cooking', 'sports', 'art', 'cooking']
round 2 -> ['space', 'space', 'space', 'cooking', 'sports']
round 6 -> ['space', 'space', 'space', 'space', 'cooking']
```

**The numbers are our own choice** — this is not the rule of any platform; it shows the *direction* of the effect.

## 72–80 — Task 2: `run_bubble_experiment(topic, other_topics, rounds)`

For every round build the feed, print `Round N - related: K of 5` and collect `K`; return the list. Five rounds:

```text
Round 0 - related: 1 of 5
Round 1 - related: 2 of 5
Round 2 - related: 3 of 5
Round 3 - related: 4 of 5
Round 4 - related: 4 of 5
[1, 2, 3, 4, 4]
```

**Task 3 (if time): `count_different(feed)`** — how many different topics are in the feed (keep a list of seen topics; `not in`). Over the five
rounds the variety drops `4, 4, 3, 2, 2` while the related count rises: a narrowing feed.

## 80–86 — Controls and the responsibility card

Pairs choose **two** controls to try or discuss: "not interested" / "don't recommend this channel"; search for new topics on your own; ask "why am I
seeing this, who gains?"; follow creators who think differently; look at the source before sharing. Then one **responsibility card**: one
advantage, one risk, one decision in *our* project that affects the result (one twin only; the first twin on a tie; a recommendation from
one friend), one action for a responsible developer, one for a responsible user.

## 86–90 — Save and exit check

Save As `G8_U9_M4_Bubble_<Name>.py`.

1. Define a filter bubble in one sentence.
2. What is the difference between a filter bubble and an echo chamber?
3. Name two practical ways to control your feed.

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| Incognito mode makes me anonymous | It separates my account and old history; the site and network still see activity |
| The feed shows the truth | It shows what keeps us watching; check the source |
| A filter bubble and an echo chamber are the same | Algorithm narrows what we *see* vs people repeat what we *think* — related, not identical |
| A short demo shows the platform's algorithm | A local observation; many signals stay unseen |
| The 2014 graph proves the algorithm caused polarisation | It shows a change of slope; causes need more evidence |
| Every recommendation is manipulation | Often useful — judge the purpose, the transparency and how much control the user has |

---

# 9. Assessment Evidence (formative)

- The fact-or-fake choices with a reason
- The observation table with observation and interpretation in separate columns
- The warm-up explained (`!=` counts the wrong cards), not only fixed
- `simulate_feed_round` and `run_bubble_experiment` correct, with the narrowing explained in words and flagged as a toy
- The cave mapped to a recommender; the three traps defined distinctly
- Two controls and a completed responsibility card
- Exit check
