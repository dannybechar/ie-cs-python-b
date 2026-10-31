# Unit 4.2 — Bringing AI into Code (API)

## Grade 8 / AI + Python B · Lesson Strategy v2
### Topic: The "Balanced Day" Project

**Status:** Built, awaiting teacher approval 🔶
**Duration:** 90 minutes
**Structure:** Lab + Lab (12 min short intro, then a 78-minute project lab)
**Minutes (theory / practice):** 0 / 90
**Current tool:** Thonny with the classroom stand-in; Colab or a real key for the live runs (see Tool Note)
**Source of inspiration:** the Ministry's own teaching materials (the source of truth).
- **6.1 deck** (13 slides, "a very short deck to present the project, mostly work time") — the intro: the problem
  (school tasks and no time for fun), what we build (input / logic / the AI's magic), "what can the AI do that plain
  code cannot?" and the list of everything the project uses.
- **6.2 worksheet + 6.2.0 teacher solution** — the project itself, stage by stage: (1) `home_hour`, `sleep_hour`,
  `calc_time_today` that **returns** the hours; (2) a `while` loop that accumulates `all_tasks`; (3) the prompt with
  an f-string, `ask_the_ai`, one call at the end; then the advanced features (emojis, language, `len` check, net fun
  time with no call if there is none, motivation sentence, a percentage summary, colors).
- **5.0 teacher emphases:** a base part everyone must finish plus extra features for advanced students; let students
  work independently — the worksheet guides them step by step.

*What changed from the previous version:* the project is now the Ministry's (input hours → a function that returns the
free hours → accumulate tasks and times → one call), not our two-part "goal + activities" version; the four-part prompt
template, the answer-critique and the 20-point rubric are kept; the warm-up is a real slip from the worksheet
(`{time_today}` instead of `{today_time}`) instead of "one call per activity" (that idea moved into golden rule 3 and
the exit check); the sentinel and the stand-in are in English (see Tool Note).
**Dropped on purpose:** colored output (`"\033[31m"` escape codes) — Thonny's Shell does not render them; they work in Colab
only. The banned-words list (4.1 worksheet) — lists come in Unit 7; our `or` chain does the same job.
**Tool-dependence rule:** Keep lesson content IDE-neutral. Any tool-specific instruction is isolated and labeled
**Tool Note – Thonny vs Colab** or **Tool Note – the AI service**.

---

## 1. Position in Unit 4

| Meeting | Focus | Theory / practice minutes |
|---|---|---|
| 4.1 | what an API is, the Gemini call, f-strings, `ask_the_ai`, limits, golden rules, the secret key | 45 / 45 |
| **4.2 (this)** | **the "Balanced Day" project: a returning function, accumulation, one prompt, one call** | 0 / 90 |

---

## 2. Official Scope Used in This Meeting

| Official goal (python-b-ai.pdf pp. 11–12) | Covered here |
|---|---|
| Goal 5: a dynamic prompt with an f-string and user input | ✅ Stage 3 |
| Goal 6: accumulate input with a `while` loop and string concatenation | ✅ Stage 2 |
| Goal 7: validate input with `len` and conditions | ✅ advanced features 3, 7 |
| Goal 8: data first, **one** API call outside the loop | ✅ Stage 3, golden rule 3 |
| Goal 4: a function that takes input and returns a value | ✅ `calc_time_today`, `ask_the_ai` |
| Goal 9: limits, errors 429 / 503, inaccurate answers | ✅ the "Calls sent" line; the answer check |
| Goal 10: privacy; check the answer | ✅ no personal data in a task; peer review and answer critique |

### Deliberate exclusions
`try`/`except` for 429/503 (we wait and run again); lists; colored output; checking that `sleep_hour` is later than
`home_hour` (the worksheet: "assume the input is valid" — an optional extension).

---

## 3. Lesson Goal

