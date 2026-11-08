# Unit 9 — Recommender Systems

**8h = 4 Theory + 4 Practice = 4 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 9 (pp. 21–23); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 reworked 8 Nov 2026 to the Ministry teaching materials (files 20.0, 20.1, 21.1, 22.1); awaiting re-approval. The v1 build
(approved earlier) came from `Downloads\python-b-codex\python_b_unit09_recommendation_systems_complete_unit.md`; the Ministry's materials use a
different survey scale (V / X / 0), a simpler twin (the most identical non-0 answers) and a different content for the last meeting, so notes,
briefs, code and data were rewritten. Decks: superseded, new NotebookLM decks pending (prep folders `unit9-m1-slides` … `unit9-m4-slides`).
No raw teacher material exists for this unit.

## Official topics and hours

Unit totals from the master table (4 theory / 4 practice), matching the chapter's own table (intro + survey design 1/1, coding the
recommender 1/2, algorithm pitfalls + ethics + the attention economy 2/1, total 4/4).

| Topic | Planned in | Minutes (T / P) | Ministry source | Status |
|---|---|---:|---|---|
| Recommender systems intro, the feed riddle, content-based vs user-based, the culinary-twin game, the Google Forms survey | 9.1 (45 T + 45 P) | 45 / 45 | 20.0, 20.1 | 🔶 |
| The participants × items table (V / X / 0), counting similarity points, the twin; `count_same` | 9.2 (45 T + 45 P) | 45 / 45 | 21.1 first half | 🔶 |
| Recommending what the twin liked, `find_twin`, `recommend_item`, `main` (checkpoint) | 9.3 (45 T + 45 P) | 45 / 45 | 21.1 second half | 🔶 |
| Dangers: fact or fake, business model, Plato's cave, three traps, controls; a toy bubble in code | 9.4 (45 T + 45 P) | 45 / 45 | 20.0 p. 2, 22.1 | 🔶 |
| **Total** | | **180 / 180** | | |

Chapter goals (source §1, fourteen in all):

1. Explain why digital services use recommender systems → 9.1
2. Distinguish content-based from user-based recommendation → 9.1
3. Represent preferences as data (a table, parallel lists, a string of V / X / 0) → 9.1–9.2
4. Explain a shared answer and why "don't know" (`0`) is excluded → 9.1–9.2
5. Trace a similarity count with a trace table → 9.2
6. Implement the similarity count with a loop and a compound condition → 9.2
7. Find the most similar user — the "digital twin" → 9.2–9.3
8. Recommend an item unknown to the current user but liked by the twin → 9.3
9. Combine several functions in a main program → 9.3
10. Test on normal cases and edge cases → 9.3
11. Define a filter bubble, an echo chamber and addiction engineering / the attention economy → 9.4
12. Analyze how behavioral signals can shape recommendations → 9.4
13. Propose practical tools for better feed control → 9.4
14. Identify ethical limits: privacy, consent, data scarcity, bias → 9.1, 9.3, 9.4

## Unit 9.1 — Knowledge + Lab: Feed Riddle, Two Kinds of Recommender, Survey
- the viewing-habits discussion, the YouTube-feed riddle (three people, three home pages — our own text), a regular algorithm vs AI,
  content-based (signals) vs user-based (the ice-cream seller), the four-scenario classification drill.
- the **culinary-twin class game** (a volunteer answers V / X / 0 on 12 foods; a point only for identical, non-0 answers).
- lab: the warm-up bug (the last `else` swallows `"v"`), `is_valid_answers`, `count_known`, then the Google Forms survey with the
  scale **V / X / 0 (capital English letters only)** and the privacy rules.

## Unit 9.2 — Knowledge + Lab: the Table and the Twin
- the Ministry's table (four participants, five foods), reading a row, counting similarity points one item at a time, the twin = the most points.
- lab: the warm-up bug (`0` and `0` counted), `show_comparison` (the trace table printed), `print_scores`, `best_score`; the class's own
  survey pasted in as three lines.

## Unit 9.3 — Knowledge + Lab: From the Twin to a Recommendation (unit checkpoint)
- recommend an item the twin liked (`V`) and the target does not know (`0`); `find_twin` (skip yourself, `None` when nobody shares anything,
  first on a tie); `recommend_item`; `main`; three named limits (cold start, sparse data, similar ≠ same).
- lab: the self-comparison warm-up bug, `recommend_item`, the project `main()`, six edge cases; a 20-point rubric.

## Unit 9.4 — Knowledge + Lab: The Trap of Recommendations
- fact or fake (five posts), the business model ("who is the product"), the five-step incognito demo, Plato's cave, the three traps (filter bubble,
  echo chamber, addiction engineering), the 2014 polarisation graph (as a question about correlation), practical controls, pros and cons.
