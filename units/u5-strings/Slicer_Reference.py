# Unit 5.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: filename[-3] is ONE character (the third from the end); a slice is needed for a substring
def warmup():
    filename = "answer.txt"
    extension = filename[-3:]
    print(extension)


# Task 1: three small slicing functions
def first_six(text):
    return text[:6]


def last_ten(text):
    return text[-10:]


def reversed_text(text):
    return text[::-1]


def task1():
    answer = "TITLE: Safe AI\nBODY: Check important facts."
    print(first_six(answer))
    print(last_ten(answer))
    print(reversed_text(answer))


# Task 2: masking, for a demo id only - never for a real key
def mask_id(demo_id):
    return "****" + demo_id[-4:]


def task2():
    print(mask_id("CLASSROOM-2026-ABCD"))


warmup()
# task1()
# task2()
