# Unit 7.1 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: What Is a List?

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit07_lists_complete_unit.md`, meeting 1 — its own clock table, the "why not
one variable per result" hook, the index table, the membership/count examples, the direct-vs-index traversal
comparison, both practice drills and the AI-report drill, and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **7.1 (this)** | **a list as an ordered, dynamic collection; indices; traversal** | 45 / 45 |
| 7.2 | list operations: append/extend/insert, remove/pop, sort/reverse, split/join | 45 / 45 |
| 7.3 | advanced operations + the accumulation pattern | 45 / 45 |
| 7.4 | counting, minimum, maximum, a report | 0 / 90 |
| 7.5 | linear search + the "AI Experiment Analyzer" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 1: what a list is and its purpose | ✅ hook |
| Goal 2: create an empty list or one with initial values | ✅ |
| Goal 3: access by index, update an element | ✅ every task |
| Goal 4: `len` and `in` with lists | ✅ |
| Goal 7: traverse directly or by index | ✅ guided practice |

### Deliberate exclusions
`append`/`extend`/`insert`/`remove`/`pop`/`sort` (7.2), the accumulation pattern (7.3), search (7.5).

---

## 3. Lesson Goal

**A list holds a growing, ordered collection of values under one name — indexed from `0`, and changeable after it's
created.**

---

## 4. Core Mental Models

```python
scores = [72, 84, 65]

print(scores[0])    # 72
print(scores[-1])   # 65 - the last item, without needing len(scores) - 1

scores[1] = 90        # update in place
print(scores)          # [72, 90, 65]
```

- Instead of `score_1`, `score_2`, `score_3`, … (a new variable for every result), one list holds them all under one
  name — and can grow to any size.
- `values[2]` (a value at a position) and `2 in values` (does this value appear anywhere) ask two different
  questions — don't confuse them.
- A list is **mutable**: it can change after it's created, unlike a string.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Hook:** `score_1 = 72`, `score_2 = 84`, `score_3 = 65` — what happens with 30 results? |
| 8–17 | A row of index cards as a physical, ordered, dynamic collection |
| 17–27 | Creating lists: `[]`, `[72, 84, 65]`, mixed types, `len()`, `type()` |
| 27–37 | Indices: a 3-value table, positive and negative, both directions; updating `scores[1] = 90` |
| 37–41 | `in`, `not in`, `count` on `["cat", "dog", "cat", "bird"]` |
| 41–45 | The two traversal styles, side by side; the lab missions |

The traversal comparison (41–45):

```python
scores = [72, 84, 65]

for score in scores:              # the value matters, not its position
    print(score)

for index in range(len(scores)):   # the position matters too
    print(index, scores[index])
```

---

# 6. Second 45 Minutes — Lab

Starter: [`Lists_Starter.py`](Lists_Starter.py). Reference: [`Lists_Reference.py`](Lists_Reference.py).

## 45–53 — Warm-up: compared, not assigned

```python
scores = [60, 70, 80]
scores[1] == 75
print(scores)
```

Predict `[60, 75, 80]`, run, get the unchanged `[60, 70, 80]` — `==` compares and the result is thrown away, it
never updates anything. Fix: `scores[1] = 75`.

## 53–65 — Task 1: an AI-results report

Write `ai_report(scores)` — prints the count, the first score, the last score, and whether `100` is among them.
Test on `[81, 24, 67, 91]`.

```text
Number of tests: 4
First score: 81
Last score: 91
Contains perfect score: False
```

## 65–80 — Task 2: a bounds-checked update

Write `update_score(scores, index, new_value)` — if `index` is a valid position, update it and return `True`;
otherwise print `"Invalid index"` and return `False`. Test on `[60, 70, 80]` with index `1` (valid) and index `5`
(invalid).

## 80–90 — Save and exit check

Save As `G8_U7_M1_Lists_<Name>.py`. For `items = ["A", "B", "C"]`:

1. What is `items[1]`?
2. What is `items[-1]`?
3. How do you update `"B"` to `"X"`?
4. What is the last valid index, by `len`?

**Answers:** `"B"`, `"C"`, `items[1] = "X"`, `len(items) - 1`.

### Tool Note – Thonny
The **Variables** view updates live as a list changes — watch it while stepping through `update_score()` to see
exactly which element changes and which stays the same.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| An index equal to the list's length is valid | The last valid index is `len(values) - 1` |
| `values[2]` and `2 in values` ask the same question | One is "what's at position 2," the other is "does 2 appear anywhere" |
| Writing `==` when an update was intended | `=` assigns, `==` compares — and a bare comparison at the top level does nothing useful |
| A list, once created, can't change | Lists are mutable — updating an element in place is normal and expected |
| Checking `"75" in scores` on a list of numbers | Type matters: `"75"` (text) never equals `75` (a number) |

---

# 8. Assessment Evidence (formative)

- The index table filled in both directions before running any code
- The warm-up explained (why nothing changed, not just the one-line fix)
- `ai_report()` producing all four correct lines
- `update_score()` correct for both a valid and an invalid index
- Exit check
