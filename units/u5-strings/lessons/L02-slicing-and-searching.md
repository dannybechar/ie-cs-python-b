# שיעורים 7.1–7.2 – מחרוזות

כיתה ח׳ · AI + Python B · **חיתוך וחיפוש בתוך מחרוזת**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `text[start:end:jump]` חותכת חלק מהמחרוזת — המקום `end` **לא** נכלל. גם `replace`, `upper`, `lower` ו-`count` לא משנים את המחרוזת המקורית: הם נותנים ערך חדש.

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
print(s.find("win", 10, 20))    # 14 - חיפוש רק בין המקומות 10 ל-20
print("think big be bold show your color"[-20:-14:2])   # bl  - מקומות שליליים בשני הקצוות
```

<div dir="rtl">

- אורך חיתוך פשוט: `end - start`.
- `find` נותן מקום, או `-1`. `in` נותן `True` או `False`.
- `in` ו-`find` מבדילים בין אותיות גדולות לקטנות.

</div>

## 1. חימום: הפקודה שלא שינתה כלום

פתחו את `Slicing_Starter.py`. בכל משימה כותבים קוד מתחת למשתנה, ומדפיסים את התשובה עם `print`. אחר כך משנים את ערך המשתנה ומריצים שוב.

```python
title = "strings are sequences"
title.upper()
print(title)
```

חזו, הריצו, ותקנו שורה אחת כך שתודפס הכותרת באותיות גדולות.

## 2. משימה 1: כותבים את החיתוך

<div dir="rtl">

עבור המשתנה `text` הדפיסו בעזרת חיתוך: `drums`, `to play`, `Ikoar`.
עבור המשתנה `number` (שימו לב: מחרוזת!) הדפיסו: `124`, `49`, `4512`, `987`.
יש כמה תשובות נכונות — השוו עם חברים.

</div>

```python
text = "I like to play drums"
number = "345124987"
```

## 3. משימה 2: כמה פעמים מופיע the?

כתבו קוד שמדפיס כמה פעמים מופיע הרצף `the` בתוך `text`.

```python
text = "the other theme is there"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `"the other theme is there"` | `4` | |

</div>

אחר כך חזו: מה ידפיס `print("aaaa".count("aa"))`? הריצו, והסבירו.

## 4. משימה 3: מחליפים רק 3 פעמים

כתבו קוד שמחליף את התו `|` ב-`we` רק ב-3 המקומות הראשונים שבהם הוא מופיע, ומדפיס את המחרוזת החדשה.

```python
text = "a|b|c|d|e"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `"a\|b\|c\|d\|e"` | `awebwecwed\|e` | |

</div>

## 5. משימה 4: יש בטקסט yes?

כתבו קוד שמדפיס `True` אם המחרוזת מכילה את המילה `yes` בכל צורת אותיות (`yes`, `YES`, `Yes`), ואחרת `False`.

```python
text = "Maybe YES maybe no"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `"Maybe YES maybe no"` | `True` | |
| `"no way"` | `False` | |

</div>

## 6. אם נשאר זמן: נראה כמו כתובת מייל?

כתבו קוד שמדפיס `True` כשיש בטקסט `@` **ואחריו** גם `.`, ואחרת `False`. השתמשו ב-`find` עם מקום התחלה.

```python
address = "dana@school.org"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `"dana@school.org"` | `True` | |
| `"dana@school"` | `False` | |
| `"dana.school"` | `False` | |

</div>

שימו לב: הקוד בודק רק את הצורה — הוא לא יודע אם הכתובת קיימת.

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
