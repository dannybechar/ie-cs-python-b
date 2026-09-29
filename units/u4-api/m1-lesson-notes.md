# Unit 4.1 — Bringing AI into Code (API)

## Grade 8 / AI + Python B · Lesson Strategy v1
### Topic: What Is an API? + a Wrapper Function That Returns

**Status:** Approved by the teacher
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny; a language-model API for the live version (see Tool Note)
**Source of inspiration:** `python_b_unit04_api_bring_ai_into_code_complete_unit.md` — meeting 1's own clock table,
the waiter analogy, the concepts table, the "find the bug" (an exposed key) activity, the teacher's first live call,
the move to a wrapper function, the robust-UX version (kept as teacher-provided background, not taught line by
line), practice 1–3 and the exit card kept nearly unchanged; the source's `try`/`except` version is summarized
rather than taught as new syntax, per the source's own note that it is "a pattern the teacher provides."
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction must be isolated and
labeled **Tool Note – Thonny** or **Tool Note – the AI service**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **4.1 (this)** | **the API path, the waiter analogy, key security, a wrapper function with `return`** | 45 / 45 |
| 4.2 | dynamic prompts, input validation, accumulation loops, the "Balanced Day" project | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf p. 11–12) | Covered here |
|---|---|
| Goal 1: explain an API via the client–server model | ✅ the path diagram, the waiter analogy |
| Goal 2: explain an API key and why it's never shared or written in code | ✅ the "find the bug" activity |
| Goal 3: import a third-party library and set up a client | ✅ teacher demo |
| Goal 4: a wrapper function that takes a prompt, calls the service, and returns the answer | ✅ every lab task |
| Goal 9: rate limits, overload errors, cost, inaccurate answers | ✅ the repeated-calls question |
| Goal 10: protect privacy; check an answer before relying on it | ✅ closing discussion |

### Deliberate exclusions
Dynamic prompts and input validation (4.2), the full loop-accumulation pattern (4.2), exception-handling syntax
taught as new material (the robust-UX code is shown as a given pattern, not built line by line).

---

## 3. Lesson Goal

**A Python program never contains an AI model — it sends a request through an API and gets a response back; a
wrapper function hides that exchange behind a plain function call that takes a prompt and `return`s the answer.**

---

## 4. Core Mental Models

```text
Python program → request → API → AI service (model on a server) → response → Python program
```

```python
def ask_ai(prompt):
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text          # return, not print - the caller gets the value back


answer = ask_ai("Explain an API in one sentence for a ninth-grade student.")
print(answer)
```

- The API key identifies and authorizes the calling project — like a membership card, not a password to type into a
  chat. It lives in an environment variable, never inside a `.py` file, a shared document or a screenshot.
- A model's answer is a probability-based guess, not a guaranteed fact — it is checked, like any other input.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–6 | **Hook:** a "smart" app is shown. How does Python code "talk" to a model that lives on someone else's server? |
| 6–18 | **The waiter analogy:** the program is the customer, the API is the waiter, the server and model are the kitchen, the response is the dish. Board the two-line path diagram; guided questions: does our program contain the whole model? what does the API actually do? why is a key needed? is the model's answer always correct? |
| 18–30 | **Key concepts (table above the deck's):** API, API key, client, prompt, response, rate limit, service unavailable, wrapper function |
| 30–41 | **"Find the bug" (pairs):** `client = genai.Client(api_key="my-real-secret-key")` — what's wrong, and what happens if this file is shared or uploaded? Fix: `genai.Client()` with no visible key, reading `GEMINI_API_KEY` from the environment instead |
| 41–57 | **Teacher demo (live, or the saved example if offline):** install the library, import it, create a client, one real call, `print(response.text)` — then move the same call inside `def ask_ai(prompt): ... return response.text` |
| 57–72 | why `return`, not `print`: a returned value can be stored, compared, combined with other text or printed later; a printed value only ever appears on screen |
| 72–84 | the lab missions |
| 84–90 | Exit card: 1) API is… 2) an API key is stored in … and not in … 3) a wrapper function uses `return` because … 4) draw four boxes for the request/response path |

### Tool Note – the AI service
This meeting's live demo needs a working API client (installed library, a valid key set as an environment
variable, internet). If none is ready, use the source document's saved fallback: run the **classroom-mode**
`ask_ai()` in the lab files (a fixed string, no network) and show the real call from a saved screenshot or
transcript instead of live.

---

# 6. Second 45 Minutes — Lab

Starter: [`Wrapper_Starter.py`](Wrapper_Starter.py). Reference: [`Wrapper_Reference.py`](Wrapper_Reference.py).
Every file runs in **classroom mode** — `ask_ai()` returns a fixed string, so nothing here needs a real key; that's
intentional, not a shortcut (see Tool Note above and `unit-strategy.md`).

## 45–54 — Warm-up: a wrapper with two bugs

```python
def ask_ai():
    response = "Mock response: balance study, movement, rest, and sleep."
    print(response.text)


answer = ask_ai("Give one healthy study habit.")
print(answer)
```

Run it: `TypeError: ask_ai() takes 0 positional arguments but 1 was given`. Fix bug 1 — add `prompt` as a
parameter. Run again: `AttributeError: 'str' object has no attribute 'text'` — the mock line already returns plain
text; `.text` doesn't apply. Bug 2 is the design itself: the function should `return` its answer, not `print` it.
Rewritten:

```python
def ask_ai(prompt):
    response = "Mock response: balance study, movement, rest, and sleep."
    return response
```

## 54–68 — Task 1: the parameter and `return`, confirmed

With the warm-up fixed, `answer = ask_ai("Give one healthy study habit."); print(answer)` should now print the mock
sentence with no error. Confirm it, then explain in one sentence why `answer` would have been `None` if `ask_ai`
still used `print` instead of `return`.

## 68–82 — Task 2: check the prompt before "calling" the service

Write a version that checks the prompt first: if `len(prompt.strip()) < 5`, return
`"The prompt is too short. Please add details."` without going any further; otherwise return the (mock) response.
Test with `"Hi"` and with a normal prompt.

```text
The prompt is too short. Please add details.
Mock response: balance study, movement, rest, and sleep.
```

## 82–86 — Discussion: how many calls, and why does it matter?

```python
count = 0
while count < 20:
    print(ask_ai("Give one study tip."))
    count += 1
```

How many calls does this send? (20.) Why might that be a problem even with a mock function, and a real problem with
a real service? (time, quota, rate limits, possible cost.) How could it be improved? (Unit 4.2's answer: collect
everything first, then ask once.)

## 86–90 — Save and exit check

Save As `G8_U4_M1_Wrapper_<Name>.py`. Complete the exit card (§5).

### Tool Note – Thonny
A `TypeError` naming a missing argument, and an `AttributeError` naming a missing attribute, both show the exact
name Python couldn't find — read that name first before guessing what's wrong.

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Our program "becomes" the AI model | It sends a request to a service and gets a response — the model never runs inside our program |
| An API key is like a password to type when asked | It's held in an environment variable, never typed, shown, or committed |
| `print` and `return` do the same job here | Only `return` lets the calling code store, check or reuse the answer |
| A model's response is always accurate | It's a probabilistic guess and should be checked, like any other input |
| More API calls simply means more information | Each call costs time, quota and possibly money — data should be gathered first, one call made after (4.2) |

---

# 8. Assessment Evidence (formative)

- The "find the bug" activity: identifying the exposed key and the fix
- The warm-up's two bugs found and explained in order (parameter, then `print` vs `return`)
- Task 2 passing both test prompts
- The repeated-calls discussion answered with a reason, not just a number
- Exit card
