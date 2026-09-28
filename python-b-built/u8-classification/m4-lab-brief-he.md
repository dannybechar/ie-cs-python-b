# יחידה 8.4 – סיווג

כיתה ח׳ · AI + Python B · **דיוק, ייצוא וטעינת המודל ב-Python — בדיקת סיום היחידה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> Accuracy הוא שיעור התחזיות הנכונות על כל סט המבחן. שורת `labels.txt` אמיתית נושאת לעיתים רווח מיותר — `.strip()` לפני השוואה, אחרת תחזית **נכונה** יכולה להיראות שגויה.

## דף עזר

```python
def calculate_accuracy(actual, predicted):
    if len(actual) == 0 or len(actual) != len(predicted):
        return 0
    correct = 0
    for index in range(len(actual)):
        if actual[index].strip() == predicted[index].strip():
            correct += 1
    return correct / len(actual) * 100
```

<div dir="rtl">

עיבוד תמונה לפני חיזוי, לפי הסדר: פתיחה והמרה ל-RGB ← התאמה ל-224×224 ← המרה למערך מספרי ← נרמול ← אצווה בגודל 1 ← `predict` ← `argmax` ← מיפוי האינדקס לשם קטגוריה.

</div>

> [!NOTE]
> `classify_image()` פועלת ב**מצב כיתה** — מנחשת לפי שם הקובץ, בלי הורדת מודל אמיתי.

## 1. חימום: תחזית "שגויה" שהייתה נכונה

פתחו את `Accuracy_Starter.py`.

```python
actual_labels = ["fist", "ok", "fist"]
predicted_labels = ["fist", "ok ", "fist"]   # רווח בסוף, כמו בשורת labels.txt אמיתית
print(calculate_accuracy(actual_labels, predicted_labels))
```

חזו `100.0` (כל השלוש תואמות בפועל), הריצו — מקבלים `66.7`. `"ok "` (עם רווח) לא שווה ל-`"ok"`. תקנו: `.strip()` על שני הצדדים לפני ההשוואה.

## 2. אישור על הדוגמה הרשמית המלאה

```python
actual_full = ["fist", "ok", "fist", "ok", "ok", "fist", "ok"]
predicted_full = ["fist", "ok", "ok", "ok", "ok", "fist", "ok"]
print(round(calculate_accuracy(actual_full, predicted_full), 1))
```

צפו ל-≈85.7, כמו בחישוב הידני.

## 3. משימה (פרויקט): טעינה וחיזוי — בדיקת סיום היחידה

השלימו את `classify_image(image_path)` — במצב כיתה: `image_path` באותיות קטנות; אם מכיל `"fist"` ← `("fist", 0.9)`; אם מכיל `"ok"` ← `("ok", 0.9)`; אחרת ← `("unknown", 0.5)`. כתבו `predict_test_set(test_images, actual_labels)`: קוראת ל-`classify_image` על כל נתיב, מדפיסה נתיב/תחזית/confidence, אוספת את התחזיות, ומדפיסה בסוף את ה-accuracy הכולל.

## 4. דוח מודל ומתעדים

כל קבוצה מדווחת: מטרת הסיווג והקטגוריות, התכונה הרצויה, שתי תכונות מקריות שנבדקו, מספרי דוגמאות האימון, תיאור סט המבחן, accuracy כולל, דוגמת טעות אחת, שינוי נתונים אחד, מגבלה אחת שנותרה.

שומרים: `File › Save As` ← `G8_U8_M4_Accuracy_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. כיצד מחשבים accuracy?
2. מה ההבדל בין confidence ל-accuracy?
3. מדוע מנרמלים את התמונה?
4. איזה כשל זיהיתם ואיזה שינוי נתונים עשוי לצמצם אותו?

</div>
