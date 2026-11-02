# יחידה 5.4 – מחרוזות

ספירה לאחור: ארבעה תיקים על מחרוזות

<div dir="rtl">

1. נכנסים למשו"ב ומורידים את הקובץ Unit 5.4 - Strings.zip
2. פותחים את ה-zip (Extract All) לתיקייה במחשב
3. פותחים ב-Thonny את הקובץ Countdown_Starter.py – כל ארבעת התיקים בו
4. בכל תיק כותבים את הפעולה במקום המילה pass, בלולאה שעל הלוח
5. מריצים (F5) ומשווים לשורה expected

</div>

## תיק 1 (6 דקות): כמה פעמים מופיע is

<div dir="rtl">

הפעולה מחזירה כמה פעמים מופיעים התווים is בטקסט – בלי השיטה count.

</div>

<div dir="rtl">

הפעולה בקובץ:

</div>

```python
def count_is(text):
    pass
```

<div dir="rtl">

בדיקות – כשהפעולה נכונה, התוצאה שווה לצפוי:

</div>

```python
count_is("this is his list")
# expected: 4
count_is("Mississippi is big")
# expected: 3
```

<pagebreak>

## תיק 2 (7 דקות): ראשי תיבות

<div dir="rtl">

הפעולה בונה ומחזירה מחרוזת מהאות הראשונה של כל מילה.

</div>

<div dir="rtl">

הפעולה בקובץ:

</div>

```python
def initials(text):
    pass
```

<div dir="rtl">

בדיקות – כשהפעולה נכונה, התוצאה שווה לצפוי:

</div>

```python
initials("American Standard Code Information Interchange")
# expected: "ASCII"
initials("grade eight python")
# expected: "gep"
```

<pagebreak>

## תיק 3 (7 דקות): צופן האות הבאה

<div dir="rtl">

כל אות הופכת לאות הבאה באלפבית, z הופכת ל-a, ורווח נשאר רווח. הטקסט באותיות קטנות בלבד.

</div>

<div dir="rtl">

הפעולה בקובץ:

</div>

```python
def next_letters(text):
    pass
```

<div dir="rtl">

בדיקות – כשהפעולה נכונה, התוצאה שווה לצפוי:

</div>

```python
next_letters("abcd")
# expected: "bcde"
next_letters("zoo")
# expected: "app"
next_letters("i like python")
# expected: "j mjlf qzuipo"
```

<pagebreak>

## תיק 4 (8 דקות): המילה הראשונה והאחרונה

<div dir="rtl">

הפעולה מחזירה את המילה הראשונה ואת המילה האחרונה, עם רווח אחד ביניהן. טקסט של מילה אחת מוחזר כמו שהוא.

</div>

<div dir="rtl">

הפעולה בקובץ:

</div>

```python
def first_and_last_word(text):
    pass
```

<div dir="rtl">

בדיקות – כשהפעולה נכונה, התוצאה שווה לצפוי:

</div>

```python
first_and_last_word("Cats and dogs are great friends")
# expected: "Cats friends"
first_and_last_word("Hello")
# expected: "Hello"
```
