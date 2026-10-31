# Unit 4.1 - reference for the teacher: the Gemini API, wrapped in ask_the_ai().
# DEFAULT = CLASSROOM STAND-IN: ZONE A below replaces the real Gemini client with a fake one that returns
# fixed answers, so this file runs with plain `python`, with no key and no internet.
# LIVE RUN (needs a real key): see "ZONE A - LIVE VERSION" right below ZONE A. Never write a key in this file.
# One function per task. Run one at a time: python -c "import AskTheAI_Reference as r; r.task3()"


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


# Warm-up, fixed: print(response.text), not print(response)
def warm_up():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Tell me a short joke about programmers")
    print(response.text)


# Task 1: the wrapper - a parameter, and RETURN (not print)
def ask_the_ai(my_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=my_prompt)
    return response.text


def task1():
    answer = ask_the_ai("What is the distance between the Earth and the Moon?")
    print(answer)


# Task 2: a dynamic prompt - the f before the quotation mark, and the variables inside { }
def task2():
    name = input("Grandma's name: ")
    trait = input("A good trait of hers: ")
    prompt = f"Write a short birthday greeting for {name}, who is a very {trait} grandmother."
    print("Prompt:", prompt)
    answer = ask_the_ai(prompt)
    print(answer)


# Task 3: collect first, ask once - the call is OUTSIDE the loop (no indentation)
def task3():
    all_ing = ""
    item = input("Add an ingredient (or done to finish): ")
    while item != "done":
        all_ing = all_ing + item + ", "
        item = input("Add another ingredient (or done to finish): ")
    prompt = f"Invent a crazy, creative dessert that uses only these ingredients: {all_ing}"
    print("Prompt:", prompt)
    answer = ask_the_ai(prompt)
    print(answer)
    print("Calls sent:", client.models.calls)          # stand-in only; delete this line for the live version


# If time: do not waste a call on bad input
def task_if_time():
    name = input("Grandma's name: ")
    if len(name) < 2:
        print("The name is too short - no call was sent.")
    else:
        trait = input("A good trait of hers (Enter for a default): ")
        if trait == "":
            trait = "wonderful"
        prompt = f"Write a short birthday greeting for {name}, who is a very {trait} grandmother."
        answer = ask_the_ai(prompt)
        print(answer)


if __name__ == "__main__":
    warm_up()
