# Ministry teaching materials — the source of truth

> **Numbering (13 Nov 2026):** the Ministry's lesson numbers are now also the numbers of this repository. Meetings are named by official lessons (e.g. *Lessons 8.2–8.7*); the mapping and the file keys (`u5/m4` …) are in [`official-numbering.md`](official-numbering.md). Old "Unit U.M" labels in this file were converted; "meeting" below means a 90-minute file-key meeting.

**Authority (teacher's decision, 31 Oct 2026):** the PDFs in
`C:\Users\Guitar\Downloads\השתלמות\מצגות-השתלמות\` are the **official teaching materials published by the Ministry of
Education** (decks, "תרגול לפיצוח" worksheets, teacher solutions, API-key guides). They override the teacher's raw
materials (`python-b-raw-meterials`, inspiration only) and the units we first built from the Ministry *program* text
alone. The program ([`ministry-source/python-b-ai.pdf`](ministry-source/python-b-ai.pdf)) still sets goals and hours;
these materials set **what is taught, in which examples and with which exercises**.

**Primary source (teacher's decision, 13 Nov 2026):** the whole repository works under the official Python B program as
downloaded from the Ministry's classroom into
`C:\Users\Guitar\Workspace\classroom-downloader\downloads\פייתון_ב\` (`Materials\` — decks, teacher notes and solutions,
guided-practice videos, summaries; `Classwork\` — worksheets as `.docx`; `links.md` — Forms, H5P, genially, YouTube and the
three virtual exams). Where it and the `מצגות-השתלמות` PDFs differ, this folder wins; it also supplies files the PDFs lacked
(lists parts B–D, worksheets and teacher solutions). Every build, review and rework starts there. Reconciliation of the
built blocks against it is tracked in the "Reconciliation" section below.

The PDFs are not copied into the repo (size, and they remain the Ministry's files). Read them with PyMuPDF
(`python`, not `python -I`, so user-site packages load); Hebrew text extracts in visual order — check the page image
when a line looks scrambled. The Ministry's file numbers (2.0 … 22.1) are **its own lesson numbers, which are also our numbers now (see the note above).**

The files for the Ministry's lessons 10–22 arrived on **8 Nov 2026** (the advanced-language-model, lists, classification and recommender blocks). They were audited the same day (section
"Audit of lessons 10–22" below); those four blocks were all reworked the same day. Some files are still missing (list below).

## File inventory and where each file lands

| Ministry file | What it is | Our meeting (file key, official lessons) |
|---|---|---|
| 2.0 מצגת למורה — לולאת תנאי while — חזרה | deck, 12 slides | `u1/m3` Lessons 2.0–2.3 |
| 2.1 תרגול לפיצוח — לולאת while | worksheet, 4 questions | `u1/m3` Lessons 2.0–2.3 |
| מלכודת הלולאה האינסופית | teacher's NotebookLM deck, 14 slides (image-only): diagnosing infinite `while` loops | `u1/m3` Lessons 2.0–2.3 |
| 3.1 מצגת — שיעור פתיחה לשנה ב AI2 | deck, 50 slides | `u2/m1`, `u2/m2` Lessons 3.0–3.1, 3.1–3.2 |
| 3.2 / 3.2.0 תרגול לפיצוח — איך מחשב רואה בלי עיניים (+ teacher solution) | Quick, Draw! worksheet | `u2/m2` Lessons 3.1–3.2 |
| 4.1 מצגת פעולות חלק א | deck, 28 slides: multiple parameters, `return` | `u3/m1` Lessons 4.1–4.2 |
| 4.2 / 4.2.0 דף תרגילים פעולה המחזירה ערך (+ solution) | worksheet | `u3/m1`, `u3/m2` Lessons 4.1–4.2, 4.4–4.5 |
| 4.3 משתנים בפעולות | deck, 24 slides: local and `global` | `u3/m3` Lessons 4.3, 4.6 |
| 4.4 תרגול לפיצוח — שאלות מבחינות | exam-style questions (functions + `while`) | `u3/m2` Lessons 4.4–4.5 |
| 4.5 / 4.5.0 תרגילי פעולות ומשתנים (+ solution) | worksheet: local vs global, `return` | `u3/m2`, `u3/m3` Lessons 4.4–4.5, 4.3 and 4.6 |
| 4.6 תרגול לפיצוח — תפקידי משתנים בפעולות | worksheet (+ solution in 4.5.0) | `u3/m3` Lessons 4.3, 4.6 |
| 5.0 דגשים למורה; 5.0.1 Gemini API key (teacher); 5.0.2 keeping the key secret (Colab Secrets) | teacher notes | `u4/m1`, `u4/m2` Lessons 5.0–5.2, 6.1–6.2 |
| 5.1 מצגת — API; 5.2 / 5.2.0 תרגול (+ solution) | deck 32 slides + worksheet | `u4/m1` Lessons 5.0–5.2 |
| 6.1 מצגת — פרויקטון יום מאוזן; 6.2 / 6.2.0 תרגול (+ solution) | deck 13 slides + worksheet | `u4/m2` Lessons 6.1–6.2 |
| 7.1 מחרוזות חלק א׳; 7.2 דף עבודה מחרוזות | deck 40 slides + worksheet (Python A material, revisited) | `u5/m1`, `u5/m2` Lesson 7.1, Lessons 7.1–7.2 |
| 8.0 מצגת למורה — מחרוזות; 8.1 פייתון ב׳ מחרוזות; 8.2 תרגול; 8.7 סיכום בקטנה | decks 27 + 33 slides, worksheet, one-page summary | `u5/m3`, `u5/m4` Lessons 8.0–8.1, 8.2–8.7 |
| 10.0 דגשים למורה; 10.1 מצגת — טוקנים (35 slides); 10.2 / 10.2.0 דף עבודה — טוקנייזר (+ solution) | teacher notes, deck, worksheet | `u6/m1` Lessons 10.0–10.2 |
| 11.1 מצגת — מפת המשמעויות והקשב העצמי (28 slides); 11.2 / 11.2.0 דף עבודה #1 הכנה לפרויקטון סמנטעל (+ solution) | deck, worksheet | `u6/m2` Lessons 11.1–11.2 |
| 11.3 / 11.3.0 דף עבודה #2 פרויקטון סמנטעל (+ solution) | project worksheet | `u6/m3` Lesson 11.3 |
| 12.0 / 12.1 רשימות חלק ב׳ (27 / 42 slides); 12.5 תרגול #2; 12.6 מאסטר פייתון; 12.7 סיכום | decks, worksheets, summary | `u7/m2`–`u7/m5` Lessons 9.3, 9.5, 12.0–12.1 · 12.6, 13.0–13.1 · 13.2, 14.0–14.2 · 12.5, 14.4 (reworked 8 Nov 2026) |
| 13.0 / 13.1 רשימות חלק ג׳ (18 / 19); 13.6 סיכום | decks, summary | `u7/m3` Lessons 12.6, 13.0–13.1 (reworked 8 Nov 2026) |
| 14.0 / 14.1 רשימות חלק ד׳ (30 / 27) | decks | `u7/m4` Lessons 13.2, 14.0–14.2 (reworked 8 Nov 2026) |
| 16.0 / 16.1 / 16.2.0 סיווג לפי תכונות (1 / 68 / 9) | teacher notes, deck, teacher solution | `u8/m1` Lessons 16.0–16.2 (reworked 8 Nov 2026) |
| 17.0 / 17.0.1 / 17.1 אימון ומבחן של מודל סיווג; 18.0 / 18.1 פרויקט סיווג; 19.0 / 19.1 חיבור מודל מאומן לפייתון | notes, Teachable Machine helper deck, decks | `u8/m2`–`u8/m4` Lessons 17.0–17.1, 18.0–18.1, 19.0–19.1 (reworked 8 Nov 2026) |
| 20.0 / 20.1 הכרות עם מערכות המלצה; 21.1 בונים מערכת המלצה; 22.1 סכנות במערכות המלצה | notes, decks | `u9/m1`–`u9/m4` Lessons 20.0–20.1, 21.1, 21.1–21.2, 22.0–22.1 (reworked 8 Nov 2026) |
| `תמונות לאימון` zip (269 AI-generated images: `ok/` 114, `fist/` 155) and `תמונות למבחן` zip (7 test images) | the fist/OK project data | `u8/m3`, `u8/m4` Lessons 18.0–18.1, 19.0–19.1 |

## Rulebook changes (they replace the older restrictions in `CLAUDE.md`)

The Ministry's own materials do these, so the course does too:

- **`global`** is taught (Lessons 4.3, 4.6): a variable defined outside every function can be read inside; changing it from
  inside needs `global name`; without it Python makes a new local variable. Includes the `UnboundLocalError` trap.
  **Verify error messages on the installed Python** — the Ministry's text is older than Python 3.14
  (`UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`).
- **`+=`** is allowed (the Ministry uses it from the Python A review and in the strings block). `x = x + 1` stays fine.
- **`print(..., end="")`** is allowed (string traversal, lessons 7.1–8.7). Writing your own functions with default or keyword
  arguments is still not taught.
- **`split` and `join`** appear in the strings block (string methods, official 8.1); the result is a list, shown and printed only.
  Lists as a topic (indexing, `append`, traversal, …) stay in the lists block (lessons 9.1–14.5), which revisits `split`/`join`.
- **`ord()` / `chr()`** (ASCII, "next letter" cipher) are taught in the strings block (official 8.0, 8.1).
- **API service: Gemini** (`from google import genai`, `genai.Client(api_key=…)`, `client.models.generate_content`,
  model `gemini-2.5-flash` in the Ministry text — check the current name before class). The teacher creates the keys
  beforehand (5.0.1: up to 10 projects, ≈15 requests/minute, 1,500/day per key — so students share and work in groups).
  The Ministry keeps the key secret with **Colab Secrets** (`google.colab.userdata.get("GEMINI_API_KEY")`), 5.0.2.
  Our default tool is Thonny, so every file of the API block (lessons 5.0–6.2) also has a stand-in `ask_the_ai()` (fixed answers) for verification
  and for a class without keys or internet. Never put a key in a file.
- **Unchanged:** no nested loops, tuples, sets, dictionaries, comprehensions, lists of lists, classes; lists as a topic
  only from the lists block (lessons 9.1–14.5).

## Gaps this closes in the units we built

- Lessons 2.0–2.3 had no infinite-loop teaching → the loop-trap deck and 2.0/2.1.
- Lessons 3.0–3.1 and 3.1–3.2 lacked the "AI or not" quizzes, the grandma greeting (classic vs AI), the revolutions story and the
  Quick, Draw! data worksheet (bias, Israeli stop sign).
- The functions block started from zero-parameter functions; the Ministry starts from multiple parameters and `return`, then scope.
- API block: the service is Gemini, the key guides exist, and the Ministry's own "Balanced Day" worksheet is the project.
- The strings block was planned 45 / 315 minutes; the official split is **90 / 270** — two Knowledge + Lab meetings (Lesson 7.1, Lessons 7.1–7.2),
  two Lab + Lab (Lessons 8.0–8.1, 8.2–8.7).

## Status

Reworked units are 🔶 (built, awaiting approval) until the teacher approves them again. Slide decks built from the
older content are marked superseded in each unit README until the new NotebookLM deck is reviewed.

## Audit of lessons 10–22 (8 Nov 2026)

Method: the text of every PDF was extracted and read, image-only slides were rendered where it mattered, and our files for lessons 10.0–22.1 were
compared with it (one reviewer per block group). **Those four blocks are reworked (🔶)**; the findings below are what each rework fixed, plus what is still open.

**Blocks:** lessons 10–11 = the advanced-language-model block (2 Ministry meetings; we keep 3), 9.x and 12–14 = the lists block,
16–19 = the classification block (4 meetings, as ours), 20–22 = the recommender block (3 Ministry meetings; ours has 4).

**Still missing (updated 13 Nov 2026 after the classroom-downloader folder arrived; lists part A 9.x and the worksheets 12.5, 12.6,
13.2, 14.2, 14.4, 16.2 are now delivered):** list part E (14.0 p. 30: "next lesson, a list of lists"); 12.2–12.4, 13.3–13.5 and
14.3 (links or videos only), 15.x, 17.2, 18.2 as a worksheet (its images are present), 19.2, 19.3 (Colab), 20.2, 21.0, 21.2 (it holds
the real recommender code), 22.0 and 22.2.

**Rule conflicts to settle:**
- `def` / `return` appear in almost every Ministry worksheet (lessons 9.1–22.1) while the class has not learned functions. Lessons 10.0–11.3 assume the functions block first.
- The Ministry previews **nested loops** (14.0 pp. 25–29, "will be learned later") and announces **lists of lists** (part E). CLAUDE.md says never.
- Our recommender block (lessons 20.0–22.1) used tuples and default arguments, both banned; to rewrite when the unit is reworked.

**Advanced language model, lessons 10.0–11.3 (done):** the Ministry uses the real `paraphrase-multilingual-MiniLM-L12-v2`; our v1 mock (with invented scores) is replaced.
Deck 10.1's token-quiz numbers come from a different tokenizer than the worksheet's (6 / 6 / 5 / 10 in the deck, 6 / 7 / 5 / 5 measured
with the worksheet's tokenizer).
**Lists block (open):** add list slicing (`[a:b:c]`, `[::-1]`), `list()`, `index()`, `+`, the flat name/price menu and parallel lists. The Ministry
decks contain bugs (`append(i)` for `append(item)`, 12.0 p. 10; curly quotes; stray parentheses) — never copy them as they are.
**Classification block (open):** the Ministry loads `converted_savedmodel.zip` with `tf.keras.layers.TFSMLayer` (we use `keras_Model.h5` and a mock);
add the two-feature scatter and separating line, the bias examples, the 85% confidence rule, the Teachable Machine guide 17.0.1 and the two
image zips.
**Recommender block (open):** the survey uses V / X / 0 (we use 0–3); add the YouTube-feed riddle, the "culinary twin" game, Plato's cave, the three
traps (filter bubble, echo chamber, addiction engineering) and the incognito demo; the Ministry's twin is simply the participant with the
most identical non-0 answers.

**Reworks done (8 Nov 2026):** the advanced-language-model, lists, classification and recommender blocks follow the Ministry decks and worksheets; decisions taken without the teacher: `def` allowed in those blocks;
the lists block has no nested loops and no lists of lists; the classification block uses the Ministry's SavedModel + `TFSMLayer` code (plus a stand-in so the files run without
TensorFlow); the recommender block keeps four meetings, uses V / X / 0 and flat lists (no tuples, defaults or `csv`), with a teacher-only `CsvToLists_Teacher.py`.
Ministry slide errors found while verifying (never to be copied): 14.0 p. 12 wrong example averages, 14.0 p. 23 `begin += 1 + i` skips a grade, 12.1 pp. 31–32
stray parenthesis and a late special-list check, 12.0 p. 10 `append(i)`. Files that still need a live run: Lessons 19.0–19.1 `Ministry_Model_Code.py` and the Teachable Machine export,
Lessons 20.0–20.1 and 22.0–22.1 Forms export and incognito demo, the lists block's `input()` tasks in Thonny.

## Reconciliation with the classroom-downloader program (opened 13 Nov 2026)

**Status: audit done and all blocks reworked (13 Nov 2026, commits b1302b2, 5e38c18, 45e0c44, 96cbfbf, 08a7d78, 26f2e7d, 6dc9681; every unit 🔶 awaiting re-approval, new decks pending).** The table below is the audit as it was before the rework; "PATCH" rows have since been applied. The folder `classroom-downloader\downloads\פייתון_ב\` holds 67
`Materials` items and 22 `Classwork` worksheets; all 89 files were extracted to text (4 are image-only: `0.6`, `2.3`, `9.5`,
`13.6`). Nine read-only audits compared each unit with the official lessons. Verdict key: OK / PATCH (small edits) / REWORK.
Limits: the audits mostly read lesson notes, not every brief, starter, answer key or slide PDF, so a verdict of OK is
"no conflict found in the notes".

| Meeting (file key, official lessons) | Verdict | Main findings |
|---|---|---|
| `u1/m1`, `u1/m2` Lessons 1.0–1.1, 1.2–1.4 | OK | Partial official counterpart (official 1.x reviews the `for` loop); official 1.0–1.4 for-loop tasks are optional enrichment |
| `u1/m3` Lessons 2.0–2.3 | OK | Covers 2.0 and part of 2.1; add the other 2.1 series tasks and the Forms links |
| `u2/m1` Lessons 3.0–3.1 | PATCH (minor) | Add the Pichai quote (3.1 slide 23) and the Gemini-window privacy tip (3.0) |
| `u2/m2` Lessons 3.1–3.2 | PATCH | Add the Amazon CV-screening story, make the Sapir video question explicit, check our key against 3.2.0 |
| `u3/m1`, `u3/m2` Lessons 4.1–4.2, 4.4–4.5 | OK | Follow 4.1/4.2/4.4/4.5 closely |
| `u3/m3` Lessons 4.3, 4.6 | PATCH | Official 4.6 q3/q4 return several values (tuple); we replaced them with globals. Teacher decides |
| `u4/m1`, `u4/m2` Lessons 5.0–5.2, 6.1–6.2 | OK | Live run with a real key still needed; 6.2 snippet has an unquoted `api_key=`; official 4.7 H5P (default argument) is undocumented here |
| `u5/m1`, `u5/m2` Lesson 7.1, Lessons 7.1–7.2 | OK | Small adds: official string definition, "two ways" `st[5]`/`st[-1]`, `find` with begin/end |
| `u5/m3`, `u5/m4` Lessons 8.0–8.1, 8.2–8.7 | PATCH | 45/45 vs 0/90 labels disagree across files (strategy total 135/225 vs official 90/270); `split`/`join` placement inconsistent; the Lessons 8.2–8.7 countdown can use official 8.2 Q2, 8.4 task 1 (middle character), the ord-number cipher |
| `u6/m1`–`u6/m3` Lessons 10.0–11.3 | PATCH | Reference code matches official solutions 10.2.0, 11.2.0, 11.3.0; missing the GPT-4/5 token example, the Hebrew-vs-English token challenge, Gemini 2M-token equivalents; Lesson 11.3 `int()` vs `round()` bar; list literal in Lessons 10.0–10.2 |
| `u7/m1`, `u7/m2`, `u7/m4` Lessons 9.1, 9.4 · 9.3, 9.5, 12.0–12.1 · 13.2, 14.0–14.2 | PATCH | Lists part A (official 9.1, 9.3, 9.4, 9.5) is now delivered but our docs still say missing; add 9.1/12.x demos, the 13-row operations table, magic list and `avg_stud` (not lists of lists), 14.2/14.4 tasks |
| `u7/m3`, `u7/m5` Lessons 12.6, 13.0–13.1 · 12.5, 14.4 | OK | Small patches only |
| `u8/m1` Lessons 16.0–16.2 | PATCH | Official 16.2 worksheet now delivered (four docs still say missing); add its advanced-features ideas, real song titles, use "פעולה" |
| `u8/m2`, `u8/m4` Lessons 17.0–17.1, 19.0–19.1 | PATCH (light) | 17.2, 19.2 and the 19.3 Colab notebook still missing; TensorFlow may not support Python 3.14; `Ministry_Model_Code.py` differs from the deck |
| `u8/m3` Lessons 18.0–18.1 | OK | Minor patch; images match (155 fist, 114 ok, 7 test) |
| `u9/m1`–`u9/m4` Lessons 20.0–22.1 | PATCH | Official has 3 lessons (20, 21, 22), our 4th meeting splits deck 21.1; 21.0, 21.2, 22.0, 22.2 missing so the Lessons 21.1–21.2 code and the Lessons 22.0–22.1 activity are unverified; poll figures in the Lessons 22.0–22.1 notes are our estimates from a chart (label approximate or verify) |

**Cross-cutting findings**
- No meeting needs a full REWORK; the units were already built from the same Ministry lessons. The gain is in patches, stale
  "missing file" claims (lists part A, worksheet 16.2) and verifying against the solutions that are now available.
- Official lessons 0.1–0.6 are Google Classroom onboarding (no Python, no hours): no meeting; optional use of the 0.1 deck.
  The short deck "מה נלמד השנה" is not in the repo (possible opener for Lessons 3.1–3.2).
- Rulebook conflicts inside the official files: nested loops (14.0 pp.25–29), a list-of-lists preview (14.0 p.30),
  `turtle.Turtle()` (12.0 p.17), a list inside a list (9.4 Q1), `sort(key=)` on the exam help sheet, default arguments (4.7 H5P),
  multiple return values (4.6). The teacher decides each; until then the rulebook stands.
- `def` is used everywhere in the official files; our code uses it from the functions block on, which is only valid once that block is taught.
  The advanced-language-model block (and parts of the strings classwork) use `def` before the functions block is taught: a policy is needed.
- Official files with errors or stale wording: 4.4 `secret4` (`while number > 1`), 6.2 unquoted `api_key`, 9.1 p.14 old error
  text, 14.0 `avg_stud` solution bug (`begin += (1+i)`).
- Still missing from the download (never invent): 17.2, 18.2 worksheet, 19.2, 19.3, 21.0, 21.2, 22.0, 22.2, and the
  exercises that exist only as links in `links.md`.

**Decisions needed from the teacher** (defaults in brackets)
1. Rework order [Lessons 8.2–8.7 → the lists block → the functions, API and AI2-opening blocks → the advanced-language-model, classification and recommender blocks → Lessons 2.0–2.3, as the class reaches them].
2. Rulebook exceptions: multiple return values (Lessons 4.3, 4.6), default arguments (4.7 H5P), nested loops and list of lists (14.0),
   `sort(key=)`; `def` in lessons 10.0–11.3 before the functions block [rulebook stands].
3. Lessons 8.0–8.1 and 8.2–8.7: one agreed time split, and `split`/`join` in Lessons 8.2–8.7 or only in Lessons 9.3, 9.5, 12.0–12.1 [rulebook allows showing it in Lessons 8.2–8.7].
4. Recommender block: keep 4 meetings (hours from the master table) [yes].
5. Slides: NotebookLM as now, or adapt the official `.pptx` decks [NotebookLM].
6. Ask the teacher to rerun the downloader and capture output if 17.2, 19.x, 21.x, 22.x should exist.
