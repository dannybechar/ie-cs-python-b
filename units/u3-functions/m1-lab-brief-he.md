# יחידה 3.1 – פעולות

כיתה ח׳ · AI + Python B · **כמה פרמטרים וערך חוזר**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `print` רק מציגה ערך על המסך. `return` שולחת ערך חזרה לשורה שזימנה את הפעולה — ורק ערך שחזר אפשר לשמור, להשוות ולהשתמש בו.

## דף עזר

```python
def print_total(product, price, quantity):
    total = price * quantity
    print("Total for", product, "is:", total, "shekels")


def square_return(num):
    return num ** 2


print_total("pencil", 3, 5)
x = square_return(5)
print(x)
```

<div dir="rtl">

- מספר הארגומנטים בזימון חייב להיות שווה למספר הפרמטרים בהגדרה, והם מתאימים **לפי הסדר**.
- `return` עוצרת את הפעולה מיד. שורה שאחריה באותו מסלול לא תרוץ.
- פעולה בלי `return` מחזירה `None`.

</div>

## 1. חימום: הפעולה שמדפיסה None

פתחו את `Return_Starter.py`. הריצו וקראו מה מודפס. הוסיפו מילה אחת כדי שהפעולה תחזיר את המספר כפול שלוש.

```python
def triple(num):
    num * 3


result = triple(7)
print(result)
```

## 2. משימה 1: מעקב ושגיאה

בכל סעיף **קודם כותבים על הנייר מה יודפס**, ורק אחר כך מריצים (הסירו את סימן `#` מהשורות בקובץ).

```python
def calculate_box(length, width):
    area = length * width
    print("Area is:", area)


calculate_box(4, 5)
```

```python
def sum_prices(item1, item2, item3):
    return item1 + item2 + item3


total = sum_prices(25, 40)
print("Total price:", total)
```

```python
def check_pass(grade):
    if grade >= 60:
        return "Pass"
        print("Congratulations!")
    return "Fail"


result = check_pass(85)
print("Result:", result)
```

<div dir="rtl">

- בסעיף השני: מה השגיאה, ואיך מתקנים את הזימון?
- בסעיף השלישי: מה יודפס, ולמה ההודעה השנייה לא מופיעה?

</div>

## 3. משימה 2: rectangle_perimeter

השלימו את החסר. הפעולה **מחזירה** את היקף המלבן.

```python
def rectangle_perimeter(length, width):
    perimeter = 2 * (________ + ________)
    ________ perimeter


res = rectangle_perimeter(6, 3)
print("Perimeter:", res)
```

פלט צפוי: `Perimeter: 18`

## 4. משימה 3: מ-print ל-return

הפעולה הזאת מדפיסה את השכר. שנו אותה כך שתחזיר את השכר, שמרו את התוצאה במשתנה `total` והדפיסו אותו.

```python
def calculate_pay(hours, wage):
    pay = hours * wage
    print("Total pay:", pay)
```

בדקו עם `calculate_pay(8, 50)`. פלט צפוי: `Total pay: 400`

## 5. משימה 4: get_cheaper

כתבו פעולה שמקבלת שני מחירים ומחזירה את הנמוך. בדקו עם `80` ו-`55`.

פלט צפוי: `Cheaper price is: 55`

## 6. אם יש זמן

כתבו `average_grade(grade1, grade2)` שמחזירה את הממוצע. השתמשו בערך החוזר בתוך `if`: אם הממוצע 60 ומעלה הדפיסו `Passed`, אחרת `Failed`. בדקו עם `55` ו-`65`.

## 7. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U3_M1_Return_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. פעולה אמורה להחזיר את הכפולה של מספר פי שניים, אבל הזימון מדפיס `None`. מה חסר?
2. הפעולה הוגדרה `def f(a, b):` והזימון הוא `f(5)`. מה קורה, ומה שם השגיאה?
3. מה ההבדל בין `print(x)` בתוך פעולה לבין `return x`?

</div>
