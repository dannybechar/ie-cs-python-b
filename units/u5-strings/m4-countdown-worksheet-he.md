# יחידה 5.4 – מחרוזות

כיתה ח׳ · בינה מלאכותית ופייתון ב׳ · **אלגוריתמים על מחרוזות** · דף עבודה בכיתה (נייר + מחשב)

שם: ______________________  תאריך: ______________

<div dir="rtl">

**מחזור העבודה: כותבים על הנייר ← מריצים ב-Thonny ← משווים ← מתקנים בצבע אחר**

- קודם חושבים וכותבים **על הנייר**, ורק אחר כך מקלידים. המחשב בודק אותכם, הוא לא פותר במקומכם.
- חמש השאלות הן עבודת הכיתה (כ-37 דקות). מה שלא הסתיים – משלימים בבית.
- בכל שאלה כותבים קוד מתחת למשתנה, ומדפיסים את התשובה עם print. אחר כך משנים את ערך המשתנה ומריצים שוב.
- בכל הדוגמאות כותבים טקסטים **בדויים** בלבד – לא שמות או מספרי טלפון אמיתיים.

</div>

<div dir="rtl">

פותחים ב-Thonny את הקובץ הבא:

</div>

```python
Worksheet_Starter.py
```

## דף עזר

<div dir="rtl">

מקומות במחרוזת:

</div>

```python
word = "python"
len(word)          # 6
word[0]            # "p"     word[-1]   # "n"
word[1:3]          # "yt"    word[-4:]  # "thon"
7 // 2             # 3       7 % 2      # 1
```

<div dir="rtl">

לולאה על המקומות, כשהמקום חשוב:

</div>

```python
for index in range(len(text)):
    if text[index] == " ":
        print("space at", index)
```

<div dir="rtl">

אותיות גדולות וקטנות:

</div>

```python
"a".upper()        # "A"     "B".lower()        # "b"
```

<pagebreak>

## שאלה 1: מצאו את הבאג (6 דקות)

```python
text = "sometimes you learn"
total = 0
for character in text:
    if character == "a" or "e" or "i" or "o" or "u":
        total += 1
print(total)
```

<div dir="rtl">

הקוד אמור להדפיס את המספר 8. חזו מה הוא מדפיס, הריצו, והסבירו למה.

</div>

| החיזוי שלי | מה הודפס בפועל | ההסבר שלי |
|---|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp;<br>&nbsp; |

<div dir="rtl">

כתבו את שורת התנאי המתוקנת:

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 2: כמה פעמים מופיע is (6 דקות)

<div dir="rtl">

כתבו קוד שמדפיס כמה פעמים מופיעים התווים is בטקסט, **בלי** השיטה count. התווים נספרים גם בתוך מילה אחרת.

</div>

```python
text = "this is his list"
```

<div dir="rtl">

רמז: בכל מקום בטקסט בודקים את שני התווים שמתחילים בו:

</div>

```python
text[index:index + 2]
```

| כתבו כאן את הקוד |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "this is his list"` | `4` | &nbsp; |
| `text = "Mississippi"` | `2` | &nbsp; |
| `text = "xyz"` | `0` | &nbsp; |

<div dir="rtl">

מה קורה כשמחשבים את החיתוך הבא במקום האחרון של הטקסט? האם התוכנית קורסת? (משפט אחד)

</div>

```python
text[index:index + 2]
```

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 3: הקצוות (7 דקות)

<div dir="rtl">

כתבו קוד שמדפיס את 4 התווים הראשונים של הטקסט ואחריהם את 4 התווים האחרונים, צמודים.
אם בטקסט יש פחות מ-4 תווים, הוא מדפיס ארבע כוכביות.

</div>

```python
text = "I like to play drums"
```

| כתבו כאן את הקוד |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "I like to play drums"` | `I lirums` | &nbsp; |
| `text = "abc"` | `****` | &nbsp; |
| `text = "abcd"` | `abcdabcd` | &nbsp; |

<div dir="rtl">

למה התוצאה הראשונה מתחילה ב-4 תווים ולא ב-3 אותיות? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 4: האות האחרונה של כל מילה (8 דקות)

<div dir="rtl">

כתבו קוד שבונה ומדפיס מחרוזת מהאות **האחרונה** של כל מילה בטקסט:

</div>

```python
text = "I like to play drums"
```

<div dir="rtl">

רמז: תו הוא אחרון במילה אם הוא בסוף הטקסט, **או** אם התו שאחריו הוא רווח. הלולאה עוברת על המקומות:

</div>

```python
for index in range(len(text)):
```

| כתבו כאן את הקוד |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "I like to play drums"` | `Ieoys` | &nbsp; |
| `text = "Hello"` | `o` | &nbsp; |

<div dir="rtl">

למה צריך לבדוק קודם אם הגענו לסוף הטקסט, ורק אחר כך את התו הבא? מה יקרה אם נבדוק את התו הבא גם בתו האחרון? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 5: גדולה, קטנה, גדולה (10 דקות)

<div dir="rtl">

כתבו קוד שבונה ומדפיס את הטקסט כשהאותיות מתחלפות: גדולה, קטנה, גדולה, קטנה... רווח נשאר רווח, **ולא נספר** בהחלפה.

</div>

```python
text = "trust yourself"
```

| כתבו כאן את הקוד |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| ערך המשתנה | צפוי | בפועל |
|---|---|---|
| `text = "trust yourself"` | `TrUsT yOuRsElF` | &nbsp; |
| `text = "ai"` | `Ai` | &nbsp; |

<div dir="rtl">

חבר מציע לבדוק אם המקום זוגי (הוראה הבאה). למה זה נותן תוצאה שגויה לטקסט הראשון? (משפט אחד)

</div>

```python
index % 2 == 0
```

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## אם נשאר זמן: המילה it

<div dir="rtl">

כתבו קוד שמדפיס כמה פעמים מופיעה **המילה** it בטקסט – כמילה שלמה, לא כחלק ממילה אחרת. הצפוי: 2.

</div>

```python
text = "it is a little bit with it"
```

<div dir="rtl">

למה ההוראה הבאה לא מתאימה כאן? (רמז: little, with)

</div>

```python
text.count("it")
```

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שומרים ומסכמים

<div dir="rtl">

שומרים את הקובץ בשם הבא (בתפריט File ← Save As):

</div>

```python
G8_U5_M4_Worksheet_<Name>.py
```

<div dir="rtl">

מגישים את דף העבודה (עם התיקונים בצבע אחר).

**בדיקת יציאה** (על הנייר, בלי מחשב):

1. מה מודפס?

</div>

```python
print(chr(ord("b") + 2))
```

| &nbsp; |
|---|

<div dir="rtl">

2. מה מודפס, ולמה לא 1?

</div>

```python
print("this is his".count("is"))
```

| &nbsp;<br>&nbsp; |
|---|

<div dir="rtl">

3. בלולאת while שעוברת על המקומות בטקסט, איזו שורה אסור לשכוח בסוף הלולאה? מה יקרה בלעדיה?

</div>

| &nbsp;<br>&nbsp; |
|---|
