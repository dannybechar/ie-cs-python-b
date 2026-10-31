# יחידה 3.3 – פעולות

כיתה ח׳ · AI + Python B · **משתנה מקומי ומשתנה גלובלי**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> משתנה שנוצר בתוך פעולה חי רק כשהיא רצה. משתנה שמוגדר מחוץ לכל הפעולות אפשר לקרוא מכל פעולה — ואם רוצים **לשנות** אותו מבפנים, חייבים לכתוב `global`.

## דף עזר

```python
score = 0


def add_bonus(bonus):
    global score
    score = score + bonus


def show_square(num):
    result = num ** 2
    print(result)
```

<div dir="rtl">

- `result` ו-`num` הם משתנים **מקומיים**: מחוץ לפעולה פייתון לא מכירה אותם (`NameError`).
- `score` הוא **גלובלי**: קריאה ממנו בתוך פעולה לא דורשת כלום; שינוי דורש `global score` בתחילת הפעולה.
- בלי `global`, השמה כמו `score = 100` בתוך פעולה יוצרת משתנה מקומי חדש.

</div>

## 1. חימום: המונה שלא סופר

פתחו את `Scope_Starter.py`. הריצו וקראו את השגיאה. הוסיפו שורה אחת כדי לתקן.

```python
counter = 0


def do_step():
    counter = counter + 1
    print("Step done!")


do_step()
print("Counter:", counter)
```

פלט צפוי אחרי התיקון: `Step done!` ואחריו `Counter: 1`

## 2. משימה 1: מקומי או גלובלי?

**על הנייר:**

```python
app_name = "Math Quiz"


def show_greeting(user_name):
    welcome_msg = "Hello " + user_name
    print(welcome_msg)
    print("Welcome to " + app_name)
```

<div dir="rtl">

א. איזה משתנה הוא גלובלי?
ב. אילו משתנים מקומיים בפעולה `show_greeting`?
ג. מה יקרה אם נוסיף בסוף התכנית, מחוץ לפעולה, את `print(welcome_msg)`? נמקו.

</div>

```python
score = 50


def update_score():
    score = 100
    print("Inside function:", score)


update_score()
print("Outside function:", score)
```

<div dir="rtl">

ד. מה יודפס? למה הערך של `score` מחוץ לפעולה לא השתנה?

</div>

אחרי שכתבתם תשובות — הריצו ובדקו.

## 3. משימה 2: add_bonus

כתבו תכנית: משתנה גלובלי `total_points` שערכו `0`, ופעולה `add_bonus(bonus)` שמוסיפה את `bonus` ל-`total_points`. זמנו אותה פעמיים עם `10` והדפיסו את `total_points`.

פלט צפוי: `20`

## 4. משימה 3: שני החניונים

<div dir="rtl">

חניון א׳ עולה 20 ש״ח ליום. חניון ב׳: עד 3 שעות — 5 ש״ח; עד 4 שעות — 15 ש״ח; יותר מ-4 שעות — 30 ש״ח.

</div>

כתבו שלוש פעולות: `parking_a()` מחזירה `20`; `parking_b(hours)` מחזירה את המחיר בחניון ב׳; `compare_parking(hours)` מזמנת את שתי הפעולות ומחזירה `"Parking A is cheaper"`, `"Parking B is cheaper"` או `"Same price"`.

בתכנית הראשית הדפיסו את התשובה עבור 2, 4, 10 ו-24 שעות, למשל `print("10 hours:", compare_parking(10))`.

פלט צפוי: חניון ב׳ זול יותר ב-2 שעות וב-4 שעות; חניון א׳ זול יותר ב-10 וב-24 שעות.

## 5. משימה 4: how_many_legs

כתבו `how_many_legs(animal)` שמחזירה את מספר הרגליים: `spider` — 8, `ant` — 6, `dog` או `cat` — 4, `chicken` — 2; כל שם אחר — `-1`. השתמשו ב-`elif`. בתכנית הראשית קלטו שם בעזרת `input` והדפיסו את התוצאה.

## 6. נקודת בקרה: קמפיין תרומות

<div dir="rtl">

בקמפיין לנטיעת עצים כל תורם נותן תרומה. תורם שתרם **יותר** מ-100 ש״ח מקבל תעודת הוקרה.

</div>

הגדירו שני משתנים גלובליים: `sum_of_donations` (מתחיל ב-`0`) ו-`number_of_high_donors` (מתחיל ב-`0`).

כתבו `add_donation(donation)`: היא מוסיפה את התרומה לסכום; אם התרומה גדולה מ-100 היא גם מוסיפה תורם אחד למספר התורמים הגדולים ומדפיסה `Thank you, the certificate is on the way`.

בתכנית הראשית: קלטו את מספר התורמים, ואז קלטו תרומה לכל תורם (בלולאת `for`) וזמנו את `add_donation`. בסוף הדפיסו את שני המשתנים הגלובליים.

דוגמה: שלושה תורמים — `150`, `80`, `200`.

```text
Thank you, the certificate is on the way
Thank you, the certificate is on the way
Total donations: 430
Number of donations above 100 nis: 2
```

בדקו גם תרומה של בדיוק `100`: היא לא נחשבת גדולה.

## 7. אם יש זמן

<div dir="rtl">

- `add_coins(new_coins)` עם משתנה גלובלי `coins = 10`. אחרי `add_coins(5)` ההדפסה: `Total coins: 15`.
- `weight_of_number(number)` — מכפלת שתי הספרות של מספר דו-ספרתי (`75` ← `35`, `12` ← `2`); תכנית שקולטת שני מספרים דו-ספרתיים ומדפיסה את זה שהמכפלה שלו גדולה יותר.
- ארבע פעולות קטנות `add_numbers`, `subtract_numbers`, `multiply_numbers`, `divide_numbers`, שכל אחת מחזירה ערך אחד, ותכנית שקולטת שני מספרים ומדפיסה את ארבע התוצאות.

</div>

## 8. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U3_M3_Scope_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. פעולה מבצעת `total = total + 5` ונכשלת בשגיאה. מה השגיאה, ואיזו שורה אחת מתקנת?
2. משתנה `area` נוצר בתוך `calculate_rectangle`. למה `print(area)` אחרי הזימון מפיל `NameError`?
3. מתי עדיף להעביר ערך כפרמטר ולא להשתמש במשתנה גלובלי?

</div>
