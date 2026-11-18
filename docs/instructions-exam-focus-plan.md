# Task for a new Claude session: exam-focus plan for Python B (mafmar, Wednesday 17 March 2027)

Written 18 Nov 2026 from the Python A session. You are working in `C:\Users\Guitar\Workspace\ie-cs-python-b` (Grade 8, "AI2 בשילוב פייתון ב'"). The user is the teacher. Do the same job that was just done for Python A, adapted to this course.

## 1. The job in one paragraph

The Ministry published a **focus document (מיקוד)** for the Python B mafmar exam. Build (a) a dated, exam-first teaching plan from today to the exam, with tests and quizzes; (b) updated progress trackers that show what was covered and what is still missing; (c) a colourful Hebrew HTML page of the plan for the **students**, with detailed content and especially what is **not** on the exam. Get the teacher's approval at the points marked **[ASK]** and commit and push only when told.

## 2. Inputs

- **Focus PDF:** `C:\Users\Guitar\Downloads\ie-cs-python-b\מיקוד פייתון ב.pdf` (2 pages, Hebrew). Read it with the Read tool (it renders as images). **Red text = NOT on the exam.** Copy it to `docs/ministry-source/focus-python-b-tashpaz-he.pdf` (first step; the Python A repo did this with `focus-python-a-tashpaz-he.pdf`).
- **Exam date:** **Wednesday 17.3.2027** (יום רביעי). The repo's `course-map.md` still says "May 2027": that is obsolete, replace it.
- **The Python A work to copy the shape of** (read these first, at `C:\Users\Guitar\Workspace\ie-cs-python-a`):
  - `docs/plan-to-mafmar-2027-03-15.md`: the plan (scope table, calendar, dated table, rules, open questions, material to build).
  - `docs/mafmar-plan-python-a-he.html`: the student page (open it in a browser or render it; copy its look and structure, not its content).
  - `course-map.md` (sections "Deadline and pace" and "Schedule") and `class-progress.md` (status text, progress table, "Exam coverage" table): the tracker format.
  - `git log` of that repo from 18 Nov 2026 shows the sequence of changes.

## 3. The focus, as read from the PDF (verify against the PDF yourself)

| Ch. | Name | On the exam | NOT on the exam (red) |
|---|---|---|---|
| 1 | Python A review | New meeting with algorithmic concepts, work environment, variables, conditional statements and loops (`for`, `while`) | — |
| 2 | AI2 opening lesson | — | **Whole chapter**: the AI revolution, classic programming vs AI, data, responsibility and biases, "makers" |
| 3 | Operations (functions) | Function without parameter(s) not returning a value; with parameter(s) not returning; without parameter returning a value; with parameter returning a value | — |
| 4 | API: bringing AI into code | AI integration in code; using an API key (emphasis on functions); prompt writing; project: solving a problem with conditions, loops, functions and API | — |
| 5 | Strings | Empty string; string operators `+` `*`; `in`; slicing `[]` and `[::]`; core operations `len`, `find`, `upper`, `lower`, `count`, `replace`; bounded definite loop (index vs content): `for i in range(len(st))` and `for ch in st` | **`startswith`, `endswith`, `isalpha`, `isnumeric`** |
| 6 | Advanced language model | Tokens; meaning map; self-attention (context) | — |
| 7 | Lists | — | **Whole chapter** (list, access, slicing, `len`, `count`, `in`, `remove`, `pop`, `index`, `append`, `insert`, `join`, `split`, `sort`, `reverse`, algorithms on lists) |
| 8 | Classification | — | **Whole chapter** (Teachable Machines, accuracy measure) |
| 9 | Recommendation systems | — | **Whole chapter** (content-based, user-based) |

Note the differences from Python A: here `while` **is** on the exam (chapter 1), functions **with parameters and return values** are on the exam, and strings, API and the language model are on the exam. Lists, classification and recommender systems are not.

## 4. Steps

