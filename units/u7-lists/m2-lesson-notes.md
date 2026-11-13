# Unit 7.2 — Lists

## Grade 8 / AI + Python B · Lesson Strategy v3 (reconciled to the official lists part A, 9 Nov 2026)
### Topic: List Operations

**Status:** 🔶 Reworked, awaiting teacher approval (the v1 build was approved before the Ministry files arrived)
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** Ministry **9.1** (part A, deck pp. 9–37: `len`, `count`, `in`, `index`, `remove`, `pop`, `append`, `insert`,
`sort`, `reverse`, `list(text)`, `split`, `join`; pp. 38–40 the **Sandwich** challenge; pp. 42–43 and the printable **help sheet** — the
13-row operations table with "returned" and "list after" columns), **9.3** (the guided "even list" exercise), **12.0 / 12.1** (the
temperature filter pp. 9–10, fruit lists with `join`/`split` pp. 12–15, the colour cycle `colors[item % 4]` p. 16, palindromes pp. 19–23,
name occurrence p. 24, name letters p. 23, `random.choice` pp. 34–36) and **12.7** (summary). Kept from v1: `extend`, `sort()` returns
`None`, copy before sort. **Dropped from v1:** the stand-alone safe-remove and `pop(0)` task-queue tasks, and the `append([7, 8])` demo
(it puts a list inside a list — see below); `join_class` (the duplicate-name check, Ministry 12.6 Q5 and 13.2 #1) moved to 7.3.
**Ministry bug not copied:** 12.0 p. 10 writes `new_list.append(i)` inside `for item in temperature` (a `NameError`). Used here as the
**warm-up**, deliberately. Also not copied: 9.1 p. 14 shows the old error text `'Dog' is not in list` (Python 3.14 says
`list.index(x): x not in list`); 9.1 p. 17 "the default is -1" is garbled (it means that `pop()` with no argument takes the **last** item);
9.1 p. 23 feeds `index = input()` straight into `insert` (a `TypeError`, no `int()`); 9.1 pp. 35–36 word `text.join(list)` backwards (the
**separator** is the object: `"@".join(lst)`); 12.0 p. 12 names a variable `str`, hiding the built-in; curly quotes and stray `))` on
12.1 pp. 12, 19, 31–32. See [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md).
**Official items deliberately left out (rulebook):** the Turtle colour list of 12.0 p. 17 (`turtle.Turtle()`, `wn.mainloop()`) — only the
`colors[item % 4]` text version is used; `sort(key=...)` / `sorted(key=...)` of the exam help sheet.
**Links only (not offline):** 9.2 (genially matching game, "Practice for cracking") and the 9.3 solution video — titles in the unit README.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.
**Prerequisite:** functions (Unit 3) — tasks are `def` functions that take a list and return a value, as in the Ministry worksheets.

---

## 1. Position in Unit 7

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 7.1 | what a list is; indices; slicing | 45 / 45 |
| **7.2 (this)** | **the 13 operations: `append`/`insert`, `count`/`in`/`index`, `remove`/`pop`, `sort`/`reverse`, `list(text)`, `split`/`join`, `random.choice`** | 45 / 45 |
| 7.3 | traversal by index and by value; accumulation; the "change while looping" trap | 45 / 45 |
| 7.4 | counting, filters, maximum, flat menus, parallel lists | 0 / 90 |
| 7.5 | linear search, phone numbers, the "AI Experiment Analyzer" | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 17) | Covered here |
|---|---|
| Goal 5: `append`, `extend`, `insert`, `remove`, `pop`, `count`, `sort`, `reverse` appropriately | ✅ demo + tasks |
| Goal 6: `split` and `join` | ✅ demo, Sandwich |
| Goal 8 (start): build a new list from a condition | ✅ Task 1 |
| Goal 12: lists in AI contexts | ✅ names, results |

### Deliberate exclusions
Accumulation and the "remove while looping" trap (7.3). Sorting with a key function, `sorted()`, dictionaries, comprehensions: out of the course.
`append([7, 8])` (a list inside a list): not shown — `extend` is contrasted with `append` of a single value instead.

---

## 3. Lesson Goal

**Every list operation has one job and one exact result: choose `append`/`insert` to add, `remove`/`pop` to delete,
`count`/`in`/`index` to ask, and remember that `sort`/`reverse` change the list itself and give back `None`.**

---

## 4. Core Mental Models

```python
my_lst = list()          # same as []
my_lst.append(1)         # [1]
my_lst.insert(0, 4)      # [4, 1]  - position first, value second
my_lst.extend([7, 8])    # [4, 1, 7, 8]  - each item of the other list is added
```

