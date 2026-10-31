# Unit 4.2 - reference for the teacher: the "Balanced Day" project (Ministry worksheet 6.2, in English).
# DEFAULT = CLASSROOM STAND-IN: ZONE A replaces the real Gemini client with a fake one that returns fixed
# answers - plain `python`, no key, no internet. The live version is described right below ZONE A.
# One function per task. Run one at a time: python -c "import BalancedDay_Reference as r; r.task3()"
# Type the word  done  to finish the task list (the Ministry worksheet uses the Hebrew word for "finished").


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

# ===== ZONE A - LIVE VERSION (teacher only; replace ZONE A above with ONE of these) =====
# Thonny:  Tools > Manage packages > install  google-genai   (or: pip install -U google-genai)
#   The key is read from an environment variable that the teacher set on the computer (Windows: setx GEMINI_API_KEY "..."
#   then restart Thonny). The key itself is never written in a file.
#
#   import os
#   from google import genai
#   my_api_key = os.environ["GEMINI_API_KEY"]
#   client = genai.Client(api_key=my_api_key)
#
# Google Colab (the Ministry's method - guide 5.0.2): left key icon > Add new secret > Name GEMINI_API_KEY >
#   paste the key > switch on "Notebook access".
#
#   from google.colab import userdata
#   from google import genai
#   my_api_key = userdata.get("GEMINI_API_KEY")
#   client = genai.Client(api_key=my_api_key)
# =========================================================================================


# The wrapper from Unit 4.1
def ask_the_ai(my_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=my_prompt)
    return response.text


# Warm-up, fixed: the variable is today_time, not time_today
def warm_up():
    home_hour = 14
    sleep_hour = 22
    today_time = sleep_hour - home_hour
    prompt = f"I have {today_time} hours today. Build me a balanced schedule that starts at {home_hour}."
    print(prompt)


# Task 1: how much time do we have this afternoon? (a function that RETURNS the number of hours)
def calc_time_today(start, end):
    return end - start


def task1():
    home_hour = int(input("What hour do you get home? "))
    sleep_hour = int(input("What hour do you want to go to sleep? "))
    today_time = calc_time_today(home_hour, sleep_hour)
    print(f"You have {today_time} hours this afternoon.")


# Task 2: collect the tasks - a while loop that accumulates one long string
def task2():
    all_tasks = ""
    task_name = input("Enter a task (or done to finish): ")
    while task_name != "done":
        task_time = float(input(f"How many hours will {task_name} take? "))
        all_tasks += f"{task_name} ({task_time} hours), "
        task_name = input("Enter another task (or done to finish): ")
    print(all_tasks)


# Task 3: the base project - collect first, then ONE call to the AI after the loop
def task3():
    print("Welcome to Balanced Day")
    home_hour = int(input("What hour do you get home? "))
    sleep_hour = int(input("What hour do you want to go to sleep? "))
    today_time = calc_time_today(home_hour, sleep_hour)
    print(f"You have {today_time} hours this afternoon.")

    all_tasks = ""
    task_name = input("Enter a task (or done to finish): ")
    while task_name != "done":
        task_time = float(input(f"How many hours will {task_name} take? "))
        all_tasks += f"{task_name} ({task_time} hours), "
        task_name = input("Enter another task (or done to finish): ")

    prompt = f"""
I am a teenager and I come home from school at {home_hour}:00.
I have these tasks, with the time each one takes: {all_tasks}
I have {today_time} hours today, for the tasks and also for fun.
Build me a balanced, encouraging schedule that includes the tasks and the fun time.
The schedule starts at {home_hour}:00 and ends at {sleep_hour}:00.
Write it as a short list of time blocks.
"""
    print(prompt)
    print("Building your balanced day...")
    result = ask_the_ai(prompt)
    print("--- Your schedule (check it before you use it) ---")
    print(result)
    print("Calls sent:", client.models.calls)          # stand-in only; delete this line for the live version


# Advanced features (any of them): a language choice, tasks of at least 3 letters, a privacy check, the
# net fun time (no call if there is none), a summary in percent, emojis and a motivation sentence in the prompt
def task4_features():
    print("Welcome to Balanced Day")
    language = input("Which language for the schedule (Hebrew / English)? ")
    home_hour = int(input("What hour do you get home? "))
    sleep_hour = int(input("What hour do you want to go to sleep? "))
    today_time = calc_time_today(home_hour, sleep_hour)
    print(f"You have {today_time} hours this afternoon.")

    all_tasks = ""
    total_task_time = 0
    task_name = input("Enter a task (or done to finish): ")
    while task_name != "done":
        lower_name = task_name.lower()
        if len(task_name) < 3:
            print("The task name is too short (at least 3 letters).")
        elif "password" in lower_name or "phone" in lower_name or "address" in lower_name:
            print("Do not write personal information in a task.")
        else:
            task_time = float(input(f"How many hours will {task_name} take? "))
            all_tasks += f"{task_name} ({task_time} hours), "
            total_task_time += task_time
        task_name = input("Enter another task (or done to finish): ")

    fun_time = today_time - total_task_time
    if today_time > 0:
        task_percent = total_task_time / today_time * 100
        rest_percent = 100 - task_percent
        print(f"Your tasks take {task_percent:.1f}% of your time, {rest_percent:.1f}% is left for rest.")

    if fun_time < 0:
        print("Warning: there are more tasks than hours today - no call was sent.")
    else:
        prompt = f"""
I am a teenager and I come home from school at {home_hour}:00.
I have these tasks, with the time each one takes: {all_tasks}
I have {fun_time} hours left for fun.
Build me a balanced, encouraging schedule that includes the tasks and the fun time.
The schedule starts at {home_hour}:00 and ends at {sleep_hour}:00.
Important:
1. Write the schedule in {language}.
2. Add a fitting emoji to every task.
3. For every task, add one short motivation sentence.
"""
        result = ask_the_ai(prompt)
        print("--- Your schedule (check it before you use it) ---")
        print(result)
        print("Calls sent:", client.models.calls)      # stand-in only; delete this line for the live version


if __name__ == "__main__":
    warm_up()