**Build a real program that combines input, a function that returns a value, a `while` accumulation loop, an f-string
prompt and one call to the AI — and explain why the AI is called once, after the loop.**

---

## 4. Core Mental Models

```python
all_tasks = ""
task_name = input("Enter a task (or done to finish): ")
while task_name != "done":                                     # collect first
    task_time = float(input(f"How many hours will {task_name} take? "))
    all_tasks += f"{task_name} ({task_time} hours), "
    task_name = input("Enter another task (or done to finish): ")   # last line of the loop

prompt = f"I have these tasks: {all_tasks} ..."                # the loop has finished
result = ask_the_ai(prompt)                                     # one call
```

Input → logic (our code: the hours, the sums) → magic (the AI: an order, splitting long tasks, encouragement). A good
prompt has **context** (who I am), **the task** (what to build), **the data** (the hours, the tasks) and **the wanted
result** (a short list of time blocks).

---

# 5. Short Intro (0–12)

| Clock | Activity |
|---|---|
| 0–3 | **Recap (deck slides 3–4):** f-strings and the wrapper `ask_the_ai` from 4.1 — the same code is on the slide. |
| 3–5 | **The problem (slides 6–7):** school tasks, and no time for fun — what are the options? An app that balances. |
| 5–8 | **What we build (slides 8–9):** 📥 input (home hour, sleep hour, tasks), ⚙ logic (the hours of the afternoon), ✨ the AI (a balanced, encouraging schedule). |
| 8–11 | **Discussion (slide 10):** "What can the AI give us that plain code cannot?" — plain code prints a dry list ("14:00–15:00 homework"); the AI can order, split long tasks, add a break and a kind word. |
| 11–12 | The map of the project (slide 11): input, conditions, two functions, `while`, prompt engineering. Hand out the starter. |

---

# 6. Lab (12–90)

Starter: [`BalancedDay_Starter.py`](BalancedDay_Starter.py). Reference: [`BalancedDay_Reference.py`](BalancedDay_Reference.py).
Default = the stand-in (ZONE A): the whole project runs with no key. **Files needing a live run with a real key:** the
base project (`task3`) and the feature version (`task4_features`) — run each once before class.

## 12–18 — Warm-up: a variable that does not exist

```python
home_hour = 14
sleep_hour = 22
today_time = sleep_hour - home_hour
prompt = f"I have {time_today} hours today. Build me a balanced schedule that starts at {home_hour}."
print(prompt)
```

`NameError: name 'time_today' is not defined`. The variable is `today_time` — the worksheet's own suggested sentences
use the other order. Fix, and say how to prevent it: print the prompt before sending it (a debug print).

## 18–28 — Stage 1: how many hours do we have?

Read `home_hour` and `sleep_hour` (whole numbers; assume valid input). Write `calc_time_today(start, end)` that
**returns** the hours; call it and print the result.

```text
What hour do you get home? 14
What hour do you want to go to sleep? 22
You have 8 hours this afternoon.
```

## 28–42 — Stage 2: collect the tasks

A `while` loop until `done`; each time a task name and the hours (`float(input(...))`); `all_tasks += f"..."`. The second
`input()` is the **last line** of the loop. Print `all_tasks` to check it.

```text
homework (2.0 hours), sport (1.5 hours), 
```

## 42–60 — Stage 3: the prompt and the one call

Before writing it: plan the prompt in an online chat first (golden rule 1) — context, task, data, result; discuss
"send only what is needed". Then **after the loop**: an f-string prompt from `all_tasks`, `today_time`, `home_hour` and
`sleep_hour` (a triple-quoted `f"""…"""` lets the prompt span lines); print it; call `ask_the_ai` **once**; print the
schedule, framed as a suggestion to check.

```text
I am a teenager and I come home from school at 14:00.
I have these tasks, with the time each one takes: homework (2.0 hours), sport (1.5 hours), 
I have 8 hours today, for the tasks and also for fun.
...
--- Your schedule (check it before you use it) ---
[stand-in] 15:00 snack and homework, 16:30 short break, 17:00 the rest of the tasks, then free time.
Calls sent: 1
```

