# G9 Unit 1 Meeting 4 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Data Inside Data - מבני נתונים מורכבים - records בתוך collection

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Knowledge + Lab  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - this meeting contains the second and final 1h theory block of Unit 1
- begins the official 2h practical work on complex structures
- use only list of lists / list of tuples as the main Core examples

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **outer collection → record → field**

    Index ראשון בוחר record. Index שני בוחר field בתוך אותו record.

    Workflow: **Read → Map Indices → Predict → Run → Modify → Build → Explain**

    ---

    ## 3. Misconception Risks

    - students[1][0] הוא “index 10”
- כל bracket pair ניגש לאותו collection
- Tuple פנימי מונע הוספת record חדש ל-outer List
- מבנה מורכב הוא תמיד Dictionary

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Place the second official theory hour here, where complex structure actually becomes a new concept.
- Use list-of-lists and list-of-tuples as the Core examples because they are explicitly named in the official curriculum.
- Delay nested dictionaries and OOP records to avoid scope creep into Unit 2.
- Teach nested access as two explicit decisions (record then field) to reduce index confusion.

    ---

    ## 5. 90-Minute Sequence

    ### 0-10 min - Parallel-list problem
Expose why related fields need to stay together.

### 10-23 min - Outer + inner model
Define record and field conceptually.

### 23-35 min - List of lists
Nested indexing and mutable inner data.

### 35-45 min - List of tuples
Fixed inner record with mutable outer collection.

### 45-55 min - Starter prediction
Map each index before Run.

### 55-68 min - Modify records
Append and replace records.

### 68-84 min - Protected Tournament Results
Construct and explain a list of tuple records.

### 84-90 min - Save + exit
One nested-index check and explanation.


    ---

    ## 6. Starter Code

    File: `G9_U1_M4_ComplexStructures_Starter.py`

    ```python
    students = [["Dana", 82], ["Ali", 91], ["Maya", 76]]
fixed_records = [("Dana", 82), ("Ali", 91), ("Maya", 76)]

print(students[1][0])
print(students[2][1])
print(fixed_records[0][1])
    ```

    ---

    ## 7. Protected Core Task - Tournament Results

    - צרו List של לפחות 4 Tuple records מסוג (name, score)
- הדפיסו record ו-field בעזרת nested index
- הוסיפו record חדש באמצעות append
- עדכנו score על ידי החלפת tuple שלם במקום המתאים
- עברו על records והדפיסו name + score
- הסבירו למה inner Tuple מתאים ל-record קבוע

    אין Classes עדיין. record מורכב מ-built-in structures בלבד.

    ---

    ## 8. Assessment Evidence

    - Map two-stage nested indexing correctly
- Distinguish outer mutability from inner tuple immutability
- Add and replace records safely
- Explain why a list of tuples represents the problem

    ---

    ## 9. Exit Check

    ```python
    records = [("Dana", 3), ("Ali", 5), ("Maya", 4)]
print(records[1][0])
    ```

    מה יודפס?

    Options: Ali, 5, Dana

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M4_Lesson_Strategy_v2.md`
- `G9_Unit1_M4_Lesson_HE_v1.pptx`
- `G9_U1_M4_ComplexStructures_Starter.py`
- `G9_Unit1_M4_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M4_Lab_Brief_HE_v1.pdf`
- `G9_U1_M4_TournamentResults_Reference_v1.py`
- `G9_U1_M4_Exit_Check_HE_v1.png`
