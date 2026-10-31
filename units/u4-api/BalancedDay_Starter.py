# WARM-UP BUG: this program should print a prompt, but it stops with an error. Run it, read the message, fix it.
# CLASSROOM STAND-IN: ZONE A is a fake Gemini client that returns fixed answers - no key, no internet.
# Do not edit ZONE A. (For a live class with a real key the teacher replaces ZONE A - see the teacher's notes.)
# Documented bug (teacher): the f-string uses {time_today} but the variable is today_time
# (the same slip is in the Ministry worksheet's suggested sentences) -> NameError.


# ===== ZONE A - CLASSROOM STAND-IN. Do not edit. =====
# It takes the place of the two real lines  `from google import genai`  and  `client = genai.Client(...)`.
SIMULATE_ERROR = None          # teacher demo: set to "429" or "503" to see what an overloaded service looks like


class FakeReply:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "GenerateContentResponse(candidates=[...], usage_metadata=...)"


class FakeModels:
    def __init__(self):
        self.calls = 0

    def generate_content(self, model, contents):
        self.calls += 1
        if SIMULATE_ERROR == "429":
            raise RuntimeError("429 RESOURCE_EXHAUSTED (stand-in simulation)")
        if SIMULATE_ERROR == "503":
            raise RuntimeError("503 UNAVAILABLE (stand-in simulation)")
        text = contents.lower()
        if "joke" in text:
            answer = "Why do programmers prefer dark mode? Because light attracts bugs."
        elif "moon" in text:
            answer = "The Moon is about 384,000 km from Earth, on average."
        elif "birthday" in text:
            answer = "Happy birthday, dear grandma! You are the warmest, kindest person we know."
        elif "dessert" in text:
            answer = "Crazy dessert: layer everything on the list with whipped cream, chill it, and enjoy."
        elif "schedule" in text:
            answer = "15:00 snack and homework, 16:30 short break, 17:00 the rest of the tasks, then free time."
        else:
            answer = "This is a fixed answer. A real model would answer your prompt here."
        return FakeReply("[stand-in] " + answer)


class FakeClient:
    def __init__(self):
        self.models = FakeModels()


client = FakeClient()
# ===== end of ZONE A =====

# ===== ZONE B - your program =====

# The wrapper from Unit 4.1 (use yours, or this one)
def ask_the_ai(my_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=my_prompt)
    return response.text


# Warm-up
home_hour = 14
sleep_hour = 22
today_time = sleep_hour - home_hour
prompt = f"I have {time_today} hours today. Build me a balanced schedule that starts at {home_hour}."
print(prompt)


# Task 1: how much time do we have this afternoon?
#   - read home_hour and sleep_hour with input() (whole numbers, e.g. 14 and 22)
#   - write a function calc_time_today(start, end) that RETURNS the number of hours
#   - call it, and print: You have 8 hours this afternoon.


# Task 2: collect the tasks
#   - all_tasks = ""  and a while loop that continues until the user types done
#   - each time: read a task name, then the hours it takes (float(input(...)))
#   - add it to all_tasks like this:  all_tasks += f"{task_name} ({task_time} hours), "
#   - the next input() is the LAST line of the loop (so the loop can end)


# Task 3: the base project - collect first, ask once
#   - plan your prompt in an online chat first (context, the task, the wanted result)
#   - AFTER the loop: build the prompt with an f-string from all_tasks, today_time, home_hour, sleep_hour
#   - print the prompt (a debug print), call ask_the_ai ONCE, and print the schedule it returns
#   - at the end print:  Calls sent:  followed by  client.models.calls  (stand-in only)


# Advanced features - choose any, in any order:
#   1. ask the AI to add a fitting emoji to every task
#   2. let the user choose the language of the schedule (Hebrew / English)
#   3. a task name shorter than 3 letters is not added (len)
#   4. total_task_time += task_time; if the tasks take more hours than today, do not call the AI - print a warning
#   5. ask the AI to add one short motivation sentence to every task
#   6. print a summary in percent: task_percent = total_task_time / today_time * 100
#   7. privacy: a task that contains the word password, phone or address is not added (with a warning)
