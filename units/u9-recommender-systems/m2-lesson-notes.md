# Lesson 21.1 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: The Table, Similarity Points, the Twin

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry deck **21.1** ("בונים מערכת המלצה משלנו", 30 slides), first half (pp. 1–25): the three-question refresh
quiz, the participants × items table with `V` / `X` / `0`, counting similarity points one item at a time, the twin = the most points. The
Ministry's own code is in worksheet **21.2** and the teacher notes **21.0**, both **not delivered**; the code in this meeting is our own and
uses only plain strings, flat lists and `def`. The Ministry's sample table (four participants, five foods) is kept exactly as data
(`ratings.csv`, with aliases instead of first names). From v1 we keep the plan-in-pseudocode → trace table → code sequence and the
"a `0` is not a match" warm-up bug (the 0–3 scale is replaced by V / X / 0). See
[`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral.
**Prerequisite:** `def`, `return`, strings and flat lists (lessons 4.1–4.6, 7.1–8.7, 9.1–9.5, 12.0–14.5). No file reading, no tuples, no dictionaries, no `csv` module.

---

## 1. Position in the recommender-systems block (lessons 20.0–22.1)

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| Lessons 20.0–20.1 | feed riddle, content-based vs user-based, culinary twin, survey | 45 / 45 |
| **Lesson 21.1 (this)** | **the table, similarity points, the twin; `count_same`** | 45 / 45 |
| Lessons 21.1–21.2 | recommend what the twin liked; the project (checkpoint) | 45 / 45 |
| Lessons 22.0–22.1 | dangers of recommender systems | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 21–22) | Covered here |
|---|---|
| Goal 3: represent preferences as data (a table, parallel lists) | ✅ the table, `item_names` / `aliases` / `answers` |
| Goal 4: a shared answer; why `0` is excluded | ✅ the point rule |
| Goal 5–6: trace a similarity count, implement it with a loop and a compound condition | ✅ trace table, `count_same` |
| Goal 7: find the most similar user | ✅ in words and by `best_score`; the full `find_twin` is lessons 21.1–21.2 |

### Deliberate exclusions
Reading files (the data is typed in as lists; a teacher helper converts the Forms CSV), similarity *rates*, tuples, dictionaries.

---

## 3. Lesson Goal

**Similarity between two people = how many items they answered identically, counting only answers that are not `0`. The twin is the
person with the most points.**

---

## 4. Core Mental Models

The data (Ministry 21.1 pp. 12–15; items in the order sushi, beet, dal, pasta, pizza):

<div dir="rtl">

| משתתף | sushi | beet | dal | pasta | pizza |
|---|:-:|:-:|:-:|:-:|:-:|
| user_01 | X | V | 0 | X | X |
| user_02 | 0 | V | V | 0 | X |
| user_03 | V | 0 | X | X | V |
| user_04 (חדש/ה) | 0 | 0 | X | V | V |

</div>

In Python, three parallel lists (the same position = the same participant) and **one string of letters per person**:

```python
item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
answers = ["XV0XX", "0VV0X", "V0XXV", "00XVV"]
```

`answers[3][2]` is user_04's answer for `dal`: `"X"`. Strings are used so that no list of lists is needed.

Counting points, user_04 against user_03 (21.1 pp. 16–23):

<div dir="rtl">

| פריט | user_04 | user_03 | נקודה? | למה |
|---|:-:|:-:|:-:|---|
| sushi | 0 | V | לא | אחד מהם לא מכיר |
| beet | 0 | 0 | לא | שניהם לא מכירים — אין דעה משותפת |
| dal | X | X | **כן** | שניהם לא אוהבים |
| pasta | V | X | לא | דעות שונות |
| pizza | V | V | **כן** | שניהם אוהבים |

</div>

The Ministry's deck uses first names (Natalie, Aviv, Ariel and the new user Keren); user_01–user_04 are the same four people in the same order, so the teacher may write the Ministry's names on the board (fictional) — in code and files we keep aliases. Total **2**. Against user_01: **0**. Against user_02: **0**. The twin of user_04 is **user_03** (the most points).

- **Ministry slips (do not copy):** p. 12 heads the table with *chips* where p. 13 on has *beet*; pp. 20–22 repeat the same slide three times; the word "דימיון" is spelled two ways. We use sushi, beet, dal, pasta, pizza throughout.
- **⚠️ Code shape assumed:** the Ministry's own code (worksheet 21.2) and teacher notes 21.0 were not delivered, so `count_same` and the string-per-person layout are ours — unverified against official 21.2. If 21.2 uses a different data layout, compare before class.
- **Identical, not `0`.** `X` and `X` *is* a point (a shared dislike is also similarity). `0` and `0` is **not** (21.1 p. 21: it teaches us nothing).
- **Ties:** two participants with the same top score are both candidates; in code the first one found stays (a documented design choice, not
  a law of nature). If the best score is 0 there is no twin.
- The twin is a statement about the data we collected, not about the people.

---

# 5. First 45 Minutes — Knowledge + Guided Practice (deck 21.1)

| Clock | Activity |
|---|---|
| 0–9 | **Title and refresh quiz** (pp. 2–5, three questions, answer with fingers, then the answers). Q1 *what is the "feed"?* — answer 1: the home page of an app (TikTok, Instagram) with a stream of content personalised to you. Q2 *the main difference between content-based and user-based?* — answer 3: content-based checks what we liked and watched before; user-based checks what people similar to us (our digital twins) liked. Q3 *does an app say "this is a recommendation just for you" every time?* — answer 2: no, TikTok and Instagram just stream videos into one feed without saying so |
| 9–12 | **The project in two steps** (pp. 6–10): step 1 collected data (the survey), step 2 programs the system |
| 12–17 | **The table** (pp. 11–14): participants on one axis, foods on the other, `V` / `X` / `0`; read user_01 aloud: dislikes pizza, pasta and sushi, likes beet, does not know dal |
| 17–20 | **A new participant** (p. 15), question only: user_04 fills the survey. *How will we know what to recommend?* Pairs predict a method |
| 20–26 | **Counting points** (pp. 16–23): the rule, one item at a time; predict-first on the `0`/`0` column: *a point or not?* |
| 26–30 | **The answer** and the completed table against user_03: 2 points |
| 30–35 | **Pairs count** user_04 against user_01 and user_02 |
| 35–39 | **Who is the twin?** (pp. 24–25): the participant with the most points (user_03). *What if two had 2 points?* |
| 39–45 | **Bridge to code:** one string per person, `first[index]` and `second[index]` — the loop pattern of the strings block (lessons 7.1–8.7) (pseudocode below) |

```text
same = 0
for every position:
    if the two answers are equal and the answer is not "0":
        same = same + 1
return same
```

---

# 6. Second 45 Minutes — Lab

Starter: [`Similarity_Starter.py`](Similarity_Starter.py). Reference: [`Similarity_Reference.py`](Similarity_Reference.py).
Brief: [`m2-lab-brief-he.md`](m2-lab-brief-he.md). The data is already in the starter (sample = [`ratings.csv`](ratings.csv)).

| Clock | Block |
|---|---|
| 45–52 | Warm-up bug: `count_same` counts `0` and `0` |
| 52–62 | Task 1: `show_comparison(first, second)` — the trace table, printed |
| 62–72 | Task 2: `print_scores(target_index)` |
| 72–80 | Task 3: `best_score(target_index)` |
| 80–86 | Task 4 (if time): the class's own survey — paste the three lines the teacher gives |
| 86–90 | Save and exit check |

## 45–52 — Warm-up: a shared "don't know" counts as a point

```python
def count_same(first, second):
    same = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            same += 1
    return same


print(count_same("00XVV", "V0XXV"))
```

Predict `2` (the table above), run: **`3`**. The `beet` column is `0` and `0`: equal, so it was counted. Fix:
`if first[index] == second[index] and first[index] != "0":`.

## 52–62 — Task 1: `show_comparison(first, second)`

For every item print the item name, the two answers and `point` or `-`. Uses the global `item_names` (reading a global inside a function needs no `global`).

```text
sushi 0 V -
beet 0 0 -
dal X X point
pasta V X -
pizza V V point
```

Students first fill the same table by hand in the brief, then compare with the program.

## 62–72 — Task 2: `print_scores(target_index)`

For every participant except the target print the alias and the points. `print_scores(3)` prints

```text
user_01 0
user_02 0
user_03 2
```

## 72–80 — Task 3: `best_score(target_index)`

The highest score among the others (the "keep the maximum so far" pattern). `best_score(3)` → `2` (user_03); `best_score(0)` → `2` too
(user_01 against user_02 shares beet `V` and pizza `X`; against user_03 only 1, against user_04 0 — students check by hand). Which
participant gives the best score is the job of `find_twin` in lessons 21.1–21.2.

## 80–86 — Task 4 (if time): the class's own survey

The teacher runs [`CsvToLists_Teacher.py`](CsvToLists_Teacher.py) on the Forms CSV (it prints `item_names = [...]`, `aliases = [...]`,
`answers = [...]`) and gives the three lines to the class. Students paste them over the sample data and run Task 2 for a target of their choice.
The helper uses `open` and `split`, which the class has not learned, so it is a teacher tool; students only paste its output.

## 86–90 — Save and exit check

Save As `G8_U9_M2_Similarity_<Name>.py`.

1. When do two answers give a similarity point?
2. `"0"` and `"0"` — a point or not, and why?
3. Who is the "twin" of a person?

### Tool Note – Thonny
Test each function alone in the Shell first (`count_same("00XVV", "V0XXV")`) before the next task calls it.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Two `0`s are a similarity | Nobody knows the item — no shared opinion, no point |
| Only shared likes count | A shared dislike (`X` and `X`) is also a point |
| The twin is a person like me | The most points on the items we collected — nothing more |
| `answers[3][2]` is a list inside a list | It is a character of a string: the 3rd item of the 4th person's string |
| A bigger score always means a better twin | With few shared (non-0) answers a score is weak evidence |

---

# 8. Assessment Evidence (formative)

- The hand-filled trace table matching `show_comparison`
- The warm-up explained (`0` and `0` are equal but not information), not only fixed
- `count_same`, `print_scores`, `best_score` passing their tests
- Exit check
