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

More files are coming from the teacher (Ministry units after strings). Units 6–9 stay as built until they arrive.

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
