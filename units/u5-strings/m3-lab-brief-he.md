# יחידה 5.3 – מחרוזות

כיתה ח׳ · AI + Python B · **חיתוך מתקדם ומעבר על מחרוזת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `find()` מחזירה אינדקס, או `-1` כשלא נמצא — תמיד בודקים לפני שמשתמשים בערך כגבול חיתוך.

## דף עזר

```python
record = "topic=loops;level=beginner"
separator = record.find(";")
if separator == -1:
    print("Separator not found")
else:
    print(record[:separator])
    print(record[separator + 1:])
```

```python
for character in text:                 # התו עצמו חשוב
    ...

for index in range(len(text)):          # גם המיקום חשוב
    print(index, text[index])
```

## 1. חימום: אינדקס אחד רחוק מדי

פתחו את `Scan_Starter.py`.

```python
text = "AI 2026"
for index in range(len(text) + 1):
    print(index, text[index])
```

הריצו — `IndexError`. ה-`+ 1` דוחף אינדקס אחד מעבר לסוף. תקנו: `range(len(text))`.

## 2. משימה 1: count_maybe(text)

מחזירה כמה פעמים מופיעה המילה `maybe`, בלי תלות בגודל אותיות. בדקו על `"Maybe it works. MAYBE verify it."`.

## 3. משימה 2: first_part(text)

מחזירה את כל מה שלפני הרווח הראשון; אם אין רווח — את כל הטקסט. בדקו על `"smart assistant"` ועל `"Python"`.

## 4. משימה 3: hide_digits(text)

מחזירה את הטקסט כשכל ספרה הוחלפה ב-`#`, בנוי תו אחר תו — לא קריאת `.replace()` לכל ספרה בנפרד. בדקו על `"Room 12 at 09:30"`.

## 5. יישום על טקסט AI שמור

על `ai_answer = "Maybe the answer is 42. Verify important facts."`, הפיקו: אורך, מספר ספרות, האם מופיעה `maybe`, האם הטקסט מסתיים בנקודה, וקדימון של 10 תווים.

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U5_M3_Scan_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מתי עדיף `for character in text`?
2. מתי צריך `range(len(text))`?
3. מה מחזירה `find()` כאשר הטקסט לא נמצא?
4. מדוע עדיף שפונקציית ניתוח תחזיר תוצאה עם `return` ולא רק תדפיס אותה?

</div>
