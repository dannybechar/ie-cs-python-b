# Unit 4 — Bringing AI into Code (API)

Unit scope, official topics and hours: [`unit-strategy.md`](unit-strategy.md)

4 academic hours = 2 meetings = 180 minutes (45 theory / 135 practice).
**Status:** 🔶 rebuilt on the Ministry's teaching materials (decks 5.1 and 6.1, worksheets 5.2 and 6.2, teacher notes 5.0–5.0.2), awaiting teacher approval.

## Setting up the live service (Gemini)

The service is **Gemini** (`google-genai`, model `gemini-2.5-flash`, exactly as in the Ministry's text — check that the
name still works before class). Full steps are in `m1-lesson-notes.md`, "Tool Note – the AI service". In short:

1. **Keys:** the teacher creates up to 10 keys in Google AI Studio (one project each; about 15 requests/minute and 1,500/day per key) and shares each key among 3–4 students.
2. **Keeping the key secret:** *Colab* — Secrets (`GEMINI_API_KEY`, "Notebook access" on) and `userdata.get(...)`; *Thonny* — install `google-genai`, set the environment variable `GEMINI_API_KEY` on the computer and read it with `os.environ[...]`. Never a key in a file, slide, screenshot or the repo.
3. **Every `.py` file here runs by default with a classroom stand-in** (ZONE A, a fake client with fixed `[stand-in]` answers): plain `python`, no key, no internet. The live replacement is in comments inside the files.
4. **Files that need a live run with a real key before class:** `AskTheAI_Reference.py` (warm-up, `task1`, `task3`), `BalancedDay_Reference.py` (`task3`, `task4_features`). Check the model name, the answer text, and a 429/503 message once.

## Unit 4.1 — Bringing AI into Code (API)

**Topic:** What Is an API? The Gemini call, f-strings, the `ask_the_ai` wrapper

90 minutes: 45 knowledge + 45 lab · **waiter analogy → prompt = string → `+` vs f-string → the Gemini code → `ask_the_ai` returns → limits, golden rules, the secret key**

| For | File | What it is |
|---|---|---|
| Teacher | [`m1-lesson-notes.md`](m1-lesson-notes.md) | Lesson plan and live-service setup |
| Student | [`m1-lab-brief-he.md`](m1-lab-brief-he.md) | Hebrew lab brief |
| Student | [`AskTheAI_Starter.py`](AskTheAI_Starter.py) | Warm-up bug (`print(response)`), stand-in client, stubs for Tasks 1–3 |
| Teacher | [`AskTheAI_Reference.py`](AskTheAI_Reference.py) | Solutions, stand-in client, the live versions (Thonny, Colab) as comments |
| Teacher | [`m1-slides-he.pdf`](m1-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 18 slides, from the previous version) |

## Unit 4.2 — Bringing AI into Code (API)

**Topic:** The "Balanced Day" project

90 minutes: Lab + Lab · **a function that returns the hours → `while` accumulation → one prompt → one call after the loop → advanced features**

| For | File | What it is |
|---|---|---|
| Teacher | [`m2-lesson-notes.md`](m2-lesson-notes.md) | Lesson plan, including the project rubric |
| Student | [`m2-lab-brief-he.md`](m2-lab-brief-he.md) | Hebrew lab brief |
| Student | [`BalancedDay_Starter.py`](BalancedDay_Starter.py) | Warm-up bug (`{time_today}`), stand-in client, stubs for the stages and features |
| Teacher | [`BalancedDay_Reference.py`](BalancedDay_Reference.py) | Solutions for every stage and the feature version |
| Teacher | [`m2-slides-he.pdf`](m2-slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 17 slides, from the previous version) |
