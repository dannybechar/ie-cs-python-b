# יחידה 6.1 – מודל שפה מתקדם

כיתה ח׳ · AI + Python B · **טוקנים, טוקניזציה ומזהים**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> טוקן הוא יחידת עיבוד של מודל מסוים — לא בהכרח מילה שלמה. אי אפשר לדעת את מספר הטוקנים בלי לדעת באיזה טוקנייזר משתמשים.

## דף עזר

```text
טקסט → טוקנייזר → טוקנים → מזהים מספריים → המודל
```

```text
"unbelievable!" → ["un", "believ", "able", "!"] → [418, 9201, 642, 12]
```

<div dir="rtl">

הפירוק והמספרים בדוגמה הם רעיוניים בלבד — לכל טוקנייזר מילון משלו.

</div>

## 1. חימום: הטוקן האחרון נעלם

פתחו את `Tokenizer_Starter.py`.

```python
def simple_tokenize(text):
    result = ""
    current = ""
    for character in text:
        if character.isalpha() or character.isnumeric():
            current += character.lower()
        else:
            if current != "":
                result += "[" + current + "]"
                current = ""
            if character != " ":
                result += "[" + character + "]"
    return result


print(simple_tokenize("AI helps"))
```

חזו `[ai][helps]`, הריצו — מקבלים רק `[ai]`. הלולאה מרוקנת את `current` רק כשהיא פוגשת תו שאינו אות; אם הטקסט מסתיים באמצע מילה, החלק האחרון אף פעם לא משתחרר. תקנו: הוסיפו את אותו שחרור **אחרי** הלולאה.

## 2. משימה 1: סימון רווחים כטוקן

כתבו `simple_tokenize_with_spaces(text)` — כל רווח הופך לטוקן `[SPACE]` משלו במקום להיעלם. בדקו על `"AI helps"` ← `[ai][SPACE][helps]`.

## 3. משימה 2: ספירת טוקנים

כתבו `token_count(text)` — כמה טוקנים `simple_tokenize` הפיקה (ספרו כמה `"["` יש בתוצאה). השתמשו בה על כמה מזוגות הניסוי מהשיעור והשוו את הספירות.

## 4. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U6_M1_Tokenizer_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. טוקן יכול להיות…
2. token ID הוא…
3. מדוע אי אפשר תמיד לנחש את מספר הטוקנים לפי מספר המילים?
4. כתבו מגבלה אחת של הטוקנייזר הפשוט שבנינו היום.

</div>
