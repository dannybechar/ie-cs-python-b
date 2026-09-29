# Unit 5.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: range(len(text) + 1) goes one index too far - the last valid index is len(text) - 1
def warmup():
    text = "AI 2026"
    for index in range(len(text)):
        print(index, text[index])


# Task 1: normalize before counting, so case never matters
def count_maybe(text):
    return text.lower().count("maybe")


def task1():
    print(count_maybe("Maybe it works. MAYBE verify it."))


# Task 2: find returns -1 when nothing matches - check before slicing
def first_part(text):
    position = text.find(" ")
    if position == -1:
        return text
    return text[:position]


def task2():
    print(first_part("smart assistant"))
    print(first_part("Python"))


# Task 3: build a new string one character at a time - no per-digit .replace() calls
def hide_digits(text):
    result = ""
    for character in text:
        if character.isnumeric():
            result += "#"
        else:
            result += character
    return result


def task3():
    print(hide_digits("Room 12 at 09:30"))


warmup()
# task1()
# task2()
# task3()
