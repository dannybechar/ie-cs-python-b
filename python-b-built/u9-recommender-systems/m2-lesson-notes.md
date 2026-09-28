# Unit 9.2 — Recommender Systems

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: From CSV to a Similarity Score

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit09_recommendation_systems_complete_unit.md`, meeting 2 — its own clock
table, `load_ratings`, the similarity-function pseudocode, the hand trace table, `similarity_score`, the
matches-vs-rate discussion, both practice drills, and the unit-test asserts kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 9

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 9.1 | content-based vs. user-based recommendation; survey design | 45 / 45 |
| **9.2 (this)** | **reading CSV data; computing similarity between users** | 45 / 45 |
| 9.3 | finding a digital twin; producing a recommendation (checkpoint) | 45 / 45 |
| 9.4 | filter bubbles, echo chambers, the attention economy | 45 / 45 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 22) | Covered here |
|---|---|
| Goal 3: represent preferences with parallel rating lists | ✅ `load_ratings` |
| Goal 5: trace a similarity calculation with a trace table | ✅ guided practice |
| Goal 6: implement similarity with a loop and compound conditions | ✅ every task |
| Goal 9: read rating data from a CSV file | ✅ Task 1 |

### Deliberate exclusions
Finding the best-matching user (9.3), producing a recommendation (9.3).

---

## 3. Lesson Goal

**A similarity function counts only shared, known ratings (`0` excluded on either side) and, among those, how many
agree — a rate normalizes that count so a user with more shared items isn't automatically favored.**

---

## 4. Core Mental Models

```text
קלט: שתי רשימות דירוגים
אתחל matches ל-0, common ל-0
עבור כל אינדקס:
    אם שני הדירוגים אינם 0:
        הגדל common
        אם הדירוגים שווים:
            הגדל matches
החזר matches ו-common
```

```python
def similarity_score(first, second):
    matches = 0
    common = 0
    for index in range(len(first)):
        if first[index] != 0 and second[index] != 0:
            common += 1
            if first[index] == second[index]:
                matches += 1
    return matches, common
```

- `aliases[i]` and `ratings[i]` describe the **same** user — that's what makes them parallel lists.
- Raw `matches` favors users with more shared items; `matches / common` (the **rate**) corrects for that — but a
  rate of `1.0` from a single shared item is weak evidence (9.3 requires at least two).

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** the rating scale and the shared-rating definition |
| 8–20 | Opening `ratings.csv` in a text editor; identifying the header row, one row per user, and the values |
| 20–32 | Reading the file in Python with the `csv` module (`load_ratings`, below) |
| 32–45 | Planning the similarity function in pseudocode (above) |

```python
import csv


def load_ratings(filename):
    aliases = []
    ratings = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        item_names = header[1:]

        for row in reader:
            if not row:
                continue
            aliases.append(row[0])
            ratings.append([int(value) for value in row[1:]])

    return item_names, aliases, ratings
```

`encoding="utf-8-sig"` handles a BOM character some spreadsheet exports add; `header[1:]` drops the alias column
from the item-name list; every rating is converted from text to `int`.

---

# 6. Second 45 Minutes — Lab

Starter: [`Similarity_Starter.py`](Similarity_Starter.py). Reference: [`Similarity_Reference.py`](Similarity_Reference.py).
A real [`ratings.csv`](ratings.csv) is provided — this meeting's file reading runs for real, no mock needed.

## 45–58 — Hand trace, then predict

```python
user_a = [3, 1, 0, 3, 2]
user_b = [3, 1, 3, 2, 2]
```

<div dir="rtl">

| `i` | `user_a[i]` | `user_b[i]` | משותף? | שווה? | `matches` | `common` |
|---:|---:|---:|---|---|---:|---:|
| 0 | 3 | 3 | כן | כן | 1 | 1 |
| 1 | 1 | 1 | כן | כן | 2 | 2 |
| 2 | 0 | 3 | לא | — | 2 | 2 |
| 3 | 3 | 2 | כן | לא | 2 | 3 |
| 4 | 2 | 2 | כן | כן | 3 | 4 |

</div>

Fill the table **before** running; expect `(3, 4)`.

## 58–66 — Warm-up: `0 == 0` looks like agreement, but isn't

```python
def broken_similarity(first, second):
    matches = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            matches += 1
    return matches


print(broken_similarity([0, 1, 3], [0, 1, 2]))
```

Predict `1` (only index 1 is a real, known agreement), run, get `2` — both users not knowing an item (`0` and `0`)
counted as if they'd agreed. Fix: only compare when **both** values are non-zero.

## 66–74 — Task 1: `load_ratings("ratings.csv")`

Complete the function (append the alias and the converted rating row inside the loop) and print all three returned
values.

```text
['museum', 'beach', 'park', 'city']
['user_01', 'user_02', 'user_03']
[[3, 1, 0, 3], [3, 1, 3, 2], [1, 3, 2, 1]]
```

## 74–80 — Task 2: `similarity_score(first, second)`

Confirm on `similarity_score([3, 1, 0, 3, 2], [3, 1, 3, 2, 2])` → `(3, 4)`, matching the trace table, then run the
source's own asserts:

```python
assert similarity_score([3, 1], [3, 1]) == (2, 2)
assert similarity_score([0, 1], [0, 1]) == (1, 1)
assert similarity_score([0, 0], [3, 2]) == (0, 0)
assert similarity_score([3, 1], [1, 3]) == (0, 2)
```

## 80–90 — Task 3 + save + exit check

`similarity_rate(first, second)` — `matches / common`, or `0.0` if `common` is `0`. Confirm
`similarity_rate([3, 1, 0], [3, 1, 2])` → `1.0`, and note: a perfect rate from one shared item isn't strong
evidence (9.3 requires at least two shared ratings before trusting a candidate).

Save As `G8_U9_M2_Similarity_<Name>.py`.

1. Why is the condition `first[index] != 0 and second[index] != 0` needed?
2. What's the difference between `matches` and `common`?
3. What's the risk of a 100% match rate based on a single shared item?

### Tool Note – Thonny
If `load_ratings("ratings.csv")` raises `FileNotFoundError`, check that `ratings.csv` sits in the **same folder** as
the `.py` file — Thonny runs relative to the script's own location.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Two `0`s in the same position count as agreement | Both mean "unknown" — that position is skipped entirely, not counted as a match |
| More raw `matches` always means a better match | A user with more shared ratings gets more chances to match — use the **rate**, not the raw count, to compare fairly |
| A 100% similarity rate is always strong evidence | Not when it's based on just one or two shared items — more shared ratings make a rate more trustworthy |
| CSV values are already numbers | Every value read from a CSV file is text — convert explicitly with `int()` |
| A missing `ratings.csv` will produce ratings of `0` | It raises `FileNotFoundError` — the program doesn't silently continue |

---

# 8. Assessment Evidence (formative)

- The `user_a`/`user_b` trace table completed before running, matching `(3, 4)`
- The warm-up's `0 == 0` bug explained (why it shouldn't count), not just fixed
- `load_ratings()` producing the exact expected output on the real CSV
- `similarity_score()` passing all four given asserts
- `similarity_rate()` correct, with the single-item-evidence risk named
- Exit check
