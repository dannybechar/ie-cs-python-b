# יחידה 7.2 – רשימות

כיתה ח׳ · AI + Python B · **פעולות על רשימה**

**קוראים ← חוזים ← מריצים ← בודקים ← מתקנים**

> [!IMPORTANT]
> `append` מוסיפה איבר אחד, `extend` מוסיפה כמה איברים. `remove` מוחקת לפי ערך, `pop` מוציאה לפי אינדקס ומחזירה את הערך.

## דף עזר

```python
tasks = ["study", "exercise"]
tasks.append("rest")
tasks.extend(["read", "sleep"])
tasks.insert(1, "eat")
```

```python
scores = [72, 95, 61]
ordered = scores.sort()   # ממיינת במקום, ומחזירה None
print(ordered)              # None
```

<div dir="rtl">

- `remove(value)` מוחקת לפי **ערך**; בדקו `in` לפני, אחרת `ValueError`.
- `pop(index)` מוחקת לפי **אינדקס** ו**מחזירה** את הערך שהוצא.
- `text.split(sep)` מחזירה רשימה; `sep.join(list)` מחברת רשימת מחרוזות חזרה לטקסט.

</div>

## 1. חימום: ממוינת, אבל לתוך כלום

פתחו את `Operations_Starter.py`.

```python
scores = [72, 95, 61]
ordered = scores.sort()
print(ordered)
```

חזו רשימה ממוינת, הריצו — מקבלים `None`. `sort()` ממיינת את `scores` במקום ומחזירה `None`. תקנו: קודם העתיקו, ואז מיינו את העותק.

## 2. משימה 1: safe_remove(items, target)

בודקת `target in items` לפני המחיקה; אם קיים — מוחקת ומחזירה `True`, אחרת מדפיסה `"Task not found"` ומחזירה `False`. בדקו על `["study", "exercise"]` עם `"exercise"` ועם `"rest"`.

## 3. משימה 2: process_queue(tasks)

כל עוד הרשימה לא ריקה, `pop(0)` את המשימה הראשונה ומדפיסים `"Working on: <task>"`. בדקו על `["collect data", "run model", "check result"]`.

## 4. משימה 3: csv_round_trip(text)

מפצלת את `text` לפי `","` ומחברת מחדש עם `" | "`. בדקו על `"cat,dog,bird"`.

## 5. מתעדים ושומרים

שומרים: `File › Save As` ← `G8_U7_M2_Operations_<Name>.py`

---

**בדיקת יציאה — התאימו פעולה למטרה:**

<div dir="rtl">

1. הוספת איבר יחיד בסוף
2. הוספת כמה איברים בסוף
3. מחיקה לפי ערך
4. הוצאה לפי אינדקס והחזרת הערך
5. מיון במקום

</div>
