# Unit 7.1 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: What Is a List? Creating, Indexing, Slicing

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **12.0 / 12.1** (Lists part B, slides 3–5, 8 and 11–15: `list()`, indexing, `[start:end:jump]`,
`[::-1]`, `in`, `+`, the temperature list `[25, 20, 21, 24, 21, 24, 21, 16, 23]`) and 13.0 p. 2 (summary table of operations). Lists
**part A** (which part B calls "as we learned") was **not delivered**: this meeting rebuilds the part-A basics (what a list is, `[]`,
indexing, updating, `len`) from the v1 build and the Ministry's own examples. Kept from v1: the "30 variables" hook, the index
table, the `==` vs `=` warm-up, `ai_report` and the bounds-checked update. **New (audit):** `list()`, `+`, slicing `[a:b:c]`,
`[::-1]`. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3 comes before Unit 7 in the schedule) — the lab tasks are small `def` functions, as in the
Ministry worksheets. The students already know slicing and `[::-1]` on strings (Unit 5); here the same notation is applied to lists.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **7.1 (this)** | **what a list is; `[]`, `list()`; indices; update; `in`; `+`; slicing** | 45 / 45 |
| 7.2 | list operations: `append`, `insert`, `count`, `index`, `remove`, `pop`, `sort`, `reverse`, `split`/`join`, `random.choice` | 45 / 45 |
| 7.3 | traversal by index and by value; accumulation; the "change while looping" trap | 45 / 45 |
| 7.4 | counting, filters, maximum, flat menus, parallel lists | 0 / 90 |
| 7.5 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 1: what a list is and its purpose | ✅ hook |
| Goal 2: create an empty list or one with initial values | ✅ `[]`, `list()`, literal |
| Goal 3: access by index, update an element | ✅ every task |
| Goal 4: `len` and `in` with lists | ✅ |
| Goal 7: traverse directly or by index | ✅ preview (full treatment in 7.3) |

### Deliberate exclusions
`append`, `insert`, `remove`, `pop`, `sort` (7.2); accumulation (7.3); search (7.5). The Ministry previews **nested loops** and a
**list of lists** (14.0 pp. 25–30, "next lesson", part E — not delivered): both stay out of this course (CLAUDE.md rulebook).

---

## 3. Lesson Goal

**A list holds a growing, ordered collection of values under one name — indexed from `0`, changeable after it was created, and
cut into pieces with the same `[start:stop:step]` the students know from strings.**

---

## 4. Core Mental Models

```python
scores = [72, 84, 65]
print(scores[0])    # 72
print(scores[-1])   # 65
scores[1] = 90      # update in place
print(scores)       # [72, 90, 65]
```

- Instead of `score_1`, `score_2`, … (a new variable per result), one list holds them all under one name and can grow.
- `values[2]` (what is at position 2) and `2 in values` (does the value 2 appear anywhere) ask different questions.
- A list is **mutable**; the same slice notation as strings gives a **new** list and leaves the original alone.
- `my_list[start:stop:step]`: from `start` (included) up to `stop` (**not** included), in jumps of `step`; `[::-1]` is the reversed copy.
- `+` joins two lists into a **new** list: `[1, 2] + [3]` is `[1, 2, 3]`; a list plus a number is an error.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–4 | **Hook:** `score_1 = 72`, `score_2 = 84`, … what happens with 30 results? |
| 4–9 | Creating lists: `[]`, `list()`, `[72, 84, 65]`, mixed types, `len()`, `type()` |
| 9–14 | Indices: a table, positive and negative, both directions |
| 14–16 | **Predict (question only):** `scores[-1]`, `scores[3]`? |
| 16–19 | The answers, including `IndexError: list index out of range` |
| 19–23 | Updating `scores[1] = 90`; updating an invalid position (`IndexError: list assignment index out of range`) |
| 23–28 | `in`, `not in`; `+` (new list), `[1, 2] + 3` is a `TypeError` |
| 28–33 | Slicing `[start:stop:step]` on the temperature list; `values[:5]`, `values[2:5]` |
| 33–35 | **Predict (question only):** `my_list[2:9:3]` |
| 35–38 | The answer `[21, 24, 23]`; `[::-1]` — the reversed copy |
| 38–45 | Two ways to traverse (preview), side by side; the lab missions |

The traversal preview (38–45), same code as the Ministry's 12.0 p. 3:

