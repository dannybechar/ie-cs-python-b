# G9 Unit 1 Meeting 5 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Scan Nested Data - אלגוריתמים על records ומבנים מורכבים

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Lab + Lab  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - first 45 min completes the 2 practical hours of the complex-structure block
- second 45 min begins the final 3h algorithm-on-complex-data block
- manual loops remain visible for tracing and explanation

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **records → inspect fields → update state → derived result**

    אותן תבניות count/sum/max חוזרות, אבל הפעם הערך שאנו בודקים נמצא בתוך record.

    Workflow: **Read → Trace → Predict → Modify → Build → Test → Explain**

    ---

    ## 3. Misconception Risks

    - nested loop תמיד נדרש כדי לעבור על list of tuples
- אפשר להשוות record שלם כאשר רוצים max לפי score בלי לחשוב על field
- כש-top_score משתנה אין צורך לעדכן top_name
- מבנה נגזר חייב להיות מאותו סוג כמו המקור

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Transfer previously learned scan patterns to record fields instead of introducing new algorithm families.
- Keep manual count/sum/max loops visible; built-ins would hide the state changes the checkpoint needs to assess.
- Introduce derivation as a simple append-based result list, not comprehensions.
- Require top_name and top_score to update together so students reason about record-level state.

    ---

    ## 5. 90-Minute Sequence

    ### 0-14 min - Trace starter
Follow total/count/top state across records.

### 14-28 min - Record modifications
Append/replace and predict effect on results.

### 28-43 min - Derived collection
Build selected names from record conditions.

### 43-45 min - Buffer
Reset before the final algorithm block.

### 45-58 min - Search in records
Find a matching record by one field.

### 58-72 min - Stats challenge
Combine count, sum and max.

### 72-85 min - Protected Class Stats
Build full record-processing solution.

### 85-90 min - Save + exit
Trace a final count without running.


    ---

    ## 6. Starter Code

    File: `G9_U1_M5_NestedAlgorithms_Starter.py`

    ```python
    records = [("Dana", 82), ("Ali", 91), ("Maya", 76), ("Omar", 88)]

total = 0
count_high = 0
top_name = records[0][0]
top_score = records[0][1]

for record in records:
    score = record[1]
    total += score
    if score >= 80:
        count_high += 1
    if score > top_score:
        top_name = record[0]
        top_score = score

print(total, count_high, top_name, top_score)
    ```

    ---

    ## 7. Protected Core Task - Class Stats

    - השתמשו ב-List of Tuples מסוג (name, score)
- חשבו total score ידנית בלולאה
- ספרו כמה scores הם לפחות 80
- מצאו top_name ו-top_score
- בנו List חדש של names עם score לפחות 85
- הדפיסו פלט ידידותי והסבירו איזה state נשמר בכל pattern

    אין להשתמש ב-sum/max כדי לעקוף את tracing; המטרה היא algorithm pattern.

    ---

    ## 8. Assessment Evidence

    - Trace state while scanning records
- Apply count/sum/max to a field inside each record
- Keep related best-record state consistent
- Generate a new structure from an existing one

    ---

    ## 9. Exit Check

    ```python
    records = [("Dana", 82), ("Ali", 91), ("Maya", 76)]
count = 0
for record in records:
    if record[1] >= 80:
        count += 1
print(count)
    ```

    מה יודפס?

    Options: 1, 2, 3

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M5_Lesson_Strategy_v2.md`
- `G9_Unit1_M5_Lesson_HE_v1.pptx`
- `G9_U1_M5_NestedAlgorithms_Starter.py`
- `G9_Unit1_M5_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M5_Lab_Brief_HE_v1.pdf`
- `G9_U1_M5_ClassStats_Reference_v1.py`
- `G9_U1_M5_Exit_Check_HE_v1.png`
