# G9 Unit 1 Meeting 1 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Choose the Structure - Bridge: List, Tuple, Set - בוחרים ייצוג מתאים

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Lab + Lab (bridge + practice)  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - Grade 8 included List; Tuple/Set are explicitly bridged here
- first half completes the 1h List/Tuple/Set bridge
- second half begins algorithm practice on simple structures

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **problem need → representation → operations**

    שואלים קודם מה המידע צריך לעשות: לשמור סדר? להשתנות? למנוע כפילויות? ורק אז בוחרים מבנה.

    Workflow: **Read → Predict → Compare → Modify → Build → Explain**

    ---

    ## 3. Misconception Risks

    - Tuple הוא “List עם סוגריים אחרים” ולכן אפשר לעדכן אותו
- Set שומר סדר מיקומים ולכן אפשר להשתמש ב-[0]
- List תמיד עדיף כי הוא הכי גמיש
- בחירת מבנה היא החלטת syntax ולא החלטת פתרון

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Treat List as reactivation but Tuple/Set as a focused bridge because the new Grade 8 Part B does not make them Core.
- Do not ask students to predict Set iteration/print order.
- Keep Dictionary completely out of the first 45-minute bridge; it starts in Meeting 2 according to the unit hour allocation.
- Require a representation explanation so the lesson is not reduced to bracket syntax.

    ---

    ## 5. 90-Minute Sequence

    ### 0-12 min - List reactivation
Short read/predict/modify work; no re-teaching of all list methods.

### 12-27 min - Tuple bridge
Fixed records, indexing, and the practical meaning of immutability.

### 27-42 min - Set bridge
Uniqueness, membership, add/remove; explicitly no indexing.

### 42-52 min - Starter prediction
Predict len/index/membership before Run.

### 52-68 min - Modify + compare
Represent similar information in List, Tuple and Set and observe what changes.

### 68-84 min - Protected Event Sign-up
Build a small program using all three structures for distinct roles.

### 84-90 min - Save + exit
Explain one representation decision and complete the visual exit check.


    ---

    ## 6. Starter Code

    File: `G9_U1_M1_StructureBridge_Starter.py`

    ```python
    names = ["Dana", "Ali", "Dana"]
point = (4, 7)
tags = {"python", "ai", "python"}

print(len(names))
print(point[1])
print(len(tags))
print("ai" in tags)
    ```

    ---

    ## 7. Protected Core Task - Event Sign-up

    - צרו List של חמש הרשמות, כולל לפחות כפילות אחת
- צרו Set מתוך הרשימות כדי לדעת כמה תלמידים ייחודיים נרשמו
- צרו Tuple קבוע עבור (room, day)
- הציגו מספר הרשמות, מספר תלמידים ייחודיים, room ו-day
- הסבירו למה כל אחד משלושת המבנים מתאים לתפקיד שלו

    אין צורך ב-Dictionary עדיין. המטרה היא בחירת ייצוג נכונה.

    ---

    ## 8. Assessment Evidence

    - Predict len / index / membership before Run
- Use List, Tuple and Set without illegal operations
- Create a derived unique set from registrations
- Explain why each representation matches the problem

    ---

    ## 9. Exit Check

    ```python
    tags = {"ai", "python", "ai"}
print(len(tags))
    ```

    מה יודפס?

    Options: 1, 2, 3

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M1_Lesson_Strategy_v2.md`
- `G9_Unit1_M1_Lesson_HE_v1.pptx`
- `G9_U1_M1_StructureBridge_Starter.py`
- `G9_Unit1_M1_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M1_Lab_Brief_HE_v1.pdf`
- `G9_U1_M1_EventSignup_Reference_v1.py`
- `G9_U1_M1_Exit_Check_HE_v1.png`
