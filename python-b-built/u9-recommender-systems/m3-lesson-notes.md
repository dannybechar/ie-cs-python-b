# Unit 9.3 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: From Digital Twin to Recommendation (Unit Checkpoint)

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit09_recommendation_systems_complete_unit.md`, meeting 3 — its own clock
table, `find_digital_twin` (with the `(rate, common)` tie-break key), `recommend_item`, the full `main()` program,
the no-CSV test data, the seven-case test table, the three named limitations, and the exit card kept nearly
unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | content-based vs. user-based recommendation; survey design | 45 / 45 |
| 9.2 | reading CSV data; computing similarity between users | 45 / 45 |
| **9.3 (this)** | **finding a digital twin; producing a recommendation (checkpoint)** | 45 / 45 |
| 9.4 | filter bubbles, echo chambers, the attention economy | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 22–23) | Covered here |
|---|---|
| Goal 7: find the most similar user | ✅ `find_digital_twin` |
| Goal 8: recommend an unknown-but-twin-liked item | ✅ `recommend_item` |
| Goal 9: combine several functions in a main program | ✅ `main()` |
| Goal 10: test on normal cases and edge cases | ✅ the checkpoint |

### Deliberate exclusions
Any new similarity concept (built in 9.2, reused unchanged here).

---

## 3. Lesson Goal

**Compare the target to every other user (never itself), keep the best `(rate, common)` pair as the digital twin,
then recommend the twin's highest-rated item the target doesn't yet know — and handle "no twin" or "no
recommendation" explicitly, without crashing.**

---

## 4. Core Mental Models

```python
def find_digital_twin(target_index, all_ratings, minimum_common=2):
    best_index = None
    best_key = (-1.0, -1)
    for candidate_index in range(len(all_ratings)):
        if candidate_index == target_index:
            continue                                  # never compare a user to itself
        matches, common = similarity_score(all_ratings[target_index], all_ratings[candidate_index])
        if common < minimum_common:
            continue                                  # too little evidence
        rate = matches / common
        candidate_key = (rate, common)                # rate first, common breaks ties
        if candidate_key > best_key:
            best_key = candidate_key
            best_index = candidate_index
    return best_index, best_key
```

```python
def recommend_item(target_ratings, twin_ratings, item_names, liked_threshold=3):
    # among items the target rated 0 AND the twin rated >= liked_threshold,
    # pick the one with the twin's highest rating - or return None
```

- `aliases[best_index]` and `all_ratings[best_index]` both refer to the twin — that's why the function returns an
  **index**, not a name or a list directly.
- A tuple `(rate, common)` compares rate first, then common — exactly the tie-break rule the project needs, with no
  extra `if`.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–10 | **Recap:** run 9.2's `similarity_score` asserts again — all green before continuing |
| 10–25 | Planning `find_digital_twin`: compare the target to everyone else, skip itself, skip low-evidence candidates, keep the best `(rate, common)` |
| 25–43 | Writing `find_digital_twin`, tracing it on the four-user, five-item test data below |
| 43–45 | Transition to the lab |

```python
items = ["museum", "beach", "park", "city", "forest"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
ratings = [
    [3, 1, 0, 3, 0],
    [3, 1, 3, 2, 3],
    [1, 3, 2, 1, 0],
    [3, 2, 2, 3, 0],
]
```

---

# 6. Second 45 Minutes — Lab

Starter: [`TwinRecommend_Starter.py`](TwinRecommend_Starter.py). Reference: [`TwinRecommend_Reference.py`](TwinRecommend_Reference.py).

## 45–53 — Warm-up: your own twin

```python
def find_digital_twin(target_index, all_ratings, minimum_common=2):
    best_index = None
    best_key = (-1.0, -1)
    for candidate_index in range(len(all_ratings)):
        matches, common = similarity_score(all_ratings[target_index], all_ratings[candidate_index])
        if common < minimum_common:
            continue
        rate = matches / common
        candidate_key = (rate, common)
        if candidate_key > best_key:
            best_key = candidate_key
            best_index = candidate_index
    return best_index, best_key
```

Run `find_digital_twin(0, ratings)` on the test data above. Predict a real other user; get `(0, (1.0, 3))` — user 0
matched with **itself**, a perfect (but meaningless) score. Fix: `if candidate_index == target_index: continue`.

## 53–65 — Task 1: `recommend_item(target_ratings, twin_ratings, item_names, liked_threshold=3)`

Finds the item the target rated `0` where the twin's rating is `>= liked_threshold`, choosing the highest such
rating; returns `None` if there is no such item.

## 65–80 — Task 2 (project — the checkpoint): `main()`

Load `items`/`aliases`/`all_ratings` from `ratings.csv` (9.2), find `target_index = 0`'s twin
(`minimum_common=2`); if none was found, print a clear message and stop; otherwise recommend an item and print the
target's alias, the twin's alias, the similarity rate, the shared-rating count, and the recommendation (or a clear
"no suitable recommendation" message).

## 80–86 — Testing, using all seven of the source's own cases

<div dir="rtl">

| מקרה | התנהגות מצופה |
|---|---|
| אין דירוגים משותפים | לא נמצא תאום דיגיטלי |
| יש רק דירוג משותף אחד | המועמד נדחה כאשר `minimum_common=2` |
| התאום אינו אוהב אף פריט חדש | אין המלצה מתאימה |
| המשתמש כבר מכיר את כל הפריטים | אין המלצה מתאימה |
| שני תאומים בעלי אותו שיעור | מספר הדירוגים המשותפים שובר שוויון |
| שוויון מלא | המועמד הראשון נשמר; יש לתעד זאת |
| אורכי רשימות שונים | הפונקציה דוחה את הנתונים (`ValueError`) |

</div>

## 86–90 — Discuss three limits + exit check

**Cold start** — a new user or a new item has too little data for a reliable match. **Data sparsity** — most users
rate most items `0`; a high rate from very little data can mislead. **Similar preferences ≠ identical people** —
travel-rating similarity proves nothing about opinions, personality, or any other domain.

Save As `G8_U9_M3_TwinRecommend_<Name>.py`.

1. Why must the target never be compared to itself?
2. What are the two conditions for choosing a recommended item?
3. What is the cold-start problem?

### Tool Note – Thonny
Run `find_digital_twin` and `recommend_item` alone in the Shell against the four-user test data before wiring them
into `main()` — much faster to isolate a bug in one function than inside the full program.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A user can be its own best match | Always skip `candidate_index == target_index` |
| Higher `common` alone should win over a higher `rate` | The rate comes first in the tie-break key; `common` only breaks a tie |
| Any twin rating above 0 counts as "liked" | Only ratings meeting `liked_threshold` (default `3`) count |
| `None` results are bugs to eliminate | They're valid, expected outcomes — the program must handle them explicitly, not crash |
| A tie should be "resolved" by picking randomly | The source's rule keeps the first candidate found — a documented, reproducible design choice |

---

# 8. Assessment Evidence (formative)

- `find_digital_twin`'s trace on the four-user test data matching a real (non-self) twin
- The warm-up's self-comparison bug explained, not just fixed
- `recommend_item()` correct, including its `None` path
- **Unit 9 checkpoint** — the full recommender (`load_ratings`, `similarity_score`, `find_digital_twin`,
  `recommend_item`, `main`), scored against the source's 20-point rubric across five weighted bands (data &
  privacy, similarity calculation, twin & recommendation, code quality, critical thinking — see `unit-strategy.md`
  for the full table and performance bands). Verified here against all seven of the source's own test cases.
- The cold-start / sparsity / similarity-isn't-identity discussion, in the student's own words