1. **Read first** (the repo's own rules apply, see `CLAUDE.md`): `CLAUDE.md`, `class-progress.md`, `course-map.md`, `docs/official-numbering.md`, `units/README.md`, `CONTENTS.md`, the memory index, and every unit's `unit-plan.md`.
2. **Save the focus PDF** into `docs/ministry-source/` and add it to `CONTENTS.md` (the `docs/ministry-source/` row).
3. **Map focus chapters to the repo's units and lessons** using `docs/official-numbering.md`. Likely: ch. 1 ↔ `u1-python-a-review`, ch. 3 ↔ `u3-functions`, ch. 4 ↔ `u4-api`, ch. 5 ↔ `u5-strings`, ch. 6 ↔ part of `u6-advanced-language-model` (find which lessons cover tokens, the meaning map and self-attention), ch. 2/7/8/9 ↔ `u2`, `u7`, `u8`, `u9`. Verify, do not assume.
4. **Audit the built material against the focus.** List what in each in-scope unit is out of scope (for example `startswith`, `endswith`, `isalpha` or `isnumeric` in the strings lessons and countdown edition; parts of unit 6 beyond tokens, meaning map and self-attention), and what the focus requires that no built lesson covers. Report findings; **do not trim or edit lessons without the teacher's decision**.
5. **[ASK] the teacher** (one concise question set, with a recommended default for each):
   - Meeting days and dates from now to 17.3.2027 and any known closures (Hanukkah, semester end, trips); the repo says the weekly day was "to confirm".
   - What was actually taught and when (the tracker says Lessons 8.2–8.7 were scheduled for 15 Nov; **confirm whether they were taught**, and whether the Form B retest on 11 Nov happened). Do not assume a lesson was taught: in the Python A session the progress file contradicted itself and an assumption had to be corrected.
   - Exam length and format if known.
   - Whether non-exam blocks (AI2 opening, lists, classification, recommender systems) move to after the exam.
   - Teaching-order constraints already known: the class has **not** learned functions yet (strings were taught first), and the API block needs the functions block first.
6. **Write the plan** `docs/plan-to-mafmar-2027-03-17.md` in the same shape as the Python A plan: scope table (the table in section 3, with repo meetings), calendar and assumptions, dated table (date, content, quiz or test, built status), rules (exam-first order; trim, don't extend; what to drop if a Sunday is lost), open questions, material to build. Include:
   - the remaining in-scope teaching, in a valid order (functions before API);
   - periodic **בחנים** (quizzes), **מבחנים** (tests), at least two full rehearsals under exam conditions with reviews, a final light meeting with no new material;
   - a realistic count: compare the meetings available with the meetings needed and say plainly if it does not fit and what must be merged or cut.
   **[ASK] approval** before touching the trackers.
7. **After approval, update the trackers** the way Python A's were: `course-map.md` (replace the May deadline, make the Schedule exam-first with dates, status and a "Built" column, list quizzes and tests with dates) and `class-progress.md` (status text, a progress table following the plan, and an **Exam coverage: done and still missing** table per focus topic). Keep the old meeting numbers in the meeting log; the check script relies on them. Add the plan and the student page to `CONTENTS.md`.
8. **Build the student page** `docs/mafmar-plan-python-b-he.html`, then copy it to `C:\Users\Guitar\Downloads\` for the teacher's review. Requirements, learned from the Python A page:
   - Hebrew, `dir="rtl"`, one self-contained file (inline CSS, tiny inline JS, no external resources), colourful, printable (`print-color-adjust: exact`), works on a phone.
   - Header with the exam date (Wednesday 17.3.2027) and a days-left countdown; a summary row with meetings, tests and exam rehearsals. **No quizzes tile.**
   - The focus chapter by chapter as colour-coded cards, ✓ for what is on the exam and ✕ in red for what is not, detailed (every excluded operation listed, e.g. `startswith`, `endswith`, `isalpha`, `isnumeric`); whole excluded chapters as grey dashed cards.
   - A prominent "what will NOT be on the exam" box with chips.
   - The dated timeline with colour-coded tests and exam rehearsals, the next lesson highlighted and past dates faded by JavaScript, the exam as a gold row, and a short "after the exam" section.
   - **Do not show quizzes to the students** (the teacher removed them from the Python A page: they stay in the teacher plan only).
   - Terminology: a quiz is **בוחן**, never חידון (which means riddle); a test is **מבחן**.
   - Render it (Edge headless: `msedge.exe --headless --screenshot=... --window-size=1100,3400 file:///...`) and look at the screenshot before delivering. Keep a footer note that dates may change.
9. **Memory:** save a project memory for the exam plan (as `mafmar-exam-plan.md` in this repo's memory folder) and update the class-progress memory; keep the index line short.
10. **Checks and git:** run `bash tools/check-structure.sh`, `python -I tools/check-repo.py` and `python tools/lesson-decks/build_decks.py --check`; report any failure (an existing warning about a starter file is acceptable only if it was there before). Commit and push **only when the teacher says "commit and push"**. Commit messages end with the attribution line given in the session's system reminder. Leave the untracked `.idea/` alone.

## 5. Working rules

- Answer in short prose; report what was done, what was checked, and what the teacher must decide.
- Do not fabricate: the exam length, the number of available meetings and the taught dates are unknown until the teacher answers.
- When a wording is ambiguous ("remove the added X"), ask one short question rather than guess; in the Python A session a guess about which quiz to remove cost a round trip.
- Every file you add must be linked from `CONTENTS.md`; do not link planned files that do not exist.
- Student-facing pages carry no teacher-only information (build status, "flex slot", plan IDs).
- Keep student names and grades out of the repo (aggregates only).

## 6. Deliverables checklist

- [ ] `docs/ministry-source/focus-python-b-tashpaz-he.pdf` saved and listed in `CONTENTS.md`
- [ ] Audit of built material against the focus (reported to the teacher)
- [ ] Teacher's answers on dates, taught status, exam length, ordering
- [ ] `docs/plan-to-mafmar-2027-03-17.md` written and approved
- [ ] `course-map.md` and `class-progress.md` rewritten (Schedule, progress table, exam coverage)
- [ ] `docs/mafmar-plan-python-b-he.html` built, rendered, copied to Downloads, approved
- [ ] `CONTENTS.md` and memory updated; checks run
- [ ] Commit and push after the teacher's go-ahead
