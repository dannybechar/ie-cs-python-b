# Unit 5.2 — Strings

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: Slicing and Searching — `[start:end:jump]`, `count`, `replace`, `in`, `find`

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny
**Source of inspiration:** the Ministry's teaching materials ([`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)):
deck **7.1** slides 14–28 (slicing with `start`, `end`, `jump`; `count`; `replace` with and without a count; `in`; `find`)
and worksheet **7.2** questions 5–11, 13, 15 (the slicing tables, `mississippi`, `replace`, `in`, `find`). **Changed from the
previous version:** the old 5.2 was a 90-minute slicing lab with `mask_id`; slicing is now a 45-minute theory block plus
practice, and `count`, `replace`, `in`, `find` are taught here as in the Ministry deck. The slice-the-title, `last_ten`
and `mask_id` tasks are gone. The Ministry shows the slicing picture of `"think big be bold show your color"`; its printed
outputs were all re-run (e.g. `text[4:25:4]` is `"kg doo"`).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny**.

---

## 1. Position in Unit 5

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 5.1 | what a string is, indices (+/−), `len`, `+`, `*`, `int`/`str` | 45 / 45 |
| **5.2 (this)** | **slicing `[start:end:jump]`, `count`, `replace`, `in`, `find`** | 45 / 45 |
| 5.3 | `lower`/`upper`, `startswith`/`endswith`, `isalpha`/`isdigit`, `for` over a string | 0 / 90 |
| 5.4 | exercises 4–7, `ord`/`chr` cipher, `split`/`join` (shown), worksheet 8.2, unit checkpoint | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 13–14) | Covered here |
|---|---|
| Goal 2: the operator `in` | ✅ |
| Goal 5: slicing of the form `[start:end:step]` (the Ministry calls the third part *jump*) | ✅ |
| Goal 6 (part): `find`, `count`, `replace` | ✅ |
| Goal 8 (start): searching and counting | ✅ `count_the`, `looks_like_email` |

### Deliberate exclusions
`startswith`/`endswith`, `isalpha`/`isdigit` (5.3); `lower`/`upper` appear here only as the tool for the recap and for `has_yes` (their full lesson, with the Ministry's examples, is 5.3); loops (5.3); `index()` from worksheet Q16 (it is the
same as `find` but raises `ValueError` when nothing is found — mentioned in one sentence, not practised).

---

## 3. Lesson Goal

**`text[start:end:jump]` cuts a piece out of a string (the `end` place is not included); `count`, `replace`, `in` and `find`
look inside a string — and none of them changes the original: each returns something new.**

---

## 4. Core Mental Models

```python
text = "think big be bold show your color"
print(text[3:])        # nk big be bold show your color
print(text[:4])        # thin          - places 0,1,2,3 (not 4)
print(text[5:12:2])    # " i e"        - places 5,7,9,11 (the 12 is not included)
print(text[-5:])       # color
print(text[::2])       # tikbgb odso orclr
print(text[::-1])      # a negative jump walks backwards
```

```python
title = "strings are sequences"
title.upper()           # a new string is returned ... and thrown away
print(title)            # strings are sequences
title = title.upper()   # keep it by assigning
```

- The length of a simple slice is `end - start`; a missing `start` means "from the beginning", a missing `end` "to the end".
- `count` does not count overlapping matches: `"aaaa".count("aa")` is `2`, `"banana".count("ana")` is `1`.
- `find` gives the place of the **first** match, or `-1`. Test for `-1` before using the number to cut.
- `in` says only `True`/`False`; it is case-sensitive: `"yes" in "YES"` is `False`.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–5 | **Recap + a surprise:** `upper()` and `lower()` in one line each (they return the text in capitals / small letters), then predict `title.upper()` followed by `print(title)` (unchanged). One sentence: strings can't be changed; operations give back a new string |
| 5–19 | **Slicing** (7.1 slides 14–17): the board shows `"think big be bold show your color"` with both numberings. Demo `text[3:]`, `text[:4]`, `text[5:12:2]`; then **predict, then run:** `text[10:16]`, `text[10:18]`, `text[-5:]`, `text[-23:-15]`, `text[::2]`, `text[4:25:4]`. Two minutes on "how many characters?" (`end - start`) and the reversed string `text[::-1]` |
| 19–26 | **`count`** (slide 18): `"I love bananas, banana are my favorite fruit".count("banana")` is `2`. Students copy the code and update the print line: `print(f"banana in text is : {x}")`. How many times is `"an"` in `"banana"`? (2) and `"ana"`? (1 — no overlap) |
| 26–33 | **`replace(old, new)` and `replace(old, new, count)`** (slides 20–23): `text.replace("day", "DAY", 2)`; the original is unchanged — compare `print(text)` before and after |
| 33–38 | **`in`** (slide 25): `"win" in "sometimes you win sometimes you learn"` is `True`, `"lose" in …` is `False`; `"x" in "jerusalem"`; `"2" in str(12345)` |
| 38–45 | **`find`** (slides 26–27 and worksheet Q11): on `"sometimes you win sometimes you learn"` — `find("win")` is `14`, `find("lose")` is `-1`, `find("some")` is `0` (why 0?), `find("some", 1)` is `18`. One sentence on `index()` (like `find`, but an error when missing) |

