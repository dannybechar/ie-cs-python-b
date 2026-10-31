# יחידה 5.3 – מחרוזות

כיתה ח׳ · בינה מלאכותית ופייתון ב׳ · **עוברים על מחרוזת בלולאה** · דף עבודה בכיתה (נייר + מחשב)

שם: ______________________  תאריך: ______________

<div dir="rtl">

**מחזור העבודה: כותבים על הנייר ← מריצים ב-Thonny ← משווים ← מתקנים בצבע אחר**

- קודם חושבים וכותבים **על הנייר**, ורק אחר כך מקלידים. המחשב בודק אותכם, הוא לא פותר במקומכם.
- חלק א' וחלק ב' הם עבודת הכיתה (כ-46 דקות). מה שלא הסתיים – משלימים בבית.
- חלק ג' הוא לבית, או לכיתה למי שמסיים מוקדם.
- בכל הדוגמאות כותבים טקסטים **בדויים** בלבד – לא שמות או מספרי טלפון אמיתיים.

</div>

<div dir="rtl">

פותחים ב-Thonny את הקובץ הבא:

</div>

```python
Classwork_Starter.py
```

## דף עזר

<div dir="rtl">

פעולה שסופרת:

</div>

```python
def count_char(text, letter):
    count = 0                      # before the loop
    for ch in text:                # next character
        if ch == letter:
            count += 1
    return count                   # after the loop
```

<div dir="rtl">

בונים מחרוזת חדשה:

</div>

```python
result = ""                        # start empty
for ch in "abc":
    result += ch * 2               # "aabbcc"
print(result)
```

<div dir="rtl">

שיטות שבודקות תו אחד:

</div>

```python
"7".isdigit()      # True          "a".isalpha()    # True
"E".lower()        # "e"           "e" in "aeiou"   # True
```

<pagebreak>

## חלק א': קוראים וחוזים (כ-10 דקות)

<div dir="rtl">

לכל קטע: **קודם** כתבו חיזוי על הנייר, **אחר כך** הריצו וכתבו מה הודפס בפועל.
כדי להריץ, כותבים בתחתית הקובץ שורה עם שם הפעולה וסוגריים, למשל:

</div>

```python
a1()
```

### א1

```python
for ch in "sometimes":
    print(ch, end=",")
print()
```

| החיזוי שלי | מה הודפס בפועל |
|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |

### א2

```python
new_text = ""
for ch in "We play on the computer":
    if ch >= "a" and ch <= "e":
        new_text = new_text + ch
print(new_text)
```

| החיזוי שלי | מה הודפס בפועל |
|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |

<div dir="rtl">

