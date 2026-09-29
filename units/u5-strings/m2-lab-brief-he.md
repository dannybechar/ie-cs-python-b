# יחידה 5.2 – מחרוזות

כיתה ח׳ · AI + Python B · **חיתוך מחרוזות: התחלה, סוף וקפיצה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `text[start:end:step]` מחזירה תווים מ-`start` עד לפני `end` (לא כולל), בקפיצות של `step`. גבול חסר משלים מההתחלה או עד הסוף.

## דף עזר

```python
word = "PROMPT"
print(word[0:3])   # PRO
print(word[3:])    # MPT
print(word[:3])    # PRO
print(word[:])     # PROMPT
print(word[::-1])  # TPMORP
```

<div dir="rtl">

- חיתוך פשוט `text[a:b]` (קפיצה 1) אורכו `b - a` — בזכות זה שהסוף לא נכלל.
- `word[2]` מחזיר **תו** אחד. `word[2:3]` מחזיר **חיתוך** באורך תו אחד — אותו ערך, סוג שונה.

</div>

## 1. חימום: תו אחד, לא חיתוך

פתחו את `Slicer_Starter.py`.

```python
filename = "answer.txt"
extension = filename[-3]
print(extension)
```

חזו `txt`, הריצו — מקבלים `t` בלבד. `filename[-3]` הוא תו יחיד, לא חיתוך. תקנו: `filename[-3:]`.

## 2. משימה 1: שלוש פעולות חיתוך

על `answer = "TITLE: Safe AI\nBODY: Check important facts."`, כתבו ובדקו:

<div dir="rtl">

- `first_six(text)` — ששת התווים הראשונים
- `last_ten(text)` — עשרת התווים האחרונים
- `reversed_text(text)` — כל הטקסט, הפוך

</div>

## 3. משימה 2: mask_id(demo_id)

מחזירה `"****"` ואחריו ארבעת התווים האחרונים. בדקו על `"CLASSROOM-2026-ABCD"`.

> [!WARNING]
> זהו מזהה הדגמה מזויף, לא מפתח API אמיתי. מפתח אמיתי לא מדפיסים בכלל — גם לא ממוסך.

## 4. מתעדים, משתפים ובודקים יציאה

שומרים: `File › Save As` ← `G8_U5_M2_Slicer_<Name>.py`

מחליפים עם בן/בת זוג: הם נותנים לכם ביטוי חיתוך לחישוב ידני לפני שמריצים.

**עבור `word = "PYTHON"`:**

<div dir="rtl">

1. `word[1:4]`?
2. `word[-2:]`?
3. `word[::2]`?
4. `word[::-1]`?

</div>
