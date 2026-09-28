# יחידה 4.1 – להכניס בינה לקוד (API)

כיתה ח׳ · AI + Python B · **מהו API? פונקציית עטיפה שמחזירה תשובה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> תוכנית פייתון לא "הופכת" למודל AI. היא שולחת בקשה דרך API ומקבלת תשובה. פונקציית עטיפה מקבלת פרומפט ומחזירה תשובה עם `return`.

## דף עזר

```text
תוכנית Python → בקשה → API → שירות AI (מודל בשרת) → תשובה → תוכנית Python
```

```python
def ask_ai(prompt):
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text
```

<div dir="rtl">

- מפתח API מזהה ומאשר את הפרויקט — לא סיסמה שמקלידים בצ'אט. הוא נשמר במשתנה סביבה, לא בקובץ, לא בשיחה, לא בצילום מסך.
- תשובת המודל היא ניחוש שמבוסס הסתברות — בודקים אותה, כמו כל קלט אחר.

</div>

> [!NOTE]
> הקבצים כאן פועלים ב**מצב כיתה** — `ask_ai()` מחזירה משפט קבוע, בלי חיבור אמיתי לשירות. זה מכוון, לא קיצור דרך.

## 1. חימום: עטיפה עם שתי תקלות

פתחו את `Wrapper_Starter.py`.

```python
def ask_ai():
    response = "Mock response: balance study, movement, rest, and sleep."
    print(response.text)


answer = ask_ai("Give one healthy study habit.")
print(answer)
```

הריצו וקראו את השגיאה. תקנו תקלה אחת בכל פעם: קודם הפרמטר החסר, ואז `print` במקום `return`.

## 2. משימה 1: הפרמטר וה-return, מאושרים

אחרי התיקון, `answer = ask_ai("Give one healthy study habit."); print(answer)` אמור להדפיס בלי שגיאה. בדקו, והסבירו במשפט אחד למה `answer` היה מקבל `None` אם `ask_ai` הייתה עדיין משתמשת ב-`print`.

## 3. משימה 2: בדיקת הפרומפט לפני "הקריאה" לשירות

כתבו גרסה שבודקת קודם את הפרומפט: אם `len(prompt.strip()) < 5`, מחזירים `"The prompt is too short. Please add details."` בלי להמשיך הלאה; אחרת מחזירים את התשובה (המדומה). בדקו עם `"Hi"` ועם פרומפט רגיל.

## 4. דיון: כמה קריאות, ולמה זה משנה

```python
count = 0
while count < 20:
    print(ask_ai("Give one study tip."))
    count += 1
```

כמה קריאות נשלחות כאן? למה זה עלול להיות בעייתי גם עם פונקציה מדומה, ובעייתי באמת עם שירות אמיתי? איך אפשר לשפר?

## 5. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U4_M1_Wrapper_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. API הוא…
2. מפתח API נשמר ב… ולא ב…
3. בפונקציית עטיפה משתמשים ב-`return` משום ש…
4. ציירו ארבע קופסאות המתארות את מסלול הבקשה והתשובה.

</div>
