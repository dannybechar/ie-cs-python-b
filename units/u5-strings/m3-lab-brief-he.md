# שיעורים 8.0–8.1 – מחרוזות

כיתה ח׳ · AI + Python B · **שיטות נוספות ומעבר על מחרוזת בלולאה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> לולאת `for` עוברת על כל תו במחרוזת, תו אחרי תו. מונה מאפסים **פעם אחת לפני הלולאה**, ומחרוזת חדשה בונים בעזרת `+=`.

## דף עזר

```python
text = "I like to play drums"
print(text.startswith("I like"))        # True
print(text.startswith("play", 10, 17))  # True - בודקים רק את המקומות 10 עד 16
print("2027".isdigit())                 # True
print("1.9.2027".isdigit())             # False
print("Hello".isalpha())                # True
print("Piano".upper(), "DRUMS".lower())
```

```python
text = "sometimes you win sometimes you learn"
letter = "e"
count = 0                       # פעם אחת, לפני הלולאה
for character in text:
    if character == letter:
        count += 1
print(count)                    # פעם אחת, אחרי הלולאה
```

```python
for character in "Learn":
    print(character * 3, end="")    # end="" - נשארים באותה שורה
print()                             # ירידת שורה בסוף
```

<div dir="rtl">

- בכל משימה כותבים קוד מתחת למשתנה, ומדפיסים את התשובה עם `print`.
- כדי לבדוק ערך אחר משנים את ערך המשתנה ומריצים שוב.
- בזמן שעובדים על משימה אחת, שמים `#` לפני הקוד של המשימות האחרות (או עובדים בקובץ חדש).

</div>

## 1. חימום: המונה שמתאפס

פתחו את `Traverse_Starter.py`. הקוד אמור להדפיס `5`.

```python
text = "sometimes you win sometimes you learn"
letter = "e"
for character in text:
    count = 0
    if character == letter:
        count += 1
print(count)
```

חזו מה יודפס, הריצו, והסבירו למה. תקנו על ידי העברת שורה אחת למקום אחר.

## 2. משימה 1: האם זו שנה?

קודם חזו והריצו את שלוש הוראות `startswith` שבקובץ. אחר כך כתבו קוד שמדפיס `True` רק כשהטקסט מורכב מספרות בלבד **ואורכו 4**:

```python
text = "2027"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "2027"` | `True` | &nbsp; |
| `text = "1.9.2027"` | `False` | &nbsp; |
| `text = "20x7"` | `False` | &nbsp; |
| `text = "99"` | `False` | &nbsp; |

</div>

## 3. משימה 2: סופרים אות

כתבו קוד שסופר כמה פעמים האות שב-`letter` מופיעה ב-`text` — **בלי** `count()`, בעזרת לולאת `for` — ומדפיס את התשובה **אחרי** הלולאה.

```python
text = "sometimes you win sometimes you learn"
letter = "e"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "sometimes you win sometimes you learn"`, `letter = "e"` | `5` | &nbsp; |
| `text = "banana"`, `letter = "a"` | `3` | &nbsp; |
| `text = "banana"`, `letter = "z"` | `0` | &nbsp; |

</div>

## 4. משימה 3: שלוש פעמים כל אות

```python
text = "Learn"
```

<div dir="rtl">

- א. כתבו קוד שמדפיס כל אות שלוש פעמים, הכול בשורה אחת: `LLLeeeaaarrrnnn`.
- ב. כתבו קוד שבונה את אותה מחרוזת במשתנה חדש `result` בעזרת `+=`, ומדפיס אותה פעם אחת, אחרי הלולאה.

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "Learn"` | `LLLeeeaaarrrnnn` | &nbsp; |
| `text = "ab"` | `aaabbb` | &nbsp; |

</div>

## 5. משימה 4: שמות משפחה

כתבו קוד שקולט `number` שמות משפחה עם `input()` ומדפיס כמה מהם מכילים את `cohen` (בכל צורת אותיות):

```python
number = 3
```

<div dir="rtl">

- גרסה א — בעזרת `count`.
- גרסה ב — בלי `count` (השתמשו ב-`in`).

</div>

בדיקה: מקלידים `Cohen`, `Levi`, `BenCOHEN` ← מודפס `2`.

> [!NOTE]
> מקלידים שמות **בדויים** בלבד — לא שמות של תלמידים אמיתיים.

## 6. משימה 5: שומרים רק אותיות מ-a עד e

כתבו קוד שבונה מחרוזת חדשה שמכילה רק את התווים שבין `"a"` ל-`"e"` (`>= "a"` ו-`<= "e"`), ומדפיס אותה.
חזו קודם מה יודפס עבור הטקסט הזה:

```python
text = "We play on the computer"
```

<div dir="rtl">

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "We play on the computer"` | (חזו קודם) | &nbsp; |
| `text = "abcdefg"` | `abcde` | &nbsp; |

</div>

## 7. אם נשאר זמן: כמה מילים?

כתבו קוד שמדפיס את מספר הרווחים ועוד 1.

```python
text = "We are learning to program"
```

צפוי: `5`. מה קורה ב-`"two  spaces"` (שני רווחים רצופים)? למה?

## 8. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U5_M3_Traverse_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. `"2027".isdigit()` היא…
2. `"Python".startswith("py")` היא…
3. מה מודפס אחרי `for ch in "abc": print(ch * 2, end="")`?
4. איפה כותבים `count = 0` בלולאת ספירה?

</div>
