# יחידה 1.2 – חזרה על פייתון א'

כיתה ח׳ · AI + Python B · **סופרים סבבים: for, range ומנתח חמשת הציונים**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> הערך stop לא נכלל אף פעם ב-`range`. מונה גדל רק כשהתנאי `True`; סכום גדל בכל סבב.

## דף עזר

```python
total = 0
above = 0
for i in range(5):
    score = int(input("Score: "))
    total = total + score
    if score >= 80:
        above = above + 1
print("Average:", total / 5)
print("Scores >= 80:", above)
```

<div dir="rtl">

| תבנית | דוגמה | ערכים |
|---|---|---|
| `range(stop)` | `range(4)` | 0, 1, 2, 3 |
| `range(start, stop)` | `range(2, 6)` | 2, 3, 4, 5 |
| `range(start, stop, step)` | `range(10, 3, -2)` | 10, 8, 6, 4 |

</div>

<div dir="rtl">

- את הסכום ואת המונה מאפסים לפני הלולאה.
- את הממוצע מחשבים אחרי הלולאה.

</div>

## 1. חימום: הסכום ששוכח

פתחו את `Scores_Starter.py`.

```python
def sum_five():
    total = 0
    for day in range(1, 6):
        score = int(input("Score: "))
        total = score
    print("Total:", total)
```

חזו מה יודפס עבור 1, 2, 3, 4, 5. הריצו, ותקנו שורה אחת כדי לקבל 15.

## 2. משימה 1: ספירה לאחור וזוגיים

כתבו שתי פונקציות, עם לולאת `for` אחת בכל אחת:

<div dir="rtl">

- `countdown()` — מדפיסה 10, 9, … 1, ואחר כך `Go!`
- `evens()` — מדפיסה 2, 4, 6 … 20

</div>

כתבו את ה-`range` על דף לפני שאתם מקלידים.

## 3. משימה 2: טבלת מעקב

הפונקציה `trace_me()` כבר כתובה. הקלט: 80, 70, 100. מלאו את הטבלה **לפני** שמריצים:

<div dir="rtl">

| i | score | total | high |
|---|---|---|---|
| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; | &nbsp; |

</div>

עכשיו הריצו והשוו.

## 4. משימה 3: מנתח חמשת הציונים

כתבו פונקציה בשם `five_scores()` שקולטת חמישה ציונים ומדפיסה את הממוצע ואת מספר הציונים שהם 80 ומעלה.

בדקו:

<div dir="rtl">

| ציונים | Average | Scores >= 80 |
|---|---|---|
| 80, 70, 100, 60, 90 | &nbsp; | &nbsp; |
| 0, 0, 0, 0, 0 | &nbsp; | &nbsp; |
| 80, 80, 80, 80, 80 | &nbsp; | &nbsp; |
| 79, 81, 90, 50, 65 | &nbsp; | &nbsp; |

</div>

## 5. אם נשאר זמן

כתבו פונקציה בשם `sevens()` שסופרת כמה מספרים בין 1 ל-100 מתחלקים ב-7. רמז: `n % 7 == 0`.

## 6. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G8_U1_M2_Scores_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. כתבו `range` שמייצר את 10, 8, 6, 4.
2. כמה סבבים תרוץ הלולאה `for i in range(2, 12, 3)`?
3. בפונקציה `five_scores()` — איזה משתנה גדל בכל סבב, ואיזה רק לפעמים?

</div>
