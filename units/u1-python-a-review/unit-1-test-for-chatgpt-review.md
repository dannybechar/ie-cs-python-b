# Request: expert review of a Grade 9 Python test

Paste this whole file into ChatGPT. It contains the request, the test, the answer key and the model solutions.

---

You are an expert Python teacher for high schools (Israeli Grade 9, ages 14–15) with more than 15 years of experience
writing and grading written exams. Please review the attached **60-minute paper test** as a critical colleague.

## Context

- Students finished a short Python course in Grade 7 ("Python A") and a 6-hour review unit: conditions
  (`if`/`elif`/`else`, `and`/`or`/`not`), `for` with `range`, `while`, counters and totals, input validation.
- **Not taught, and must not be required:** lists, tuples, dictionaries, nested loops, functions with parameters or
  `return`, `+=`, `break`, string methods, f-strings.
- The test is on paper, without a computer. The test text is Hebrew; code and program output are English.
- Goal: find out what each student can read, trace, debug and write. It is a diagnostic, not a competition.

## What to check

1. **Correctness.** Run or trace every code snippet and every expected output. Are the answer key, the rubric and
   `Test_Reference.py` correct and consistent with each other and with the test? List every error with its question number.
2. **Coverage and balance.** Does the test fairly cover the stated topics? Is there a good spread of skills
   (trace, debug, write)? Is anything over- or under-weighted?
3. **Difficulty and time.** Can an average student finish in 60 minutes? Estimate the time per question and compare it
   with the suggested split (A 14 / B 8 / C 33 / 5 review). Which questions are too easy or too hard for this level?
4. **Clarity.** Is each question unambiguous? Are there traps that test reading skills rather than Python?
   Is the Hebrew natural and age-appropriate? Will right-to-left text mixed with English code confuse students?
5. **Fairness and rubric.** Is the partial credit sensible? Would two teachers grade the same answer the same way?
   Does the common-error list miss any typical student mistake?
6. **Pedagogy.** Does any question reward memorizing instead of understanding? Would you add or drop a question type
   (for example an off-by-one "predict the output", or "which test value exposes the bug")?

## Answer format

1. **Verdict** — two or three sentences: ready to use, or needs changes.
2. **Errors found** — table: question · problem · suggested fix.
3. **Timing estimate** — table: question · minutes for a strong / average / weaker student.
4. **Suggestions** — a prioritised list (high / medium / low), each with one sentence of reasoning.
5. **A revised version of the weakest question**, written in full in the same style, with its key and rubric.

Be specific and concise. If you are unsure whether something is wrong, say so and explain how to check it.

---

# PART 1 — THE STUDENT TEST (Hebrew)

כיתה ט׳ · AI + Python B · יחידה 1 · **זמן: 60 דקות** · **ניקוד: 100**

שם: ______________________  תאריך: ______________

<div dir="rtl">

**הוראות**

- אין מחשב ואין מחברת.
- קוד כותבים בפייתון בלבד. בשאלות 6–8 אפשר לכתוב פונקציה (`def`) או קוד רגיל.
- תוכנית שאפשר להבין ולעקוב אחריה מקבלת ניקוד גם אם יש בה שגיאת כתיב קטנה (נקודתיים, גרשיים).
- מומלץ: חלק א' – 14 דקות, חלק ב' – 8 דקות, חלק ג' – 33 דקות, ו-5 דקות לבדיקה.

</div>

---

### חלק א' – מה התוכנית מדפיסה? (24 נקודות)

#### שאלה 1 (8 נקודות)

```python
age = int(input("Age: "))
member = input("Member (yes/no): ")
if age < 10:
    print("Child")
elif age < 18 and member == "yes":
    print("Teen member")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

<div dir="rtl">

השלימו את הפלט (הודעה אחת בלבד בכל שורה):

| age | member | פלט |
|---|---|---|
| 7 | no | &nbsp; |
| 15 | yes | &nbsp; |
| 15 | no | &nbsp; |
| 18 | yes | &nbsp; |

</div>

#### שאלה 2 (10 נקודות)

```python
total = 0
count = 0
for i in range(2, 12, 3):
    total = total + i
    if i > 6:
        count = count + 1
print("Total:", total, "Big:", count)
```

<div dir="rtl">

א. (6 נק') השלימו טבלת מעקב. כתבו את הערכים **בסוף** כל סבב.

| i | total | count |
|---|---|---|
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |

ב. (2 נק') כמה סבבים רצה הלולאה? ______

ג. (2 נק') מה מודפס בסוף? ______________________

</div>

#### שאלה 3 (6 נקודות)

```python
x = 20
steps = 0
while x > 3:
    x = x - 6
    steps = steps + 1