- `append(x)` adds one item at the end; `insert(position, x)` adds at a position (position first!); `extend(items)` adds every item of another list.
- `count(x)` — how many times; `index(x)` — the **first** position (an error if absent: check `x in values` first). All of them tell `"cat"` from `"Cat"`.
- `remove(x)` deletes the **first** item equal to `x`; `pop()` deletes the last and **returns** it; `pop(position)` deletes that position and returns it.
- `values.sort()` and `values.reverse()` change the list and return `None`; `reverse()` is **not** a sort; `sort(reverse=True)` sorts downwards.
- `list("I love python")` keeps the spaces as items; `"a b  c".split()` splits on any run of spaces (the default); `"@".join(lst)` puts the **separator** first.
- A **new list** is built with `result = []` before the loop and `result.append(item)` inside it.
- `input()` always returns text: appending it keeps `"44"`, not `44`.

Verified demo (`Operations_Reference.py`, function `demo`):

```text
[1, 2, 3]
[4, 1, 2, 3]
[4, 1, 2, 3, 7, 8]
4 0 0                     # animals.count("Giraffe"), .count("Dog"), .count("cat")   (the list has "Cat")
False True                # "giraffe" in animals, "Giraffe" in animals
0                         # animals.index("Giraffe"): the FIRST one
[...]                     # animals.remove("Giraffe") removed only the first "Giraffe"
Giraffe [...]             # last = animals.pop()
Lion [...]                # first = animals.pop(0)
None [10, 20, 30]         # result = numbers.sort() on [30, 10, 20]
[30, 20, 10]              # numbers.sort(reverse=True)
[3, 9, 2, 5, 1]           # [1, 5, 2, 9, 3].reverse()  - not sorted!
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
['a', 'b', 'c']           # "a-b-c".split("-")  and  "a b  c".split()
guitar@piano@drums        # "@".join(["guitar", "piano", "drums"])
```

The colour cycle (12.0 p. 16): `colors[item % 4]` with `end="\t"` prints `red 0`, `blue 1`, `green 2`, `yellow 3`, `red 4`, `blue 5` …

Errors, exact text on Python 3.14:

```text
[1, 2].index(9)   ValueError: list.index(x): x not in list
[1, 2].remove(9)  ValueError: list.remove(x): x not in list
[1, 2].pop(12)    IndexError: pop index out of range
[].pop()          IndexError: pop from empty list
```

The 13-row table (9.1 pp. 42–43 and the help sheet; also in the lab brief, to print and keep). Every row was run (`table_demo`):

| Operation | Returns | List after |
|---|---|---|
| `len([1,2,3])` | `3` | unchanged |
| `[1,2,2,3].count(2)` | `2` | unchanged |
| `2 in [1,2,3]` | `True` | unchanged |
| `[1,2,3].index(2)` | `1` | unchanged |
| `[1,2,3,2].remove(2)` | `None` | `[1, 3, 2]` |
| `[1,2,3].pop(0)` | `1` | `[2, 3]` |
| `[1,2].append(3)` | `None` | `[1, 2, 3]` |
| `[1,3].insert(1,2)` | `None` | `[1, 2, 3]` |
| `[3,1,2].sort()` | `None` | `[1, 2, 3]` |
| `[1,2,3].reverse()` | `None` | `[3, 2, 1]` |
| `list("abc")` | `['a', 'b', 'c']` | a new list |
| `"?".join(["a","b","c"])` | `"a?b?c"` | unchanged |
| `"a?b?c".split("?")` | `['a', 'b', 'c']` | (acts on a string) |

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–3 | Quick recall from 7.1: one prediction on slicing, `[::-1]` and `in` |
| 3–8 | Growing a list: `list()`, `append` (and `append(input(...))` in a loop: the values stay text), `insert(0, x)` (position first), `extend` |
| 8–14 | `count` and `in` (case-sensitive: `"cat"` is not `"Cat"`), `index` (the first match only), the `ValueError` and the `in` guard |
| 14–20 | `remove` (first match only; try to remove it twice), `pop()` / `pop(0)` returning the removed value, the `IndexError` |
| 20–22 | **Predict (question only):** `result = numbers.sort()` then `print(result)` |
| 22–28 | The answer `None`; `sort()` and `sort(reverse=True)`; `reverse()` is **not** a sort; `list("I love python")` keeps the spaces |
| 28–35 | `split` (the separator is not part of the list, the default is a space) and `join` (the separator goes first), on `"guitar#piano#drums#trumpet#saxophone"` |
| 35–38 | **Predict (question only):** `colors[item % 4]` for `range(20)` (12.0 p. 16); `random.choice(names)` — a random student |
| 38–42 | The 13-row table: which rows return `None`? Which leave the list unchanged? (hand out the page) |
| 42–45 | Lab missions: the Sandwich challenge is announced |