- lab: pairs build a bubble (live incognito, or cards), observation vs interpretation; warm-up bug (`!=`), `simulate_feed_round` and
  `run_bubble_experiment` (a toy that grows the related share), `count_different`; controls and the responsibility card.

### Scope decisions
- **The Ministry materials are the source (8 Nov 2026).** The Ministry has **three** lessons (20, 21, 22); we keep **four** and 360 minutes
  (master table). 9.1 = 20.0 + 20.1; 9.2 = the first half of 21.1; 9.3 = the second half of 21.1 plus the code; 9.4 = 22.0 + 22.1.
  Where the Ministry is thin, the v1 content stays: the classification drill, the survey privacy rules, the three limits, the edge-case table,
  the experiment safety rules, the offline card simulation, the responsibility card.
- **Not delivered:** worksheets 20.2, 21.2 (the Ministry's recommender code), 22.2 and teacher notes 21.0, 22.0. Nothing from them is invented
  as Ministry content. Assumed and flagged in the notes: the Forms options are literally `V`, `X`, `0`; the programming step is our own code.
- **The survey scale is V / X / 0** (liked / disliked / don't know), capital English letters only (20.0 p. 1). v1's 0–3 scale and the
  rate / minimum-common machinery are gone. The twin is the participant with the **most identical non-0 answers** (21.1); a shared `X` counts,
  a shared `0` does not; a tie keeps the first; a best score of 0 means no twin.
- **Rulebook (from the teacher):** `def` and lists are allowed (Unit 9 comes after Units 3 and 7). **Forbidden in our own code:** tuples
  (also tuple returns and `in (0, 1, 2, 3)`), default arguments, sets, dictionaries, comprehensions and generator expressions, nested loops,
  lists of lists, classes. v1's `best_key = (-1.0, -1)`, `minimum_common=2`, `liked_threshold=3`, `return matches, common`, `all(c >= 2 for c in counts)`
  and `csv.reader` are therefore replaced: each person's answers are **one string** (`"00XVV"`), the data are three flat parallel lists
  (`item_names`, `aliases`, `answers`), every function returns one value (`None` for "nothing found").
- **No file reading in student code.** Nothing in Python A or the Ministry decks teaches `open`, and the Ministry shows no CSV code on its slides
  (it lives in the missing 21.2). The data are typed in as lists; [`CsvToLists_Teacher.py`](CsvToLists_Teacher.py) (a teacher tool using
  `open` / `split`) turns the Forms CSV into the three lines the students paste. [`ratings.csv`](ratings.csv) is the Ministry's sample table with
  aliases instead of first names.
- **9.4 simulation redesigned.** v1's card rule (two same-topic cards plus one other each round) gave a constant 2 of 3 and showed no
  growth. The new toy grows the related share (1, 2, 3, 4, 4 of 5) and adds `count_different`; it is flagged everywhere as a toy with invented numbers.
  v1's `all(...)` generator was removed. The live demo keeps the v1 safety rules; the cards stay as the fallback.
- **Ministry-deck points we did not copy:** the AI-generated people of the riddle (we use text only); the Elon Musk made-up quote (no
  real person is quoted); the named-camp 2020 election example (we teach the principle, named examples only by the teacher's choice);
  p. 37's causal claim ("in 2014 the platforms switched to AI and the slope grew") is shown as a hypothesis, "correlation is not proof";
  p. 30 repeats the filter-bubble text box on the echo-chamber slide; p. 36–37 text overlaps the picture. The "dopamine" wording of 20.0
  is simplified and flagged as a popular explanation.
- **Privacy:** aliases only, no names, faces or personal data; the survey privacy rules of v1 are kept and extended (no e-mail collection,
  teacher check, deletion at the end of the unit).
- **Not taught:** dictionaries, content-based filtering in code (named and contrasted only), matrix factorization, similarity rates.

## Exit criteria
The student distinguishes content-based from user-based recommendation, explains why a `0` ("don't know") is not a shared answer, counts
similarity points, writes `count_same`, `find_twin` and `recommend_item` and handles "no twin / nothing new" without crashing, and explains
filter bubble, echo chamber and addiction engineering with at least one practical response to each.

## Checkpoint
9.3's recommender (`count_same`, `find_twin`, `recommend_item`, `main`) is the unit's capstone, scored on the 20-point rubric in `m3-lesson-notes.md`
(data and privacy 3, similarity count 4, twin and recommendation 6, code quality 3, critical thinking 4). Verified here on the sample table
and on five edge cases (no twin, nothing new, target knows everything, a tie, a shared `0`).

## Enrichment
Partial credit for close answers; recommending from several neighbours; returning ranked recommendations with reasons; a similarity rate
(points divided by the items both answered); comparing a user-based result to a content-based one; a "model card" documenting the
data, limits and prohibited uses.
