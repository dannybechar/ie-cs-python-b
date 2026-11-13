# שיעורים 19.0–19.1 – סיווג

כיתה ח׳ · AI + Python B · **מחברים את המודל המאומן לפייתון — ביטחון ופעולה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> מודל סיווג יודע רק לומר לאיזו קטגוריה שייכת תמונה. תוכנית פייתון הופכת את ההחלטה לפעולה: היא קוראת את הקטגוריה **וגם** את רמת הביטחון, ופועלת רק כשהביטחון גבוה מספיק.

## דף עזר

<div dir="rtl">

הקוד של המודל האמיתי (`Ministry_Model_Code.py`) הוא "קופסה שחורה": לא נבהלים מקוד ארוך, ומשנים רק **שלוש שורות**:

</div>

```python
model_path = "model.savedmodel"
labels_path = "labels.txt"
image_path = "test_image.png"
```

<div dir="rtl">

תיקיית `converted_savedmodel.zip` מחולצת (קליק ימני ← Extract All) לתיקייה `model.savedmodel` ולקובץ `labels.txt`. שורה בקובץ התוויות נראית כך: `1 ok`.

</div>

```python
def calculate_accuracy(successes, attempts):
    if attempts == 0:
        return 0
    return successes / attempts * 100
```

> [!NOTE]
> אם אין TensorFlow במחשב, עובדים עם **מודל מדומה**: `classify_image()` בקובץ `Model_Starter.py` מחזירה תשובות קבועות לשבעה שמות תמונה. זה לא מודל אמיתי. ההשוואה עם המודל האמיתי נעשית בכיתה או ב-Colab.

## 1. חימום: סימן ה-OK שלא פתח את הדלת

פתחו את `Model_Starter.py` (והקובץ `labels_standin.txt` באותה תיקייה).

```python
result = classify_image("test_1_ok.png")
label = result[0]
confidence = result[1]
print("label:", label)
if label == "ok":
    print("Gesture recognized: OK - opening the door")
else:
    print("Not an OK sign - the door stays closed")
```

<div dir="rtl">

חזו שיודפס `opening the door`, הריצו — והדלת נשארת סגורה. הסתכלו על `label`: מה כתוב בו? תקנו כך שתישאר רק התווית עצמה (רמז: מה שבא אחרי הרווח הראשון, `text[text.find(" ") + 1:]`).

</div>

## 2. משימה 1: מחליפים נתיבים וכותבים report

<div dir="rtl">

**עם מודל אמיתי:** ב-`Ministry_Model_Code.py` שנו רק את `model_path`, `labels_path` ו-`image_path`, והריצו על אחת מתמונות המבחן.

**בשני המצבים:** כתבו `report(image_path)` שמסווגת את התמונה ומדפיסה שורה אחת, למשל `test_1_ok.png -> ok (99%)` (רמת הביטחון כאחוז שלם: `round(confidence * 100)`). הריצו על `"test_1_ok.png"` ועל `"test_4_ok_drawing.png"`.

</div>

## 3. משימה 2: מחליטים אם לפעול

<div dir="rtl">

כתבו `decide(label, confidence)` שמחזירה:

- ביטחון 0.85 ומעלה: `"ACT: <label>"`
- ביטחון נמוך יותר: `"NOT SURE: ask for another photo"`

בדקו על `("ok", 0.99)` ועל `("fist", 0.73)`.

</div>

## 4. משימה 3: דיוק על כל תמונות המבחן

<div dir="rtl">

כתבו `evaluate(test_images, true_labels)`: סווגו כל תמונה, הדפיסו `correct` או `WRONG`, ספרו הצלחות, והחזירו את הדיוק בעזרת `calculate_accuracy`.

</div>

```python
test_images = ["test_1_ok.png", "test_2_fist.png", "test_3_fist_dark.png", "test_4_ok_drawing.png",
               "test_5_ok_side.png", "test_6_fist_blurry.png", "test_7_ok_far.png"]
true_labels = ["ok", "fist", "fist", "ok", "ok", "fist", "ok"]
```

<div dir="rtl">

עם המודל האמיתי: השתמשו ב-7 תמונות המבחן של המורה ובתוויות האמת שלהן.

**אם נשאר זמן:** על כמה תמונות התוכנית **תפעל** לפי כלל ה-85%, והאם היא צדקה בכולן?

</div>

## 5. דוח מודל

<div dir="rtl">

כל קבוצה מדווחת: מטרת הסיווג והקטגוריות; התכונה הרצויה ושתי תכונות מקריות שנבדקו; מספר תמונות האימון בכל קטגוריה; הדיוק על 7 תמונות המבחן; דוגמה אחת לטעות עם רמת הביטחון שלה; שינוי נתונים אחד שהייתם עושים; ומגבלה אחת שנשארה (מה המודל עושה ליד שאינה אגרוף ואינה OK?).

</div>

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U8_M4_Model_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מה מודל לבדו עושה, ומה הקוד מוסיף?
2. אילו שלוש שורות משנים כדי לבדוק תמונה משלכם?
3. מה ההבדל בין דיוק (accuracy) לרמת ביטחון (confidence)?
4. למה פועלים רק כשהביטחון מעל 85%?

</div>