---

# 6. Second 45 Minutes — Lab

Starter: [`Operations_Starter.py`](Operations_Starter.py). Reference: [`Operations_Reference.py`](Operations_Reference.py).

## 45–49 — Warm-up: the `NameError` (the Ministry's own bug)

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

## 49–54 — Task 1: `colder_than(values, limit)`

Returns a **new** list with the values smaller than `limit`. `colder_than(temperature, 21)` → `[20, 16]`; with limit `10` → `[]`.

## 54–60 — Task 2: `name_check(names, name)` (Ministry 12.1 p. 24)

If the name is in the list, print how many times it appears; otherwise add it. On `["Dana", "Avi", "Dana", "Noa"]` with `"Dana"`, `"dana"`, `"Lior"`:

```text
Dana appears 2 times
dana was added
Lior was added
['Dana', 'Avi', 'Dana', 'Noa', 'dana', 'Lior']
```

The point: `"Dana"` and `"dana"` are different values.

## 60–67 — Task 3: `all_palindromes(words)` (Ministry 12.1 pp. 19–23)

`True` when every word reads the same backwards, ignoring capital letters (hint: `word[::-1]`, `lower()`).
`["ABA", "1221", "A12321A"]` → `True`; `["ACA", "AcCA"]` → `True` (with the case upgrade); `["ACA", "ACB"]` → `False`.
**Ministry bug not copied:** the 12.0 p. 19–20 solutions leave a stale `print(item, "Is not a palindrome")` in the `else` branch of the
second version, and the strings use curly quotes. Our task returns a value instead of printing.

## 67–77 — Task 4: the Sandwich challenge (Ministry 9.1 pp. 38–40)

`sandwich(text)` returns a new text with only the words whose first and last letter are the same; **`split` and `join` are required, `+` is forbidden**.
`sandwich("anna told bob he won level two!")` → `anna bob level`. (A one-letter word such as `a` qualifies: its first and last letter are the same.
We split with `text.split()`, which also survives a double space; the Ministry's text says the words are separated by one space.) The Ministry has a solution
video (link only); ours is `sandwich` in `Operations_Reference.py`.

## 77–83 — Task 5: the even list (Ministry 9.3, guided exercise)

`even_list(values)` is `True` when the length is even **and** the first half equals the second half: `["A", "b", "c", "A", "b", "c"]` → `True`,
`[1, 2, 3]` → `False`, `[1, 2, 3, 1, 2, 4]` → `False`. Slices do the work: `values[:half] == values[half:]`. (The empty list gives `True`: say so
if a student asks.) The 9.3 solution video is a link only.

## 83–86 — If time

(a) `same_initials(names)` (12.0 p. 23): first and last names in pairs; the sample list gives `3` (`chen`/`Cohen`, `dana`/`dikla`, `Carmi`/`Cohen`); a loop `for index in range(0, len(names), 2)`.
(b) `to_sentence`, `random_word` (12.1 pp. 34–36) and the "Great match" `ord` check (12.1 p. 36: two random letters, `(ord + ord) % 7 == 0`).
The `songs.sort()` and bug-severity counting exercises (12.1 pp. 39–40) are used in 7.4.

## 86–90 — Save and exit check

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
| `append` and `extend` are the same | `append(7)` adds one item; `extend([7, 8])` adds two |
| `values = values.sort()` sorts the list | It sorts, then replaces the list with `None` |
| `reverse()` sorts downwards | It only flips the order; `sort(reverse=True)` sorts |
| `insert(5)` adds the number 5 | `insert` needs a position **and** a value, position first |
| `remove(x)` removes every `x` | Only the first one |
| `pop()` and `remove()` both take a value | `remove(value)` takes a value, `pop(position)` takes a position and returns the item |
| `"Dana"` and `"dana"` are the same name | Every comparison tells capital and small letters apart |
| `input()` into a list gives numbers | It gives text (`"44"`); convert with `int()` first |
| A variable you never created exists inside the loop | Use exactly the loop variable's name (`item`, not `i`) |

---

# 8. Assessment Evidence (formative)

- The warm-up error message read aloud and fixed
- `colder_than()` returns a new list and leaves the original alone
- `name_check()` correct for a present, a differently-capitalised and a new name
- `all_palindromes()` correct on the three samples
- `sandwich()` gives `anna bob level` using `split` and `join` and no `+`
- `even_list()` correct on the three samples
- Exit check
