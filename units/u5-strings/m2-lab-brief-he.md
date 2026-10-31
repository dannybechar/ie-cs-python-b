# יחידה 5.2 – מחרוזות

כיתה ח׳ · AI + Python B · **חיתוך וחיפוש בתוך מחרוזת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `text[start:end:jump]` חותכת חלק מהמחרוזת — המקום `end` **לא** נכלל. הפעולות `replace`, `upper`, `lower` ו-`count` לא משנות את המחרוזת המקורית: הן מחזירות ערך חדש.

## דף עזר

```python
text = "think big be bold show your color"
print(text[3:])       # מהמקום 3 עד הסוף
print(text[:4])       # thin - מקומות 0 עד 3
print(text[5:12:2])   # בקפיצות של 2
print(text[-5:])      # color
print(text[::-1])     # הפוך
```

```python
s = "sometimes you win sometimes you learn"
print(s.count("some"))          # 2
print(s.replace("you", "we", 1))
print("win" in s)               # True
print(s.find("win"))            # 14
print(s.find("lose"))           # -1 - לא נמצא
```

<div dir="rtl">

- אורך חיתוך פשוט: `end - start`.
- `find` מחזירה מקום, או `-1`. `in` מחזירה `True` או `False`.
- `in` ו-`find` מבדילות בין אותיות גדולות לקטנות.

</div>

## 1. חימום: השיטה שלא שינתה כלום

פתחו את `Slicing_Starter.py`.

```python
title = "strings are sequences"
title.upper()
print(title)
```

חזו, הריצו, ותקנו שורה אחת כך שיודפס הכותרת באותיות גדולות.

## 2. משימה 1: כותבים את החיתוך

עבור `text = "I like to play drums"` הדפיסו בעזרת חיתוך: `drums`, `to play`, `Ikoar`.
עבור `number = "345124987"` (שימו לב: מחרוזת!) הדפיסו: `124`, `49`, `4512`, `987`.
יש כמה תשובות נכונות — השוו עם חברים.

## 3. משימה 2: count_the(text)

מחזירה כמה פעמים מופיע הרצף `the`. הבדיקה: `"the other theme is there"` ← `4`.
אחר כך חשבו: מה יחזיר `"aaaa".count("aa")`? הריצו, והסבירו.

## 4. משימה 3: replace_first_three(text)

מחליפה את התו `|` ב-`we` רק ב-3 המקומות הראשונים שבהם הוא מופיע, ומחזירה את המחרוזת החדשה. `"a|b|c|d|e"` ← `"awebwecwed|e"`.

## 5. משימה 4: has_yes(text)

מחזירה `True` אם המחרוזת מכילה את המילה `yes` בכל צורת אותיות (`yes`, `YES`, `Yes`), אחרת `False`.
`"Maybe YES maybe no"` ← `True`; `"no way"` ← `False`.

## 6. אם נשאר זמן: looks_like_email(address)

מחזירה `True` כשיש בטקסט `@` **ואחריו** גם `.`. השתמשו ב-`find`.
`"dana@school.org"` ← `True`; `"dana@school"` ← `False`; `"dana.school"` ← `False`.
(שימו לב: התוכנית בודקת רק את הצורה — היא לא יודעת אם הכתובת קיימת.)

## 7. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U5_M2_Slicing_<Name>.py`

---

**בדיקת יציאה — עבור `text = "think big"`, מה מודפס?**

<div dir="rtl">

1. `text[:5]`
2. `text[-3:]`
3. `text.find("big")`
4. `text.replace("big", "small")` — ואחר כך `text` עצמו

</div>
