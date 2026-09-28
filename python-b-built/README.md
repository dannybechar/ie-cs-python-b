# python-b-built — staged units (not yet in `units/`)

This folder holds Units 3–9, built from `Downloads\python-b-codex\` at the teacher's request
("build units 3–9 using the codex materials... place your built units each one in a directory under python-b-built").
It is a **staging area**, kept deliberately separate from `units/` and from the root `course-map.md` / `README.md`,
which describe the official, reviewed course. Nothing here has been through the "review U.M" (slide check) or
"approve unit N" routines.

## What's in each unit folder

Same internal shape as `units/`: `unit-strategy.md`, a unit `README.md`, and per meeting `m<K>-lesson-notes.md`,
`m<K>-lab-brief-he.md`, `<Topic>_Starter.py` / `<Topic>_Reference.py`. **No NotebookLM slide-prep folders** were
made this pass (the teacher chose "core materials only" when asked) — use "prepare slides U.M" per meeting later,
the same way it works for Units 1–2.

## Sources

- Units 3, 4–9 core content: `Downloads\python-b-codex\` — Unit 3 is three PowerPoint decks (one per meeting, the
  same shape as Units 1–2's codex decks); Units 4–9 are each one `..._complete_unit.md` document covering every
  meeting of that unit, richly detailed (goals, full 90-minute timings, worked code, bug clinics, a graded project
  with a rubric).
- Official scope and hours: [`../docs/ministry-source/python-b-ai.pdf`](../docs/ministry-source/python-b-ai.pdf),
  read directly per unit (chapters 3–9) rather than relying only on the provisional outline in
  [`../docs/annual-strategy.md`](../docs/annual-strategy.md), which was written before any of this unit's source
  material existed. Where the real build's meeting split differs from that provisional guess, each unit's
  `unit-strategy.md` says so under "Scope decisions".
- Hours follow the master table (`python-b-ai.pdf` pp. 3–4), same as Units 1–2 — a chapter's own hours table is used
  only for the order and weight of its topics, never for the theory/practice split.

## Verification

Every `.py` file compiles and was run with representative test inputs before being committed. Units 4, 6, 8 and 9
call an outside service or library the classroom can't run headlessly (a language-model API, an embedding library,
a trained image classifier, a CSV survey) — those are verified with a stand-in that returns fixed values, exactly as
each source document's own "no internet / no key" fallback describes; the lesson notes say which files need a live
run with the real service before class.

## Status by unit

| Unit | Folder | Meetings | Status |
|---|---|---|---|
| 3 Functions | [`u3-functions`](u3-functions) | 3 | 🔶 built |
| 4 Bringing AI into Code (API) | [`u4-api`](u4-api) | 2 | 🔶 built |
| 5 Strings | [`u5-strings`](u5-strings) | 4 | 🔶 built |
| 6 Advanced Language Model | [`u6-advanced-language-model`](u6-advanced-language-model) | 3 | 🔶 built |
| 7 Lists | [`u7-lists`](u7-lists) | 5 | 🔶 built |
| 8 Classification | [`u8-classification`](u8-classification) | 4 | 🔶 built |
| 9 Recommender Systems | [`u9-recommender-systems`](u9-recommender-systems) | 4 | ⏳ |

## Moving a unit into the official course

Once the teacher has reviewed a unit here: move `python-b-built/u<N>-<slug>/` to `units/u<N>-<slug>/`, then update
`course-map.md` (time budget row, schedule rows, meeting log) and the root `README.md` exactly as the normal
"build unit N" routine in `CLAUDE.md` would have — those files were deliberately left untouched while this unit
lived here, so no existing tracking was disturbed.
