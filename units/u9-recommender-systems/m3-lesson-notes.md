# Lessons 21.1–21.2 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: From the Twin to a Recommendation — the Unit Checkpoint

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**⚠️ Unverified against official 21.2 / 21.0:** the whole code shape of this meeting (`find_twin`, `recommend_item`, `main`, the edge cases, the rubric) is **ours**.
All that the delivered Ministry deck 21.1 contains is pp. 24–27 (the twin, the recommendation of sushi) and p. 28 ("go to activity 21.2 in Classroom").
Because the Ministry has only three lessons, our fourth meeting is **our split of deck 21.1** (lesson 21.1 = pp. 1–25, lessons 21.1–21.2 = pp. 26–28 plus the code), supported by the master table's 8 hours only.
If 21.2 arrives, compare its function names, data layout and expected output with this meeting and adapt before class; do not present our code as the Ministry's.
**Source of inspiration:** Ministry deck **21.1**, second half (pp. 24–30): the twin is the participant with the most points; *an item the
twin liked and the new user does not know* becomes the recommendation (p. 26–27: user_03 likes sushi, user_04 does not know it); the
programming step (p. 28, worksheet 21.2 — **not delivered**). The Ministry's own code is therefore **assumed**: ours is a plain
`find_twin` + `recommend_item` + `main` on strings and flat lists. From v1 we keep the three named limits (cold start, sparse data, similar
preferences ≠ similar people), the edge-case testing table and the 20-point project rubric. The v1 code (tuples such as
`best_key = (-1.0, -1)`, default arguments `minimum_common=2`, `liked_threshold=3`, `csv.reader`) is replaced: the course forbids tuples and
default arguments in our own functions, and the Ministry's twin is simply "the most identical non-0 answers", so no rate is needed.
See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and labeled **Tool Note – Thonny**.
**Prerequisite:** `def`, `return`, `None`, strings, flat lists (lessons 4.1–4.6, 7.1–8.7, 9.1–9.5, 12.0–14.5).

---

## 1. Position in the recommender-systems block (lessons 20.0–22.1)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 20.0–20.1 | feed riddle, content-based vs user-based, culinary twin, survey | 45 / 45 |
| Lesson 21.1 | the table, similarity points, `count_same` | 45 / 45 |
| **Lessons 21.1–21.2 (this)** | **`find_twin`, `recommend_item`, `main` — the checkpoint** | 45 / 45 |
| Lessons 22.0–22.1 | dangers of recommender systems | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 22–23) | Covered here |
|---|---|
| Goal 7: find the most similar user — the "digital twin" | ✅ `find_twin` |
| Goal 8: recommend an item unknown to the user but liked by the twin | ✅ `recommend_item` |
| Goal 9: combine several functions in one main program | ✅ `main()` |
| Goal 10: test on normal and edge cases | ✅ the six cases |
| Goal 14: limits (data scarcity, consent) | ✅ the three limits |

### Deliberate exclusions
Similarity rates, weights, several neighbours, reading files (all enrichment).

---

## 3. Lesson Goal

**Compare the target with every *other* participant, keep the one with the most points (the twin; nobody with 0 points), then recommend an
item the twin liked (`V`) and the target does not know (`0`) — and print a clear message, instead of crashing, when there is no twin or nothing to recommend.**

---

## 4. Core Mental Models

```python
def find_twin(target_index):
    best_index = None
    best_score = 0
    for index in range(len(answers)):
        if index != target_index:             # never compare a person with themselves
            score = count_same(answers[target_index], answers[index])
            if score > best_score:            # strictly greater: on a tie the first one stays
                best_score = score
                best_index = index
    return best_index                         # None when nobody shares anything


def recommend_item(target_answers, twin_answers):
    for index in range(len(target_answers)):
        if target_answers[index] == "0" and twin_answers[index] == "V":
            return item_names[index]
    return None
```

Trace of `find_twin(3)` on the class table (lesson 21.1): user_01 → 0, user_02 → 0, user_03 → 2 → `best_index = 2`.
`recommend_item("00XVV", "V0XXV")`: index 0 → target `0` and twin `V` → `"sushi"`.

- `best_score` starts at `0` on purpose: somebody who shares nothing is never a twin.
- A recommendation needs **both** conditions: the twin liked it (`V`) and the target does not know it (`0`). Twin `X` → no. Target already
  answered `V` or `X` → no (the target knows it).
- `None` is a valid answer ("no twin", "nothing to recommend"); `main` must handle it.
- `return` inside the loop stops at the **first** item found. (If time, Task 3 collects all.)

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 21.1, pp. 24–30)

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** the class table; predict the twin of user_04 (pairs), then run `count_same` on the three pairs — all as before |
| 8–16 | **From twin to recommendation** (pp. 26–27): is there a food the twin liked and user_04 does not know? Predict first (which food?), then the answer (sushi). Counter-cases: twin disliked it (`X`); user_04 already has an opinion |
| 16–30 | **Plan `find_twin`:** pseudocode (the "best so far" pattern of `best_score` from lesson 21.1, now also remembering *who*), then a trace on the class table. Why start `best_score` at 0? What if everyone has 0? **The code is not shown:** the starter holds a version with the classic mistake (warm-up), so the bug is found by the students |
| 30–40 | **Plan `recommend_item`** in pseudocode, with the three cases (twin `V` + target `0` → recommend; twin `X` → no; target already answered → no); then the plan of `main()`: target = the last participant, find the twin, print or print a message. Students write `recommend_item` themselves in the lab |
| 40–45 | **Three limits (kept from v1):** *cold start* — a new person with only `0`s has no twin; *sparse data* — a score of 2 from 3 shared answers is weak evidence; *similar ≠ same* — the twin shares food opinions, not necessarily anything else. A recommendation is a prediction, not a fact |

