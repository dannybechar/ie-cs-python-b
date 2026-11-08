# Unit 7.2 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v2 (reworked to the Ministry materials, 8 Nov 2026)
### Topic: List Operations

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **12.0 / 12.1** (the operations summary p. 18 and 13.0 p. 2: `append`, `count`, `index`, `insert`,
`remove`, `reverse`, `sort`, `pop`, `list()`, `join`, `split`; the temperature filter p. 9–10; the palindrome-list exercise pp. 19–23;
`random.choice` p. 34–35; the fruit lists with `join`/`split`, p. 12–15) and worksheet **12.6** (master Python, Q5: duplicate names).
Kept from v1: `extend`, `sort()` returns `None`, copy before sort. **Dropped from v1:** the stand-alone safe-remove and `pop(0)`
task-queue tasks (the behaviour is shown in the demo; `join_class` is the Ministry's duplicate-name task). **New (audit):**
`index()`, `list()`, `random.choice`, the palindrome-list task, the duplicate-name check.
**Ministry bug not copied:** 12.0 p. 10 writes `new_list.append(i)` inside `for item in temperature` (a `NameError`). Used here as the
**warm-up**, deliberately. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3) — tasks are `def` functions that take a list and return a value, as in the Ministry worksheets.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | what a list is; indices; slicing | 45 / 45 |
| **7.2 (this)** | **`append`/`insert`/`extend`, `count`/`index`, `remove`/`pop`, `sort`/`reverse`, new lists in a loop, `split`/`join`, `random.choice`** | 45 / 45 |
| 7.3 | traversal by index and by value; accumulation; the "change while looping" trap | 45 / 45 |
| 7.4 | counting, filters, maximum, flat menus, parallel lists | 0 / 90 |
| 7.5 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 5: `append`, `extend`, `insert`, `remove`, `pop`, `count`, `sort`, `reverse` appropriately | ✅ demo + tasks |
| Goal 6: `split` and `join` | ✅ |
| Goal 8 (start): build a new list from a condition | ✅ Task 1 |
| Goal 12: lists in AI contexts | ✅ names, results |

### Deliberate exclusions
Accumulation and the "remove while looping" trap (7.3). Sorting with a key function, `sorted()`, dictionaries, comprehensions: out of the course.

---

## 3. Lesson Goal

**Every list operation has one job and one exact result: choose `append`/`insert`/`extend` to add, `remove`/`pop` to delete,
`count`/`index` to ask, and remember that `sort`/`reverse` change the list itself and give back `None`.**

---

## 4. Core Mental Models

```python
my_lst = list()          # same as []
my_lst.append(1)         # [1]
my_lst.insert(0, 4)      # [4, 1]  - position first, value second
my_lst.extend([7, 8])    # [4, 1, 7, 8]  - each item added
my_lst.append([7, 8])    # [4, 1, 7, 8, [7, 8]] - ONE item that happens to be a list (shown only as a warning)
```

- `append(x)` adds one item at the end; `insert(position, x)` adds at a position; `extend(items)` adds every item of another list.
- `count(x)` — how many times; `index(x)` — the first position (an error if absent: check `x in values` first).
- `remove(x)` deletes the first item equal to `x`; `pop()` deletes the last and **returns** it; `pop(position)` deletes that position.
- `values.sort()` and `values.reverse()` change the list and return `None`; so `result = values.sort()` leaves `result` empty-handed.
- A **new list** is built with `result = []` before the loop and `result.append(item)` inside it.

Verified demo (`Operations_Reference.py`, function `demo`):

```text
[1, 2, 3]
[4, 1, 2, 3]
[4, 1, 2, 3, 7, 8]
[4, 1, 2, 3, 7, 8, [7, 8]]
2 1                       # letters.count("a"), letters.index("a") on ["c", "a", "d", "a"]
['c', 'd', 'a']           # letters.remove("a") removed the FIRST "a" only
a ['c', 'd']              # last = letters.pop()
c ['d']                   # first = letters.pop(0)
None [10, 20, 30]         # result = numbers.sort() on [30, 10, 20]
[30, 20, 10]              # numbers.reverse()
['c', 'a', 't']           # list("cat")
a-b-c                     # "-".join(["a", "b", "c"])
['a', 'b', 'c']           # "a-b-c".split("-")
```

Errors, exact text on Python 3.14:

