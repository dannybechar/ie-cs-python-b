# יחידה 7.2 – רשימות

כיתה ח׳ · AI + Python B · **פעולות על רשימה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> לכל פעולה על רשימה יש תפקיד אחד ותוצאה אחת מדויקת. `sort()` ו-`reverse()` משנות את הרשימה עצמה ומחזירות `None`. רשימה **חדשה** בונים עם `result = []` לפני הלולאה ו-`result.append(item)` בתוכה.

## דף עזר

```python
my_lst = list()               # כמו []
my_lst.append(4)              # הוספה לסוף
my_lst.insert(0, 9)           # הוספה במקום 0: קודם מקום, אחר כך ערך
my_lst.extend([7, 8])         # מוסיפה כל פריט מהרשימה השנייה
my_lst.count(4)               # כמה פעמים
my_lst.index(4)               # המקום הראשון (שגיאה אם אין)
my_lst.remove(4)              # מוחקת את הראשון שערכו 4
last = my_lst.pop()           # מוחקת את האחרון ומחזירה אותו
first = my_lst.pop(0)         # מוחקת את מקום 0 ומחזירה אותו
my_lst.sort()                 # ממיינת במקום, מחזירה None
my_lst.reverse()              # הופכת במקום, מחזירה None

list("cat")                   # ['c', 'a', 't']
"-".join(["a", "b", "c"])     # a-b-c
"a-b-c".split("-")            # ['a', 'b', 'c']

import random
random.choice(["a", "b", "c"])   # איבר אקראי
```

## 1. חימום: משתנה שלא קיים

פתחו את `Operations_Starter.py`. התוכנית אמורה לבנות רשימה חדשה של הטמפרטורות הנמוכות מ-21, אך היא קורסת.

```python
temperature = [25, 20, 21, 24, 21, 24, 21, 16, 23]
new_list = []
for item in temperature:
    if item < 21:
        new_list.append(i)
print(new_list)
```

חזו מה אמור להיות מודפס. הריצו, קראו את הודעת השגיאה (השורה האחרונה ומה שהחץ מצביע עליו) ותקנו.

## 2. משימה 1: רשימה חדשה מתנאי

כתבו `colder_than(values, limit)` שמחזירה רשימה **חדשה** של הערכים הקטנים מ-`limit`. בדקו על `[25, 20, 21, 24, 21, 24, 21, 16, 23]` עם 21 ועם 10.

## 3. משימה 2: אין שמות כפולים

כתבו `join_class(students, name)`. אם השם כבר ברשימה — מדפיסים `"We cannot place you in this class"` ומחזירים `False`. אחרת מוסיפים אותו לסוף ומחזירים `True`. בדקו על `["Dana", "Avi", "Noa"]` עם `"Avi"` ועם `"Lior"`.

```text
We cannot place you in this class
False ['Dana', 'Avi', 'Noa']
True ['Dana', 'Avi', 'Noa', 'Lior']
```

## 4. משימה 3: כולן פלינדרומים?

כתבו `all_palindromes(words)` שמחזירה `True` אם **כל** המילים נקראות אותו דבר מימין ומשמאל, בלי להבדיל בין אותיות גדולות לקטנות (רמז: חיתוך עם צעד `-1` ו-`lower()`). בדקו:

```python
["ABA", "1221", "A12321A"]
["ACA", "AcCA"]
["ACA", "ACB"]
```

כתבו קודם על הדף מה תחזיר כל קריאה.

## 5. משימה 4: split, join ואקראיות

כתבו `to_sentence(text)` שהופכת `"One#Apple#a#day#keeps#the#doctor#away"` למשפט עם רווחים. אחר כך כתבו `random_word(text)` שמחזירה מילה אקראית אחת מהטקסט, והריצו אותה שלוש פעמים.

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U7_M2_Operations_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. איזו פעולה מוסיפה לסוף הרשימה? ואיזו למקום שנבחר?
2. מה מחזירה `pop()`?
3. מה יודפס אחרי הקוד הבא?

</div>

```python
result = [3, 1].sort()
print(result)
```

<div dir="rtl">

4. איך נמנעים מהשגיאה של `index()` על ערך שלא קיים?

</div>