---

# 6. Second 45 Minutes — Lab

Starter: [`TwinRecommend_Starter.py`](TwinRecommend_Starter.py). Reference: [`TwinRecommend_Reference.py`](TwinRecommend_Reference.py).
Brief: [`m3-lab-brief-he.md`](m3-lab-brief-he.md). Data: the sample table is in the starter (or the class survey, pasted as in lesson 21.1).

| Clock | Block |
|---|---|
| 45–52 | Warm-up bug: your own twin |
| 52–62 | Task 1: `recommend_item(target_answers, twin_answers)` |
| 62–80 | Task 2 (project, checkpoint): `main()` |
| 80–86 | Testing the edge cases |
| 86–90 | Save and exit check |

## 45–52 — Warm-up: a person is their own twin

The starter's `find_twin` has no check for the target's own index. `print(find_twin(3))` should be `2` (user_03) and prints **`3`**: user_04 shares every non-0 answer with
themselves (3 points), more than with anyone else. Fix: wrap the score and the "best so far" update in `if index != target_index:`.
(`continue` is **not** used: it appears nowhere in Python A or in the Ministry materials, so the class has not been taught it; an earlier build of this meeting used it and was rewritten.)

## 52–62 — Task 1: `recommend_item(target_answers, twin_answers)`

Return the **name** of the first item the twin liked and the target does not know, otherwise `None`. `recommend_item("00XVV", "V0XXV")` → `sushi`.

## 62–80 — Task 2 (project — the checkpoint): `main()`

Target = the last participant (`len(aliases) - 1`). Find the twin; if there is none print `No twin found.` and stop; print the target, the twin
and the points; print the recommendation or `Nothing new to recommend.` Expected with the sample data:

```text
Target: user_04
Twin: user_03
Points: 2
Recommendation: sushi
```

## 80–86 — Testing the edge cases

<div dir="rtl">

| מקרה | נתונים לדוגמה | התנהגות מצופה |
|---|---|---|
| אף אחד לא חולק תשובה | `"00000"` מול `"0000V"` ו-`"XXXX0"` | אין תאום (`None`) |
| התאום אינו אוהב דבר חדש | `recommend_item("V0XXV", "V0XXV")` | `None` — אין המלצה |
| המטרה מכירה הכול | `recommend_item("VXVXV", "VXXXV")` | `None` — אין המלצה |
| שוויון | שני משתתפים עם 2 נקודות | הראשון נשאר (מתועד) |
| `0` ו-`0` בלבד | `count_same("0V", "0X")` | `0` — אין נקודה |
| מחרוזות באורכים שונים | `count_same("V0", "V0X")` מול `count_same("V0X", "V0")` | הראשון מחזיר 1; השני `IndexError: string index out of range` — לכן בודקים אורך ב-`has_all_answers` (שיעורים 20.0–20.1) |

</div>

The reference has `run_edge_cases()` that prints the first five; the mismatched-length row is a discussion (the second call raises
`IndexError: string index out of range` on Python 3.14).

## 86–90 — Save and exit check

Save As `G8_U9_M3_TwinRecommend_<Name>.py`.

1. Why must the target never be compared with itself?
2. What are the two conditions for recommending an item?
3. What is the cold-start problem?

### Tool Note – Thonny
Run `find_twin` and `recommend_item` alone in the Shell before wiring them into `main()`. If a student's `main` prints `None` instead of
a message, they forgot the `if ... is None` check.

### Project rubric — 20 points (the checkpoint; our own scale, v1 had no table)

<div dir="rtl">

| תחום | נקודות | מה בודקים |
|---|---:|---|
| נתונים ופרטיות | 3 | הנתונים בסקאלה V / X / 0 בלבד; כינויים בלבד; אין שם או פרט מזהה |
| חישוב הדמיון | 4 | `count_same` נכונה: זהות ולא `0`; שני `X` נספרים; שני `0` לא |
| תאום והמלצה | 6 | `find_twin` לא משווה לעצמו; `None` כשאין תאום; `recommend_item` בודקת את שני התנאים |
| איכות הקוד | 3 | פעולה לכל משימה, שמות ברורים, `main` מטפלת ב-`None` |
| חשיבה ביקורתית | 4 | מסבירים לפחות שניים משלושת המגבלות ומה זה אומר על אמינות ההמלצה |

</div>

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| A person can be their own best match | Always skip `index == target_index` |
| `0` points can still be "the best" | `best_score` starts at 0, so nobody with 0 points is a twin |
| Every `V` of the twin is a recommendation | Only if the target answered `0` |
| `None` is a bug to remove | It is a valid result; the program must print a clear message |
| A tie is resolved randomly | We keep the first one found: a reproducible, documented rule |
| The recommendation is true for me | It is a prediction from a few answers |

---

# 8. Assessment Evidence (formative)

- `find_twin` traced on the class table, giving user_03
- The warm-up (self-comparison) explained, not only fixed
- `recommend_item` correct including its `None` path
- **Recommender-systems checkpoint (lessons 20.0–22.1)** — `count_same`, `find_twin`, `recommend_item`, `main`, scored on the 20-point rubric above, run on the sample data and on the class data
- The three limits explained in the student's own words
