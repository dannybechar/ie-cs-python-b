# Unit 4.1 — Bringing AI into Code (API)

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: What Is an API? The Gemini Call, f-Strings, and the `ask_the_ai` Wrapper

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** 45 min Knowledge + Guided Practice, then 45 min Lab
**Minutes (theory / practice):** 45 / 45
**Current tool:** Thonny (the Ministry worksheets assume Google Colab + Google Classroom — see "Tool Note – Thonny vs Colab")
**Source of inspiration:** the Ministry's own teaching materials (the teacher's decision: the source of truth).
Rebuilt from:
- **5.1 deck** (32 slides) — the lesson spine, in the Ministry's order: waiter analogy → "what an API looks like to
  Python" → a prompt is a string → building it with `+` and then with f-strings → the Gemini code walked through
  line by line → `ask_the_ai(my_prompt)` that returns the text (clean code, reuse, black box) → usage limits →
  the three golden rules → errors 429 / 503.
- **5.2 worksheet + 5.2.0 teacher solution** — the lab tasks (connection check, the wrapper, the grandma greeting with
  an f-string, the dream dessert with a `while` accumulation, advanced features).
- **5.0 teacher emphases, 5.0.1 (Gemini API key), 5.0.2 (keeping the key secret in Colab)** — the setup notes below.

