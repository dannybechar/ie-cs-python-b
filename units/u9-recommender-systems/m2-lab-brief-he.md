# יחידה 9.2 – מערכות המלצה

כיתה ח׳ · AI + Python B · **מקריאת CSV לחישוב דמיון**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> שני `0` באותו מיקום לא נחשבים התאמה — שניהם "לא מכיר/ה". בודקים ששני הדירוגים שונים מ-0 לפני שמשווים.

## דף עזר

```python
def similarity_score(first, second):
    matches = 0
    common = 0
    for index in range(len(first)):
        if first[index] != 0 and second[index] != 0:
            common += 1
            if first[index] == second[index]:
                matches += 1
    return matches, common
```

<div dir="rtl">

- `aliases[i]` ו-`ratings[i]` מתארים אותו משתמש — לכן הן רשימות מקבילות.
- `matches` גולמי מעדיף משתמש עם יותר פריטים משותפים. `matches / common` (**השיעור**) מתקן זאת.

</div>

## 1. טבלת מעקב — חזו לפני שמריצים

```python
user_a = [3, 1, 0, 3, 2]
user_b = [3, 1, 3, 2, 2]
```

<div dir="rtl">

| `i` | `user_a[i]` | `user_b[i]` | משותף? | שווה? | `matches` | `common` |
|---:|---:|---:|---|---|---:|---:|
| 0 | 3 | 3 | | | | |
| 1 | 1 | 1 | | | | |
| 2 | 0 | 3 | | | | |
| 3 | 3 | 2 | | | | |
| 4 | 2 | 2 | | | | |

</div>

## 2. חימום: `0 == 0` נראה כמו הסכמה, אבל לא

פתחו את `Similarity_Starter.py`.

```python
def broken_similarity(first, second):
    matches = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            matches += 1
    return matches


print(broken_similarity([0, 1, 3], [0, 1, 2]))
```

חזו `1` (רק אינדקס 1 הוא הסכמה אמיתית), הריצו — מקבלים `2`. שני "לא מכיר/ה" נספרים כאילו הסכימו. תקנו: השוו רק כששני הערכים שונים מ-0.

## 3. משימה 1: load_ratings("ratings.csv")

השלימו את הפונקציה (הוסיפו את הכינוי ואת שורת הדירוגים הממירה ללולאה) והדפיסו את שלוש התוצאות.

## 4. משימה 2: similarity_score(first, second)

אשרו על `similarity_score([3, 1, 0, 3, 2], [3, 1, 3, 2, 2])` ← `(3, 4)`, ואז הריצו את הבדיקות:

```python
assert similarity_score([3, 1], [3, 1]) == (2, 2)
assert similarity_score([0, 1], [0, 1]) == (1, 1)
assert similarity_score([0, 0], [3, 2]) == (0, 0)
assert similarity_score([3, 1], [1, 3]) == (0, 2)
```

## 5. משימה 3: similarity_rate(first, second)

`matches / common`, או `0.0` אם `common` הוא 0. אשרו: `similarity_rate([3, 1, 0], [3, 1, 2])` ← `1.0`.

## 6. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U9_M2_Similarity_<Name>.py`

---

**בדיקת יציאה:**

<div dir="rtl">

1. מדוע נדרש התנאי `first[index] != 0 and second[index] != 0`?
2. מה ההבדל בין `matches` ל-`common`?
3. מה הסיכון בשיעור התאמה של 100% המבוסס על פריט יחיד?

</div>
