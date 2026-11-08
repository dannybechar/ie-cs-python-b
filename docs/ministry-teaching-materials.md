# Ministry teaching materials — the source of truth

**Authority (teacher's decision, 31 Oct 2026):** the PDFs in
`C:\Users\Guitar\Downloads\השתלמות\מצגות-השתלמות\` are the **official teaching materials published by the Ministry of
Education** (decks, "תרגול לפיצוח" worksheets, teacher solutions, API-key guides). They override the teacher's raw
materials (`python-b-raw-meterials`, inspiration only) and the units we first built from the Ministry *program* text
alone. The program ([`ministry-source/python-b-ai.pdf`](ministry-source/python-b-ai.pdf)) still sets goals and hours;
these materials set **what is taught, in which examples and with which exercises**.

The PDFs are not copied into the repo (size, and they remain the Ministry's files). Read them with PyMuPDF
(`python`, not `python -I`, so user-site packages load); Hebrew text extracts in visual order — check the page image
when a line looks scrambled. The Ministry's file numbers (2.0 … 8.7) are **its own lesson numbers, not our unit numbers.**

The files for the Ministry's lessons 10–22 arrived on **8 Nov 2026** (our Units 6–9). They were audited the same day (section
"Audit of lessons 10–22" below); Units 6–9 were all reworked the same day. Some files are still missing (list below).

## File inventory and where each file lands

| Ministry file | What it is | Our meeting |
|---|---|---|
| 2.0 מצגת למורה — לולאת תנאי while — חזרה | deck, 12 slides | 1.3 |
| 2.1 תרגול לפיצוח — לולאת while | worksheet, 4 questions | 1.3 |
| מלכודת הלולאה האינסופית | teacher's NotebookLM deck, 14 slides (image-only): diagnosing infinite `while` loops | 1.3 |
| 3.1 מצגת — שיעור פתיחה לשנה ב AI2 | deck, 50 slides | 2.1, 2.2 |
| 3.2 / 3.2.0 תרגול לפיצוח — איך מחשב רואה בלי עיניים (+ teacher solution) | Quick, Draw! worksheet | 2.2 |
| 4.1 מצגת פעולות חלק א | deck, 28 slides: multiple parameters, `return` | 3.1 |
| 4.2 / 4.2.0 דף תרגילים פעולה המחזירה ערך (+ solution) | worksheet | 3.1, 3.2 |
| 4.3 משתנים בפעולות | deck, 24 slides: local and `global` | 3.3 |
| 4.4 תרגול לפיצוח — שאלות מבחינות | exam-style questions (functions + `while`) | 3.2 |
| 4.5 / 4.5.0 תרגילי פעולות ומשתנים (+ solution) | worksheet: local vs global, `return` | 3.2, 3.3 |
| 4.6 תרגול לפיצוח — תפקידי משתנים בפעולות | worksheet (+ solution in 4.5.0) | 3.3 |
| 5.0 דגשים למורה; 5.0.1 Gemini API key (teacher); 5.0.2 keeping the key secret (Colab Secrets) | teacher notes | 4.1, 4.2 |
| 5.1 מצגת — API; 5.2 / 5.2.0 תרגול (+ solution) | deck 32 slides + worksheet | 4.1 |
| 6.1 מצגת — פרויקטון יום מאוזן; 6.2 / 6.2.0 תרגול (+ solution) | deck 13 slides + worksheet | 4.2 |
| 7.1 מחרוזות חלק א׳; 7.2 דף עבודה מחרוזות | deck 40 slides + worksheet (Python A material, revisited) | 5.1, 5.2 |
| 8.0 מצגת למורה — מחרוזות; 8.1 פייתון ב׳ מחרוזות; 8.2 תרגול; 8.7 סיכום בקטנה | decks 27 + 33 slides, worksheet, one-page summary | 5.3, 5.4 |
| 10.0 דגשים למורה; 10.1 מצגת — טוקנים (35 slides); 10.2 / 10.2.0 דף עבודה — טוקנייזר (+ solution) | teacher notes, deck, worksheet | 6.1 |
| 11.1 מצגת — מפת המשמעויות והקשב העצמי (28 slides); 11.2 / 11.2.0 דף עבודה #1 הכנה לפרויקטון סמנטעל (+ solution) | deck, worksheet | 6.2 |
| 11.3 / 11.3.0 דף עבודה #2 פרויקטון סמנטעל (+ solution) | project worksheet | 6.3 |
| 12.0 / 12.1 רשימות חלק ב׳ (27 / 42 slides); 12.5 תרגול #2; 12.6 מאסטר פייתון; 12.7 סיכום | decks, worksheets, summary | 7.x (reworked 8 Nov 2026) |
| 13.0 / 13.1 רשימות חלק ג׳ (18 / 19); 13.6 סיכום | decks, summary | 7.x (reworked 8 Nov 2026) |
| 14.0 / 14.1 רשימות חלק ד׳ (30 / 27) | decks | 7.x (reworked 8 Nov 2026) |
| 16.0 / 16.1 / 16.2.0 סיווג לפי תכונות (1 / 68 / 9) | teacher notes, deck, teacher solution | 8.1 (reworked 8 Nov 2026) |
| 17.0 / 17.0.1 / 17.1 אימון ומבחן של מודל סיווג; 18.0 / 18.1 פרויקט סיווג; 19.0 / 19.1 חיבור מודל מאומן לפייתון | notes, Teachable Machine helper deck, decks | 8.2–8.4 (reworked 8 Nov 2026) |
| 20.0 / 20.1 הכרות עם מערכות המלצה; 21.1 בונים מערכת המלצה; 22.1 סכנות במערכות המלצה | notes, decks | 9.1–9.4 (reworked 8 Nov 2026) |
| `תמונות לאימון` zip (269 AI-generated images: `ok/` 114, `fist/` 155) and `תמונות למבחן` zip (7 test images) | the fist/OK project data | 8.3, 8.4 |

## Rulebook changes (they replace the older restrictions in `CLAUDE.md`)

The Ministry's own materials do these, so the course does too:

- **`global`** is taught (Unit 3.3): a variable defined outside every function can be read inside; changing it from
  inside needs `global name`; without it Python makes a new local variable. Includes the `UnboundLocalError` trap.
  **Verify error messages on the installed Python** — the Ministry's text is older than Python 3.14
  (`UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`).
- **`+=`** is allowed (the Ministry uses it from Unit 1's review and in the strings unit). `x = x + 1` stays fine.
- **`print(..., end="")`** is allowed (Unit 5 string traversal). Writing your own functions with default or keyword
  arguments is still not taught.
- **`split` and `join`** appear in Unit 5 (string methods, 8.1); the result is a list, shown and printed only.
  Lists as a topic (indexing, `append`, traversal, …) stay in Unit 7, which revisits `split`/`join`.
- **`ord()` / `chr()`** (ASCII, "next letter" cipher) are taught in Unit 5 (8.0, 8.1).
- **API service: Gemini** (`from google import genai`, `genai.Client(api_key=…)`, `client.models.generate_content`,
  model `gemini-2.5-flash` in the Ministry text — check the current name before class). The teacher creates the keys
  beforehand (5.0.1: up to 10 projects, ≈15 requests/minute, 1,500/day per key — so students share and work in groups).
  The Ministry keeps the key secret with **Colab Secrets** (`google.colab.userdata.get("GEMINI_API_KEY")`), 5.0.2.
  Our default tool is Thonny, so every Unit 4 file also has a stand-in `ask_the_ai()` (fixed answers) for verification
  and for a class without keys or internet. Never put a key in a file.
- **Unchanged:** no nested loops, tuples, sets, dictionaries, comprehensions, lists of lists, classes; lists as a topic
  only from Unit 7.

## Gaps this closes in the units we built

- 1.3 had no infinite-loop teaching → the loop-trap deck and 2.0/2.1.
- 2.1/2.2 lacked the "AI or not" quizzes, the grandma greeting (classic vs AI), the revolutions story and the
  Quick, Draw! data worksheet (bias, Israeli stop sign).
- Unit 3 started from zero-parameter functions; the Ministry starts from multiple parameters and `return`, then scope.
- Unit 4: the service is Gemini, the key guides exist, and the Ministry's own "Balanced Day" worksheet is the project.
- Unit 5 was planned 45 / 315 minutes; the official split is **90 / 270** — two Knowledge + Lab meetings (5.1, 5.2),
  two Lab + Lab (5.3, 5.4).

## Status

Reworked units are 🔶 (built, awaiting approval) until the teacher approves them again. Slide decks built from the
older content are marked superseded in each unit README until the new NotebookLM deck is reviewed.

## Audit of lessons 10–22 (8 Nov 2026)

Method: the text of every PDF was extracted and read, image-only slides were rendered where it mattered, and our Unit 6–9 files were
compared with it (one reviewer per unit group). **Units 6–9 are reworked (🔶)**; the findings below are what each rework fixed, plus what is still open.

**Numbering:** the Ministry's numbers are its own lessons. 10–11 = our Unit 6 (2 Ministry meetings; we keep 3), 12–14 = Unit 7,
16–19 = Unit 8 (4 meetings, as ours), 20–22 = Unit 9 (3 Ministry meetings; ours has 4).

**Still missing from the folder (to ask the teacher for):** Lists part A (part B opens with "as we learned") and part E (14.0 p. 30:
"next lesson, a list of lists"); the numbered worksheets and keys 12.2–12.4, 13.2–13.5, 14.2 onward, 15, 16.2 (only its key 16.2.0
exists), 17.2, 18.2, 19.2, 19.3 (Colab), 20.2, 21.2 (it holds the real recommender code), 22.2, and the teacher notes 21.0 and 22.0.

**Rule conflicts to settle:**
- `def` / `return` appear in almost every Ministry worksheet (Units 6–9) while the class has not learned functions. Unit 6 assumes Unit 3 first.
- The Ministry previews **nested loops** (14.0 pp. 25–29, "will be learned later") and announces **lists of lists** (part E). CLAUDE.md says never.
- Our Unit 9 uses tuples and default arguments, both banned; to rewrite when the unit is reworked.

**Unit 6 (done):** the Ministry uses the real `paraphrase-multilingual-MiniLM-L12-v2`; our v1 mock (with invented scores) is replaced.
Deck 10.1's token-quiz numbers come from a different tokenizer than the worksheet's (6 / 6 / 5 / 10 in the deck, 6 / 7 / 5 / 5 measured
with the worksheet's tokenizer).
**Unit 7 (open):** add list slicing (`[a:b:c]`, `[::-1]`), `list()`, `index()`, `+`, the flat name/price menu and parallel lists. The Ministry
decks contain bugs (`append(i)` for `append(item)`, 12.0 p. 10; curly quotes; stray parentheses) — never copy them as they are.
**Unit 8 (open):** the Ministry loads `converted_savedmodel.zip` with `tf.keras.layers.TFSMLayer` (we use `keras_Model.h5` and a mock);
add the two-feature scatter and separating line, the bias examples, the 85% confidence rule, the Teachable Machine guide 17.0.1 and the two
image zips.
**Unit 9 (open):** the survey uses V / X / 0 (we use 0–3); add the YouTube-feed riddle, the "culinary twin" game, Plato's cave, the three
traps (filter bubble, echo chamber, addiction engineering) and the incognito demo; the Ministry's twin is simply the participant with the
most identical non-0 answers.

**Reworks done (8 Nov 2026):** Units 6–9 follow the Ministry decks and worksheets; decisions taken without the teacher: `def` allowed in Units 6–9;
Unit 7 has no nested loops and no lists of lists; Unit 8 uses the Ministry's SavedModel + `TFSMLayer` code (plus a stand-in so the files run without
TensorFlow); Unit 9 keeps four meetings, uses V / X / 0 and flat lists (no tuples, defaults or `csv`), with a teacher-only `CsvToLists_Teacher.py`.
Ministry slide errors found while verifying (never to be copied): 14.0 p. 12 wrong example averages, 14.0 p. 23 `begin += 1 + i` skips a grade, 12.1 pp. 31–32
stray parenthesis and a late special-list check, 12.0 p. 10 `append(i)`. Files that still need a live run: Unit 8 `Ministry_Model_Code.py` and the Teachable Machine export,
Unit 9 Forms export and incognito demo, Unit 7 `input()` tasks in Thonny.
