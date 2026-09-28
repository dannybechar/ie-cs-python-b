# Working in this repository

This is the Grade 8 **AI + Python B** course — the Israeli Ministry of Education's new program
"בינה מלאכותית בשילוב מדעי המחשב — AI2 בשילוב פייתון ב'", first taught in תשפ"ז (60 hours, 9 units, 30 meetings).
The user is the teacher. Together we build every meeting — lesson notes, a Hebrew lab brief, starter and
reference code, and a Hebrew slide deck — the same way the Grade 7 **Python A** course was built in
[`ie-cs-python-a`](https://github.com/dannybechar/ie-cs-python-a) (local: `C:\Users\Guitar\Workspace\ie-cs-python-a`).
That repository is complete (31 meetings, all approved, all decks patched) and is **the working example**:
when a format is unclear, open the matching file there and copy its shape.

Start every session by reading `course-map.md` (what is built, approved and pending) and the memory index.

## The teacher's commands

The teacher gives short commands. Each one has a fixed meaning; finish the whole routine, then commit and push
without asking (`git push` is already set up — see "Git" below). Report back briefly: what was done, what was
checked, any decision the teacher must make.

### "build unit N" / "build U.M"

Build every meeting of the unit (or one meeting), one at a time.

1. **Sources.** The Ministry program [`docs/ministry-source/python-b-ai.pdf`](docs/ministry-source/python-b-ai.pdf)
   is the authority: the master syllabus table (pp. 3–4) and one chapter per unit (goals, concepts, teaching methods,
   assessment, per-topic hours — pp. 5–23). **Hours come from the master table** (teacher's decision): the chapter tables
   of Units 1, 3, 5 and 7 give a different theory/practice split and are used only for the order and weight of topics.
   The year plan is [`docs/annual-strategy.md`](docs/annual-strategy.md) (provisional meeting outline, depth boundaries,
   tools to settle). The teacher's raw materials are **inspiration only**:
   `Downloads\python-b-raw-meterials\ie-cs-python-b\` — `U<N>_M<M>\` folders (strategy `.md`, raw deck `.pptx`, lab brief,
   starter and reference `.py`, exit-check `.png`) for meetings 1.1–1.3, 2.1–2.2 and 3.1, plus a year strategy.
   The raw year strategy is wrong wherever it says the syllabus leaves a unit open (Units 4, 6, 8, 9): the official
   chapters name the activities — follow them. For meetings with no raw material, build from the Ministry program alone.
2. **Plan the unit first** (`units/u<N>-<slug>/unit-strategy.md`): official topics with theory/practice hours from the
   Ministry master table, which meeting covers each topic, meeting-by-meeting outline, scope decisions (what the raw decks
   do that the course won't), exit criteria. Meetings are 90 minutes: **Knowledge + Lab** (45 theory / 45 practice) or
   **Lab + Lab** (0 / 90). A unit's planned minutes must equal its official minutes (1 academic hour = 45 min).
3. **Per meeting**, in the unit folder (flat — no subfolders):
   - `m<M>-lesson-notes.md` — teacher plan (template below).
   - `m<M>-lab-brief-he.md` — Hebrew student brief (template below).
   - `<Topic>_Starter.py` / `<Topic>_Reference.py` — the starter usually opens with a **warm-up bug** (a real,
     common mistake, documented in the lesson notes); the reference solves every task, one function per task.
4. **Verify all code**: run every example, output and trace in the lesson notes, brief and slides; check every error
   message against the installed Python (3.14). Code that calls an outside service or library (the language-model API
   in Unit 4, the embedding library in Unit 6, the exported model in Unit 8) is verified with a stand-in function that
   returns fixed answers; tell the teacher which files need a live run in Thonny, with the real service, before class.
   Never put an API key in any file.
5. **Records**: unit `README.md` (one section per meeting, table of files; the slides row is
   `| Teacher | slides | Pending (NotebookLM) |`), `unit-strategy.md` status 🔶, `course-map.md` (time budget row,
   schedule rows 🔶, meeting log row, open gaps), root `README.md` unit line ("🔶 built, awaiting approval").
6. **Prepare the NotebookLM folder** for each meeting (next routine) as part of the build.
7. Commit per meeting or per unit ("Build Unit 3 Functions (3 meetings)"), push, report: a table of meetings
   (topic, theory/practice, starter bug, slide count), changes from the raw decks, open decisions.

### "prepare slides U.M" (the NotebookLM folder)

The teacher makes each deck in NotebookLM. Create `Downloads\python-b-unit<U>-m<M>-slides\` containing:

- `0-START-HERE-instructions.md` — written with `tools/deck-patch-kit/mkinstr.py` (`make(...)`): Hebrew output language
  as its own step; the prompt to paste; the exact NAMING block (title "יחידה U.M – <שם היחידה>", the theme as the subtitle,
  the same footer on every slide, never "מפגש", "שיעור" or "פרק"); exact slide count; straight double quotes only;
  keep table column order; bug slides show the bug exactly as written; "question only" slides show no answer;
  timers ("N דקות") only on student-activity slides; a warning not to upload the raw decks; a check list.
- `1-source-slide-content.md` — every slide spelled out as `### Slide N — <title>`: Hebrew text, exact code and output,
  tables, a description of every picture (drawn by running the real code), minutes per slide summing to **90**.
  Keep it to **≤ 20 slides** (NotebookLM drops slides past ~21). Question and answer on separate slides.
- Copies of `m<M>-lesson-notes.md` and `m<M>-lab-brief-he.md`.

### "review U.M" (a deck came back from NotebookLM)

1. Take the **newest PDF in Downloads** — its file name is thematic, not the unit number — and confirm from the
   **title slide** that it really is U.M. If it isn't, say so and stop.
2. Review every slide against `1-source-slide-content.md` (or, if the folder is gone, the lesson notes and the
   `_Reference` code): Hebrew wording, every code line and output, tables, pictures, timers, footer, naming,
   question-only slides, challenge slides (must not show the full solution), and the total time.
3. **Patch the PDF with pixel edits** using `tools/deck-patch-kit/` (see its README: copy `common.py` + `heb.py` to the
   scratchpad, write `p<D>.py`, `build`). Don't ask for regeneration — it trades old errors for new ones.
4. Save to `units/<unit dir>/m<M>-slides-he.pdf` **and** `Downloads\python-b\unit U.M - <English unit name>.pdf`
   (the teacher uploads that copy to Google Drive).
5. Update the unit README slides row → `| Teacher | [`m<M>-slides-he.pdf`](m<M>-slides-he.pdf) | Hebrew slide deck (N slides, NotebookLM, patched) |`
   and the course-map meeting-log note → `slides: `m<M>-slides-he.pdf` (N slides, 90 min; NotebookLM, patched)`.
6. Commit ("Add Unit U.M slide deck (patched NotebookLM PDF)"), push, report what was patched, slide by slide.

### "approve unit N"

- Every `m*-lesson-notes.md` of the unit: `**Status:** Approved by the teacher`.
- `unit-strategy.md`: build status "✅ complete — all K meetings built and approved by the teacher"; topic rows ✅.
- `course-map.md`: budget row ✅ K/K, schedule rows ✅.
- Root `README.md`: drop "awaiting approval" for the unit.
- Check `git diff` so no other unit changed; commit ("Mark Unit N <name> as approved"), push.

### "review entire repository and clean up"

Compile every `.py` (intentional starter bugs excepted — they are documented), check every relative Markdown link,
check that every meeting has notes, brief, code and deck, look for leftover "Pending", "awaiting", TODO and ⚠️ markers,
and make the README and course map describe the current state.

## Conventions (same as Python A)

- **Naming rule:** a meeting is named by its curriculum unit: **Unit U.M — <unit name>**, in Hebrew
  **יחידה U.M – <שם היחידה>**. The lesson's theme is only a subtitle. This applies everywhere: headings, course map,
  briefs, slide titles and footers, NotebookLM notebook names, and how you refer to meetings in chat.
  Meetings are 1-based (2.1, 2.2 …); files `m1-`, `m2-` ….
- **Units** (from the master table, `python-b-ai.pdf` pp. 3–4; 60 h = 21 theory + 39 practice = 30 meetings).
  A unit has one Knowledge + Lab meeting per theory hour; its other meetings are Lab + Lab.
  The Hebrew names are the official chapter names, shortened so a title never contains "שיעור" or a second dash
  (official: "שיעור פתיחה לשנה ב' AI2", "API - להכניס בינה לקוד", "מודל שפה - מתקדם", "רשימה list").

  | # | English | Hebrew | Hours (T / P) | Meetings (K+L / L+L) | Folder |
  |---|---|---|---:|---:|---|
  | 1 | Python A Review | חזרה על פייתון א' | 6 (1 / 5) | 3 (1 / 2) | `units/u1-python-a-review` |
  | 2 | AI2 Year Opening | פתיחת שנת AI2 | 4 (2 / 2) | 2 (2 / 0) | `units/u2-ai2-year-opening` |
  | 3 | Functions | פעולות | 6 (2 / 4) | 3 (2 / 1) | `units/u3-functions` |
  | 4 | Bringing AI into Code (API) | להכניס בינה לקוד (API) | 4 (1 / 3) | 2 (1 / 1) | `units/u4-api` |
  | 5 | Strings | מחרוזות | 8 (2 / 6) | 4 (2 / 2) | `units/u5-strings` |
  | 6 | Advanced Language Model | מודל שפה מתקדם | 6 (2 / 4) | 3 (2 / 1) | `units/u6-advanced-language-model` |
  | 7 | Lists | רשימות | 10 (3 / 7) | 5 (3 / 2) | `units/u7-lists` |
  | 8 | Classification | סיווג | 8 (4 / 4) | 4 (4 / 0) | `units/u8-classification` |
  | 9 | Recommender Systems | מערכות המלצה | 8 (4 / 4) | 4 (4 / 0) | `units/u9-recommender-systems` |

- **Lesson rhythm:** never more than 10–15 minutes of teacher talk before students act (predict, trace, type, run,
  discuss); 4–5-minute demos in lab meetings; short demo → task → short demo → task. Predict-first questions get their
  own step, with the answer after. One flexible "if time" block per lab. One function per task.
- **Code style:** double quotes, 4-space indents, `snake_case`, a comment line at the top of each starter saying what
  to find or do. Use only what the students have been taught: the Python A course (Grade 7) and earlier meetings of
  this course. **Lists are new in Unit 7** — no lists before it (Units 1–6 accumulate into strings and counters).
  Never, in any unit: nested loops (dropped from the new program — clarifications p. 3), tuples, sets, dictionaries,
  list comprehensions, lists of lists (all moved to Part C), default or keyword arguments, classes.
  f-strings are new in Unit 4 (the program lists them there, p. 12). If Turtle is used, follow Python A
  (module-level `turtle.` calls, no `turtle.Turtle()`). Ask the teacher before using `+=` (Python A wrote `x = x + 1`).
- **AI safety in every file:** no API keys, no student names, faces or personal data; model output is always shown
  as something to check, not as the truth (program rationale, p. 2).
- Every `.py` compiles before it is committed (except a documented intentional syntax bug in a starter).
- Markdown is the source format; GitHub must render it well. Hebrew lines start with a Hebrew word; code in fenced blocks;
  wrap Hebrew tables and lists in `<div dir="rtl">` … `</div>` with blank lines inside.
- Hebrew-facing files end in `-he`. No version suffixes in file names. Never commit student data or secrets.
- Status marks: ✅ built and approved · 🔶 built, awaiting approval · ⚠️ gap · ❌/⏳ not built.

## File templates (copy the shape from `ie-cs-python-a/units/u8-functions-parameters/`)

**`m<M>-lesson-notes.md`:** `# Unit U.M — <name>` · `## Grade 8 / AI + Python B · Lesson Strategy v1` ·
`### Topic: <theme>` · header lines `**Status:**` (🔶 text: "Built, awaiting teacher approval"), `**Duration:** 90 minutes`,
`**Structure:**`, `**Minutes (theory / practice):**`, `**Current tool:** Thonny`, `**Source of inspiration:**` (the raw
deck, what was kept, what was changed and why), `**Tool-dependence rule:**` · sections: 1 Position in Unit N (table of
all meetings) · 2 Official Scope Used in This Meeting (Ministry goals with page numbers; deliberate exclusions) ·
3 Lesson Goal · 4 Core Mental Models · 5 First 45 Minutes (clock table) · 6 Second 45 Minutes — Lab (one `## a–b — Task`
heading per block, the warm-up bug, save, exit check) · Tool Note – Thonny · 7 Misconception Risks · 8 Assessment Evidence.

**`m<M>-lab-brief-he.md`:** `# יחידה U.M – <שם>` · a one-line subtitle with the theme · the work cycle line ·
a `> [!IMPORTANT]` key idea · `## דף עזר` (a short code reference) · numbered task sections (warm-up first) ·
save/document · exit check.

**`course-map.md`** and **`unit-strategy.md`**: keep the structure already in this repo (built from Python A's).

## Deadline and pace

Keep `course-map.md` current whenever a meeting is added, retimed or taught: time budget vs official minutes,
the schedule (target week / taught on), open coverage gaps, the meeting log, and the pace check (meetings left in
the schedule ≤ meetings left before the exam). The Ministry exam (בחינת מפמ"ר) is set for **May 2027**
(circular, p. 2). Not yet known for this class — ask the teacher: the weekly meeting day, the first meeting date,
and the exact exam date (see "Deadline and pace" in the course map).

## Git

- Remote `dannybechar/ie-cs-python-b`. The machine's global gh account (`danny-gh-is`) gets 403; this repo's
  `.git/config` has a credential helper that supplies `dannybechar` + `gh auth token --user dannybechar`, so plain
  `git push` works. If a push 403s, check that config.
- Work on `main`, one commit per routine, message in the style above.