---

# 6. Second 45 Minutes — Lab

Starter: [`Slicing_Starter.py`](Slicing_Starter.py). Reference: [`Slicing_Reference.py`](Slicing_Reference.py).

## 45–50 — Warm-up: the method that changed nothing

```python
title = "strings are sequences"
title.upper()
print(title)
```

Predict, run: still lower case. Fix: `title = title.upper()`. (A real, very common mistake — it comes up again with `replace`.)

## 50–58 — Task 1: write the slice (worksheet 7.2 Q5–6)

For `text = "I like to play drums"` print `drums` (`text[-5:]`), `to play` (`text[7:14]`), `Ikoar` (`text[::4]`). For
`number = "345124987"` (a string!) print `124` (`[3:6]`), `49` (`[-4:-2]`), `4512` (`[1:5]`), `987` (`[6:]`). Any slice that
gives the same output is correct — compare the different answers in the room.

## 58–66 — Task 2: `count_the(text)` (worksheet Q15)

Return how many times the characters `the` appear. `"the other theme is there"` → `4`. Then run `"aaaa".count("aa")`
and explain the `2`.

## 66–74 — Task 3: `replace_first_three(text)` (worksheet Q9)

Replace the character `|` with the two letters `we`, only in the first three places. `"a|b|c|d|e"` → `"awebwecwed|e"`.

## 74–82 — Task 4: `has_yes(text)` (worksheet Q13)

Return `True` when the text contains `yes` in any letter case. `"Maybe YES maybe no"` → `True`; `"no way"` → `False`.

## 82–87 — If time: `looks_like_email(address)` (worksheet Q10b)

`True` when the text has an `@` **and** a `.` somewhere after it. `"dana@school.org"` → `True`; `"dana@school"` and `"dana.school"` →
`False`. Use `find` and its start position. (A real check would be much stricter — a program can verify the *shape* of an
address, never that it exists or that a person owns it.)

## 87–90 — Save and exit check

Save As `G8_U5_M2_Slicing_<Name>.py`. For `text = "think big"`, write what each line prints:

1. `text[:5]`
2. `text[-3:]`
3. `text.find("big")`
4. `text.replace("big", "small")`, and then `text` itself

**Answers:** `think`, `big`, `6`, `think small` — and `think big` (unchanged).

### Tool Note – Thonny
Type slices in the **Shell** first (`text[5:12:2]`): the result appears at once, with its quotes, so a stray space shows up.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| `text[2:5]` includes place 5 | The end place is never included — the slice has `end - start` characters |
| `replace`/`upper` change the variable | They return a new string; assign it or print it |
| `count` finds overlapping matches | It does not: `"aaaa".count("aa")` is 2 |
| `find` returns `True`/`False` | It returns a place, or `-1`; `in` is the one that returns `True`/`False` |
| `in` ignores letter case | It is case-sensitive — normalise with `lower()` (5.3 completes the picture) |
| A digit string is a number | `"345124987"[0:3]` is the string `"345"` |

---

# 8. Assessment Evidence (formative)

- The slicing predictions written before running
- The warm-up explained, not only fixed
- `count_the`, `replace_first_three`, `has_yes` passing their test inputs
- Exit check
