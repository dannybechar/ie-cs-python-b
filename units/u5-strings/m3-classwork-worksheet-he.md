# יחידה 5.3 – מחרוזות

כיתה ח׳ · AI + Python B · **עוברים על מחרוזת בלולאה** · דף עבודה בכיתה (נייר + מחשב)

שם: ______________________  תאריך: ______________

<div dir="rtl">

**מחזור העבודה: כותבים על הנייר ← מריצים ב-Thonny ← משווים ← מתקנים בצבע אחר**

- קודם חושבים וכותבים **על הנייר**, ורק אחר כך מקלידים. המחשב בודק אותכם, הוא לא פותר במקומכם.
- חלק א' וחלק ב' הם עבודת הכיתה (כ-46 דקות). מה שלא הסתיים – משלימים בבית.
- חלק ג' הוא לבית, או לכיתה למי שמסיים מוקדם.
- פותחים את הקובץ `Classwork_Starter.py`. בכל הדוגמאות כותבים טקסטים **בדויים** בלבד – לא שמות או מספרי טלפון אמיתיים.

</div>

## דף עזר

```python
def count_char(text, letter):
    count = 0                      # once, before the loop
    for ch in text:                # ch: the next character
        if ch == letter:
            count += 1
    return count                   # after the loop
```

```python
result = ""                        # empty string before the loop
for ch in "abc":
    result += ch * 2               # add to the end: "aabbcc"
print(result)
```

```python
for ch in "Learn":
    print(ch * 3, end="")          # stay on the same line
print()                            # new line at the end
```

```python
"7".isdigit()      # True          "a".isalpha()    # True
"E".lower()        # "e"           "e" in "aeiou"   # True
```

## חלק א': קוראים וחוזים (כ-10 דקות)

<div dir="rtl">

לכל קטע: **קודם** כתבו חיזוי על הנייר, **אחר כך** הריצו וכתבו מה הודפס בפועל. כדי להריץ, כותבים בתחתית הקובץ שורה עם שם הפעולה וסוגריים, למשל `a1()`.

</div>

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

