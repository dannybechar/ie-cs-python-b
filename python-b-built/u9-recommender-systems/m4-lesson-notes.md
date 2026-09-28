# Unit 9.4 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Filter Bubbles, Echo Chambers, the Attention Economy

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; a private/incognito browser window for the live YouTube option (see Tool Note) — this
meeting has its own safety rules, read them before class
**Source of inspiration:** `python_b_unit09_recommendation_systems_complete_unit.md`, meeting 4 — its own clock
table, the "what's known and what isn't" framing, both experiment options (live YouTube and the offline card
simulation), the observation table, the filter-bubble/echo-chamber comparison, the attention-economy discussion
questions, the code-decisions-to-consequences table, the feed-control toolkit, the responsibility-card summary and
the exit card kept nearly unchanged, including its full experiment safety rules.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – the live experiment**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | content-based vs. user-based recommendation; survey design | 45 / 45 |
| 9.2 | reading CSV data; computing similarity between users | 45 / 45 |
| 9.3 | finding a digital twin; producing a recommendation (checkpoint) | 45 / 45 |
| **9.4 (this)** | **filter bubbles, echo chambers, the attention economy** | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 23) | Covered here |
|---|---|
| Goal 11: define filter bubble, echo chamber, attention economy | ✅ every task |
| Goal 12: analyze how behavioral signals shape recommendations | ✅ the experiment |
| Goal 13: propose practical feed-control tools | ✅ the toolkit |
| Goal 14: ethical limits — privacy, consent, data scarcity, bias | ✅ discussion, responsibility card |

### Deliberate exclusions
Any new code pattern for the recommender itself (finished in 9.3) — this meeting connects the built system to its
real-world consequences.

---

## 3. Experiment Safety (read before class)

- Only neutral, teacher-approved topics.
- Never search for harmful, extreme, violent, or dangerous content "to test the algorithm."
- No likes, comments, subscriptions, or signing into a personal account.
- Private/incognito mode reduces account-history linkage — it does **not** make browsing fully anonymous.
- Stop immediately and report to the teacher if inappropriate content appears.
- The goal is critical observation, not increasing watch time.

---

## 4. Lesson Goal

**A short controlled experiment reveals a local, real pattern — not the platform's complete algorithm; a filter
bubble narrows what's *shown*, an echo chamber narrows what's *believed and reinforced socially* — related, but not
the same thing.**

---

## 5. Core Mental Models

<div dir="rtl">

| מושג | מנגנון מרכזי | דוגמה |
|---|---|---|
| בועת סינון | התאמה אישית מסננת חלק מהמידע ומציגה בעיקר תוכן שנחזה כרלוונטי | פיד שמציג שוב ושוב אותו סוג תוכן |
| תיבת תהודה | קבוצה חוזרת ומחזקת דעות דומות, ולעיתים דוחה מידע סותר | קהילה שבה אותה טענה חוזרת ללא ביקורת |

</div>

- **Known**: recommendations may draw on watch/search history, subscriptions, likes/dislikes, and "not interested"
  feedback. **Not known**: the exact internal ranking rules, each signal's precise weight, whether a specific change
  caused a specific result, or whether two users would see identical outcomes.
- **Attention economy**: attention and time are limited resources; a free service earning from ads or engagement has
  an incentive to keep users engaged — which isn't automatically the same as optimizing for learning or well-being.
