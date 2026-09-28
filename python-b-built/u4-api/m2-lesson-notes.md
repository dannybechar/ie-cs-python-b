# Unit 4.2 — Bringing AI into Code (API)

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: Dynamic Prompts + the "Balanced Day" Project

**Status:** Built, awaiting teacher approval — staged in `python-b-built/`, not yet in `units/`
**Duration:** 90 minutes
**Structure:** Lab + Lab (24 min guided practice, then 66 min lab, including the capstone project)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny; a language-model API for the live version (see Tool Note)
**Source of inspiration:** `python_b_unit04_api_bring_ai_into_code_complete_unit.md` — meeting 2's own clock table,
the two-prompt comparison, the four-part prompt template, the input-validation and sensitive-word examples, the
accumulation loop, the "Balanced Day" project brief, skeleton, full solution and test-case table, the peer-review
checklist, the answer-critique checklist, and the 20-point rubric kept almost unchanged; the source's
one-call-per-activity antipattern became this meeting's warm-up, read and explained rather than "fixed" line by
line (the point is architectural, not a syntax bug).
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny** or **Tool Note – the AI service**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 4.1 | the API path, the waiter analogy, key security, a wrapper function with `return` | 45 / 45 |
| **4.2 (this)** | **dynamic prompts, input validation, accumulation loops, the "Balanced Day" project** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 12) | Covered here |
|---|---|
| Goal 5: build a dynamic prompt with an f-string and user input | ✅ Task 1, the project |
| Goal 6: accumulate input with a `while` loop and string concatenation | ✅ the project |
| Goal 7: validate input with `len`, compound conditions and `in` | ✅ Task 2, the project |
| Goal 8: explain why data is collected first and one call is made outside the loop | ✅ warm-up, the project |
| Goal 9: rate limits, overload errors, cost | ✅ warm-up discussion |
| Goal 10: privacy; check an answer before relying on it | ✅ the project's output framing, answer critique |

### Deliberate exclusions
The wrapper function itself (built in 4.1; reused here unchanged), new AI concepts (Unit 6).

---

## 3. Lesson Goal

**A good prompt has four parts — role, task, data, and the wanted structure — built from data collected first; the
API is called exactly once, after collection, not once per item.**

---

## 4. Core Mental Models

```python
activities = ""
activity = input("Activity or done: ").strip()

while activity.lower() != "done":            # collect first
    if len(activity) >= 3:
        activities += f"- {activity}\n"
    activity = input("Activity or done: ").strip()

# The loop has already finished here.
prompt = f"Create a balanced plan for these activities:\n{activities}"
answer = ask_ai(prompt)                        # call once, after the loop
```

A prompt worth sending has: **role/context** (who is the model helping?), **task** (what should it produce?),
**data** (what real information from the user?), **structure** (how many parts, what length?).

---

# 5. Guided Practice (0–24)

| Clock | Activity |
|---|---|
| 0–8 | **Recap:** the API path, key security, `return` |
| 8–20 | **Two prompts, compared:** `"Plan my day."` vs. a version with role, task, data (90 min homework, 30 min exercise, a 21:30 deadline) and a wanted structure (four time blocks, one safety reminder) — which gives the model more to work with, and what personal information does neither one need? |
| 20–24 | The four-part template (role, task, data, structure); transition to the lab |

---

# 6. Lab (24–90)

Starter: [`BalancedDay_Starter.py`](BalancedDay_Starter.py). Reference: [`BalancedDay_Reference.py`](BalancedDay_Reference.py).
Classroom mode again — `ask_ai()` returns a fixed string; no key needed for the lab itself (Tool Note below).

## 24–32 — Warm-up: one call per activity

```python
activity = input("Activity or done: ").strip()
while activity.lower() != "done":
    print(ask_ai(f"One tip for fitting in: {activity}"))
    activity = input("Activity or done: ").strip()
```

Run it with `Homework`, `Walk`, `done`. Count the calls (two here — but with ten activities, ten calls). Why is that
wasteful even with a mock function, and a real cost with a real service? This meeting's project fixes exactly this.

