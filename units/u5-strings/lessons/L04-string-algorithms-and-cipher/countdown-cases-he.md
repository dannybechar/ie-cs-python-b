# שיעורים 8.2–8.7 – מחרוזות

ספירה לאחור: ארבעה תיקים על מחרוזות

<div dir="rtl">

1. נכנסים למשו"ב ומורידים את הקובץ Lessons 8.2–8.7 - Strings.zip
2. פותחים את ה-zip (Extract All) לתיקייה במחשב
3. פותחים ב-Thonny את הקובץ של התיק (השם שלו על הכרטיס)
4. כותבים את הקוד מתחת לשורה של text, בלולאה שעל הלוח
5. מריצים (F5) ומשווים לצפוי. אחר כך משנים את הטקסט לערך הבא ומריצים שוב

</div>

## תיק 1 (5 דקות): ראשון כוכבית אחרון

<div dir="rtl">

התוכנית מדפיסה את התו הראשון של הטקסט, אחריו כוכבית, ואחריה את התו האחרון. למשל Cats הופך ל-C*s.

</div>

<div dir="rtl">

פותחים את הקובץ הבא:

</div>

```python
FirstStarLast_Starter.py
```

<div dir="rtl">

בדיקות – בכל פעם משנים את הטקסט ומריצים. כשהקוד נכון, הפלט שווה לצפוי:

</div>

```python
text = "Cats"
# expected: C*s
text = "Python"
# expected: P*n
text = "a"
# expected: a*a
```

<pagebreak>

## תיק 2 (6 דקות): התו האמצעי

<div dir="rtl">

התוכנית מדפיסה את התו האמצעי של המילה. כשמספר התווים זוגי היא מדפיסה את שני התווים האמצעיים. מילה קצרה מ-3 תווים מודפסת כולה.

</div>

<div dir="rtl">

פותחים את הקובץ הבא:

</div>

```python
MiddleChar_Starter.py
```

<div dir="rtl">

בדיקות – בכל פעם משנים את הטקסט ומריצים. כשהקוד נכון, הפלט שווה לצפוי:

</div>

```python
text = "robot"
# expected: b
text = "python"
# expected: th
text = "a"
# expected: a
text = "ab"
# expected: ab
```

<pagebreak>

## תיק 3 (7 דקות): ראשי תיבות

<div dir="rtl">

התוכנית בונה ומדפיסה מחרוזת מהאות הראשונה של כל מילה.

</div>

<div dir="rtl">

פותחים את הקובץ הבא:

</div>

```python
Initials_Starter.py
```

<div dir="rtl">

בדיקות – בכל פעם משנים את הטקסט ומריצים. כשהקוד נכון, הפלט שווה לצפוי:

</div>

```python
text = "American Standard Code Information Interchange"
# expected: ASCII
text = "grade eight python"
# expected: gep
```

<pagebreak>

## תיק 4 (8 דקות): הצפנה חדשה

<div dir="rtl">

כל אות באנגלית הופכת למספר שלה (קוד ASCII) ואחריו רווח אחד. רווח הופך לשלושה רווחים. כל תו אחר נשאר כמו שהוא. התוכנית מדפיסה את התוצאה.

</div>

<div dir="rtl">

פותחים את הקובץ הבא:

</div>

```python
NumberCipher_Starter.py
```

<div dir="rtl">

בדיקות – בכל פעם משנים את הטקסט ומריצים. כשהקוד נכון, הפלט שווה לצפוי:

</div>

```python
text = "Big Secret!"
# expected: 66 105 103    83 101 99 114 101 116 !
text = "x=1;"
# expected: 120 =1;
text = "go home!"
# expected: 103 111    104 111 109 101 !
```
