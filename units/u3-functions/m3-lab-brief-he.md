# יחידה 3.3 – פעולות

כיתה ח׳ · AI + Python B · **ערך חוזר וטווח הכרה — בדיקת סיום היחידה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `print` מציגה ערך על המסך. `return` מחזירה ערך לשורת הזימון — רק ערך שחוזר אפשר לשמור, להשוות או לשלב בחישוב נוסף.

## דף עזר

```python
def double(number):
    result = number * 2
    return result


answer = double(6)
print(answer + 1)
```

<div dir="rtl">

- משתנה שנוצר בתוך פעולה הוא מקומי — קיים רק בזמן ריצת הזימון, ואי אפשר לקרוא אותו מבחוץ.
- פעולה בלי `return` מחזירה `None` — ערך אמיתי שיכול לגרום לבלבול.
- מספר הפרמטרים ונוכחות ה-`return` הם שתי בחירות נפרדות.

</div>

## 1. חימום: חושב, אבל לא מחזיר

פתחו את `Points_Starter.py`.

```python
def discounted(price, percent):
    discount = price * percent / 100
    price - discount


final_price = discounted(80, 25)
print(final_price)
```

חשבו קודם: 25 אחוז מ-80 הם 20, אז המחיר אחרי ההנחה אמור להיות 60. הריצו — מה בעצם מודפס? הוסיפו מילה אחת כדי לתקן.

## 2. משימה 1: is_even(number)

מחזירה `True` או `False` — בלי `print` בתוך הפעולה. בדקו עם 14 ועם 9.

## 3. משימה 2: passed(score) בתוך if

מחזירה `True` כאשר `score >= 60`. השתמשו בערך החוזר ישירות בתוך `if` / `else` שמדפיס `Continue` או `Try again`. בדקו עם 72.

## 4. משימה 3 (בדיקת סיום היחידה): מחשבון המשימות

שלוש פעולות קטנות, בנו ובדקו **אחת בכל פעם**:

<div dir="rtl">

- `calculate_points(level, tasks)` ← `level * tasks * 10`
- `passed_checkpoint(points)` ← `True` כאשר `points >= 100`
- `show_result(name, points, success)` ← מדפיסה את השלושה

</div>

אחר כך חברו אותן מהתכנית הראשית לפחות עבור שלושה תלמידים, כולל מקרה גבול בדיוק על 100 נקודות.

## 5. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U3_M3_Points_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. כתבו פעולה קצרה שמקבלת ערך ומחזירה ערך אחר. הוסיפו זימון שמשתמש בערך החוזר (לא רק מתעלם ממנו).
2. למה `print(secret)` נכשל מחוץ ל-`build_code()`, למרות ש-`secret` בהחלט החזיק ערך בזמן ריצת הפעולה?

</div>
