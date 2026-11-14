# Lessons 5.0–6.2 — Bringing AI into Code (API)

Python B, Grade 8 · 4 academic hours = 2 meetings = 180 minutes (45 theory / 135 practice, official master table). 2 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

[Back to the ordered table of contents](../../CONTENTS.md) · [Repository home](../../README.md)

## Start here

| I want to… | Open |
|---|---|
| Read the unit's official scope, topics and hours | [`unit-strategy.md`](unit-strategy.md) |
| Read the background paper | *not yet added* (see below) |
| See the lesson sequence, minutes and status | [`unit-plan.md`](unit-plan.md) |
| Open a lesson (Hebrew lab brief, HTML deck, PDFs, worksheets) | [Lessons in teaching order](#lessons-in-teaching-order) |
| Get the student starter code and data files | [`exercises/`](exercises) |
| Plan a lesson, see solutions, answer keys, live-demo code (**teacher-only, do not distribute**) | [`teacher/`](teacher) |
| See external reviews | none yet: this repository has no per-unit `feedback/` folder |

## Background paper: go straight to a statement

The unit's background paper (`background-paper.md`) is **not yet added**; it is to be supplied by the owner and copied in unchanged. Until then the official scope per topic is in [`unit-strategy.md`](unit-strategy.md) and the Ministry sources are indexed in [`docs/ministry-teaching-materials.md`](../../docs/ministry-teaching-materials.md). There are no anchors to link, so the statement table is omitted.

## Lessons in teaching order

| # | Lesson (label · theme · Hebrew lab brief as `.md`, HTML deck, slide PDFs and worksheets) | Theory / practice min | Review status |
|---|---|---|---|
| 1 | **Lessons 5.0–5.2**<br>What Is an API? The Gemini Call, f-Strings, and the `ask_the_ai` Wrapper<br>[md](lessons/L01-the-gemini-call.md) · [html](lessons/L01-the-gemini-call.html) · [slides PDF](lessons/L01-the-gemini-call/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 6.1–6.2**<br>The "Balanced Day" Project<br>[md](lessons/L02-balanced-day.md) · [html](lessons/L02-balanced-day.html) · [slides PDF](lessons/L02-balanced-day/slides-he.pdf) | 0 / 90 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-the-gemini-call-notes.md`](teacher/L01-the-gemini-call-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-balanced-day-notes.md`](teacher/L02-balanced-day-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (2 files) |

## Status and open checks

- 0 of 2 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

4 academic hours = 2 meetings = 180 minutes (45 theory / 135 practice).
**Status:** 🔶 rebuilt on the Ministry's teaching materials (decks 5.1 and 6.1, worksheets 5.2 and 6.2, teacher notes 5.0–5.0.2), awaiting teacher approval.

### Setting up the live service (Gemini)

The service is **Gemini** (`google-genai`, model `gemini-2.5-flash`, exactly as in the Ministry's text — check that the
name still works before class). Full steps are in `m1-lesson-notes.md`, "Tool Note – the AI service". In short:

1. **Keys:** the teacher creates up to 10 keys in Google AI Studio (one project each; about 15 requests/minute, 1,000,000 tokens/minute and 1,500/day per key) and shares each key among 3–4 students.
2. **Keeping the key secret:** *Colab* — Secrets (`GEMINI_API_KEY`, "Notebook access" on) and `userdata.get(...)`; *Thonny* — install `google-genai`, set the environment variable `GEMINI_API_KEY` on the computer and read it with `os.environ[...]`. Never a key in a file, slide, screenshot or the repo.
3. **Every `.py` file here runs by default with a classroom stand-in** (ZONE A, a fake client with fixed `[stand-in]` answers): plain `python`, no key, no internet. The live replacement is in comments inside the files.
4. **Files that need a live run with a real key before class:** `AskTheAI_Reference.py` (warm-up, `task1`, `task3`), `BalancedDay_Reference.py` (`task3`, `task4_features`). Check the model name, the answer text, and a 429/503 message once.

**Live-run checklist (teacher, before class — everything else is verified offline with the stand-in):**

- [ ] Model name `gemini-2.5-flash` still accepted (it may be retired; the one-line test is in `m1-lesson-notes.md`).
- [ ] Library: `pip install -U google-genai` for Thonny (Tools › Manage packages) — **not** in the Ministry text, taken from the Gemini quickstart; Colab has it installed.
- [ ] Decide once: Colab (Ministry method, Secrets, nothing to install) or Thonny + environment variable.
- [ ] `AskTheAI_Reference.py`: warm-up (`print(response)`), `task1`, `task3` with the real client; check that `response.text` is the answer and read one real 429/503 message.
- [ ] `BalancedDay_Reference.py`: `task3` and `task4_features` with the real client; the call count must be 1.
- [ ] The key is in no file, slide or screenshot; the Ministry's own 6.2 snippet has an unquoted `YOUR_API_KEY` (a `NameError`, see `m2-lesson-notes.md`).

### Lessons 5.0–5.2 — Bringing AI into Code (API)

**Topic:** What Is an API? The Gemini call, f-strings, the `ask_the_ai` wrapper

90 minutes: 45 knowledge + 45 lab · **waiter analogy → prompt = string → `+` vs f-string → the Gemini code → `ask_the_ai` returns → limits, golden rules, the secret key**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-the-gemini-call-notes.md`](teacher/L01-the-gemini-call-notes.md) | Lesson plan and live-service setup |
| Student | [`L01-the-gemini-call.md`](lessons/L01-the-gemini-call.md) | Hebrew lab brief |
| Student | [`AskTheAI_Starter.py`](exercises/AskTheAI_Starter.py) | Warm-up bug (`print(response)`), stand-in client, stubs for Tasks 1–3 |
| Teacher | [`AskTheAI_Reference.py`](teacher/solutions/AskTheAI_Reference.py) | Solutions, stand-in client, the live versions (Thonny, Colab) as comments |
| Teacher | [`slides-he.pdf`](lessons/L01-the-gemini-call/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 18 slides, from the previous version) |

### Lessons 6.1–6.2 — Bringing AI into Code (API)

**Topic:** The "Balanced Day" project

90 minutes: Lab + Lab · **a function that returns the hours → `while` accumulation → one prompt → one call after the loop → advanced features**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-balanced-day-notes.md`](teacher/L02-balanced-day-notes.md) | Lesson plan, including the project rubric |
| Student | [`L02-balanced-day.md`](lessons/L02-balanced-day.md) | Hebrew lab brief |
| Student | [`BalancedDay_Starter.py`](exercises/BalancedDay_Starter.py) | Warm-up bug (`{time_today}`), stand-in client, stubs for the stages and features |
| Teacher | [`BalancedDay_Reference.py`](teacher/solutions/BalancedDay_Reference.py) | Solutions for every stage and the feature version |
| Teacher | [`slides-he.pdf`](lessons/L02-balanced-day/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, 17 slides, from the previous version) |
