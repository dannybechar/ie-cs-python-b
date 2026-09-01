# G9 Unit 1 Meeting 2 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Search the Collection - תבניות אלגוריתמיות + כניסה ל-Dictionary

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Lab + Knowledge (official topic boundary)  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - first 45 min completes the official 2h simple-structure algorithm practice
- second 45 min is the official 1h Dictionary theory block
- functions may be used as prior knowledge, not re-taught

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **collection → scan → update state → result**

    חיפוש, מניה, סכימה ומקסימום שונים במטרה - אבל כולם מבוססים על מעבר שיטתי ועדכון state.

    Workflow: **Read → Trace → Predict → Run → Modify → Build → Explain**

    ---

    ## 3. Misconception Risks

    - חיפוש סדרתי חייב לעצור מיד כשמוצאים ערך
- max יכול תמיד להתחיל מ-0
- Dictionary הוא List עם שני indexes
- in על Dictionary בודק values כברירת מחדל

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Use manual scan patterns rather than only sum/min/max built-ins so tracing remains visible and assessable.
- Do not initialize max to 0 as a generic rule; start from an existing collection value.
- Place the Dictionary concept exactly in the second academic hour so the official 2h simple-structure algorithm block is completed first.
- Teach dict membership as key membership and avoid adding methods such as get/items unless they solve a clear later need.

    ---

    ## 5. 90-Minute Sequence

    ### 0-12 min - Trace integrated scan
Track found, count, total and highest across the list.

### 12-26 min - Pattern isolation
Short focused examples for search/count/sum/max.

### 26-40 min - Apply to simple structures
Use the same scan idea on List/Tuple/Set where appropriate.

### 40-45 min - Buffer + transition
Close simple-structure practice before introducing Dictionary.

### 45-57 min - Dictionary problem
Why name→score is awkward with positional lookup.

### 57-70 min - Key/value operations
Create, access and membership.

### 70-83 min - Add/update/delete
Mutate a score book safely.

### 83-90 min - Protected Score Book + exit
Build a small mapping and explain the key choice.


    ---

    ## 6. Starter Code

    File: `G9_U1_M2_CollectionScan_Starter.py`

    ```python
    values = [12, 7, 18, 4, 15]
target = 18
found = False
count_high = 0
total = 0
highest = values[0]

for value in values:
    total += value
    if value == target:
        found = True
    if value >= 10:
        count_high += 1
    if value > highest:
        highest = value

print(found, count_high, total, highest)
    ```

    ---

    ## 7. Protected Core Task - Score Book

    - צרו Dictionary עם לפחות 3 תלמידים וציונים
- הדפיסו ציון לפי key
- בדקו membership של תלמיד לפני lookup
- עדכנו ציון קיים והוסיפו תלמיד חדש
- מחקו key אחד באמצעות del
- הסבירו למה student name הוא key מתאים

    המשימה בודקת model של key→value, לא רק כתיבת סוגריים מסולסלים.

    ---

    ## 8. Assessment Evidence

    - Trace a manual collection scan
- Apply count/sum/max correctly
- Create and safely access a Dictionary
- Explain what the keys represent

    ---

    ## 9. Exit Check

    ```python
    scores = {"Dana": 82, "Ali": 91}
print("Ali" in scores)
print(scores["Ali"])
    ```

    איזה זוג פלטים יתקבל?

    Options: True, 91, 91, True, False, 91

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M2_Lesson_Strategy_v2.md`
- `G9_Unit1_M2_Lesson_HE_v1.pptx`
- `G9_U1_M2_CollectionScan_Starter.py`
- `G9_Unit1_M2_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M2_Lab_Brief_HE_v1.pdf`
- `G9_U1_M2_ScoreBook_Reference_v1.py`
- `G9_U1_M2_Exit_Check_HE_v1.png`