print(x, steps)
```

<div dir="rtl">

א. (2 נק') כמה פעמים נבדק התנאי `x > 3`? ______

ב. (4 נק') מה מודפס בסוף? ______________________

</div>

---

### חלק ב' – תיקון וכתיבת טווחים (16 נקודות)

#### שאלה 4 (10 נקודות)

<div dir="rtl">

א. (6 נק') התוכנית אמורה להדפיס את המספרים 1 עד 5 ואחר כך `Done`. יש בה **שתי תקלות**. מצאו אותן ותקנו (אפשר לכתוב על הקוד).

</div>

```python
n = 1
while n < 5:
    print(n)
print("Done")
```

<div dir="rtl">

ב. (4 נק') התוכנית אמורה להדפיס `Access granted` רק לבני 13 עד 15. בן 20 נכנס בטעות. מה הבעיה, ואיך מתקנים?

</div>

```python
age = int(input("Age: "))
if age >= 13 or age <= 15:
    print("Access granted")
```

#### שאלה 5 (6 נקודות)

<div dir="rtl">

א. (2 נק') כתבו שורת `for` שמייצרת את הערכים 1, 2, 3, … 9:

`for i in ______________________:`

ב. (2 נק') כתבו שורת `for` שמייצרת את הערכים 20, 15, 10, 5:

`for i in ______________________:`

ג. (2 נק') לכל מצב כתבו איזו לולאה מתאימה, `for` או `while`, ונמקו במשפט:

1. הדפסת לוח הכפל של 7 (עשר שורות). ______________________
2. לבקש סיסמה עד שהיא נכונה. ______________________

</div>

---

### חלק ג' – כתיבת תוכניות (60 נקודות)

<div dir="rtl">

כתבו כל תוכנית במלואה, כולל קליטת הקלט והדפסה בדיוק כפי שמופיע בשאלה.

</div>

#### שאלה 6 – כרטיס כניסה (18 נקודות)

<div dir="rtl">

כתבו תוכנית שקולטת גיל ומדפיסה **הודעה אחת בלבד**:

- גיל מחוץ לטווח 0 עד 120 ← `Invalid age`
- פחות מ-6 ← `Free`
- 6 עד 17 ← `Student: 20`
- 18 ומעלה ← `Regular: 40`

כתבו גם **חמישה ערכי בדיקה** שיבדקו את כל הגבולות (גיל ← פלט צפוי).

</div>

#### שאלה 7 – ציוני המבחנים (18 נקודות)

<div dir="rtl">

כתבו תוכנית שקולטת **שישה** ציונים, ובסוף מדפיסה:

- `Average:` והממוצע
- `Grades >= 90:` ומספר הציונים שהם 90 ומעלה

עבור הציונים 90, 80, 70, 100, 60, 80 הפלט הוא:

</div>

```
Average: 80.0
Grades >= 90: 2
```

#### שאלה 8 – חיסכון (24 נקודות)

<div dir="rtl">

ילד חוסך למטרה של 100 שקלים, ומפקיד סכום אחד בכל פעם. כתבו תוכנית שקולטת הפקדות **עד שהסכום מגיע ל-100 או עד שבוצעו 5 הפקדות**, המוקדם מביניהם. בסוף מדפיסים:

- הגיע ל-100 או יותר ← `Goal reached after N deposits`
- אחרת ← `Goal not reached. Total: T`

דוגמאות:

| הקלט | הפלט |
|---|---|
| 60, 50 | `Goal reached after 2 deposits` |
| 10, 10, 10, 10, 10 | `Goal not reached. Total: 50` |

חובה להשתמש ב-`while` עם תנאי מורכב אחד. ההפקדה החמישית היא האחרונה – אין הפקדה שישית.

</div>

---

<div dir="rtl">

**בהצלחה!**

</div>

---

# PART 2 — ANSWER KEY AND RUBRIC


Test: [`unit-1-test-he.md`](unit-1-test-he.md) · 60 minutes · 100 points · code: [`Test_Reference.py`](Test_Reference.py)
(every output below was produced by running that file).

**Scope:** only Unit 1 (conditions with `and`/`or`/`not`, `elif`, `for` + `range`, `while`, counters and totals, input
validation). No lists, functions with parameters, `+=`, nested loops or string methods.
**Timing:** A 14 min · B 8 min · C 33 min · 5 min review.
**Grade level:** Grade 9 (students who took Python A and the Unit 1 review). Nothing beyond Python A + Unit 1 is required.

### Part A (24)

**Q1 (8, 2 each):** Child · Teen member · Teen · Adult.

**Q2 (10):** `range(2, 12, 3)` = 2, 5, 8, 11.

| i | total | count |
|---:|---:|---:|
| 2 | 2 | 0 |
| 5 | 7 | 0 |
| 8 | 15 | 1 |
| 11 | 26 | 2 |

(a) 6 pts: 1.5 per row. (b) 2 pts: 4 rounds. (c) 2 pts: `Total: 26 Big: 2`.

**Q3 (6):** (a) 2 pts: 4 checks (x = 20, 14, 8, 2). (b) 4 pts: `2 3` (2 for each value).

### Part B (16)

**Q4a (6):** `n` never changes → add `n = n + 1` inside the loop (3); `n < 5` stops before 5 → `n <= 5` (3).
The fixed program prints 1 2 3 4 5 Done.
**Q4b (4):** `or` lets every age pass; use `and` (`age >= 13 and age <= 15`). 2 for the diagnosis, 2 for the fix.

**Q5 (6, 1 each for the loop / the reason):** (a) `range(1, 10)` · (b) `range(20, 0, -5)` (any stop from 0 to 4 is fine) ·
(c) 1 → `for` (known number of rounds); 2 → `while` (the number of rounds depends on the input).

### Part C (60)

**Q6 (18):** input and `int` (2) · invalid age checked first, or equivalent logic (4) · `elif` chain with exactly one
message (6) · correct boundaries (2) · test values (4: should include −1 or 121, 0 or 5, 6, 17, 18).
Common errors: `age < 0 and age > 120` (never True); testing `age < 6` before validation (−1 gives `Free`);
`if` instead of `elif` (two messages).

**Q7 (18):** total and counter set to 0 **before** the loop (4) · `for` with 6 rounds (3) · `int(input())` inside the loop (2) ·
`total = total + grade` (3) · counter grows only when `grade >= 90` (3) · average computed **after** the loop, divided by 6 (3).
Common errors: `total = grade` (the 1.2 warm-up bug), dividing inside the loop, resetting inside the loop, `range(1, 6)` (5 rounds).

**Q8 (24):** `total` and `deposits` start at 0 (4) · `while total < 100 and deposits < 5` (8; 4 if only one side is right) ·
input and both updates inside the loop (6) · final `if`/`else` decides by the total (4) · both messages correct (2).
The flag style (`success = False`) from 1.3 is accepted if it is consistent.
Check: 60, 50 → `Goal reached after 2 deposits`; 10 ×5 → `Goal not reached. Total: 50`; 30, 40, 30 → `Goal reached after 3 deposits`.
Common errors: `or` instead of `and` (runs too long), no update to `deposits` (never ends when the goal is not reached),
`while total <= 100`.

### Model solutions

[`Test_Reference.py`](Test_Reference.py): `q1`–`q3` and `q4_fixed` (Parts A–B), `ticket()`, `grades()`, `savings()` (Q6–Q8).

### Grading scale (suggestion)

| Points | Meaning |
|---|---|
| 90–100 | Full command of Unit 1 |
| 75–89 | Solid, small slips |
| 56–74 | Basic; revisit `while` and accumulators |
| below 56 | Needs support before Unit 3 (functions) |

---

# PART 3 — MODEL SOLUTIONS (Test_Reference.py)

```python
# Unit 1 test - reference solutions for the teacher (not for students).
# Questions 1-3 are trace questions; the code is shown in the test itself.


