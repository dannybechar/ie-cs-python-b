# יחידה 5.1 – מחרוזות

כיתה ח׳ · AI + Python B · **מחרוזת היא רצף סדור**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> מחרוזת היא רצף סדור של תווים, החל מאינדקס `0`. מתודות מחזירות מחרוזת חדשה — הן אף פעם לא משנות את המקורית.

## דף עזר

```python
word = "ROBOT"
#        R  O  B  O  T
# אינדקס: 0  1  2  3  4
#        -5 -4 -3 -2 -1

print(word[0])    # R
print(word[-1])   # T
```

```python
name = "python"
name.upper()          # מוחזרת מחרוזת חדשה, אבל היא נזרקת
print(name)             # python
name = name.upper()     # רק השמה שומרת את המחרוזת החדשה
print(name)              # PYTHON
```

<div dir="rtl">

- האינדקס האחרון תמיד `len(text) - 1`.
- `in` רגיש לגודל אותיות — מנרמלים עם `.lower()` כשצריך.

</div>

## 1. חימום: המתודה שלא שינתה כלום

פתחו את `Checker_Starter.py`.

```python
text = "python"
text.upper()
print(text)
```

חזו, ואז הריצו. עדיין `python`? תקנו שורה אחת.

## 2. משימה 1: בודק פרומפט

קלטו פרומפט עם `input()` והדפיסו: את האורך שלו, האם הוא ריק, האם הוא מכיל את המילה `password` (בכל גודל אותיות), והאם הוא מסתיים ב-`?`.

## 3. משימה 2: header_check(answer)

מחזירה `"Structured answer"` כאשר `answer` מתחילה ב-`"SUMMARY:"`, אחרת `"Missing title"`. בדקו על `"SUMMARY: Python loops repeat instructions."` ועל אותו משפט בלי הכותרת.

## 4. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U5_M1_Checker_<Name>.py`

---

**בדיקת יציאה — עבור `text = "MODEL"`:**

<div dir="rtl">

1. `text[1]` הוא…
2. `text[-1]` הוא…
3. `len(text)` הוא…
4. תוצאת `"del" in text.lower()` היא…

</div>
