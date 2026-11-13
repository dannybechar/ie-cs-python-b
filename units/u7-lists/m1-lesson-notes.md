# Unit 7.1 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v3 (reconciled to the official Python B program, 9 Nov 2026)
### Topic: What Is a List? Creating, Indexing, Slicing

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **Lists part A, now delivered** — deck **9.1** (pp. 3–9: the "28 students / a million customers" hook,
the data types so far, the rules of a list, mixed types, `list()` vs `[]`, the index table `0..4 / -5..-1` for
`[24.56, "Itamar", 340, -7, "Yael"]`, slices `[1:3]`, `[-4:-1]`, `[1:]`, `[2:]`, `+` of three lists, `len`) and worksheet **9.4**
(Q1–Q3, the "write the output" tables). Also **12.0 / 12.1** (the temperature list and `[start:end:jump]`, pp. 4–5). Kept from v1: the
`==` vs `=` warm-up, `ai_report` (the AI link of the program), the bounds-checked update. See
[`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Official items deliberately left out (rulebook):** 9.4 Q1 row `data[5] = list(range(2, 5))` puts a **list inside a list** (a list of lists is
not taught in this course, CLAUDE.md) — the predict table below drops that row. Official 9.4 Q2 prints `12,988` (a comma typo of the
Ministry; read here as the two items `12` and `988`). 9.4 Q3 `data_3 = data_2` (an alias) is taught in 7.3, where the trap lives. The
9.2 matching game (genially) and the 9.3 "even list" video exist only as links: their titles are in the unit README (the exercise itself is built in 7.2).
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
**list of lists** (14.0 pp. 25–30, "next lesson"; the list-of-lists lesson itself, part E, was not delivered). **Official item deliberately left out:** both
stay out of this course (CLAUDE.md rulebook); so does the 9.4 Q1 row that puts `list(range(2, 5))` inside a list.

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
| 0–4 | **Hook (9.1 p. 3):** save the data of 28 students? of a million customers? Data types so far: `int`, `float`, `str`, `bool` — a list holds many of them |
| 4–9 | Creating lists (9.1 p. 4): a meaningful name, square brackets, commas, **mixed types** (`everything = [24.56, "Itamar", 340, -7]`), `[]` and `list()`, `len()`, `type()` |
| 9–14 | Indices (9.1 p. 6): the table `0..4 / -5..-1` for `[24.56, "Itamar", 340, -7, "Yael"]`, positive and negative |
| 14–16 | **Predict (question only):** `scores[-1]`, `scores[3]`? |
| 16–19 | The answers, including `IndexError: list index out of range` |
| 19–23 | Updating `scores[1] = 90`; updating an invalid position (`IndexError: list assignment index out of range`) |
| 23–28 | `in`, `not in`; `+` (new list), `[1, 2] + 3` is a `TypeError` |
| 28–33 | Slicing (9.1 p. 7 and 12.0 p. 4): `my_list[1:3]`, `[-4:-1]`, `[1:]`, `[2:]` on the Itamar list; then `[start:stop:step]` on the temperature list; `+` of **three** lists (9.1 p. 8) |
| 33–35 | **Predict (question only):** `my_list[2:9:3]` |
| 35–38 | The answer `[21, 24, 23]`; `[::-1]` — the reversed copy |
| 38–45 | Two ways to traverse (preview), side by side; the lab missions (the predict table comes first) |

The traversal preview (38–45), same code as the Ministry's 12.0 p. 3:

```python
scores = [72, 84, 65]

for score in scores:               # the value matters, not its position
    print(score)

for index in range(len(scores)):   # the position matters too
    print(index, scores[index])
```

Verified outputs used in the demo (9.1 pp. 4–9 are in `Lists_Reference.py`, function `official_demo`):

```text
>>> my_list = [24.56, "Itamar", 340, -7, "Yael"]
>>> my_list[1:3]
['Itamar', 340]
>>> my_list[-4:-1]
['Itamar', 340, -7]
>>> my_list[1:]
['Itamar', 340, -7, 'Yael']
>>> my_list[2:]
[340, -7, 'Yael']
>>> my_list = [25, 20, 21, 24, 21, 24, 21, 16, 23]
>>> my_list[:5]
[25, 20, 21, 24, 21]
>>> my_list[2:5]
[21, 24, 21]
>>> my_list[2:9:3]
[21, 24, 23]
>>> my_list[::-1]
[23, 16, 21, 24, 21, 24, 21, 20, 25]
>>> ["A", "B", "C", "D", "E"] + ["F", "G", "H", "I", "J"] + ["K", "L"]
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']      # the originals do not change
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

## 51–61 — Predict table (Ministry 9.4 Q1–Q3)

On paper, **before running anything**, the students write the output of every line (the brief gives the two tables; the starter repeats them as
comments); then they type the lines, run them and mark every wrong prediction. A wrong prediction costs nothing. Verified answers
(`Lists_Reference.py`, function `predict_table`):

| Line | Output |
|---|---|
| `data = [4, 5, 6, "Yael", "Ester", 7, 8]` — `print(data[1])` | `5` |
| `print(data[-3])` | `Ester` |
| `data[2] = "Amir"` then `print(data)` | `[4, 5, 'Amir', 'Yael', 'Ester', 7, 8]` |
| `print(len(data))` | `7` |
| `data = [4, 5, "Amir", "Yael", "Adi", 12, 988, 20, "20", 97]` — `print(data[::2])` | `[4, 'Amir', 'Adi', 988, '20']` |
| `print(data[::-1])` | `[97, '20', 20, 988, 12, 'Adi', 'Yael', 'Amir', 5, 4]` |
| `print(data[2:7:2])` | `['Amir', 'Adi', 988]` |
| `print(data[-8:-3])` | `['Amir', 'Yael', 'Adi', 12, 988]` |
| `print(data[1:])` | `[5, 'Amir', 'Yael', 'Adi', 12, 988, 20, '20', 97]` |
| `print(data[-4:-1])` | `[988, 20, '20']` |
| `my_list = [4] * 3` then `print(my_list)` | `[4, 4, 4]` (Ministry 9.4 Q4; `*` on a list is harmless, shown once) |

## 61–68 — Task 1: an AI-results report

Write `ai_report(scores)` — prints the count, the first score, the last score, and whether `100` is among them. Test on `[81, 24, 67, 91]`.

```text
Number of tests: 4
First score: 81
Last score: 91
Contains perfect score: False
```

## 68–75 — Task 2: a bounds-checked update

Write `update_score(scores, index, new_value)` — if `index` is a valid position, update it and return `True`;
otherwise print `"Invalid index"` and return `False`. Test on `[60, 70, 80]` with index `1` and index `5`.

```text
True [60, 75, 80]
Invalid index
False [60, 75, 80]
```

## 75–83 — Task 3: slicing report

Write `slice_report(values)` and test it on the temperature list: the whole list, the first five, items 2 up to 5, every third from
index 2, reversed.

```text
All: [25, 20, 21, 24, 21, 24, 21, 16, 23]
First five: [25, 20, 21, 24, 21]
From index 2 up to 5: [21, 24, 21]
Every third, from index 2: [21, 24, 23]
Reversed: [23, 16, 21, 24, 21, 24, 21, 20, 25]
```

## 83–86 — Task 4 (if time): `+` and `list()`

`combine(first, second)` returns `first + second`; print it, its `len`, and show the originals did not change. Then `list()` (`[]`).
(`list("cat")` is the first demo of 7.2.)

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
| `20` and `"20"` are the same value | A number and a text never compare equal (`data[-2]` vs. `data[-3]` in the predict table) |
| `+` adds numbers inside the lists | `+` joins the lists; `[1, 2] + [3, 4]` is `[1, 2, 3, 4]`, not `[4, 6]` |
| Checking `"75" in scores` on a list of numbers | `"75"` (text) never equals `75` (a number) |

---

# 8. Assessment Evidence (formative)

- The index table filled in both directions before running any code
- The warm-up explained (why nothing changed, not just the one-line fix)
- The predict table: how many of the 11 predictions were right, and why the wrong ones were wrong
- `ai_report()` printing all four lines; `update_score()` correct for a valid and an invalid index
- `slice_report()` matching the sample output (predicting `[2:9:3]` first)
- Exit check