```python
scores = [72, 84, 65]

for score in scores:               # the value matters, not its position
    print(score)

for index in range(len(scores)):   # the position matters too
    print(index, scores[index])
```

Verified outputs used in the demo:

```text
>>> my_list = [25, 20, 21, 24, 21, 24, 21, 16, 23]
>>> my_list[:5]
[25, 20, 21, 24, 21]
>>> my_list[2:5]
[21, 24, 21]
>>> my_list[2:9:3]
[21, 24, 23]
>>> my_list[::-1]
[23, 16, 21, 24, 21, 24, 21, 20, 25]
>>> [1, 2] + [3]
[1, 2, 3]
>>> [1, 2] + 3
TypeError: can only concatenate list (not "int") to list
>>> [1, 2][5]
IndexError: list index out of range
```

---

# 6. Second 45 Minutes — Lab

Starter: [`Lists_Starter.py`](Lists_Starter.py). Reference: [`Lists_Reference.py`](Lists_Reference.py).

## 45–51 — Warm-up: compared, not assigned

```python
scores = [60, 70, 80]
scores[1] == 75
print(scores)
```

Predict `[60, 75, 80]`, run, get the unchanged `[60, 70, 80]` — `==` compares and the result is thrown away, it
never updates anything. Fix: `scores[1] = 75`.

## 51–61 — Task 1: an AI-results report

Write `ai_report(scores)` — prints the count, the first score, the last score, and whether `100` is among them. Test on `[81, 24, 67, 91]`.

```text
Number of tests: 4
First score: 81
Last score: 91
Contains perfect score: False
```

## 61–71 — Task 2: a bounds-checked update

Write `update_score(scores, index, new_value)` — if `index` is a valid position, update it and return `True`;
otherwise print `"Invalid index"` and return `False`. Test on `[60, 70, 80]` with index `1` and index `5`.

```text
True [60, 75, 80]
Invalid index
False [60, 75, 80]
```

## 71–80 — Task 3: slicing report

Write `slice_report(values)` and test it on the temperature list: the whole list, the first five, items 2 up to 5, every third from
index 2, reversed.

```text
All: [25, 20, 21, 24, 21, 24, 21, 16, 23]
First five: [25, 20, 21, 24, 21]
From index 2 up to 5: [21, 24, 21]
Every third, from index 2: [21, 24, 23]
Reversed: [23, 16, 21, 24, 21, 24, 21, 20, 25]
```

## 80–86 — Task 4 (if time): `+` and `list()`

`combine(first, second)` returns `first + second`; print it, its `len`, and show the originals did not change. Then `list("cat")`
(`['c', 'a', 't']`) and `list()` (`[]`).

## 86–90 — Save and exit check

Save As `G8_U7_M1_Lists_<Name>.py`. For `items = ["A", "B", "C"]`:

1. What is `items[1]`?
2. What is `items[-1]`?
3. How do you update `"B"` to `"X"`?
4. What is the last valid index, by `len`?
5. What does `items[::-1]` give?

**Answers:** `"B"`, `"C"`, `items[1] = "X"`, `len(items) - 1`, `["C", "B", "A"]`.

### Tool Note – Thonny
The **Variables** view updates live as a list changes — watch it while stepping through `update_score()` to see which element changes.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An index equal to the list's length is valid | The last valid index is `len(values) - 1` |
| `values[2]` and `2 in values` ask the same question | One is "what is at position 2", the other "does 2 appear anywhere" |
| Writing `==` when an update was intended | `=` assigns, `==` compares — and a bare comparison does nothing useful |
| A slice includes its `stop` position | The stop index is **not** included: `values[2:5]` has three items |
| A slice changes the original list | A slice is a new list; the original stays as it was |
| `+` adds numbers inside the lists | `+` joins the lists; `[1, 2] + [3, 4]` is `[1, 2, 3, 4]`, not `[4, 6]` |
| Checking `"75" in scores` on a list of numbers | `"75"` (text) never equals `75` (a number) |

---

# 8. Assessment Evidence (formative)

- The index table filled in both directions before running any code
- The warm-up explained (why nothing changed, not just the one-line fix)
- `ai_report()` printing all four lines; `update_score()` correct for a valid and an invalid index
- `slice_report()` matching the sample output (predicting `[2:9:3]` first)
- Exit check
