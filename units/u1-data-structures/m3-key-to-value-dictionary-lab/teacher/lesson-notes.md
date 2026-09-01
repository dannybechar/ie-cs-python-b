# G9 Unit 1 Meeting 3 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Key → Value - Dictionary Lab - עובדים עם מיפוי אמיתי

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Lab + Lab  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - completes the 2 practical hours of the official 3h Dictionary block
- students modify state rather than only read literals
- conditions/functions are prior knowledge used inside the problem

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **key → current value → update → new state**

    Dictionary אינו רק lookup table. פעולות התוכנית משנות את המיפוי לאורך הזמן, ולכן צריך לעקוב אחרי state.

    Workflow: **Read → Predict → Modify → Test → Debug → Build → Explain**

    ---

    ## 3. Misconception Risks

    - השמה ל-key חדש תגרום error כי key לא היה קיים
- השמה ל-key קיים מוסיפה entry נוסף
- len(dict) סופר values ייחודיים
- lookup של key חסר תמיד בטוח

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Keep the entire meeting practical because the official Dictionary theory hour was already placed in M2.
- Make dictionary state visible after every mutation to prevent add-vs-update confusion.
- Require membership guarding before user-driven lookup rather than teaching exception handling here.
- Delay nested dictionaries/lists until the official complex-structure block in M4.

    ---

    ## 5. 90-Minute Sequence

    ### 0-12 min - Starter prediction
Track dictionary state after each mutation.

### 12-26 min - Mutation drills
Add, update and delete keys.

### 26-39 min - Safe lookup
Use membership before uncertain access.

### 39-45 min - Debug challenge
Repair a missing-key failure without try/except.

### 45-58 min - Inventory task
Process an item request and update state.

### 58-72 min - Process by key
Loop over dictionary keys and inspect values.

### 72-85 min - Protected Inventory Tracker
Build an input-driven state-changing mapping.

### 85-90 min - Save + exit
Explain the final value of one key.


    ---

    ## 6. Starter Code

    File: `G9_U1_M3_DictionaryLab_Starter.py`

    ```python
    stock = {"pencil": 12, "eraser": 5, "notebook": 8}

print(stock["pencil"])
stock["eraser"] = 7
stock["marker"] = 4

if "notebook" in stock:
    stock["notebook"] -= 1

print(len(stock))
print(stock["notebook"])
    ```

    ---

    ## 7. Protected Core Task - Inventory Tracker

    - התחילו Dictionary של לפחות 4 מוצרים וכמויות
- קלטו item מהמשתמש
- אם item קיים - הפחיתו 1 והציגו את הכמות החדשה
- אם item אינו קיים - הציגו הודעה ידידותית
- הוסיפו מוצר חדש ועדכנו מוצר קיים בקוד
- בשלב תרגול נפרד מחקו key אחד באמצעות del

    המשימה המוגנת אינה דורשת nested data - רק שליטה אמיתית ב-Dictionary state.

    ---

    ## 8. Assessment Evidence

    - Predict dictionary state after mutations
- Distinguish add from update
- Guard a lookup with membership
- Build a state-changing dictionary program

    ---

    ## 9. Exit Check

    ```python
    stock = {"pen": 4}
stock["pen"] = stock["pen"] - 1
print(stock["pen"])
    ```

    מה יודפס?

    Options: 3, 4, KeyError

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M3_Lesson_Strategy_v2.md`
- `G9_Unit1_M3_Lesson_HE_v1.pptx`
- `G9_U1_M3_DictionaryLab_Starter.py`
- `G9_Unit1_M3_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M3_Lab_Brief_HE_v1.pdf`
- `G9_U1_M3_InventoryTracker_Reference_v1.py`
- `G9_U1_M3_Exit_Check_HE_v1.png`
