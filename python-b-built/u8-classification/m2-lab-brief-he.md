# יחידה 8.2 – סיווג

כיתה ח׳ · AI + Python B · **תהליך למידת מכונה ו-Teachable Machine**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> מודל לומד מסט אימון ונשפט על סט מבחן נפרד — אם אותה דוגמה נמצאת בשניהם, המדידה אופטימית מדי ולא בודקת הכללה אמיתית.

## דף עזר

```text
הגדרת בעיה → הגדרת קטגוריות → איסוף ותיוג נתוני אימון → אימון המודל →
בדיקה על נתונים חדשים → חישוב מדד וניתוח טעויות → שיפור הנתונים או התכנון
```

<div dir="rtl">

- **Confidence** שייך לתחזית אחת. **Accuracy** מסכם ביצועים על כל סט המבחן.
- מודל יכול לטעות ב-confidence גבוה.

</div>

## 1. חימום: דליפה שלא נתפסה

פתחו את `TrainTest_Starter.py`.

```python
def has_leak(train_ids, test_ids):
    return train_ids == test_ids


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))
```

חזו `True` (`"img2"` נמצא בשניהם), הריצו — מקבלים `False`. השוואת שתי רשימות שלמות לשוויון אינה בודקת חפיפה בין איברים בודדים. תקנו: עברו על `test_ids` ובדקו `in train_ids`.

## 2. משימה 1: describe_trial(true_label, predicted, confidence)

מחזירה שורה קריאה: `"<true_label> -> <predicted> (confidence <confidence>) - correct"` או `"... - WRONG"`. בדקו על `("fist", "fist", 0.91)` ועל `("ok", "fist", 0.55)`.

## 3. משימה 2: count_correct(true_labels, predicted_labels)

כמה מיקומים תואמים בין שתי הרשימות (באותו אורך). בדקו על `["fist", "ok", "fist", "ok", "ok"]` / `["fist", "ok", "ok", "ok", "ok"]`.

## 4. רפלקציה, מתעדים ושומרים

איזו תכונה רצינו שהמודל ילמד? איזו תכונה מקרית ייתכן שלמד במקום? איזה ניסוי הפריד בין השתיים?

שומרים: `File › Save As` ← `G8_U8_M2_TrainTest_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מדוע צריך סט מבחן נפרד?
2. מהי דליפת מידע בין אימון למבחן?
3. כיצד רקע יכול להפוך לתכונה לא רצויה?
4. מה ההבדל בין confidence ל-accuracy?

</div>