מדוע האות `W` לא נכנסה? מדוע האות `p` לא נכנסה? (כתבו משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

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

מה בעצם סופר המשתנה `count`? ולמה מוסיפים לו 1 בהדפסה?

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

השלימו את הטבלה על הנייר: בכל סבב כתבו את `ch`, אם התנאי התקיים, ואת `count` **בסוף** הסבב. אחר כך הריצו `a4()` ובדקו שהתשובה זהה.

</div>

| סבב | ch | האם ch == "a"? | count בסוף הסבב |
|---|---|---|---|
| 1 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 2 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 3 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 4 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 5 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |
| 6 | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; |

## חלק ב': כותבים פעולות (כ-36 דקות)

<div dir="rtl">

בכל משימה: כתבו את הפעולה **על הנייר**, הקלידו אותה בקובץ במקום המילה `pass`, הריצו, והשוו לעמודה "צפוי".

</div>

### ב1: מצאו את הבאג (5 דקות)

```python
def count_letter(text, letter):
    for ch in text:
        count = 0
        if ch == letter:
            count += 1
    return count

print(count_letter("sometimes you win sometimes you learn", "e"))
```

<div dir="rtl">

הפעולה אמורה להחזיר `5`. חזו מה היא מחזירה, הריצו, והסבירו למה. תקנו על ידי הזזת שורה אחת.

</div>

| החיזוי שלי | מה הודפס בפועל | ההסבר שלי |
|---|---|---|
| &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp; | &nbsp;<br>&nbsp;<br>&nbsp; |

### ב2: count_char (7 דקות)

<div dir="rtl">

כתבו `count_char(text, letter)` שמחזירה כמה פעמים האות מופיעה בטקסט. **בלי** להשתמש ב-`count()`.

</div>

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_char("sometimes you win sometimes you learn", "e")` | 5 | &nbsp; |
| `count_char("banana", "a")` | 3 | &nbsp; |
| `count_char("banana", "x")` | 0 | &nbsp; |
| `count_char("", "a")` | 0 | &nbsp; |

### ב3: שלוש פעמים כל אות (8 דקות)

<div dir="rtl">

כתבו `triple(text)` שבונה מחרוזת חדשה שבה כל אות מופיעה שלוש פעמים, **ומחזירה** אותה (לא מדפיסה).

</div>

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `triple("Learn")` | LLLeeeaaarrrnnn | &nbsp; |
| `triple("")` | (מחרוזת ריקה) | &nbsp; |

<div dir="rtl">

למה צריך לכתוב `result = ""` **לפני** הלולאה? מה היה קורה אילו כתבנו אותה בתוך הלולאה? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

### ב4: מה יש בתשובה של הבינה המלאכותית? (8 דקות)

<div dir="rtl">

הטקסט הבא נכתב על ידי מודל שפה. כתבו שתי פעולות: `count_letters(text)` סופרת תווים שהם אותיות (`isalpha`), ו-`count_digits(text)` סופרת תווים שהם ספרות (`isdigit`).

</div>

```python
ai = "In 2024 the model answered 3 questions."
```

| כתבו כאן את שתי הפעולות |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_letters(ai)` | 27 | &nbsp; |
| `count_digits(ai)` | 5 | &nbsp; |

<div dir="rtl">

אפשר לספור ספרות בעזרת `ai.count("5")`? למה זה לא מספיק כאן? (משפט אחד)

</div>

| &nbsp;<br>&nbsp; |
|---|

### ב5: כמה תנועות? (8 דקות)

<div dir="rtl">

כתבו `count_vowels(text)` שמחזירה כמה תווים בטקסט הם אחת מהאותיות `a e i o u`, בין אם הן קטנות ובין אם גדולות. רמז: `.lower()` ו-`ch in "aeiou"`.

</div>

| כתבו כאן את הפעולה |
|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

| קריאה | צפוי | בפועל |
|---|---|---|
| `count_vowels("Hello World")` | 3 | &nbsp; |
| `count_vowels("rhythm")` | 0 | &nbsp; |
| `count_vowels("AEIOU")` | 5 | &nbsp; |

## חלק ג': לבית, או לכיתה למי שסיים

### ג1: רק הספרות

<div dir="rtl">

כתבו `only_digits(text)` שבונה ומחזירה מחרוזת שמכילה רק את הספרות של הטקסט. `only_digits("In 2027 I turn 15")` ← `"202715"`.

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

### ג2: מסתירים ספרות

<div dir="rtl">

כתבו `hide_digits(text)` שמחזירה את הטקסט כשכל ספרה מוחלפת בכוכבית. `hide_digits("Room 12 floor 3")` ← `"Room ** floor *"`.
חשבו: למה כדאי להסתיר מספרים לפני ששולחים טקסט למודל שפה?

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

### ג3: בודקים תשובה של AI

```python
answer = "The Moon orbits the Earth. It takes about 27 days. Some answers are wrong, so we check."
```

<div dir="rtl">

הריצו על הטקסט: `count_char(answer, ".")` (כמה משפטים?), `count_char(answer, " ") + 1` (כמה מילים?) ו-`count_digits(answer)`. אחר כך ענו:

1. מה התוכנית שלנו **יכולה** לבדוק על התשובה?
2. מה היא **לא יכולה** לבדוק? (רמז: האם 27 ימים נכון?)

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

### ג4: אתגר

<div dir="rtl">

כתבו `count_each_vowel(text)` שמדפיסה כמה פעמים הופיעה כל אחת מחמש התנועות (חמישה מונים ו-`elif`). `count_each_vowel("Education is the key")` ← `a: 1 e: 3 i: 2 o: 1 u: 1`.

</div>

## שומרים ומסכמים

<div dir="rtl">

1. שומרים: `File › Save As` ← `G8_U5_M3_Classwork_<Name>.py`
2. מניחים את דף העבודה (עם התיקונים בצבע אחר) בתיק, ומביאים אותו לשיעור הבא.

**בדיקת יציאה** (על הנייר, בלי מחשב):

1. איפה כותבים `count = 0` בלולאת ספירה, ולמה שם?
2. מה מודפס אחרי `for ch in "abc": print(ch * 2, end="")`?
3. במה שונה `print(result)` בסוף פעולה מ-`return result`?

</div>
