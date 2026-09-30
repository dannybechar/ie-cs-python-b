# Unit 9.1 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: What Is a Recommender System? + Data Collection

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; Google Forms for the real survey (see Tool Note)
**Source of inspiration:** `python_b_unit09_recommendation_systems_complete_unit.md`, meeting 1 — its own clock
table, the "who recommended this to me" hook, the concepts table, the content-based/user-based comparison and its
classification drill, the manual digital-twin card simulation, the survey design guidance, the pre-publish quality
checklist and the CSV export note kept nearly unchanged, including its full data-collection privacy rules.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Google Forms**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **9.1 (this)** | **content-based vs. user-based recommendation; survey design** | 45 / 45 |
| 9.2 | reading CSV data; computing similarity between users | 45 / 45 |
| 9.3 | finding a digital twin; producing a recommendation (checkpoint) | 45 / 45 |
| 9.4 | filter bubbles, echo chambers, the attention economy | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 21–22) | Covered here |
|---|---|
| Goal 1: why digital services use recommender systems | ✅ hook |
| Goal 2: content-based vs. user-based recommendation | ✅ every task |
| Goal 3: represent preferences with parallel rating lists | ✅ the card simulation |
| Goal 4: a shared rating; why an unknown item is excluded | ✅ the rating scale |
| Goal 14: privacy limits on data collection | ✅ the survey design section |

### Deliberate exclusions
Reading CSV in code, the similarity function itself (9.2), the recommendation algorithm (9.3).

---

## 3. Lesson Goal

**A user-based recommender finds users with similar preferences and suggests what they liked that the current user
hasn't tried — built from a rating scale everyone agrees on, so code can compare values without guessing.**

---

## 4. Core Mental Models

```text
המלצה מבוססת תוכן:   אהבתי פריט ← מאפייני הפריט ← פריטים בעלי מאפיינים דומים
המלצה מבוססת משתמשים: הדירוגים שלי ← משתמש דומה ← פריט שהוא אהב ואני לא מכיר/ה
```

Rating scale used throughout the unit: `0` = don't know this item (no preference at all), `1` = disliked,
`2` = neutral, `3` = liked. **`0` is never a preference** — it's excluded from every similarity calculation (9.2).

- "Digital twin" is a teaching term for "the user whose rating pattern is most similar, on the data collected" — not
  a claim that two people are alike, or that one person's taste is right for the other.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Hook:** "who recommended this to me?" — a music service, a shop, a friend, a news site: what's the input, what's the output in each case? Is a recommendation a fact or a prediction? |
| 10–24 | Key concepts: recommendation system, item, rating, content-based filtering, collaborative (user-based) filtering, digital twin, signal |
| 24–38 | **Classify (pairs):** four example sentences — is each one content-based or user-based reasoning? |
| 38–45 | The rating scale and why a shared, closed scale matters for code (`"אהבתי"`, `"3"`, `"כן"` all look the same to a person, but are different strings to code) |

The classification drill (24–38):

<div dir="rtl">

| תרחיש | הגישה המתאימה |
|---|---|
| "אהבת שיר קצבי; הנה שיר קצבי נוסף" | מבוססת תוכן |
| "אנשים שאהבו את אותם שלושה משחקים אהבו גם משחק רביעי" | מבוססת משתמשים |
| "הסרט דומה בז'אנר ובבמאי לסרט שאהבת" | מבוססת תוכן |
| "משתמש בעל דירוגים דומים לשלך נתן לפריט 3" | מבוססת משתמשים |

</div>

---

# 6. Second 45 Minutes — Lab

Starter: [`SurveyData_Starter.py`](SurveyData_Starter.py). Reference: [`SurveyData_Reference.py`](SurveyData_Reference.py).

## 45–53 — Warm-up: the meaning of `0`

```python
def describe_rating(value):
    if value == 0:
        return "not liked"
    elif value == 1:
        return "disliked"
    elif value == 2:
        return "neutral"
    elif value == 3:
        return "liked"


print(describe_rating(0))
```

Predict `"don't know"` (the agreed meaning of `0`), run, get `"not liked"` — the function conflates "unknown" with
"disliked," which will break the similarity logic in 9.2. Fix: return `"don't know"` for `0`.

## 53–65 — Manual digital-twin simulation (rating cards)

<div dir="rtl">

| משתמש | מוזיאון | חוף | פארק | עיר |
|---|---:|---:|---:|---:|
| נועה | 3 | 1 | 0 | 3 |
| עומר | 3 | 1 | 3 | 2 |
| ליה | 1 | 3 | 2 | 1 |

</div>

By hand: Noa and Omer share two identical ratings (museum, beach). Omer likes the park, which Noa hasn't rated.
Park becomes a recommendation candidate — **not** proof that Noa and Omer are "the same," only that their data
overlaps on what was collected.

## 65–71 — Task 1: `validate_ratings(row)`

Returns `True` when every value in the list is one of `0, 1, 2, 3`. Test on `[3, 1, 0, 3]` (valid) and
`[3, 1, 5, 3]` (invalid).

## 71–76 — Task 2: `count_known(ratings)`

How many values are **not** `0`. Test on `[3, 1, 0, 3, 2]` → `4`.

## 76–86 — Design a class survey (pairs)

Choose a neutral topic (trips, fruit, board games, general music genres — never health, politics, religion, family
status, or anything personal). 6–10 items, the same rating scale for every one, a random alias instead of a name,
and a stated purpose/deletion policy. Then a pre-publish check: same scale everywhere? `0` clearly means "don't
know"? item names unambiguous and consistent? no identifying information collected?

## 86–90 — Save and exit check

Save As `G8_U9_M1_SurveyData_<Name>.py`.

1. In one sentence, what's the difference between the two recommendation approaches?
2. Why doesn't `0` count as a shared rating?
3. Name one privacy rule that must apply to the survey.

### Tool Note – Google Forms
Create the form with one multiple-choice (or linear-scale) question per item, all sharing the same options
(`0`–`3`, each labeled). Link responses to Google Sheets, or use **Responses → Download responses (.csv)**. Before
the next meeting, check the column headers and remove a timestamp column if present, and hand out the source's
clean CSV shape as the fallback if Forms is unavailable.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `0` means the user disliked the item | It means the user has no opinion at all — it's excluded from comparisons |
| A "digital twin" is a genuinely similar person | It's a data-pattern match on the items collected — nothing more |
| Free-text answers work as well as a fixed scale | Code sees different strings as different values, even when a person would read them the same way |
| Any survey question is fine as long as it's about preferences | Personal, sensitive, or identifying questions are excluded regardless of topic |
| A recommendation is a proven fact | It's a prediction based on partial, collected data |

---

# 8. Assessment Evidence (formative)

- The four-scenario classification, with reasons
- The Noa/Omer/Lia manual simulation walked through correctly by hand
- The warm-up's `0`-vs-`1` conflation explained, not just fixed
- `validate_ratings()` and `count_known()` both passing their tests
- A survey design passing the pre-publish checklist, with no identifying questions
- Exit check
