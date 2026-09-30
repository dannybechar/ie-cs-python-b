# יחידה 8.1 – סיווג

כיתה ח׳ · AI + Python B · **סיווג, תכונות וקו מפריד**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> סיווג משייך דוגמה לאחת מקטגוריות קבועות, לפי התכונות שלה. קו מפריד הוא בחירה של מתכנן המערכת — לא עובדה שהתגלתה בטבע.

## דף עזר

```python
def classify_fruit(color, shape, hardness):
    color = color.lower()
    shape = shape.lower()
    hardness = hardness.lower()

    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"
```

<div dir="rtl">

תכונה טובה היא גם **רלוונטית** (קשורה לקטגוריה) וגם **מבדילה** (באמת משתנה בין הקטגוריות).

</div>

## 1. חימום: המקרה שלא התאים

פתחו את `Classifier_Starter.py`.

```python
def classify_fruit(color, shape, hardness):
    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"


print(classify_fruit("Yellow", "Long", "Soft"))
```

חזו `banana`, הריצו — מקבלים `unknown`. אותיות רישיות בקלט לא תואמות את המחרוזות הקטנות שבחוקים. תקנו: נרמלו עם `.lower()` על כל קלט.

## 2. משימה 1: מסווג לפי מזג אוויר

כתבו `classify_activity(temperature, raining, strong_wind)`, שמחזירה `"indoor"` או `"outdoor"`: גשם או רוח חזקה ← indoor; אחרת טמפרטורה בין 18 ל-30 (כולל) ← outdoor, אחרת indoor. מצאו **שני** מקרי קצה שבהם ההחלטה מרגישה שגויה או חסרה, וציינו את התכונה החסרה בכל אחד.

## 3. משימה 2: מעקב לפני הרצה

```python
def classify_level(score, attempts):
    if score >= 80 and attempts <= 3:
        return "advanced"
    elif score >= 50:
        return "intermediate"
    else:
        return "beginner"
```

עקבו על דף אחר `(90, 2)`, `(90, 6)`, `(55, 8)`, `(40, 1)` לפני שמריצים.

## 4. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U8_M1_Classifier_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מהי תכונה?
2. מהו קו מפריד?
3. תנו דוגמה לתכונה מקרית.
4. מדוע בננה ירוקה היא מקרה קצה למסווג צבע פשוט?

</div>