```text
[1, 2].index(9)   ValueError: list.index(x): x not in list
[1, 2].remove(9)  ValueError: list.remove(x): x not in list
[].pop()          IndexError: pop from empty list
```

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–4 | Quick recall from 7.1: one prediction on slicing, `[::-1]` and `in` |
| 4–10 | Growing a list: `list()`, `append`, `insert(0, x)`, `extend` vs. `append([...])` |
| 10–15 | `count`, `index`, the `ValueError` and the `in` guard |
| 15–20 | `remove` (first match only), `pop()` / `pop(0)` returning the removed value |
| 20–22 | **Predict (question only):** `result = numbers.sort()` then `print(result)` |
| 22–26 | The answer `None`; `sort`/`reverse` change the list in place; `list("cat")` |
| 26–32 | Building a **new** list in a loop: the temperatures below 21 → `[20, 16]` |
| 32–37 | `split` and `join`: text ⇄ list |
| 37–41 | `random.choice(names)` — a random student |
| 41–45 | The summary table (12.0 p. 18) and the lab missions |

---

# 6. Second 45 Minutes — Lab

Starter: [`Operations_Starter.py`](Operations_Starter.py). Reference: [`Operations_Reference.py`](Operations_Reference.py).

## 45–51 — Warm-up: the `NameError` (the Ministry's own bug)

```python
temperature = [25, 20, 21, 24, 21, 24, 21, 16, 23]
new_list = []
for item in temperature:
    if item < 21:
        new_list.append(i)
print(new_list)
```

Predict `[20, 16]`, run: `NameError: name 'i' is not defined. Did you mean: 'id'?` — the loop variable is `item`; there is no `i`.
Teach reading the message: the last line names the problem, the arrow points at the line. Fix: `append(item)`.

## 51–60 — Task 1: `colder_than(values, limit)`

Returns a **new** list with the values smaller than `limit`. `colder_than(temperature, 21)` → `[20, 16]`; with limit `10` → `[]`.

## 60–70 — Task 2: `join_class(students, name)` (Ministry 12.6 Q5)

If `name` is already in the list, print `We cannot place you in this class` and return `False`; otherwise add it and return `True`.

```text
We cannot place you in this class
False ['Dana', 'Avi', 'Noa']
True ['Dana', 'Avi', 'Noa', 'Lior']
```

## 70–82 — Task 3: `all_palindromes(words)` (Ministry 12.1 p. 20–22)

`True` when every word reads the same backwards, ignoring capital letters (hint: `word[::-1]`, `lower()`).
`["ABA", "1221", "A12321A"]` → `True`; `["ACA", "AcCA"]` → `True` (with the case upgrade); `["ACA", "ACB"]` → `False`.
**Ministry bug not copied:** the 12.0 p. 19–20 solutions leave a stale `print(item, "Is not a palindrome")` in the `else` branch of the
second version, and the strings use curly quotes. Our task returns a value instead of printing.

## 82–87 — Task 4: `split` and `join`, `random.choice`

`to_sentence("One#Apple#a#day#keeps#the#doctor#away")` → `One Apple a day keeps the doctor away`; `random_word(text)` returns one random word.

## 87–90 — Save and exit check

Save As `G8_U7_M2_Operations_<Name>.py`.

1. Which method adds to the end of a list? To a chosen position?
2. What does `pop()` return?
3. What is printed by `result = [3, 1].sort(); print(result)`?
4. How do you avoid the error of `index()` on a missing value?

**Answers:** `append`, `insert(position, value)`; the removed value; `None`; check `value in values` first.

### Tool Note – Thonny
Type each method in the Shell after a list and watch the **Variables** view: `append` changes `my_lst` immediately, a slice does not.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `append` and `extend` are the same | `append([7, 8])` adds one item (a list); `extend([7, 8])` adds two |
| `values = values.sort()` sorts the list | It sorts, then replaces the list with `None` |
| `insert(5)` adds the number 5 | `insert` needs a position **and** a value |
| `remove(x)` removes every `x` | Only the first one |
| `pop()` and `remove()` both take a value | `remove(value)` takes a value, `pop(position)` takes a position and returns the item |
| A variable you never created exists inside the loop | Use exactly the loop variable's name (`item`, not `i`) |

---

# 8. Assessment Evidence (formative)

- The warm-up error message read aloud and fixed
- `colder_than()` returns a new list and leaves the original alone
- `join_class()` correct for a duplicate and a new name
- `all_palindromes()` correct on the three samples
- Exit check