*What changed from the previous version (built from the Ministry program text and the teacher's raw document):*
the service is now settled (Gemini); the wrapper is called `ask_the_ai(my_prompt)`; **f-strings are taught here** (they
were assumed before); the lesson now follows the deck's flow instead of the "find the bug" exposed-key activity
(key secrecy is kept, as the Ministry's golden rules + the Colab-Secrets method); the warm-up bug is now
`print(response)` (the whole response object) instead of the two-bug mock wrapper; the lab uses the Ministry's
four tasks instead of the "short-prompt" check; the Hebrew deck is superseded.
**Kept from our version:** input validation with `len` (the worksheet's advanced feature 1) and the rule "no personal
data in a prompt; the answer is checked, not trusted".
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction is isolated and labeled
**Tool Note – Thonny vs Colab** or **Tool Note – the AI service**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| **4.1 (this)** | **what an API is, the Gemini call, f-strings, the `ask_the_ai` wrapper, limits, golden rules, the secret key** | 45 / 45 |
| 4.2 | the "Balanced Day" project (Ministry 6.1 / 6.2) | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 11–12) | Covered here |
|---|---|
| Goal 1: explain an API via the client–server model | ✅ the waiter analogy; "what an API looks like to Python" |
| Goal 2: an API key, and why it is never shared or written in code | ✅ slide on the key; Colab Secrets / environment variable |
| Goal 3: import a library and set up a client | ✅ the Gemini code, line by line |
| Goal 4: a wrapper function that takes a prompt and returns the answer | ✅ Tasks 1 and the whole lab |
| Goal 5 (start): a dynamic prompt with an f-string | ✅ `+` versus f-string, Task 2 (continued in 4.2) |
| Goal 9: rate limits, overload errors, inaccurate answers | ✅ 15/min, 1,500/day, 429, 503; the answer is checked |
| Goal 10: privacy | ✅ golden rule 2 ("send only what is needed"); no personal data in a prompt |

### Deliberate exclusions
`try`/`except` (the Ministry does not teach it here either: a 429/503 means "wait and run again"); HTTP internals; a
`while` loop that waits and retries; the project (4.2).

---

## 3. Lesson Goal

**A Python program never contains the AI: it calls an outside function (the API) with a prompt — a string — and gets a
string back. We hide that call in `ask_the_ai(my_prompt)`, which RETURNS the text, and we use it carefully: plan the
prompt first, send only what is needed, and never call it inside a loop.**

---

## 4. Core Mental Models

```text
Python program (customer) → API (waiter) → Gemini on Google's servers (kitchen) → API → Python program
```

```python
from google import genai
client = genai.Client(api_key=my_api_key)          # once, at the top: the key is "who is asking"

def ask_the_ai(my_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=my_prompt)    # the model name: do not change
    return response.text                                  # return, not print

answer = ask_the_ai(f"Write a short birthday greeting for {name}.")
print(answer)
```

- An API call is **just a function call to somewhere else** — it takes time (the waiter travels over the internet), and
  with no internet it fails with an error message. The code is fine.
- The prompt is only a string, so everything we know about strings (input, `+`, f-strings) builds prompts.
- The key is a password that belongs to the teacher's project: it never appears in a file, a screenshot or a chat.
- The model's answer is text to check, not a fact.

---

# 5. First 45 Minutes — Knowledge + Guided Practice

| Clock | Activity |
|---|---|
| 0–4 | **Recap and hook (deck slides 3–4):** last time — functions, parameters, `return`. This year we move "from consumers to producers": not only using AI, building with it. Today's goal: one function that asks Gemini. |
| 4–11 | **The waiter analogy (slide 6) + "what does an API look like to Python?" (slides 7–8).** Customer = our code, kitchen = Google's server, waiter = the API. For Python it is *an external function call* that **takes time**. **Predict (own step):** "what happens if we call it with no internet?" — then the answer: an error message, because the request cannot reach the server. |
| 11–14 | **A prompt is just a string (slide 9).** `prompt = "..."`. The grandma's-birthday prompt; pose slide 10's question: "how do we make a general program for any grandma, any age, any hobby?" |
| 14–24 | **Two ways to build the prompt (slides 11–12) — students type.** First `+` (trace the output: where did the spaces go?), then the f-string (`f` before the quote, variables inside `{ }`). Pairs type both versions in Thonny and print the prompt — **no AI needed yet.** |
| 24–31 | **The Gemini code, line by line (slides 13–23).** `from google import genai` · `client = genai.Client(api_key=…)` (the key — we get it from the teacher) · `model="gemini-2.5-flash"` (**we do not change it**) · `contents=` is the prompt, the only line we change · `response = …` keeps the answer · `print(response.text)`. **Teacher demo, live (4–5 min):** run it with the real key, or with the stand-in; run twice — same answer? (A real model does not always repeat itself.) |
| 31–37 | **Wrap it in a function (slides 24–25).** `ask_the_ai(my_prompt)`: the prompt becomes a parameter; `return response.text`. **Predict (own step):** "what would `answer` be if the function used `print` instead of `return`?" — `None`, and the text appears on the screen only. Why wrap: (1) clean code — the main program says `answer = ask_the_ai(prompt)`; (2) reuse — ask again and again without copying lines; (3) a black box — the main program does not need to know how the API works; changing the model happens in one place. |
| 37–43 | **Use it wisely (slides 27–29).** Limits: about **15 requests per minute and 1,500 per day per key** (it varies between models and periods) — so we work in groups. Errors **429** (quota exceeded) and **503** (server busy) mean the code is fine: wait, call less, test the prompt in an online chat before the code. **The three golden rules:** plan the prompt first (context + task + wanted output) and test it in a chat; send only what is needed; **never call the API inside a loop** — collect first, send once. The key: never in the file (see the setup notes). |
| 43–45 | **Bridge:** key groups, the lab sheet, "warm-up first". |

### Tool Note – the AI service (setup, before the lesson — teacher)
1. **Create the keys** (guide 5.0.1): Google AI Studio → *Get API key* → *Create API key* → *Create project*. Up to
   **10 independent keys** (each in its own project, each with its own limit). A key is about 15 requests/minute,
   1,500/day — so 3–4 students share a key and take turns. Free keys cost nothing; still, treat each key as a secret.
2. **Check the model name** before class. The Ministry's text uses `gemini-2.5-flash`; run the one-line test below
   once with your own key. If Google has retired the name, change the string in the single `ask_the_ai` line and tell
   the students it was changed.
3. **Keep the key secret — two methods:**
   - **Google Colab (the Ministry's method, guide 5.0.2):** the left key icon → *Add new secret* → Name `GEMINI_API_KEY`
     → paste the key → **switch on "Notebook access"**. In the code:
     `from google.colab import userdata` · `my_api_key = userdata.get("GEMINI_API_KEY")` ·
     `client = genai.Client(api_key=my_api_key)`. When the notebook is shared, the key is not shared.
   - **Thonny (our default tool):** install the library once: *Tools › Manage packages › google-genai* (or
     `pip install -U google-genai` — this install line is from the Gemini quickstart that guide 5.0.1 points to; the
     Ministry's own materials are written for Colab, where the library is already installed). Set an environment variable
     on the computer (Windows: `setx GEMINI_API_KEY "<the key>"`, then restart Thonny) and read it:
     `import os` · `my_api_key = os.environ["GEMINI_API_KEY"]` · `client = genai.Client(api_key=my_api_key)`.
     The key is on the machine, never in a `.py` file. (Last resort: the teacher writes the key on the board and
     students paste it into an `input()` at run time — never saved, but visible on screen.)
4. **A one-line test:** `python -c "from google import genai; import os; c=genai.Client(api_key=os.environ['GEMINI_API_KEY']); print(c.models.generate_content(model='gemini-2.5-flash', contents='Say hi').text)"`
5. **Without keys or internet:** every file of this unit starts with **ZONE A**, a stand-in "client" that returns
   fixed answers (tagged `[stand-in]`), so the lab runs on plain Python. The student code under it is identical to the
   real code. Say plainly, once, that the answers are fixed — the real model varies.
6. Never put a key in a file, a slide, a screenshot, a chat message or the repo.

### Tool Note – Thonny vs Colab (open decision for the teacher)
The Ministry worksheets assume Colab and Google Classroom (notebooks, Colab Secrets, "copy your code here"). Our files
run in Thonny with the stand-in and, with the setup above, with the real service. Choose once: **Colab** for the live
runs (nothing to install, the Ministry's key method) and Thonny for everything else, or Thonny throughout.

---

# 6. Second 45 Minutes — Lab

Starter: [`AskTheAI_Starter.py`](AskTheAI_Starter.py). Reference: [`AskTheAI_Reference.py`](AskTheAI_Reference.py).
Default = the stand-in (ZONE A). **Files needing a live run with a real key:** the Gemini demo of minute 24 and, if you
want, the lab with ZONE A replaced by the live version (comments in the reference).

## 45–51 — Warm-up: a joke that prints as an object

```python
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me a short joke about programmers")
print(response)
```

Run it: the output is `GenerateContentResponse(candidates=[...], usage_metadata=...)` (with the real library it is
a long object dump), not a joke. The answer is *inside* the response; the text is `response.text`. Fix: `print(response.text)`.
Run again, and again — is it the same joke? (Stand-in: yes, fixed. Real model: probably not — that is why we **check**
what comes back.)

## 51–60 — Task 1: the wrapper `ask_the_ai`

Define `ask_the_ai(my_prompt)`: send `my_prompt`, **return** `response.text` (do not print inside). In the main program
call it with `"What is the distance between the Earth and the Moon?"`, keep the result in a variable, print it.
Check on every screen: `return`, and the `print` is in the main program (the Ministry teacher's emphasis, 5.2.0).

```text
[stand-in] The Moon is about 384,000 km from Earth, on average.
```

## 60–69 — Task 2: a dynamic prompt (f-string)

Read a grandma's name and a good trait; build the prompt with an f-string; print the prompt, then the answer.

```text
Grandma's name: Sara
A good trait of hers: kind
Prompt: Write a short birthday greeting for Sara, who is a very kind grandmother.
[stand-in] Happy birthday, dear grandma! You are the warmest, kindest person we know.
```

Common slip (Ministry teacher note): forgetting the `f`, or the `{ }`. The prompt printed on screen shows it at once —
which is why we **print the prompt before sending it**.

## 69–81 — Task 3: the dream dessert — collect first, ask once

A `while` loop until the user types `done`, adding each ingredient to `all_ing` with a comma and a space; **after** the
loop (no indentation) one prompt, one call, print the answer. The Ministry teacher's checks: string accumulation
(`all_ing = all_ing + item + ", "`) and the call **outside** the loop.

```text
Add an ingredient (or done to finish): cream
Add another ingredient (or done to finish): strawberries
Add another ingredient (or done to finish): done
Prompt: Invent a crazy, creative dessert that uses only these ingredients: cream, strawberries,
[stand-in] Crazy dessert: layer everything on the list with whipped cream, chill it, and enjoy.
Calls sent: 1
```

## 81–86 — If time: do not waste a call (worksheet advanced features 1 and 2)

`if len(name) < 2:` print a warning and do not call the AI; if the trait is empty (`""`) use a default such as
`"wonderful"`. (The worksheet's other ideas — a style choice with `if`/`elif`/`else`, a length limit, a list of banned
words — stay as extensions; the banned-words version in the worksheet uses a list, which we do not teach until
Unit 7: use `trait == "x" or trait == "y"`.)

## 86–90 — Save and exit check

Save As `G8_U4_M1_AskTheAI_<Name>.py` — and check that the file contains no key. Exit check on the board: (1) an API is…;
(2) a key is kept in… and never in…; (3) a wrapper function uses `return` because…; (4) the three golden rules.

### Tool Note – Thonny
A `TypeError` or `NameError` names the exact thing Python could not find — read that name first. The Shell shows
Hebrew and English fine; keep the prompts in English in the files (the live model also answers Hebrew prompts in Hebrew
if a student wants to try).

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| Our program contains the AI | It sends a request to Google's server and waits for the answer; with no internet it fails |
| `print(response)` shows the answer | The text is in `response.text` (the warm-up bug) |
| `print` inside the wrapper is the same as `return` | Only `return` lets `answer = ask_the_ai(...)` hold the text; with `print` it is `None` |
| A key is something to paste into the code and share | A key is a secret: Colab Secrets or an environment variable |
| A 429 / 503 means my code is broken | The code is fine: quota or a busy server — wait, call less |
| Calling the API in a loop is more convenient | It is how a class burns the quota in a second: collect first, send once |
| The model's answer is the truth | It is text to check |
| A forgotten `f` still works | The prompt then contains the words `{name}` — print the prompt and see |

---

# 8. Assessment Evidence (formative)

- The prediction "no internet → error" and "`print` instead of `return` → `None`" argued in words
- The warm-up bug found from the printed output and fixed with `response.text`
- Task 1: `ask_the_ai` with a parameter and `return`; Task 2: a correct f-string prompt (shown by the printed prompt)
- Task 3: the call is outside the loop (the `Calls sent:` line shows 1)
- The saved file contains no key
- Exit check
