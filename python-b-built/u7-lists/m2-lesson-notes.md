# Unit 7.2 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: List Operations

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** `python_b_unit07_lists_complete_unit.md`, meeting 2 — its own clock table, the
append/extend/insert examples (with the append-a-list-as-one-item pitfall), the remove/pop examples (with the
check-before-remove pattern), the sort/reverse examples (with the `sort()`-returns-`None` pitfall), the split/join
example, the step-by-step trace drill, the task-queue challenge and the exit card kept nearly unchanged.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | a list as an ordered, dynamic collection; indices; traversal | 45 / 45 |
| **7.2 (this)** | **list operations: append/extend/insert, remove/pop, sort/reverse, split/join** | 45 / 45 |
| 7.3 | advanced operations + the accumulation pattern | 45 / 45 |
| 7.4 | counting, minimum, maximum, a report | 0 / 90 |
| 7.5 | linear search + the "AI Experiment Analyzer" checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 5: `append`, `extend`, `insert`, `remove`, `pop`, `count`, `sort`, `reverse` | ✅ every task |
| Goal 6: `split` (text → list) and `join` (list → text) | ✅ Task 3 |

### Deliberate exclusions
The accumulation pattern (7.3), any list-modification-during-traversal pitfall (7.3), search (7.5).

---

## 3. Lesson Goal

**Choose `append` for one item, `extend` for several, `insert` for a position; `remove` deletes by value, `pop`
deletes by index and returns what it removed; `sort`/`reverse` change the list in place and return `None`.**

---

## 4. Core Mental Models

```python
tasks = ["study", "exercise"]
tasks.append("rest")               # one item added
tasks.extend(["read", "sleep"])      # each item of the collection added separately
tasks.insert(1, "eat")                # inserted at position 1
```

```python
values = [1, 2]
values.append([3, 4])
print(values)   # [1, 2, [3, 4]] - one list added as a single item, not two numbers
```

```python
scores = [72, 95, 61]
ordered = scores.sort()   # sorts scores in place - and returns None
print(ordered)              # None - a very common surprise
```

- `remove(value)` deletes the first match by **value**; check `value in items` first, or it raises `ValueError`.
- `pop(index)` deletes by **position** and **returns** the removed item — useful when you need that value.
- `text.split(sep)` is a **string** method that returns a list; `sep.join(list_of_strings)` is a **string** method
  (called on the separator) that returns text.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** creating a list, indexing, updating |
| 8–24 | Adding: `append`, `extend`, `insert` — and the `append([3, 4])` pitfall (one item, not two) |
| 24–33 | Removing: `remove` (by value, with a check-first pattern) vs. `pop` (by index, returns the value) |
| 33–41 | Sorting and reversing in place; the `ordered = scores.sort()` pitfall and its fix with `.copy()` |
| 41–45 | `split` / `join`: `"cat,dog,bird".split(",")` → the list; `" | ".join(...)` → back to text |

---

# 6. Second 45 Minutes — Lab

Starter: [`Operations_Starter.py`](Operations_Starter.py). Reference: [`Operations_Reference.py`](Operations_Reference.py).

## 45–53 — Warm-up: sorted, but into nothing

```python
scores = [72, 95, 61]
ordered = scores.sort()
print(ordered)
```

Predict a sorted list, run, get `None` — `sort()` sorts `scores` in place and returns `None`, nothing to store. Fix:
copy first, then sort the copy: `ordered = scores.copy(); ordered.sort()`.

## 53–63 — Task 1: `safe_remove(items, target)`

Checks `target in items` before removing; if present, removes it and returns `True`, otherwise prints
`"Task not found"` and returns `False`. Test on `["study", "exercise"]` with `"exercise"` and with `"rest"`.

## 63–74 — Task 2: `process_queue(tasks)`

While the list isn't empty, `pop(0)` the first task and print `"Working on: <task>"`. Test on
`["collect data", "run model", "check result"]`.

```text
Working on: collect data
Working on: run model
Working on: check result
```

## 74–83 — Task 3: `csv_round_trip(text)`

Splits `text` on `","` and rejoins the pieces with `" | "`. Test on `"cat,dog,bird"` → `"cat | dog | bird"`.

## 83–90 — Save and exit check

Save As `G8_U7_M2_Operations_<Name>.py`. Match each operation to its purpose:

1. Add one item at the end
2. Add several items at the end
3. Delete by value
4. Take out by index and return the value
5. Sort in place

**Answers:** `append`, `extend`, `remove`, `pop`, `sort`.

### Tool Note – Thonny
Step through `process_queue()` in the debugger and watch the **Variables** view — `tasks` visibly shrinks by one
element each time `pop(0)` runs.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `append` and `extend` are interchangeable | `append` adds one item (even a whole list, as one item); `extend` adds each item of a collection separately |
| `sort()` returns a new sorted list | It sorts in place and returns `None` — copy first if the original order is also needed |
| `remove` and `pop` both take an index | `remove` takes a **value**; `pop` takes an **index** |
| `remove` on a missing value just does nothing | It raises `ValueError` — check `in` first |
| `join` works on a list of any type | Every item must already be a string |

---

# 8. Assessment Evidence (formative)

- The `append`/`extend` pitfall explained in the student's own words
- The warm-up's `None` explained (not just the copy-first fix applied)
- `safe_remove()`, `process_queue()`, `csv_round_trip()` all passing their tests
- Exit check