**Prompt engineering (slide 11 of the deck):** compare a weak prompt ("make me a schedule") with ours: which one gives
the model something to work with? What information must **not** go in (names, phone, address)?

## 60–62 — Limits check

Open `Calls sent:` — it must be 1. A run that sends 10 calls would use two thirds of a key's minute. If a real call
returns 429 or 503: the code is fine — wait a minute and run again (the stand-in can show it:
`SIMULATE_ERROR = "429"` in ZONE A, teacher only).

## 62–82 — Advanced features (any order, any number)

Choose from the worksheet's list: (1) emojis for every task; (2) a language choice; (3) `len(task_name) >= 3` before
adding a task; (4) `total_task_time += task_time`, net fun time `today_time - total_task_time`, and **no call** if it
is negative; (5) a motivation sentence for every task; (6) a percentage summary
(`task_percent = total_task_time / today_time * 100`, printed with `:.1f`). Our addition, (7) privacy: a task that
contains `password`, `phone` or `address` is not added. Colors (the worksheet's feature 7) are Colab-only — optional there.
The worksheet calls this "the real hi-tech challenge: adding code to an existing program" — say so.

## 82–86 — Peer review

Swap with a partner: is the key absent from the file? do `calc_time_today` and `ask_the_ai` `return` (not print)? is
the prompt built with context, task, data and a wanted result? are the tasks collected before the call? is there exactly
one call? are short and sensitive tasks handled?

## 86–90 — Answer critique, save, exit

After a run (real or stand-in): mark one detail that clearly comes from the input, one suggestion that looks useful,
one assumption the model added, one detail to check or change. Save As `G8_U4_M2_BalancedDay_<Name>.py` (no key in the
file). Exit question: "Why is the API called once, after the loop?"

### Tool Note – the AI service
Same setup as 4.1 (keys from AI Studio, the model name `gemini-2.5-flash` checked before class, the key from Colab
Secrets or an environment variable). **Quota plan:** ≈15 requests/minute per key; a class of 30 on 10 keys is three
students per key, and each student needs only a few calls — so develop with the stand-in and switch to the real
service for the **final run** only.

### Tool Note – Thonny vs Colab
The Ministry worksheet is a Colab notebook. Files here use the English word `done` as the stop word, so students do
not switch keyboards; the Ministry's Hebrew `"סיום"` works exactly the same if you prefer it (a one-word change).

---

# 7. Misconception Risks

| Misconception | Correction |
|---|---|
| The call can sit inside the loop "because the data is right there" | It multiplies calls; collect first, send once, after the loop (no indentation) |
| `calc_time_today` should print the result | It returns it, so the main program can print it, compare it and put it in the prompt |
| A variable named differently in the prompt will still work | The name inside `{ }` must be exactly the variable's name (the warm-up) |
| More text in the prompt is better | Detail that comes from the data and focus beat length; no personal data |
| The schedule is final | It is a suggestion, checked against the real day |
| The privacy check is complete | It is a basic classroom filter |

---

# 8. Assessment Evidence

- The warm-up error read and fixed; the debug print used
- Stage 1, 2, 3 each run with a test input and the printed prompt
- **Unit 4 checkpoint — "Balanced Day"** (20 points): functions that return a value (`calc_time_today`, `ask_the_ai`) 4 ·
  key security (no key in the file) 3 · dynamic prompt 3 · accumulation loop 3 · one call outside the loop 2 ·
  validation and privacy 3 · testing and explanation 2. Bands: 18–20 complete, safe and economical · 14–17 works with a minor flaw ·
  10–13 partial (a missing check or the call inside the loop) · 0–9 needs support
- The peer review and the answer critique, each with at least one concrete note
- The exit question answered with a reason