מדוע האות הגדולה שבתחילת המשפט לא נכנסה לתוצאה? ומדוע האות p לא נכנסה? (כתבו משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

### א3

```python
sentence = "We are learning to program"
count = 0
for ch in sentence:
    if ch == " ":
        count += 1
print(sentence)
print("Number of words:", count + 1)
```

| החיזוי שלי | מה הודפס בפועל |
|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |

<div dir="rtl">

מה בעצם סופר המונה בקוד? ולמה מוסיפים 1 להדפסה האחרונה?

</div>

| &nbsp;<br>&nbsp; |
|---|

### א4: טבלת מעקב

```python
count = 0
for ch in "banana":
    if ch == "a":
        count += 1
```

<div dir="rtl">

השלימו את הטבלה על הנייר: בכל סבב כתבו את התו, אם התנאי התקיים, ואת ערך המונה **בסוף** הסבב.
אחר כך הריצו את הפעולה הבאה ובדקו שהתשובה זהה:

</div>

```python
a4()
```

| סבב | התו | האם התו הוא a? | המונה בסוף הסבב |
|---|---|---|---|
| 1 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 2 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 3 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 4 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 5 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 6 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |

<pagebreak>

## חלק ב': כותבים פעולות (כ-36 דקות)

<div dir="rtl">

בכל משימה: כתבו את הפעולה **על הנייר**, הקלידו אותה בקובץ במקום המילה הבאה, הריצו, והשוו לעמודה "צפוי".

</div>

```python
pass
```

### ב1: מצאו את הבאג (5 דקות)

```python
def count_letter(text, letter):
    for ch in text:
        count = 0
        if ch == letter:
            count += 1
    return count

sentence = "sometimes you win sometimes you learn"
print(count_letter(sentence, "e"))
```

<div dir="rtl">

הפעולה אמורה להחזיר את המספר 5. חזו מה היא מחזירה, הריצו, והסבירו למה.
תקנו על ידי הזזת שורה אחת.

</div>

| החיזוי שלי | מה הודפס בפועל | ההסבר שלי |
|---|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp;<br>&nbsp; |

<pagebreak>

### ב2: סופרים אות (7 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא מחזירה כמה פעמים האות מופיעה בטקסט.

</div>

```python
count_char(text, letter)
```

<div dir="rtl">

אסור להשתמש בשיטה המובנית הבאה. עוברים על המחרוזת בלולאה:

</div>

```python
text.count(letter)
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

<div dir="rtl">

הטקסט לבדיקות:

</div>

```python
sentence = "sometimes you win sometimes you learn"
```

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_char(sentence, "e")` | 5 | &nbsp; |
| `count_char("banana", "a")` | 3 | &nbsp; |
| `count_char("banana", "x")` | 0 | &nbsp; |
| `count_char("", "a")` | 0 | &nbsp; |

<pagebreak>

### ב3: שלוש פעמים כל אות (8 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא בונה מחרוזת חדשה שבה כל אות מופיעה שלוש פעמים, **ומחזירה** אותה (לא מדפיסה).

</div>

```python
triple(text)
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `triple("Learn")` | `LLLeeeaaarrrnnn` | &nbsp; |
| `triple("")` | (מחרוזת ריקה) | &nbsp; |

<div dir="rtl">

למה צריך לכתוב את השורה הבאה **לפני** הלולאה? מה היה קורה אילו כתבנו אותה בתוך הלולאה? (משפט אחד)

</div>

```python
result = ""
```

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

### ב4: מה יש בתשובה של הבינה המלאכותית? (8 דקות)

<div dir="rtl">

הטקסט הבא נכתב על ידי מודל שפה:

</div>

```python
ai = "In 2024 the model answered 3 questions."
```

<div dir="rtl">

כתבו שתי פעולות. הראשונה סופרת תווים שהם אותיות, והשנייה סופרת תווים שהם ספרות:

</div>

```python
count_letters(text)     # use isalpha
count_digits(text)      # use isdigit
```

| כתבו כאן את שתי הפעולות |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_letters(ai)` | 27 | &nbsp; |
| `count_digits(ai)` | 5 | &nbsp; |

<div dir="rtl">

אפשר לספור ספרות בעזרת ההוראה הבאה? למה זה לא מספיק כאן? (משפט אחד)

</div>

```python
ai.count("5")
```

| &nbsp;<br>&nbsp; |
|---|

<pagebreak>

### ב5: כמה תנועות? (8 דקות)

<div dir="rtl">

כתבו פעולה בשם הבא. היא מחזירה כמה תווים בטקסט הם תנועות, בין אם הן קטנות ובין אם גדולות:

</div>

```python
count_vowels(text)
```

<div dir="rtl">

התנועות הן:

</div>

```python
a e i o u
```

<div dir="rtl">

רמז: שתי ההוראות הבאות יעזרו לכם.

</div>

```python
text.lower()
ch in "aeiou"
```

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_vowels("Hello World")` | 3 | &nbsp; |
| `count_vowels("rhythm")` | 0 | &nbsp; |
| `count_vowels("AEIOU")` | 5 | &nbsp; |

<pagebreak>

## חלק ג': לבית, או לכיתה למי שסיים

### ג1: רק הספרות

<div dir="rtl">

כתבו פעולה בשם הבא. היא בונה ומחזירה מחרוזת שמכילה רק את הספרות של הטקסט. לדוגמה:

</div>

```python
only_digits(text)
only_digits("In 2027 I turn 15")      # "202715"
```

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

### ג2: מסתירים ספרות

<div dir="rtl">

כתבו פעולה בשם הבא. היא מחזירה את הטקסט כשכל ספרה מוחלפת בכוכבית. לדוגמה:

</div>

```python
hide_digits(text)
hide_digits("Room 12 floor 3")        # "Room ** floor *"
```

<div dir="rtl">

חשבו: למה כדאי להסתיר מספרים לפני ששולחים טקסט למודל שפה?

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

### ג3: בודקים תשובה של בינה מלאכותית

```python
answer = "The Moon orbits the Earth. It takes about 27 days. Some answers are wrong, so we check."
```

<div dir="rtl">

הריצו על הטקסט את שלוש ההוראות הבאות וכתבו מה קיבלתם:

</div>

```python
count_char(answer, ".")           # how many sentences?
count_char(answer, " ") + 1       # how many words?
count_digits(answer)              # how many digits?
```

<div dir="rtl">

אחר כך ענו:

1. מה התוכנית שלנו **יכולה** לבדוק על התשובה?
2. מה היא **לא יכולה** לבדוק? (רמז: האם 27 ימים זה נכון?)

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

### ג4: אתגר

<div dir="rtl">

כתבו פעולה בשם הבא. היא מדפיסה כמה פעמים הופיעה כל אחת מחמש התנועות (חמישה מונים ושרשרת תנאים). לדוגמה:

</div>

```python
count_each_vowel(text)
count_each_vowel("Education is the key")
# a: 1 e: 3 i: 2 o: 1 u: 1
```

<pagebreak>

## שומרים ומסכמים

<div dir="rtl">

שומרים את הקובץ בשם הבא (בתפריט File ← Save As):

</div>

```python
G8_U5_M3_Classwork_<Name>.py
```

<div dir="rtl">

מניחים את דף העבודה (עם התיקונים בצבע אחר) בתיק, ומביאים אותו לשיעור הבא.

**בדיקת יציאה** (על הנייר, בלי מחשב):

1. באיזה מקום בפעולה כותבים את השורה הבאה בלולאת ספירה, ולמה שם?

</div>

```python
count = 0
```

<div dir="rtl">

2. מה מודפס אחרי הקוד הבא?

</div>

```python
for ch in "abc": print(ch * 2, end="")
```

<div dir="rtl">

3. במה שונה ההוראה הראשונה מהשנייה בסוף פעולה?

</div>

```python
print(result)
return result
```
