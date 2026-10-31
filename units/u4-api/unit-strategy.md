# Unit 4 — Bringing AI into Code (API)

**4h = 1 Theory + 3 Practice = 2 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 4 (pp. 11–13); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 rebuilt on the Ministry's teaching materials — both meetings built, awaiting teacher approval.
**Sources** (the teacher's decision: the Ministry's own materials are the source of truth; see
[`../../docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md)): teacher notes 5.0, 5.0.1 (Gemini
API key), 5.0.2 (keeping the key secret); deck 5.1 (32 slides) + worksheet 5.2 / solution 5.2.0 → meeting 4.1;
deck 6.1 (13 slides) + worksheet 6.2 / solution 6.2.0 ("Balanced Day") → meeting 4.2. The earlier version (built from
the program text and the teacher's raw document) is replaced; its Hebrew decks are kept but superseded.

## Official topics and hours

Unit totals from the master table (1 theory / 3 practice). The chapter's own table (p. 11) gives the same split
(2 h / 2 h across its two topic rows, T 1 + P 1 and T 0 + P 2) — for once master table and chapter table agree.
Minutes = hours × 45.

| Topic (Ministry, p. 11) | Chapter-table hours (T / P) | Planned in | Minutes (T / P) | Status |
|---|---:|---|---:|---|
| מבוא ל-API, מפתח, ייבוא ספריות ופונקציית עטיפה — API intro, key, imports, wrapper function | 1 / 1 | 4.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| פרומפטים דינמיים, לולאות צבירה ופרויקטון "יום מאוזן" — dynamic prompts, accumulation loops, the project | 0 / 2 | 4.2 (90 P) | 0 / 90 | 🔶 |
| **Total** | **1 / 3** | | **45 / 135** | |

Chapter goals (p. 11 continues to p. 12 in the source document's own numbering):

1. Explain what an API is via the client–server model / the waiter analogy → 4.1 🔶
2. Explain what an API key is and why it must never be written in code or shared → 4.1 🔶
3. Import a third-party library and set up a client for an AI service → 4.1 🔶
4. Write a wrapper function that takes a prompt, makes the API call, and returns the answer with `return` → 4.1 🔶
5. Build a dynamic prompt with an f-string and user input → 4.2 🔶
6. Accumulate input with a `while` loop and string concatenation → 4.2 🔶
7. Validate input with `len`, compound conditions and `in` → 4.2 🔶
8. Explain why data is collected first and **one** API call is made outside the loop → 4.2 🔶
9. Identify rate limits, overload errors, possible costs, and inaccurate answers → 4.1–4.2 🔶
10. Protect user privacy and check an AI answer before relying on it → 4.1–4.2 🔶

## Unit 4.1 — Knowledge + Lab: What Is an API? The Gemini Call and `ask_the_ai`
Follows the Ministry deck 5.1 in order (45 theory / 45 lab):
- the waiter analogy (client = our code, kitchen = Google's server, waiter = the API); "what an API looks like to
  Python": an external function call that takes time — no internet, an error;
- a prompt is just a string; building it with `+` and then with **f-strings (new here)**;
- the Gemini code line by line: `from google import genai`, `client = genai.Client(api_key=…)`, the model name (not
  changed), `contents=` the prompt, `response.text`;
- the wrapper `ask_the_ai(my_prompt)` that **returns** the text — why: clean code, reuse, a black box;
- limits (≈15 requests/minute, 1,500/day per key), errors 429 / 503, the three golden rules (plan first and test in a chat ·
  send only what is needed · never call the API inside a loop), keeping the key secret;
- lab (worksheet 5.2): warm-up bug `print(response)` → the wrapper → the grandma greeting with an f-string → the dream
  dessert with a `while` accumulation and one call; if time: `len` guard and a default value.

## Unit 4.2 — Lab + Lab: the "Balanced Day" Project
Follows the Ministry deck 6.1 (a very short intro) and worksheet 6.2 (90 minutes, all practice):
- stage 1: `home_hour`, `sleep_hour`, `calc_time_today` returns the hours;
- stage 2: a `while` loop that accumulates the task names and times into one string (`all_tasks +=`);
- stage 3: an f-string prompt (context, task, data, wanted result), `ask_the_ai` called **once**, after the loop;
- a base part everyone finishes, then advanced features (emojis, language, `len` check, net fun time and no call when
  there is none, a motivation sentence, percentage summary); our additions: a basic privacy check and an answer critique.

### Scope decisions
- **The AI service is settled: Gemini** (`google-genai`, model `gemini-2.5-flash` exactly as the Ministry shows it — to be
  re-checked before class, the Ministry text is older than today's model list). Keys: created by the teacher (5.0.1),
  up to 10, shared in groups of 3–4; the Ministry keeps them secret with **Colab Secrets**; for Thonny we read an
  **environment variable**. Never a key in a file.
- **Tool: open decision.** The Ministry worksheets are Colab / Google Classroom notebooks; our default is Thonny. Every
  `.py` file runs by default with a **classroom stand-in** (ZONE A: a fake `client` with fixed answers, tagged
  `[stand-in]`), so it runs on plain Python with no key or internet; the student code under ZONE A is identical to the
  real code, and the live replacement is documented in comments. The stand-in also counts calls (`client.models.calls`)
  to make "one call, after the loop" visible.
- **Rulebook changes used:** f-strings are taught (the Ministry teaches them here); `+=` is used; a keyword-argument
  *call* (`generate_content(model=…, contents=…)`) is shown as part of the library's syntax — students do not define
  functions with keyword arguments. `try`/`except` is not taught: 429/503 means wait and run again.
- **Dropped from the worksheets:** a list of banned words (lists are Unit 7 — an `or` chain does the same), colored
  console output (ANSI codes do not render in Thonny; Colab only).
- **Language of the code:** prompts, `input()` texts and the stop word (`done`) are in English in our files (no keyboard
  switching, clean left-to-right code in decks and briefs); the Ministry's Hebrew `"סיום"` is a one-word swap.

## Exit criteria
The student explains the API request/response path (the waiter) and why a key is a secret, writes a wrapper function
that takes a prompt and **returns** the answer, builds a dynamic prompt with an f-string, writes a function that returns
a value (`calc_time_today`), accumulates input into one string with a `while` loop, and explains why data is
collected first and the AI is called once, after the loop.

## Checkpoint
4.2's "Balanced Day" project is the unit's capstone, scored on the 20-point rubric in `m2-lesson-notes.md` (functions
that return a value, key security, dynamic prompt, accumulation loop, one call outside the loop, validation and privacy,
testing) — the rubric is ours; the Ministry gives none.

## Enrichment
The worksheets' advanced features not done in class (a style choice with `if`/`elif`/`else`, a length limit, a check that
`sleep_hour` is after `home_hour`, comparing two versions of the same prompt, colored output in Colab).
