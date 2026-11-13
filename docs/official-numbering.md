# Official numbering — how every meeting is named

**Decision (teacher, 13 Nov 2026):** the files and structure under `classroom-downloader\downloads\פייתון_ב\` are the source of truth, and
that includes **the numbers**. Meetings, decks, briefs, worksheets, the course map and chat use the **official lesson numbers**
(`8.1`, `8.2` …), not the repository's old unit/meeting numbers (`5.3`, `5.4` …).

- A 90-minute meeting usually covers several official lessons, so it is named by a **range of official lessons**:
  Hebrew **שיעורים 8.0–8.1 – מחרוזות** (one lesson: **שיעור 11.3 – …**), English **Lessons 8.0–8.1 — Strings** (one lesson: **Lesson 11.3 — …**).
  A non-contiguous set is written with commas: **שיעורים 9.1, 9.4 – רשימות**. The theme stays a subtitle.
- Titles, slide footers, NotebookLM notebook names, briefs and chat use this label. The words "מפגש" and "פרק" are still never used.
  Old labels (`Unit 5.4`, `יחידה 5.4`) must not appear in anything new; PDFs made before 13 Nov 2026 keep the old footer until they are regenerated.
- **File and folder names do not change** (`units/u5-strings/m4-…`, `Live4_Step…`, `PaperLab4_…`): they are internal keys. In this file and in
  `course-map.md` they are called the *file key* (`u5-strings/m4`).
- The official folder has gaps (never invented): 17.2, 19.2, 19.3, 21.0, 21.2, 22.0, 22.2, the 18.2 worksheet.
  Lessons 0.1–0.6 are Classroom onboarding (no meeting).

## The mapping (30 meetings → official lessons)

| File key | Official lessons (label) | English label | Theme | Main official files |
|---|---|---|---|---|
| `u1/m1` | שיעורים 1.0–1.1 | Lessons 1.0–1.1 | Python A review: conditions | 1.0, 1.1 (for-loop review; our content is mostly Python A conditions, partial match) |
| `u1/m2` | שיעורים 1.2–1.4 | Lessons 1.2–1.4 | Python A review: counting rounds | 1.2 worksheet, 1.4 summary (partial match) |
| `u1/m3` | שיעורים 2.0–2.3 | Lessons 2.0–2.3 | the `while` loop | 2.0, 2.1, 2.3 loop-trap deck |
| `u2/m1` | שיעורים 3.0–3.1 | Lessons 3.0–3.1 | AI2 year opening: AI or not | 3.0 notes, 3.1 deck (first half) |
| `u2/m2` | שיעורים 3.1–3.2 | Lessons 3.1–3.2 | AI2 year opening: Quick, Draw! | 3.1 deck (second half), 3.2, 3.2.0 |
| `u3/m1` | שיעורים 4.1–4.2 | Lessons 4.1–4.2 | functions: parameters and `return` | 4.1, 4.2, 4.2.0 |
| `u3/m2` | שיעורים 4.4–4.5 | Lessons 4.4–4.5 | functions: practice | 4.4, 4.5, 4.5.0 |
| `u3/m3` | שיעורים 4.3, 4.6 | Lessons 4.3, 4.6 | local and `global` variables | 4.3, 4.6, 4.5.0 |
| `u4/m1` | שיעורים 5.0–5.2 | Lessons 5.0–5.2 | API: the Gemini call | 5.0, 5.0.1, 5.0.2, 5.1, 5.2, 5.2.0 |
| `u4/m2` | שיעורים 6.1–6.2 | Lessons 6.1–6.2 | API: Balanced Day project | 6.1, 6.2, 6.2.0 |
| `u5/m1` | שיעור 7.1 | Lesson 7.1 | strings: first half | 7.1 |
| `u5/m2` | שיעורים 7.1–7.2 | Lessons 7.1–7.2 | strings: slicing, `count`, `replace`, `in`, `find` | 7.1, 7.2 |
| `u5/m3` | שיעורים 8.0–8.1 | Lessons 8.0–8.1 | strings: loops over a string | 8.0, 8.1 |
| `u5/m4` | שיעורים 8.2–8.7 | Lessons 8.2–8.7 | strings: practice and cipher | 8.2, 8.4 video, 8.7 summary |
| `u6/m1` | שיעורים 10.0–10.2 | Lessons 10.0–10.2 | advanced language model: tokens | 10.0, 10.1, 10.2, 10.2.0 |
| `u6/m2` | שיעורים 11.1–11.2 | Lessons 11.1–11.2 | meaning map and self-attention | 11.1, 11.2, 11.2.0 |
| `u6/m3` | שיעור 11.3 | Lesson 11.3 | Semantle project | 11.3, 11.3.0 |
| `u7/m1` | שיעורים 9.1, 9.4 | Lessons 9.1, 9.4 | lists part A | 9.1, 9.4 |
| `u7/m2` | שיעורים 9.3, 9.5, 12.0–12.1 | Lessons 9.3, 9.5, 12.0–12.1 | list methods | 9.1 (rest), 9.3, 9.5, 12.0, 12.1, 12.7, help sheet |
| `u7/m3` | שיעורים 12.6, 13.0–13.1 | Lessons 12.6, 13.0–13.1 | traversal | 12.6, 13.0, 13.1, 13.6 |
| `u7/m4` | שיעורים 13.2, 14.0–14.2 | Lessons 13.2, 14.0–14.2 | lists lab | 13.2, 14.0, 14.1, 14.2, 14.5 |
| `u7/m5` | שיעורים 12.5, 14.4 | Lessons 12.5, 14.4 | search and capstone | 12.5, 14.4 |
| `u8/m1` | שיעורים 16.0–16.2 | Lessons 16.0–16.2 | classification by features | 16.0, 16.1, 16.2, 16.2.0 |
| `u8/m2` | שיעורים 17.0–17.1 | Lessons 17.0–17.1 | training and test | 17.0, 17.0.1, 17.1 |
| `u8/m3` | שיעורים 18.0–18.1 | Lessons 18.0–18.1 | classification project | 18.0, 18.1, image data |
| `u8/m4` | שיעורים 19.0–19.1 | Lessons 19.0–19.1 | connecting a trained model | 19.0, 19.1 |
| `u9/m1` | שיעורים 20.0–20.1 | Lessons 20.0–20.1 | recommender systems: intro | 20.0, 20.1 |
| `u9/m2` | שיעור 21.1 | Lesson 21.1 | building a recommender: the table | 21.1 (first half) |
| `u9/m3` | שיעורים 21.1–21.2 | Lessons 21.1–21.2 | building a recommender: code | 21.1 (second half); 21.2 missing |
| `u9/m4` | שיעורים 22.0–22.1 | Lessons 22.0–22.1 | dangers of recommender systems | 22.0 missing, 22.1 |

Whole blocks (old "Unit N"): Python A review = lessons 1.0–2.3 · AI2 year opening = 3.0–3.2 · Functions = 4.1–4.6 · API = 5.0–6.2 ·
Strings = 7.1–8.7 · Advanced language model = 10.0–11.3 · Lists = 9.1–9.5 and 12.0–14.5 · Classification = 16.0–19.1 · Recommender systems = 20.0–22.1.
In prose write the block as "the strings block (lessons 7.1–8.7)", never "Unit 5".

Open points: (1) 1.1 and 1.2 have only a partial official match (official 1.x reviews the `for` loop; ours also covers conditions and counters);
(2) our four recommender meetings cover three official lessons (21.1 is split across two meetings);
(3) official lesson 15.x (exam preparation) and 9.2/12.2–12.4/13.4–13.5/14.3 exist only as links in `links.md`.

## Where the old numbers still appear (on purpose)

- File and folder names, links and `git` history (`units/u5-strings/m4-…`).
- Already-rendered PDFs (NotebookLM decks, patched decks, printed tests) until they are regenerated.
- The old numbers are kept in this table's first column only as the *file key*.
