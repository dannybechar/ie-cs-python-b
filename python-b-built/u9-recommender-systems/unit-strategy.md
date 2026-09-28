# Unit 9 — Recommender Systems

**8h = 4 Theory + 4 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 9 (pp. 21–23); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 built from the codex material only — **staged in `python-b-built/`, not yet in `units/`.**
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit09_recommendation_systems_complete_unit.md` —
one detailed document covering all four meetings, including its own exact 90-minute clock tables and meeting split.

## Official topics and hours

Unit totals from the master table (4 theory / 4 practice), matching the chapter's own table exactly (intro +
survey design 1/1, coding the recommender 1/2, algorithm pitfalls + ethics + the attention economy 2/1, total 4/4 —
for once both agree, same as Units 4, 6 and 8).

| Topic | Planned in | Minutes (T / P) | Status |
|---|---|---:|---|
| Recommender systems intro, project design, Google Forms data collection | 9.1 (45 T + 45 P) | 45 / 45 | 🔶 |
| Reading CSV data, computing similarity between users | 9.2 (45 T + 45 P) | 45 / 45 | 🔶 |
| Finding a digital twin, producing a recommendation | 9.3 (45 T + 45 P) | 45 / 45 | 🔶 |
| Filter bubble experiment, ethics, the attention economy | 9.4 (45 T + 45 P) | 45 / 45 | 🔶 |
| **Total** | | **180 / 180** | |

Chapter goals (source §1, fourteen in all):

1. Explain why digital services use recommender systems → 9.1
2. Distinguish content-based from user-based recommendation → 9.1
3. Represent preferences with parallel rating lists → 9.1–9.2
4. Explain a shared rating and why an unknown item is excluded → 9.1–9.2
5. Trace a similarity-score calculation with a trace table → 9.2
6. Implement a similarity function with a loop and compound conditions → 9.2
7. Find the most similar user — the "digital twin" → 9.3
8. Recommend an item unknown to the current user but liked by the twin → 9.3
9. Read rating data from a CSV file and combine several functions in a main program → 9.2–9.3
10. Test the system on normal cases and edge cases → 9.2–9.3
11. Define a filter bubble, an echo chamber, and the attention economy → 9.4
12. Analyze how behavioral signals can shape recommendations → 9.4
13. Propose practical tools for better feed control → 9.4
14. Identify ethical limits: privacy, consent, data scarcity, bias → 9.1, 9.4

## Unit 9.1 — Knowledge + Lab: What Is a Recommender System? + Data Collection
- input/process/output in a recommendation system; content-based (by item features) vs. user-based (by similar
  users' preferences) filtering, with a "which approach?" classification drill.
- a manual "digital twin" simulation with rating cards, before any code; the agreed rating scale
  (`0`=don't know, `1`=disliked, `2`=neutral, `3`=liked) and why a shared, closed scale matters for code.
- designing a short, anonymous class survey (an alias, not a name; a neutral topic; 6–10 items; the same scale for
  every item) and exporting it to a clean CSV.
- lab: an inverted-rating-meaning warm-up bug, a row validator, a "known items" counter.

## Unit 9.2 — Knowledge + Lab: From CSV to a Similarity Score
- reading `ratings.csv` into three parallel structures (item names, aliases, rating lists) with `csv.reader`.
- a similarity function's plan in pseudocode, then a hand-traced table, then Python: count `common` items (neither
  rating is `0`) and `matches` (equal ratings) in one loop; a match **rate**, guarded against division by zero.
- lab: the source's own "counts `0 == 0` as a match" bug as the warm-up, completing `load_ratings` on a real
  `ratings.csv`, `similarity_score`, `similarity_rate` — checked against the source's own asserts.

## Unit 9.3 — Knowledge + Lab: From Digital Twin to Recommendation (unit checkpoint)
- comparing the target user to every other user (never itself), keeping the best `(rate, common)` pair — the rate
  is primary, shared-count breaks ties.
- recommending an item the target rated `0` where the twin's rating is at least a threshold, choosing the twin's
  highest such rating; returning `None` explicitly rather than crashing when no twin or no recommendation exists.
- combining `load_ratings`, `similarity_score`, `find_digital_twin` and `recommend_item` into one `main()`.
- three real limits, named explicitly: cold start, data sparsity, and "similar preferences" not implying similar
  people.
- lab: the source's own "compared to itself" bug as the warm-up, completing `recommend_item`, then the checkpoint —
  the full pipeline, verified against all seven of the source's own test cases.

## Unit 9.4 — Knowledge + Lab: Filter Bubbles, Echo Chambers, the Attention Economy
- what is and isn't known about a real platform's ranking signals — the point of a short controlled experiment is a
  **local observation**, not proof of the full algorithm.
- a controlled "building a bubble" experiment (safe-topic private browsing, or an offline card simulation using the
  exact rule the source specifies — two same-topic cards plus one other per round), logging observation separately
  from interpretation.
- filter bubble (algorithmic filtering narrows what's shown) vs. echo chamber (social reinforcement narrows what's
  believed) — related but distinct; the attention economy (engagement as the optimized metric, not necessarily
  learning or well-being).
- connecting the class's own code decisions (a single twin, a low `minimum_common`, a fixed tie-break rule) to their
  real downstream effects; a concrete feed-control toolkit.
- lab: an inverted related/unrelated-count warm-up bug, then a deterministic simulation of the card rule
  (`simulate_feed_round`, `run_bubble_experiment`) that reproduces the bubble effect numerically, without needing
  a real account, network access, or a random module.

### Scope decisions
- **The source document is the only material and is unusually complete** — clock tables (verified to sum to 90 for
  each meeting), worked code, a full privacy section for the survey, a thorough YouTube-experiment safety section,
  a project rubric and closing summary questions. Followed closely; adapted into the house lesson-notes/lab-brief
  split and warm-up-bug convention.
- **A real `ratings.csv` is used and genuinely read from disk** (unlike Units 4, 6 and 8's external-service code):
  reading a local CSV file needs no network, no API key, and no installed package beyond the standard library, so
  9.2–9.3's `load_ratings()` is verified for real, not with a stand-in. The sample file matches the source's own
  example data (three users, four travel destinations) and holds no real personal information — aliases only.
- **9.1's Google Forms / survey collection and 9.4's YouTube experiment are real-world activities, not code.** The
  lesson notes describe both in full, including every privacy and safety rule from the source verbatim, but neither
  is something to "run" in a `.py` file. 9.4's lab instead gives a **deterministic** in-code simulation of the
  source's own offline card-simulation rule (Option B) — a legitimate, fully testable stand-in for the live
  experiment that needs no account, network, or `random` module.
- **Not taught:** dictionaries (an obvious fit for name→rating lookups, but not in this course — parallel lists are
  used throughout, exactly as the source itself does), content-based filtering in code (named and contrasted with
  user-based filtering, but only user-based is implemented, matching the source's own scope), matrix factorization
  or any real collaborative-filtering algorithm.

## Exit criteria
The student distinguishes content-based from user-based recommendation, represents preferences as parallel rating
lists and correctly excludes unshared (`0`) ratings from a similarity calculation, implements a similarity function
and finds the most similar user, produces and tests a recommendation (including its `None` cases), and explains
filter bubbles, echo chambers and the attention economy with at least one concrete, practical response to each.

## Checkpoint
9.3's user-based recommender (`load_ratings`, `similarity_score`, `find_digital_twin`, `recommend_item`, `main`) is
the unit's capstone, with the source's own 20-point rubric across five weighted bands (data & privacy, similarity
calculation, twin & recommendation, code quality, critical thinking) — see the lesson notes for the full rubric.
Verified here against all seven of the source's own test cases: no shared ratings, exactly one shared rating (below
and at the minimum), a twin with no new liked item, a target who already knows everything, a tie broken by shared
count, a full tie (first candidate kept), and mismatched list lengths (rejected).

## Enrichment
From the source: partial credit for close (not just equal) ratings; recommending from several similar neighbors
instead of one twin; returning three ranked recommendations with reasons; testing how `minimum_common` changes the
result; a diversity measure over the recommendation list; comparing a user-based result to a content-based one; a
"model card" documenting the system's data, limits and prohibited uses.
