# יחידה 5.4 – מחרוזות

כיתה ח׳ · בינה מלאכותית ופייתון ב׳ · **אלגוריתמים על מחרוזות** · דף עבודה בכיתה (נייר + מחשב)

שם: ______________________  תאריך: ______________

<div dir="rtl">

**מחזור העבודה: כותבים על הנייר ← מריצים ב-Thonny ← משווים ← מתקנים בצבע אחר**

- קודם חושבים וכותבים **על הנייר**, ורק אחר כך מקלידים. המחשב בודק אותכם, הוא לא פותר במקומכם.
- חמש השאלות הן עבודת הכיתה (כ-37 דקות). מה שלא הסתיים – משלימים בבית.
- כל פעולה **מחזירה** ערך (לא מדפיסה).
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
def count_vowels(text):
    total = 0
    for character in text:
        if character == "a" or "e" or "i" or "o" or "u":
            total += 1
    return total

print(count_vowels("sometimes you learn"))
```

<div dir="rtl">

הפעולה אמורה להחזיר את המספר 8. חזו מה היא מחזירה, הריצו, והסבירו למה.

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

## שאלה 2: האות האמצעית (6 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא מחזירה את האות האמצעית של המילה. כשאורך המילה זוגי, היא מחזירה את **שתי** האותיות האמצעיות.

</div>

```python
middle(word)
```

<div dir="rtl">

רמז: מה מחזירות שתי ההוראות הבאות?

</div>

```python
len(word) // 2
len(word) % 2
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `middle("robot")` | `b` | &nbsp; |
| `middle("python")` | `th` | &nbsp; |
| `middle("a")` | `a` | &nbsp; |

<pagebreak>

## שאלה 3: הקצוות (7 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא מחזירה את 4 התווים הראשונים ואחריהם את 4 התווים האחרונים, צמודים.
אם בטקסט יש פחות מ-4 תווים, היא מחזירה ארבע כוכביות.

</div>

```python
edges(text)
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `edges("I like to play drums")` | `I lirums` | &nbsp; |
| `edges("abc")` | `****` | &nbsp; |
| `edges("abcd")` | `abcdabcd` | &nbsp; |

<div dir="rtl">

למה התוצאה הראשונה מתחילה ב-4 תווים ולא ב-3 אותיות? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 4: האות האחרונה של כל מילה (8 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא בונה ומחזירה מחרוזת מהאות **האחרונה** של כל מילה.

</div>

```python
last_letters(text)
```

<div dir="rtl">

רמז: תו הוא אחרון במילה אם הוא בסוף הטקסט, **או** אם התו שאחריו הוא רווח. הלולאה עוברת על המקומות:

</div>

```python
for index in range(len(text)):
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `last_letters("I like to play drums")` | `Ieoys` | &nbsp; |
| `last_letters("Hello")` | `o` | &nbsp; |

<div dir="rtl">

למה צריך לבדוק קודם אם הגענו לסוף הטקסט, ורק אחר כך את התו הבא? מה יקרה אם נבדוק את התו הבא גם בתו האחרון? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 5: גדולה, קטנה, גדולה (10 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. האותיות בתוצאה מתחלפות: גדולה, קטנה, גדולה, קטנה... רווח נשאר רווח, **ולא נספר** בהחלפה.

</div>

```python
alternate_case(text)
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `alternate_case("trust yourself")` | `TrUsT yOuRsElF` | &nbsp; |
| `alternate_case("ai")` | `Ai` | &nbsp; |

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

כתבו פעולה בשם הבא. היא מחזירה כמה פעמים מופיעה **המילה** it בטקסט – כמילה שלמה, לא כחלק ממילה אחרת.

</div>

```python
count_word_it(text)
count_word_it("it is a little bit with it")      # 2
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
