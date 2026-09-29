# python-b-built — staged units (not yet in `units/`)

This folder holds Units 4–9, built from `Downloads\python-b-codex\` at the teacher's request
("build units 3–9 using the codex materials... place your built units each one in a directory under python-b-built").
It is a **staging area** for the files themselves — a unit only moves to `units/` once the teacher approves it.
The root `course-map.md` and `README.md` *do* track what's here, though: built (🔶/⚠️) status is recorded as soon
as it's true, separately from approval (✅), which still only happens on "approve unit N". Nothing here has been
through the "approve unit N" routine yet. (Unit 3 was staged here too; it has since been reviewed, approved and
moved to [`units/u3-functions`](../units/u3-functions).)

## What's in each unit folder

Same internal shape as `units/`: `unit-strategy.md`, a unit `README.md`, and per meeting `m<K>-lesson-notes.md`,
`m<K>-lab-brief-he.md`, `<Topic>_Starter.py` / `<Topic>_Reference.py`. **No NotebookLM slide-prep folders** were
made this pass (the teacher chose "core materials only" when asked) — use "prepare slides U.M" per meeting later,
the same way it works for Units 1–2.

## Sources

- Units 4–9 core content: `Downloads\python-b-codex\` — each one `..._complete_unit.md` document covering every
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

Every `.py` file compiles and was run with representative test inputs before being committed. Of the units still
staged here, Units 4, 6, 8 and 9
call an outside service or library the classroom can't run headlessly (a language-model API, an embedding library,
a trained image classifier, a CSV survey) — those are verified with a stand-in that returns fixed values, exactly as
each source document's own "no internet / no key" fallback describes; the lesson notes say which files need a live
run with the real service before class.

## Status by unit

| Unit | Folder | Meetings | Status |
|---|---|---|---|
| 4 Bringing AI into Code (API) | [`u4-api`](u4-api) | 2 | 🔶 built (lesson notes, briefs, code and slides all done; awaiting approval) |
| 5 Strings | [`u5-strings`](u5-strings) | 4 | ⚠️ lesson notes, briefs and code done for all 4; slides done for 5.1–5.3, pending for 5.4 |
| 6 Advanced Language Model | [`u6-advanced-language-model`](u6-advanced-language-model) | 3 | ⚠️ lesson notes, briefs and code done; slides not yet prepared |
| 7 Lists | [`u7-lists`](u7-lists) | 5 | ⚠️ lesson notes, briefs and code done; slides not yet prepared |
| 8 Classification | [`u8-classification`](u8-classification) | 4 | ⚠️ lesson notes, briefs and code done; slides not yet prepared |
| 9 Recommender Systems | [`u9-recommender-systems`](u9-recommender-systems) | 4 | ⚠️ lesson notes, briefs and code done; slides not yet prepared |

## Moving a unit into the official course

Once the teacher approves a unit here (via "approve unit N"): move `python-b-built/u<N>-<slug>/` to
`units/u<N>-<slug>/`, then flip its status from 🔶 to ✅ in `course-map.md` and the root `README.md` — those files
already track this unit as built (🔶 or ⚠️) from the moment it's true, so approval only needs to update the status
mark and the physical location, not create the tracking from scratch.