def q1(age, member):
    if age < 10:
        print("Child")
    elif age < 18 and member == "yes":
        print("Teen member")
    elif age < 18:
        print("Teen")
    else:
        print("Adult")


def q2():
    total = 0
    count = 0
    for i in range(2, 12, 3):
        total = total + i
        if i > 6:
            count = count + 1
    print("Total:", total, "Big:", count)


def q3():
    x = 20
    steps = 0
    while x > 3:
        x = x - 6
        steps = steps + 1
    print(x, steps)


def q4_fixed():
    n = 1
    while n <= 5:
        print(n)
        n = n + 1
    print("Done")


# Question 6
def ticket():
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    elif age < 6:
        print("Free")
    elif age <= 17:
        print("Student: 20")
    else:
        print("Regular: 40")


# Question 7
def grades():
    total = 0
    excellent = 0
    for i in range(6):
        grade = int(input("Grade: "))
        total = total + grade
        if grade >= 90:
            excellent = excellent + 1
    print("Average:", total / 6)
    print("Grades >= 90:", excellent)


# Question 8
def savings():
    total = 0
    deposits = 0
    while total < 100 and deposits < 5:
        amount = int(input("Deposit: "))
        total = total + amount
        deposits = deposits + 1
    if total >= 100:
        print("Goal reached after", deposits, "deposits")
    else:
        print("Goal not reached. Total:", total)
```
