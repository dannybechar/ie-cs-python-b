# יחידה 5.1 – מחרוזות

כיתה ח׳ · בינה מלאכותית ופייתון ב׳ · **מעבדה כתובה: מחרוזות ולולאות** · 45 דקות

שם: ______________________  תאריך: ______________

<div dir="rtl">

**מחזור העבודה: כותבים על הנייר ← מריצים ב-Thonny ← משווים ← מתקנים בצבע אחר**

- קודם חושבים וכותבים **ביד על הנייר**, ורק אחר כך מקלידים ובודקים. המחשב בודק אותכם, הוא לא פותר במקומכם.
- **בסוף המעבדה מגישים את הדף הזה, עם הקוד כתוב ביד.** מה שתיקנתם אחרי ההרצה כותבים בצבע אחר.
- חמש שאלות ובדיקת יציאה. שאלה שנגמר לה הזמן – עוברים הלאה.
- בכל הדוגמאות כותבים טקסטים **בדויים** בלבד – לא שמות אמיתיים.

</div>

<div dir="rtl">

פותחים ב-Thonny את הקובץ הבא:

</div>

```python
PaperLab_Starter.py
```

## דף עזר

<div dir="rtl">

מקומות במחרוזת, אורך ולולאה על המקומות:

</div>

```python
word = "robot"
len(word)          # 5
word[0]            # "r"     word[-1]   # "t"
for i in range(len(word)):
    print(i, word[i])
```

<div dir="rtl">

בונים מחרוזת חדשה, סופרים, ומחברים מחרוזת למספר:

</div>

```python
new_text = ""                    # before the loop
new_text = new_text + word[0]    # grow it
count += 1                       # count
"Age: " + str(7)                 # "Age: 7"
"*" * 5                          # "*****"
```

<pagebreak>

## שאלה 1: קוראים וחוזים (6 דקות)

<div dir="rtl">

כתבו על הנייר את הפלט של התוכנית. רק אחרי זה הריצו וכתבו מה הודפס בפועל.

</div>

```python
word = "STAR"
result = ""
for i in range(len(word)):
    result = word[i] + result
    print(i, result)
print(result)
```

| החיזוי שלי | מה הודפס בפועל |
|---|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; | &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

<div dir="rtl">

מה התוכנית בונה? כתבו משפט אחד.

</div>

| &nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 2: מצאו את הבאג (6 דקות)

<div dir="rtl">

התוכנית אמורה להדפיס כל אות עם המקום שלה. חזו מה היא מדפיסה, הריצו, וקראו את השגיאה.

</div>

```python
word = "STAR"
for i in range(len(word) + 1):
    print(i, word[i])
```

| החיזוי שלי | מה הודפס בפועל |
|---|---|
| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; | &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |

<div dir="rtl">

הסבירו למה התוכנית נעצרת ובאיזה ערך של i. אחר כך כתבו את שורת ה-for המתוקנת.

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 3: כינוי טייס (10 דקות)

<div dir="rtl">

כתבו תוכנית שקוראת כינוי. כל עוד הכינוי קצר מ-4 תווים, היא מדפיסה הודעה ושואלת שוב. אחר כך היא מדפיסה את האות הראשונה, את האות האחרונה ואת האורך, ובונה קוד: אות ראשונה, אות אחרונה, מקף ואורך.

</div>

<div dir="rtl">

דוגמת הרצה (הקלט של המשתמש: `ox`, אחר כך `FALCON`):

</div>

```text
Callsign: ox
Too short, try again
Callsign: FALCON
First: F
Last: N
Length: 6
Code: FN-6
```

<div dir="rtl">

כתבו את הקוד כאן:

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 4: הודעה סודית (10 דקות)

<div dir="rtl">

כתבו תוכנית שקוראת הודעה ואות. התוכנית מדפיסה את ההודעה עם כוכבית בין כל שני תווים, ומדפיסה כמה פעמים האות מופיעה בהודעה.

</div>

<div dir="rtl">

דוגמת הרצה (הקלט של המשתמש: `BANANA`, אחר כך `A`):

</div>

```text
Message: BANANA
Letter: A
B*A*N*A*N*A
A appears 3 times
```

<div dir="rtl">

כתבו את הקוד כאן:

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## שאלה 5: כרטיס כניסה (10 דקות)

<div dir="rtl">

כתבו תוכנית שקוראת שם וגיל. הגיל חייב להיות בין 1 ל-120, וכל עוד הוא לא תקין שואלים שוב. התוכנית מדפיסה כרטיס ממוסגר: שורת כוכביות באורך השם ועוד 4, שורה עם השם בין כוכבית ורווח משני הצדדים, ושוב שורת כוכביות. אחר כך היא מדפיסה מושב (האות הראשונה של השם והגיל) ואת הגיל בשנה הבאה.

</div>

<div dir="rtl">

דוגמת הרצה (הקלט של המשתמש: `LUNA`, אחר כך `200`, אחר כך `12`):

</div>

```text
Name: LUNA
Age: 200
Age must be 1 to 120
Age: 12
********
* LUNA *
********
Seat: L12
Next year: 13
```

<div dir="rtl">

כתבו את הקוד כאן:

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|

<pagebreak>

## בדיקת יציאה (3 דקות)

```python
text = "PLANET"
```

<div dir="rtl">

מה הערך של כל ביטוי? כתבו תשובה לכל אחד.

</div>

| הביטוי | הערך |
|---|---|
| `text[0]` | &nbsp;<br>&nbsp; |
| `text[-2]` | &nbsp;<br>&nbsp; |
| `len(text)` | &nbsp;<br>&nbsp; |
| `text[len(text)]` | &nbsp;<br>&nbsp; |

<div dir="rtl">

שומרים: `File › Save As` ← `G8_U5_M1_PaperLab_<Name>.py`

</div>

## אם נשאר זמן: הודעה שנקראת אותו דבר בשני הכיוונים

<div dir="rtl">

הוסיפו לשאלה 4 קוד שבונה את ההודעה בסדר הפוך, ומדפיס "Same both ways" אם ההודעה זהה להודעה ההפוכה. נסו עם `ANNA` ועם `BANANA`.

</div>

| &nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp;<br>&nbsp; |
|---|
