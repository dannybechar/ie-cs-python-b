# Unit 4.2 - reference for the teacher.
# CLASSROOM MODE: ask_ai() is a stand-in, not a real service - see Wrapper_Starter.py.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


def ask_ai(prompt):
    return "Mock response: balance study, movement, rest, and sleep."


# Warm-up, explained: one ask_ai call per activity wastes time, quota and possibly money.
# The fix (Task 3) collects everything first and calls ask_ai ONCE, after the loop.


# Task 1: a dynamic prompt built with an f-string
def task1():
    student_goal = input("What is your main goal for today? ").strip()
    available_minutes = input("How many minutes are available? ").strip()
    prompt = f"""
You help a ninth-grade student plan a balanced afternoon.
Goal: {student_goal}
Available time: {available_minutes} minutes
Return three short steps and one reminder to take a break.
"""
    print(prompt)


# Task 2: a default value for empty input, and a basic sensitive-word check
def task2():
    text = input("Enter a short, non-personal goal: ").strip()
    if len(text) == 0:
        text = "create a generally balanced afternoon"
    lower_text = text.lower()
    contains_sensitive_word = (
        "password" in lower_text
        or "phone" in lower_text
        or "address" in lower_text
    )
    if contains_sensitive_word:
        print("Do not send passwords, phone numbers, or addresses.")
    else:
        print("The text passed the basic classroom check:", text)


# Task 3 (project): "Balanced Day"
def balanced_day():
    goal = input("Main goal: ").strip()
    if len(goal) == 0:
        goal = "create a generally balanced afternoon"

    activities = ""
    activity = input("Activity or done: ").strip()

    while activity.lower() != "done":
        lower_activity = activity.lower()
        contains_sensitive_word = (
            "password" in lower_activity
            or "phone" in lower_activity
            or "address" in lower_activity
        )
        if contains_sensitive_word:
            print("Do not enter personal information.")
        elif len(activity) >= 3:
            activities += f"- {activity}\n"
        else:
            print("Activity is too short.")
        activity = input("Activity or done: ").strip()

    if len(activities) == 0:
        activities = "- no activities were entered\n"

    prompt = f"""
You help a ninth-grade student plan a balanced afternoon.
Goal: {goal}
Activities:
{activities}
Return four short time blocks, include one break,
and finish with a reminder that this is only a suggestion.
Do not ask for or infer personal information.
"""
    # One API call, after data collection is complete.
    answer = ask_ai(prompt)

    print("\nAI suggestion - check it before using it:")
    print(answer)


# task1()
# task2()
balanced_day()
