# יחידה 5.3 – מחרוזות

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
def count_char(text, letter):
    count = 0                       # פעם אחת, לפני הלולאה
    for character in text:
        if character == letter:
            count += 1
    return count
```

```python
for character in "Learn":
    print(character * 3, end="")    # end="" - נשארים באותה שורה
print()                             # ירידת שורה בסוף
```

## 1. חימום: המונה שמתאפס

פתחו את `Traverse_Starter.py`. הפעולה אמורה להחזיר `5`.

```python
def count_letter(text, letter):
    for character in text:
        count = 0
        if character == letter:
            count += 1
    return count

print(count_letter("sometimes you win sometimes you learn", "e"))
```

חזו מה יודפס, הריצו, והסבירו למה. תקנו על ידי העברת שורה אחת למקום אחר.

## 2. משימה 1: is_year(text)

קודם חזו והריצו את שלוש הוראות `startswith` שבקובץ. אחר כך כתבו `is_year(text)` — מחזירה `True` רק כשהטקסט מורכב מספרות בלבד **ואורכו 4**.
`"2027"` ← `True`; `"1.9.2027"`, `"20x7"`, `"99"` ← `False`.

## 3. משימה 2: count_char(text, letter)

פעולה שסופרת כמה פעמים אות מופיעה במחרוזת — **בלי** `count()`, בעזרת לולאת `for`. הבדיקה: במשפט שבחימום עם `"e"` מתקבל `5`.

## 4. משימה 3: שלוש פעמים כל אות

- `triple_print(text)` — מדפיסה כל אות שלוש פעמים, הכול בשורה אחת: `"Learn"` ← `LLLeeeaaarrrnnn`.
- `triple(text)` — בונה את אותה מחרוזת בעזרת `+=` **ומחזירה** אותה במקום להדפיס.

## 5. משימה 4: שמות משפחה

כתבו שתי פעולות שמקבלות את `number`, קולטות `number` שמות משפחה עם `input()` ומחזירות כמה מהם מכילים את `cohen` (בכל צורת אותיות):

- `count_cohen_a` — בעזרת `count`.
- `count_cohen_b` — בלי `count` (השתמשו ב-`in`).

> [!NOTE]
> מקלידים שמות **בדויים** בלבד — לא שמות של תלמידים אמיתיים.

## 6. משימה 5: שומרים רק אותיות מ-a עד e

כתבו `keep_a_to_e(text)` — בונה ומחזירה מחרוזת חדשה שמכילה רק את התווים שבין `"a"` ל-`"e"` (`>= "a"` ו-`<= "e"`).
חזו קודם מה תקבלו מ-`"We play on the computer"`.

## 7. אם נשאר זמן: count_words(text)

מספר הרווחים ועוד 1. `"We are learning to program"` ← `5`. מה קורה ב-`"two  spaces"` (שני רווחים רצופים)? למה?

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
