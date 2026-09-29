# Unit 5.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, explained: strings are immutable. text.upper() returns a NEW string; it does not
# change text in place. Fix: text = text.upper()
def warmup():
    text = "python"
    text = text.upper()
    print(text)


# Task 1: a basic prompt checker
def prompt_checker():
    prompt = input("Enter a prompt: ").strip()
    lower_prompt = prompt.lower()
    print("Length:", len(prompt))
    print("Empty:", prompt == "")
    print("Contains password:", "password" in lower_prompt)
    print("Ends with question:", prompt.endswith("?"))


# Task 2: a returning function, not a print inside an if
def header_check(answer):
    if answer.startswith("SUMMARY:"):
        return "Structured answer"
    return "Missing title"


def task2():
    print(header_check("SUMMARY: Python loops repeat instructions."))
    print(header_check("Python loops repeat instructions."))


warmup()
# prompt_checker()
# task2()