## 32–44 — Task 1: a dynamic prompt

Build an f-string prompt from a goal and a minutes count, both read with `input()`. Print the prompt — don't call
`ask_ai` yet.

```text
You help a ninth-grade student plan a balanced afternoon.
Goal: Finish math homework
Available time: 45 minutes
Return three short steps and one reminder to take a break.
```

## 44–57 — Task 2: default value + a basic privacy check

Read a short text. If it's empty, use a default goal (`"create a generally balanced afternoon"`). Separately, check
whether it contains `"password"`, `"phone"` or `"address"` (case-insensitive) and print a warning if it does.

<div dir="rtl">

| קלט | פלט |
|---|---|
| (ריק) | The text passed the basic classroom check: create a generally balanced afternoon |
| my phone is 555-1234 | Do not send passwords, phone numbers, or addresses. |
| review flashcards | The text passed the basic classroom check: review flashcards |

</div>

This is a basic classroom filter, not a full personal-information detector — say so explicitly.

## 57–77 — Task 3 (project): "Balanced Day"

Build a program that: asks for a short daily goal (default if empty); collects activities until `"done"`; skips
activities under 3 characters; skips (with a warning) any activity containing a sensitive word; builds **one**
dynamic prompt from the goal and the collected activities; calls `ask_ai` **once**, after the loop; presents the
result as a suggestion to check, not a fact.

<div dir="rtl">

| מקרה | קלט | תוצאה צפויה |
|---|---|---|
| שימוש רגיל | מטרה ושתי פעילויות תקינות | פרומפט נבנה, קריאה אחת נשלחת |
| פעילות קצרה | `x` | הפעילות לא מצטרפת, מוצגת הודעת תיקון |
| מידע רגיש | טקסט הכולל `password` | הטקסט לא מצטרף, מוצגת אזהרה |
| מטרה ריקה | Enter | ערך ברירת המחדל מופעל |
| אין פעילויות | `done` מיד | נשלח טקסט ברירת מחדל במקום רשימה ריקה |

</div>

## 77–84 — Peer review

Swap with a partner. Check: is the key absent from the code? does the wrapper function return a value? does the
prompt include role, task, data and structure? is data collected before the call? is there exactly one API call?
are empty input, short input and sensitive text all handled? is the answer shown as something to check?

## 84–90 — Answer critique + exit reflection

After a run (real or mock), mark: one detail that clearly comes from the input; one suggestion that looks useful;
one assumption the model added on its own; one detail that needs checking or changing; whether anything in the
answer seems unrealistic or age-inappropriate.

### Tool Note – the AI service
For a real run, follow the same setup as 4.1 (installed library, a valid key as an environment variable). Test the
real call once before class and keep a saved transcript as a fallback if the connection fails during the lesson.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| More detail in the prompt is always better, regardless of source | It should come from real collected data, not invented detail |
| Calling the API inside the loop is simpler | It multiplies calls, time, quota use and possible cost for no benefit |
| A default value is only needed for a crash | It's needed whenever the user could reasonably leave a field empty |
| The privacy check here is a complete filter | It's a basic classroom check, not a real personal-information detector |
| The AI's plan should be shown as final | It's a suggestion, always presented as something to check |

---

# 8. Assessment Evidence (formative)

- The warm-up's call count and its explanation
- Task 1's prompt containing all four parts (role, task, data, structure)
- Task 2 passing all three cases (empty, sensitive, normal)
- **Unit 4 checkpoint — "Balanced Day"**: all five test cases from the table above, scored against the source's
  20-point rubric (wrapper function 4, key security 3, dynamic prompt 3, accumulation loop 3, one call outside the
  loop 2, validation and privacy 3, testing and explanation 2). Bands: 18–20 complete/safe/economical/well explained
  · 14–17 works, minor flaw · 10–13 partial, missing a check or the single-call separation · 0–9 needs support.
- The peer review and answer critique, completed with at least one concrete note each
