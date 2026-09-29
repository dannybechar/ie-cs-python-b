# Warm-up: this "wrapper" function has two bugs. Run it, read the error, then fix them one at a time.
# CLASSROOM MODE: ask_ai() below does not call a real service - it is a stand-in so the file runs
# with plain Python. Before class, swap in the real client (see the teacher's setup notes) and test
# it live in Thonny.


def ask_ai():
    response = "Mock response: balance study, movement, rest, and sleep."
    print(response.text)


answer = ask_ai("Give one healthy study habit.")
print(answer)


# Task 1: fix ask_ai() above so it:
#   1. takes prompt as a parameter
#   2. returns the answer with return, not print
# Then it should work with the call already written.


# Task 2: write a version of ask_ai() that checks the prompt first:
#   - if the prompt (after .strip()) is shorter than 5 characters, return
#     "The prompt is too short. Please add details." without "calling" the service at all.
#   - otherwise return the (mock) response, same as above.
