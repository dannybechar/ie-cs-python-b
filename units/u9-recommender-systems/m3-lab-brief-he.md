# יחידה 9.3 – מערכות המלצה

כיתה ח׳ · AI + Python B · **מהתאום להמלצה — פרויקט הסיכום**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> ממליצים על פריט ששני התנאים מתקיימים בו: **התאום אהב אותו** (`V`) ו**המשתמש לא מכיר אותו** (`0`). אם אין תאום או אין פריט כזה — מדפיסים הודעה ברורה, לא קורסים.

## דף עזר

```python
def find_twin(target_index):
    best_index = None
    best_score = 0
    for index in range(len(answers)):
        # ... בודקים את המשתתף, ושומרים את הטוב ביותר עד כה
    return best_index
```

<div dir="rtl">

`None` אומר "לא נמצא". כשיש שוויון — נשאר המשתתף הראשון שנמצא.

</div>

## 1. חימום: האדם הוא התאום של עצמו

פתחו את `TwinRecommend_Starter.py`, חזו מה יודפס, והריצו.

```python
print(find_twin(3))
```

<div dir="rtl">

התאום של `user_04` (מקום 3) אמור להיות `user_03` — מקום 2. מקבלים `3`. מי הוא התאום שנמצא? מדוע? תקנו בעזרת תנאי `index != target_index`.

</div>

## 2. משימה 1: recommend_item(target_answers, twin_answers)

<div dir="rtl">

כתבו פעולה שמחזירה את **שם** הפריט הראשון שהתאום אהב (`V`) והמטרה לא מכירה (`0`). אם אין פריט כזה — מחזירה `None`. בדקו:

</div>

```python
print(recommend_item("00XVV", "V0XXV"))   # sushi
print(recommend_item("V0XXV", "V0XXV"))   # None
```

## 3. משימה 2 (פרויקט): main()

<div dir="rtl">

כתבו `main()` שמבצעת:

1. המטרה היא המשתתף האחרון: `target_index = len(aliases) - 1`.
2. מוצאים תאום. אם אין — מדפיסים `No twin found.` ועוצרים (`return`).
3. מדפיסים את כינוי המטרה, כינוי התאום ומספר הנקודות.
4. מדפיסים את ההמלצה, או `Nothing new to recommend.`

</div>

<div dir="rtl">

הפלט הצפוי עם נתוני הדוגמה:

</div>

```text
Target: user_04
Twin: user_03
Points: 2
Recommendation: sushi
```

<div dir="rtl">

הריצו גם על נתוני הכיתה (שלוש השורות שהמורה נותן). האם ההמלצה נשמעת לכם הגיונית? למה כן או לא?

</div>

## 4. בדיקת מקרי קצה

<div dir="rtl">

| מקרה | מה מצפים |
|---|---|
| אף אחד לא חולק תשובה עם המטרה | אין תאום — `No twin found.` |
| התאום לא אוהב דבר שהמטרה לא מכירה | `Nothing new to recommend.` |
| המטרה כבר מכירה הכול | `Nothing new to recommend.` |
| שני משתתפים עם אותו מספר נקודות | נשאר הראשון |
| `0` מול `0` בלבד | אין נקודה |

</div>

<div dir="rtl">

בחרו שני מקרים, הכינו להם נתונים משלכם, והריצו.

</div>

## 5. אם נשאר זמן: כל ההמלצות

<div dir="rtl">

כתבו `recommend_all(target_answers, twin_answers)` שמחזירה **מחרוזת אחת** עם כל הפריטים המומלצים, מופרדים ב-`", "` (מחרוזת ריקה אם אין).

</div>

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U9_M3_TwinRecommend_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מדוע אסור להשוות את המטרה לעצמה?
2. מהם שני התנאים להמלצה על פריט?
3. מהי בעיית ההתחלה הקרה (cold start)?

</div>
