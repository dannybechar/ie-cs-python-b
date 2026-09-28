# יחידה 9.3 – מערכות המלצה

כיתה ח׳ · AI + Python B · **מהתאום הדיגיטלי להמלצה — בדיקת סיום היחידה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> משתמש היעד לעולם לא מושווה לעצמו. `(rate, common)` — השיעור קובע ראשון, מספר הדירוגים המשותפים שובר שוויון.

## דף עזר

```python
def find_digital_twin(target_index, all_ratings, minimum_common=2):
    best_index = None
    best_key = (-1.0, -1)
    for candidate_index in range(len(all_ratings)):
        if candidate_index == target_index:
            continue
        matches, common = similarity_score(all_ratings[target_index], all_ratings[candidate_index])
        if common < minimum_common:
            continue
        rate = matches / common
        candidate_key = (rate, common)
        if candidate_key > best_key:
            best_key = candidate_key
            best_index = candidate_index
    return best_index, best_key
```

## 1. חימום: התאום של עצמו

פתחו את `TwinRecommend_Starter.py`. הריצו `find_digital_twin(0, ratings)` על נתוני הבדיקה בקובץ. חזו משתמש אחר אמיתי; מקבלים `(0, (1.0, 3))` — משתמש 0 הותאם ל**עצמו**. תקנו: `if candidate_index == target_index: continue`.

## 2. משימה 1: recommend_item(target_ratings, twin_ratings, item_names, liked_threshold=3)

מוצאת את הפריט שהיעד דירג `0` והתאום דירג `>= liked_threshold`, בוחרת את הדירוג הגבוה ביותר מביניהם; מחזירה `None` אם אין פריט כזה.

## 3. משימה 2 (פרויקט): main() — בדיקת סיום היחידה

טוענת `items`/`aliases`/`all_ratings` מ-`ratings.csv`, מוצאת את התאום של `target_index = 0` (`minimum_common=2`); אם לא נמצא — מדפיסה הודעה וברורה ועוצרת; אחרת ממליצה ומדפיסה כינוי היעד, כינוי התאום, שיעור הדמיון, מספר הדירוגים המשותפים וההמלצה (או הודעה ברורה שאין המלצה מתאימה).

## 4. בדיקות — שבעת המקרים

<div dir="rtl">

| מקרה | התנהגות מצופה |
|---|---|
| אין דירוגים משותפים | לא נמצא תאום דיגיטלי |
| יש רק דירוג משותף אחד | המועמד נדחה כאשר `minimum_common=2` |
| התאום אינו אוהב אף פריט חדש | אין המלצה מתאימה |
| המשתמש כבר מכיר את כל הפריטים | אין המלצה מתאימה |
| שני תאומים בעלי אותו שיעור | מספר הדירוגים המשותפים שובר שוויון |
| שוויון מלא | המועמד הראשון נשמר |
| אורכי רשימות שונים | הפונקציה דוחה את הנתונים |

</div>

## 5. דיון: שלוש מגבלות

**התחלה קרה** — למשתמש או פריט חדש אין מספיק נתונים. **דלות נתונים** — רוב המשתמשים לא מדרגים את רוב הפריטים. **דמיון אינו זהות** — דמיון בדירוגי טיולים לא מוכיח דבר על דעות או אופי.

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U9_M3_TwinRecommend_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מדוע אסור להשוות את משתמש היעד לעצמו?
2. מהם שני התנאים לבחירת פריט מומלץ?
3. מהי בעיית ההתחלה הקרה?

</div>