- Separate **observation** ("related recommendations increased") from **interpretation** ("the algorithm wants to
  trap me") — the second is a claim the short experiment can't actually prove.

---

# 6. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Hook:** compare two different feeds (screenshots or two students' own) — why might they differ? |
| 10–22 | **Preparation:** what recommendation signals are actually documented; safety rules (§3); write a one-sentence hypothesis before starting |
| 22–42 | **The "building a bubble" experiment** — pick Option A or B below |
| 42–45 | Begin the observation table (below), started during the experiment |

### Option A — Live, teacher-led (YouTube)
1. Open a new private/incognito window, signed out.
2. Choose a safe topic (recipes, space, a specific sport).
3. Record the initial recommendations / "up next."
4. Search and watch 3–5 short videos on that topic only.
5. After each watch, record the top five recommendations.
6. Count how many relate to the chosen topic.
7. Close the private window when done.

### Option B — Offline card simulation
The teacher prepares a deck of content cards across four topics. Each round: the student picks one card; "the
algorithm" returns two cards from the same topic plus one random card for the next round; repeat five rounds;
observe how the variety of options changes.

### Tool Note – the live experiment
Option A needs a browser and the safety rules in §3 followed exactly. If YouTube access isn't appropriate for the
school, use Option B — it teaches the identical pattern, is fully reproducible, and collects no data at all.

---

# 7. Second 45 Minutes — Lab

Starter: [`Bubble_Starter.py`](Bubble_Starter.py). Reference: [`Bubble_Reference.py`](Bubble_Reference.py).

## 45–55 — Finish the observation table

<div dir="rtl">

| סיבוב | פעולה שבוצעה | המלצות קשורות לנושא מתוך 5 | מה ראינו? | הסבר אפשרי |
|---:|---|---:|---|---|
| 0 | לפני צפייה | | | |
| 1 | צפייה ראשונה | | | |
| 2 | צפייה שנייה | | | |
| 3 | צפייה שלישית | | | |
| 4 | צפייה רביעית | | | |

</div>

Write **"related recommendations increased"** as an observation — not **"the algorithm wants to trap me"**, which
is interpretation the short experiment can't prove.

## 55–63 — Warm-up: counted the wrong direction

```python
def count_related(recommendations, topic):
    count = 0
    for rec in recommendations:
        if rec != topic:
            count += 1
    return count


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))
```

Predict `3` (three of the five relate to `"space"`), run, get `2` — the condition counts **unrelated** items
instead of related ones. Fix: `==`, not `!=`.

## 63–73 — Task 1: `simulate_feed_round(current_topic, other_topics, round_number)`

Models Option B's card rule: returns a list of 3 recommendations — **two** copies of `current_topic`, and **one**
"other" topic, picked deterministically as `other_topics[round_number % len(other_topics)]` (not random, so the
result is reproducible). Test with `current_topic="space"`, `other_topics=["cooking", "sports", "art"]`,
`round_number=0`, then `1`.

## 73–83 — Task 2: `run_bubble_experiment(start_topic, other_topics, rounds)`

Repeats `simulate_feed_round` for `rounds` rounds, printing and collecting `count_related(...)` each time. Test with
`start_topic="space"`, `other_topics=["cooking", "sports", "art"]`, `rounds=5`; confirm the related-count never
drops below 2 of 3 — a small, reproducible model of what the live experiment shows qualitatively.

## 83–90 — Concepts, the code→consequences table, the toolkit, and the exit check

Filter bubble vs. echo chamber (§5); the attention economy discussion questions (what is the system maximizing?
who benefits from more watch time? does a click prove satisfaction?); then this project's own decisions and their
downstream effects:

<div dir="rtl">

| החלטה בקוד שלנו | השפעה אפשרית |
|---|---|
| בחירה בתאום יחיד | המלצה רגישה מאוד לאדם אחד ולשוויון מקרי |
| דרישה לשני דירוגים משותפים בלבד | מאפשרת המלצה מהירה, אך על בסיס מידע חלש |
| המלצה רק על פריט שהציון שלו 3 | מסננת פריטים ניטרליים, אך אינה מבטיחה גיוון |
| בחירת המועמד הראשון בשוויון | סדר הקובץ משפיע על התוצאה |

</div>

**Feed-control toolkit** (pick at least two to try or discuss): "not interested" / "don't recommend this channel";
pausing or clearing watch/search history for a one-off search; actively seeking varied sources instead of relying
only on the feed; checking who made the content and why; comparing a claim against an independent source; setting a
time limit in advance; periodically asking "what am I not seeing here?"

**Responsibility card** (small groups): one benefit of recommender systems, one risk, one design decision from this
project's own code that affects outcomes, one action for a responsible developer, one action for a responsible
user.

Save As `G8_U9_M4_Bubble_<Name>.py`.

1. Define a filter bubble in one sentence.
2. What's the difference between it and an echo chamber?
3. Name two practical actions for better feed control.

---

# 8. Misconception Risks

| Misconception | Correction |
|---|---|
| Private/incognito mode makes browsing fully anonymous | It reduces local and account-history linkage — it doesn't eliminate all data collection |
| A filter bubble and an echo chamber are the same thing | One is algorithmic filtering; the other is social reinforcement — related, not identical |
| A short experiment reveals the platform's whole algorithm | It shows a local, real pattern — many signals and rules stay unobserved |
| Every recommendation is manipulation | Recommendations can be genuinely useful — evaluate purpose, transparency, and how much control the user has |
| A single unusual result proves a general conclusion | Report it as a local observation with its limits, not a universal claim |

---

# 9. Assessment Evidence (formative)

- The observation table, with observation and interpretation kept in separate columns
- The warm-up's inverted comparison explained, not just fixed
- `simulate_feed_round()` and `run_bubble_experiment()` both passing their tests, with the related-count pattern
  correctly explained
- Filter bubble and echo chamber defined distinctly, in the student's own words
- The code-decisions table connected to at least one concrete real-world consequence
- The feed-control toolkit and responsibility card, both completed
- Exit check
