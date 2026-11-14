# Lessons 3.0–3.2 — AI2 Year Opening

Python B, Grade 8 · 4 academic hours = 2 meetings = 180 minutes (90 theory / 90 practice, official master table). 2 lessons: the Hebrew lab brief is the lesson page, with a generated HTML deck beside it. Official scope: [`unit-strategy.md`](unit-strategy.md).

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
| 1 | **Lessons 3.0–3.1**<br>AI or Not? A Greeting for Grandma Sarah — Classic Code vs AI<br>[md](lessons/L01-ai-or-not.md) · [html](lessons/L01-ai-or-not.html) · [slides PDF](lessons/L01-ai-or-not/slides-he.pdf) | 45 / 45 | Built, awaiting approval |
| 2 | **Lessons 3.1–3.2**<br>How Does a Computer See Without Eyes? Quick, Draw!, Data and the Road Ahead<br>[md](lessons/L02-quick-draw.md) · [html](lessons/L02-quick-draw.html) · [slides PDF](lessons/L02-quick-draw/slides-he.pdf) | 45 / 45 | Built, awaiting approval |

The `.html` decks are generated from the `.md` lesson pages by [`tools/lesson-decks/`](../../tools/lesson-decks/README.md); they have not been reviewed by the teacher. GitHub shows `.html` as source: open a downloaded copy in a browser. Lesson folders `lessons/L<NN>-<slug>/` hold the PDFs (NotebookLM decks, live-lesson decks) and printable worksheets.

## Teacher-only material (do not distribute)

| File | What it is |
|---|---|
| [`teacher/L01-ai-or-not-notes.md`](teacher/L01-ai-or-not-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/L02-quick-draw-notes.md`](teacher/L02-quick-draw-notes.md) | Lesson notes: minute-by-minute teacher plan |
| [`teacher/solutions/`](teacher/solutions) | Reference solutions, one `.py` per task or question (2 files) |

## Status and open checks

- 0 of 2 lessons approved by the teacher; the rest are built and awaiting approval.
- Background paper: not yet added. The anchor-link check cannot run for this unit until it exists.
- HTML decks: generated from the lab briefs; not reviewed by the teacher. Layout was checked in a browser on a sample only.
- File names inside the folders changed in the 14 Nov 2026 restructure; older notes use the flat `m<K>-…` names (map in [`units/README.md`](../README.md)).

## Detailed materials index

The text below is the unit's earlier README, links updated to the new layout.

4 academic hours = 2 meetings = 180 minutes (90 theory / 90 practice).
Reworked from the Ministry teaching materials (deck 3.1, worksheet 3.2) — 🔶 built, awaiting approval.

### Lessons 3.0–3.1 — AI2 Year Opening

**Topic:** AI or Not? A Greeting for Grandma Sarah (classic code vs AI)

90 minutes: 45 knowledge + 45 lab · **AI or not? → quiz → definition → revolutions → classic greeting in Python vs AI greeting**

| For | File | What it is |
|---|---|---|
| Teacher | [`L01-ai-or-not-notes.md`](teacher/L01-ai-or-not-notes.md) | Lesson plan |
| Student | [`L01-ai-or-not.md`](lessons/L01-ai-or-not.md) | Hebrew lab brief (greeting program, exit check) |
| Student | [`Greeting_Starter.py`](exercises/Greeting_Starter.py) | Warm-up bug (variable inside quotes) and task stubs |
| Teacher | [`Greeting_Reference.py`](teacher/solutions/Greeting_Reference.py) | Answers, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L01-ai-or-not/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, "Rules or Learning?", 18 slides) |

Needs-regeneration note (13 Nov 2026): the Pichai quote (slide 6) was added to the source content of the NotebookLM deck; the Gemini-window tip is in the notes.

Live check: the chatbot demo of the AI greeting (needs a chatbot the school allows) and the Ministry's image pairs (deck 3.1, slides 3–6).

### Lessons 3.1–3.2 — AI2 Year Opening

**Topic:** How Does a Computer See Without Eyes? (Quick, Draw!, data and the road ahead)

90 minutes: 45 knowledge + 45 lab · **Quick, Draw! on the board → consumers to creators → road map → worksheet 3.2 → responsibility**

| For | File | What it is |
|---|---|---|
| Teacher | [`L02-quick-draw-notes.md`](teacher/L02-quick-draw-notes.md) | Lesson plan, with the Ministry's model answers |
| Student | [`L02-quick-draw.md`](lessons/L02-quick-draw.md) | Hebrew lab brief that follows the Ministry worksheet 3.2 |
| Student | [`Audit_Starter.py`](exercises/Audit_Starter.py) | If-time block: reversed-comparison warm-up bug, stub for the car audit |
| Teacher | [`Audit_Reference.py`](teacher/solutions/Audit_Reference.py) | Solutions, one function per task |
| Teacher | [`slides-he.pdf`](lessons/L02-quick-draw/slides-he.pdf) | Superseded — pending new NotebookLM deck (old deck, "Data, Bias and Responsibility", 18 slides) |

Added 13 Nov 2026 from the Ministry teacher notes 3.0: the Amazon CV-screening story (2014-2018), an explicit question after the Sapir video, and the optional 5-minute short deck "מצגת קצרצרה — מה נלמד השנה" (10 slides) inside the road-map block. The deck's prep-folder source content gained the Sapir question and the Amazon story (slides 8 and 18; still 20 slides) — regenerate the deck in NotebookLM if you want them on the slides.

Needs internet for Quick, Draw! (`quickdraw.withgoogle.com`) and its data page; the worksheet 3.2 is the Ministry's file (Classroom).

### Ministry links and notes

- Ministry self-check Forms (Master Python): [2.2 Master Python — `while` loop](https://docs.google.com/forms/d/1iVIu9A1WjI1BOVbBhOSiwelbBcOfQL38EZjM8INNy9A/edit) · [1.3 Master Python — `for` loop](https://docs.google.com/forms/d/1WUsETmUxov-vwmOvYFyUP2Z_DvkNL31lyC_0G7iGbbk/edit) · [0.5 Forms task](https://docs.google.com/forms/d/1yKQi6ZiFGpd7DH8khMaxQ2Qiq0IPaWJGJGkNqZBMuwU/edit) (the first two belong to the Python A review block (lessons 1.0–2.3); listed here with the Ministry set).
- The Ministry's lessons 0.1–0.6 are Google Classroom onboarding only (Classroom, screenshot, file upload, a Google Form; no Python, no AI). They have no meeting and no hours in the master table; the class is past them.
