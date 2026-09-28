# יחידה 1.1 – חזרה על פייתון א'

כיתה ח׳ · AI + Python B · **מי יכול להיכנס? תנאים מורכבים, elif ובדיקת קלט**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> שרשרת `if` / `elif` / `else` מריצה ענף אחד בלבד — הראשון שהתנאי שלו `True`.

## דף עזר

```python
age = int(input("Age: "))
permission = input("Permission (yes/no): ")
if age >= 13 and age <= 15 and permission == "yes":
    print("Access granted")
elif age < 13 or age > 15:
    print("Age out of range")
else:
    print("Permission required")
```

<div dir="rtl">

- הפעולה `input()` מחזירה טקסט. למספר ממירים עם `int()`.
- הסימן `=` שומר ערך, והסימן `==` משווה.
- `and` — כל החלקים `True`. `or` — מספיק חלק אחד. `not` — הופך `True` ל-`False`.
- טווח כותבים עם המשתנה פעמיים: `age >= 13 and age <= 15`.
- בודקים קלט לא תקין קודם, ורק אחר כך את שאר המקרים.

</div>

## 1. חימום: המחיר שקורס

פתחו את `Entry_Starter.py`. ילדים מתחת לגיל 12 משלמים 8 לכרטיס, וכל השאר 12.

```python
def ticket_price():
    age = input("Age: ")
    tickets = int(input("Tickets: "))
    if age < 12:
        price = 8
    else:
        price = 12
    print("Total:", tickets * price)
```

הריצו עם גיל 10 ו-2 כרטיסים. קראו את הודעת השגיאה ותקנו שורה אחת. בדקו שוב: 10 ו-2, ואחר כך 12 ו-3.

## 2. משימה 1: השער של המועדון

בפונקציה `fix_the_gate()` יש שתי תקלות.

```python
def fix_the_gate():
    age = int(input("Age: "))
    permission = input("Permission (yes/no): ")
    if age >= 13 or age <= 15:
        if permission == yes:
            print("Access granted")
```

הריצו עם גיל 20 ו-`yes`. תקנו את התקלה הראשונה והריצו שוב עם אותו קלט. האם בן 20 צריך להיכנס? תקנו גם את התקלה השנייה.

## 3. משימה 2: בודק כניסה

כתבו פונקציה בשם `entry_check()` שקולטת גיל ותשובה לשאלה אם יש אישור, ומדפיסה הודעה אחת בלבד:

<div dir="rtl">

- `Access granted` — גיל 13 עד 15, עם אישור.
- `Age out of range` — גיל מחוץ לטווח.
- `Permission required` — גיל בטווח, בלי אישור.

</div>

בדקו את כל המקרים בטבלה:

<div dir="rtl">

| גיל | אישור | פלט |
|---|---|---|
| 14 | yes | &nbsp; |
| 14 | no | &nbsp; |
| 12 | yes | &nbsp; |
| 16 | yes | &nbsp; |
| 13 | yes | &nbsp; |
| 15 | yes | &nbsp; |

</div>

## 4. משימה 3: רמת הציון

כתבו פונקציה בשם `score_level()` שקולטת ציון. קודם בודקים שהציון תקין:

<div dir="rtl">

- מחוץ לטווח 0 עד 100 ← `Invalid score`
- 90 ומעלה ← `Excellent`
- 70 ומעלה ← `Good`
- אחרת ← `Keep practicing`

</div>

בדקו עם מינוס 5, 101, 100, 90, 89, 70, 69 ו-0.

## 5. אם נשאר זמן

כתבו פונקציה בשם `club_open()`. המועדון פתוח בימים 1 עד 5, אבל לא בחג. השתמשו ב-`not`:

```python
is_holiday = input("Holiday (yes/no): ") == "yes"
```

בדקו: יום 3 בלי חג, יום 3 בחג, יום 6 בלי חג.

## 6. מתעדים ושומרים

מעל כל פונקציה — הערה. רק זימון אחד פעיל.

שומרים: `File › Save As` ← `G8_U1_M1_Entry_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. כתבו תנאי אחד שהוא `True` רק כאשר `number` בין 10 ל-20 ואינו 15.
2. בפונקציה `score_level()` הציון הוא 95. למה מודפס `Excellent` ולא גם `Good`?
3. מה מחזירה הפעולה `input()`, ואיך מקבלים ממנה מספר?

</div>
