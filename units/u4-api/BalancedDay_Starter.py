# Warm-up: this collects activities into a prompt, then "calls" the AI once per activity - very wasteful.
# Run it with "Homework", "Walk", "done" - watch how many times ask_ai would really be called.
# CLASSROOM MODE: ask_ai() is a stand-in, not a real service - see Wrapper_Starter.py.


def ask_ai(prompt):
    return "Mock response: balance study, movement, rest, and sleep."


activity = input("Activity or done: ").strip()
while activity.lower() != "done":
    print(ask_ai(f"One tip for fitting in: {activity}"))
    activity = input("Activity or done: ").strip()


# Task 1: build a dynamic f-string prompt from a goal and a minutes count, both read with input().
# Print the prompt (do not call ask_ai yet).


# Task 2: read a short text with input(). If it is empty, use a default goal instead.
# Separately, check whether it contains "password", "phone" or "address" (case-insensitive) and
# print a warning if it does.


# Task 3 (project - "Balanced Day"): collect activities in a loop until "done"; skip activities
# under 3 characters; skip (with a warning) any activity containing a sensitive word; build ONE
# dynamic prompt from the goal and the collected activities; call ask_ai ONCE, after the loop.
