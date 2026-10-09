# Prompt for ChatGPT — Expert Review of the Unit 1 Test

Copy everything below the line into ChatGPT and attach (or paste) these files:
`unit-1-test-he.md` (the student test), `unit-1-test-answer-key.md` (key and rubric) and `Test_Reference.py`
(model solutions). Do not paste any student data.

---

You are an expert Python teacher for high schools (Israeli Grade 9, ages 14–15) with more than 15 years of experience
writing and grading written exams. Please review the attached **60-minute paper test** as a critical colleague.

## Context

- Students finished a short Python course in Grade 7 ("Python A") and a 6-hour review unit: conditions
  (`if`/`elif`/`else`, `and`/`or`/`not`), `for` with `range`, `while`, counters and totals, input validation.
- **Not taught, and must not be required:** lists, tuples, dictionaries, nested loops, functions with parameters or
  `return`, `+=`, `break`, string methods, f-strings.
- The test is on paper, without a computer. The test text is Hebrew; code and program output are English.
- Goal: find out what each student can read, trace, debug and write. It is a diagnostic, not a competition.

## What to check

1. **Correctness.** Run or trace every code snippet and every expected output. Are the answer key, the rubric and
   `Test_Reference.py` correct and consistent with each other and with the test? List every error with its question number.
2. **Coverage and balance.** Does the test fairly cover the stated topics? Is there a good spread of skills
   (trace, debug, write)? Is anything over- or under-weighted?
3. **Difficulty and time.** Can an average student finish in 60 minutes? Estimate the time per question and compare it
   with the suggested split (A 14 / B 8 / C 33 / 5 review). Which questions are too easy or too hard for this level?
4. **Clarity.** Is each question unambiguous? Are there traps that test reading skills rather than Python?
   Is the Hebrew natural and age-appropriate? Will right-to-left text mixed with English code confuse students?
5. **Fairness and rubric.** Is the partial credit sensible? Would two teachers grade the same answer the same way?
   Does the common-error list miss any typical student mistake?
6. **Pedagogy.** Does any question reward memorizing instead of understanding? Would you add or drop a question type
   (for example an off-by-one "predict the output", or "which test value exposes the bug")?

## Answer format

1. **Verdict** — two or three sentences: ready to use, or needs changes.
2. **Errors found** — table: question · problem · suggested fix.
3. **Timing estimate** — table: question · minutes for a strong / average / weaker student.
4. **Suggestions** — a prioritised list (high / medium / low), each with one sentence of reasoning.
5. **A revised version of the weakest question**, written in full in the same style, with its key and rubric.

Be specific and concise. If you are unsure whether something is wrong, say so and explain how to check it.
