# יחידה 7.3 – רשימות

כיתה ח׳ · AI + Python B · **מעבר על רשימה וצבירה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> מעבר לפי **אינדקס** (`range(len(values))`) נותן מספר מקום; מעבר לפי **ערך** (`for item in values`) נותן את הערך עצמו. צבירה: `total = 0` לפני הלולאה, עדכון בתוכה, ושימוש בתוצאה אחריה. לא משנים רשימה בזמן שלולאה עוברת עליה.

## דף עזר

```python
def sum_by_index(values):
    total = 0
    for item in range(len(values)):    # item הוא מקום
        total = total + values[item]
    return total


def sum_by_value(values):
    total = 0
    for item in values:                # item הוא ערך
        total = total + item
    return total


copy = values.copy()                   # עותק אמיתי (כמו values[:])
other = values                         # לא עותק! שני שמות לאותה רשימה
```

## 1. חימום: מחיקה בזמן מעבר

פתחו את `Accumulate_Starter.py`.

```python
def remove_even(values):
    for item in values:
        if item % 2 == 0:
            values.remove(item)


numbers = [2, 4, 6, 8, 1]
remove_even(numbers)
print(numbers)
```

חזו מה יודפס. הריצו. עקבו על הדף אחרי הלולאה: איזה מספר "דלגו" עליו, ולמה?

## 2. משימה 1: סכום בשתי דרכים

כתבו `sum_by_index(values)` ו-`sum_by_value(values)`. בתוך כל לולאה הדפיסו את `item` לפני העדכון. בדקו על `[51, 84, 72, 13, 29]`; שתיהן מחזירות 249. מה ההבדל בין מה שהודפס?

## 3. משימה 2: ממוצע

כתבו `calculate_average(values)` שמחזירה את הממוצע, ו-`0` עבור רשימה ריקה. בדקו על `[25.1, 20.0, 21.5, 24.0, 21.4, 24.5, 21.5, 16.0, 23.3]` ועל `[]`.

## 4. משימה 3: הקניות של רוני

רוני קנתה 5 פריטים. כתבו `read_prices(count)` שקולטת `count` מחירים (`float`) לתוך רשימה ומחזירה אותה. מחוץ לפעולה הדפיסו את הרשימה ואת הסכום (בעזרת `sum_by_value`).

```text
Enter price: 400
Enter price: 350
Enter price: 100
Enter price: 250
Enter price: 70
[400.0, 350.0, 100.0, 250.0, 70.0]
total = 1170.0
```

## 5. משימה 4: רשימה חדשה ועותק ממוין

כתבו `without_even(values)` שמחזירה רשימה **חדשה** בלי המספרים הזוגיים, ו-`sorted_copy(values)` שמחזירה עותק ממוין כשהרשימה המקורית נשארת בסדר שלה. בדקו על `[5, 2, 8, 1, 4]` והדפיסו גם את הרשימה המקורית.

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U7_M3_Accumulate_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. ב-`for item in range(len(values))` — מה `item`? ובמעבר `for item in values`?
2. מה ערכו של `total` לפני הלולאה?
3. למה `calculate_average` בודקת רשימה ריקה?
4. למה לא מוחקים איברים מרשימה בתוך `for` על אותה רשימה?

</div>
