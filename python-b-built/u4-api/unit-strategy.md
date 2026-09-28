# Unit 4 — Bringing AI into Code (API)

**4h = 1 Theory + 3 Practice = 2 double meetings**
Source: [`python-b-ai.pdf`](../../docs/ministry-source/python-b-ai.pdf) Chapter 4 (pp. 11–13); hours from the master table (p. 3).
Framing: [`../../docs/annual-strategy.md`](../../docs/annual-strategy.md).

**Build status:** 🔶 built from the codex material only — **staged in `python-b-built/`, not yet in `units/`.**
No raw teacher material exists for this unit. Built from `Downloads\python-b-codex\python_b_unit04_api_bring_ai_into_code_complete_unit.md` —
a single, very detailed document covering both meetings (goals, full clock tables, worked code, common mistakes, a
graded project with a rubric), not a slide deck.

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

1. Explain what an API is via the client–server model / the waiter analogy → 4.1 ✅
2. Explain what an API key is and why it must never be written in code or shared → 4.1 ✅
3. Import a third-party library and set up a client for an AI service → 4.1 ✅
4. Write a wrapper function that takes a prompt, makes the API call, and returns the answer with `return` → 4.1 ✅
5. Build a dynamic prompt with an f-string and user input → 4.2 ✅
6. Accumulate input with a `while` loop and string concatenation → 4.2 ✅
7. Validate input with `len`, compound conditions and `in` → 4.2 ✅
8. Explain why data is collected first and **one** API call is made outside the loop → 4.2 ✅
9. Identify rate limits, overload errors, possible costs, and inaccurate answers → 4.1–4.2 ✅
10. Protect user privacy and check an AI answer before relying on it → 4.1–4.2 ✅

## Unit 4.1 — Knowledge + Lab: What Is an API? + a Wrapper Function
- the path: Python program → request → AI server → response → Python program; the waiter analogy (the program is
  the customer, the API is the waiter, the server and model are the kitchen).
- API, API key, client, prompt, response, rate limit, service unavailable, wrapper function.
- a key written directly in code is a security bug; it belongs in an environment variable, never in the file, a
  chat message or a screenshot.
- `print` shows a value; `return` hands it back to the calling code — a wrapper function must `return`, not `print`.
- lab: a two-bug wrapper (missing parameter, `print` instead of `return`), then a version that rejects a too-short
  prompt before "calling" the service.

## Unit 4.2 — Lab + Lab: Dynamic Prompts + the "Balanced Day" Project
- a good classroom prompt has four parts: role/context, task, data, and the wanted response structure.
- f-strings build a prompt from `input()` values; a default value covers empty input; `len`/`in` catch input that's
  too short or contains a sensitive word.
- accumulate every activity into one string inside a `while` loop; the **one** API call happens after the loop ends
  — never once per activity.
- lab: a wasteful one-call-per-activity warm-up, a dynamic-prompt task, an input-validation task, then the
  "Balanced Day" project itself (the unit's official capstone product).

### Scope decisions
- **The source document is the only material, and it is unusually complete** — full clock tables (already summing
  to 90 minutes for each meeting), worked code for every step, a bug clinic, a project rubric and a fallback for no
  internet/no key. Followed closely; adapted into the house lesson-notes/lab-brief split and our warm-up-bug
  convention (the source's own "no-return, no-parameter" broken wrapper became the 4.1 warm-up almost unchanged; the
  source's "one call per activity inside the loop" antipattern became the 4.2 warm-up, made explicit as something to
  read and explain rather than run to completion — see `m2-lesson-notes.md`).
- **AI service left unresolved, by design.** The source explicitly declines to fix a vendor at the strategy stage and
  gives a `google-genai`/Gemini example only as a documented illustration, with a note that library and model names
  change and must be checked against current documentation before teaching. Every code file here defaults to
  **classroom (mock) mode** — `ask_ai()` returns a fixed string, exactly as the source's own no-internet fallback
  does — so the files run and are verifiable with plain `python`, no key required. The real client code is included
  as a clearly marked, commented block to fill in once the teacher has chosen and tested a service. This is a
  decision for the teacher (`docs/annual-strategy.md` §8: "which service; teacher-held key, never in student code").
- **Not taught:** exception-handling mechanics in depth (the source's robust-UX example uses `try`/`except` as a
  given pattern, not a new concept to teach here — see `annual-strategy.md` §7), HTTP internals, authentication
  protocols.

## Exit criteria
The student explains the API request/response path and why a key is a secret, writes a wrapper function that takes
a prompt and returns an answer, builds a dynamic prompt from user input with an f-string, validates input before
using it, and explains why data is collected before a single API call rather than one call per item.

## Checkpoint
4.2's "Balanced Day" project is the unit's capstone, with the source's own 20-point rubric (wrapper function,
key security, dynamic prompt, accumulation loop, one call outside the loop, validation and privacy, testing) —
see the lesson notes for the full rubric and performance bands.

## Enrichment
From the source: add a language choice to the response; cap each activity's length; count activities without a
list; ask the model for a fixed four-line format; compare two versions of the same prompt without adding new
information; add an `OFFLINE_MODE` toggle between the mock and the real service.
