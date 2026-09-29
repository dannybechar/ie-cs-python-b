# Unit 4.1 - reference for the teacher.
# CLASSROOM MODE: ask_ai() calls a stand-in, not a real service, so this file runs with plain Python
# and needs no key. Before class, swap MOCK_MODE to False and fill in the real client (see below) -
# then test it live in Thonny with the real service.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.

MOCK_MODE = True


def ask_ai(prompt):
    if MOCK_MODE:
        return "Mock response: balance study, movement, rest, and sleep."

    # Real service (needs `pip install -U google-genai` and GEMINI_API_KEY set as an
    # environment variable - never write the key itself in this file):
    #
    # import os
    # from google import genai
    # MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    # client = genai.Client()
    # response = client.models.generate_content(model=MODEL, contents=prompt)
    # return response.text
    raise NotImplementedError("Fill in the real client above and set MOCK_MODE = False.")


# Task 1: the warm-up, fixed - a parameter, and return instead of print
def task1():
    answer = ask_ai("Give one healthy study habit.")
    print(answer)


# Task 2: check the prompt before "calling" the service
def ask_ai_checked(prompt):
    clean_prompt = prompt.strip()
    if len(clean_prompt) < 5:
        return "The prompt is too short. Please add details."
    return ask_ai(clean_prompt)


def task2():
    print(ask_ai_checked("Hi"))
    print(ask_ai_checked("Give one healthy study habit."))


task1()
# task2()
