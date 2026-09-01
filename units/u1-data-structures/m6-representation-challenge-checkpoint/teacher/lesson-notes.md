# G9 Unit 1 Meeting 6 Lesson Strategy v2

    ## Grade 9 / Python C - Transition Year
    ### Representation Challenge - Unit 1 Checkpoint - לבחור ייצוג, לעבד ולהסביר

    **Status:** Approved after critical review; ready for asset creation  
    **Duration:** 90 minutes  
    **Structure:** Lab + Lab (integrated checkpoint)  
    **Current tool assumption:** Thonny, with IDE-neutral lesson content

    ---

    ## 1. Position and Official Scope

    This meeting belongs to **Unit 1 - Data Structures (12 academic hours)**.

    - completes the final 2h of the official complex-data algorithm block
- checkpoint is embedded inside the 12 official hours
- students must justify representation, not only produce output

    Deliberate boundaries:
    - no classes or OOP (Unit 2)
    - no event-driven programming (Units 3-4)
    - no comprehensions or advanced Python shortcuts as Core
    - algorithmic reasoning and representation choice take priority over syntax memorization

    ---

    ## 2. Core Mental Model

    **problem → representation → algorithm → derived data → explanation**

    Unit 1 נסגר רק כאשר התלמיד יודע לבחור structure, לעבד אותו ולנמק את הבחירה.

    Workflow: **Read → Plan → Choose → Build → Test → Debug → Explain**

    ---

    ## 3. Misconception Risks

    - צריך לבחור structure אחד לכל הבעיה
- Set יכול לשמור כמה pages שייכים לכל student
- Dictionary מתאים ל-event log אם אותו student מופיע כמה פעמים בלי aggregation
- אם התוכנית מדפיסה מספרים נכונים אין צורך להסביר representation

    ---

    ## 4. Critical Review Decisions Incorporated in v2

    - Keep the checkpoint fully inside the official Unit 1 hours; no extra assessment lesson.
- Use one coherent dataset that naturally requires multiple representations rather than six disconnected syntax questions.
- Require manual aggregation and a representation rationale so the task measures algorithmic ownership.
- Do not introduce classes as an “extension”; Unit 2 begins only after this checkpoint.

    ---

    ## 5. 90-Minute Sequence

    ### 0-10 min - Read specification
Identify source data, required results and constraints.

### 10-20 min - Representation plan
Choose structures before writing code.

### 20-35 min - Core scan
Calculate total pages and count large entries.

### 35-48 min - Derived Set
Collect unique genres.

### 48-63 min - Derived Dictionary
Aggregate pages by student.

### 63-76 min - Top reader
Scan the derived dictionary for max.

### 76-86 min - Test + debug
Change one record and verify expected impact.

### 86-90 min - Explain + submit
Short ownership explanation and exit check.


    ---

    ## 6. Starter Code

    File: `G9_U1_M6_ReadingChallenge_Starter.py`

    ```python
    reads = [
    ("Dana", "Fantasy", 120),
    ("Ali", "Science", 80),
    ("Dana", "Mystery", 60),
    ("Maya", "Fantasy", 150),
    ("Ali", "Fantasy", 40)
]

# Build your analysis below.
# Do not change the data.
    ```

    ---

    ## 7. Protected Core Task - Reading Challenge Analyzer

    - השתמשו ב-List of Tuples הנתון כ-event log
- חשבו total pages ידנית בלולאה
- ספרו כמה entries הם לפחות 100 pages
- בנו Set של genres ייחודיים
- בנו Dictionary של total pages לכל student
- מצאו את top reader מתוך ה-Dictionary
- כתבו 2-3 משפטים שמנמקים את בחירת המבנים
- בדקו עם לפחות שינוי dataset אחד לפני submission

    זהו checkpoint של Unit 1: representation + algorithm + explanation. אין Classes.

    ---

    ## 8. Assessment Evidence

    - Choose structures that match the required information
- Implement traceable aggregation algorithms
- Generate Set and Dictionary derived from complex source data
- Explain and defend representation/state decisions

    ---

    ## 9. Exit Check

    ```python
    reads = [("Dana", 120), ("Ali", 80), ("Dana", 60)]
pages = {}
for record in reads:
    name = record[0]
    amount = record[1]
    if name in pages:
        pages[name] += amount
    else:
        pages[name] = amount
print(pages["Dana"])
    ```

    מה יודפס?

    Options: 120, 180, 60

    ---

    ## 10. Required Lesson Assets

    - `G9_Unit1_M6_Lesson_Strategy_v2.md`
- `G9_Unit1_M6_Lesson_HE_v1.pptx`
- `G9_U1_M6_ReadingChallenge_Starter.py`
- `G9_Unit1_M6_Lab_Brief_HE_v1.docx`
- `G9_Unit1_M6_Lab_Brief_HE_v1.pdf`
- `G9_U1_M6_ReadingChallenge_Reference_v1.py`
- `G9_U1_M6_Exit_Check_HE_v1.png`
