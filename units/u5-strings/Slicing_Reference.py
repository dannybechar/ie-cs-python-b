# Unit 5.2 - reference for the teacher.
# One task per function; run ONE at a time by removing the # from its call at the bottom.


# Warm-up, explained: upper() returns a NEW string and the program threw it away. Fix: title = title.upper()
def warmup():
    title = "strings are sequences"
    title = title.upper()
    print(title)


# Task 1: write the slice for each wanted output (worksheet 7.2, questions 5-6)
def task1():
    text = "I like to play drums"
    print(text[-5:])       # drums
    print(text[7:14])      # to play
    print(text[::4])       # Ikoar
    number = "345124987"
    print(number[3:6])     # 124
    print(number[-4:-2])   # 49
    print(number[1:5])     # 4512
    print(number[6:])      # 987


# Task 2: count (worksheet question 15). count never counts overlapping matches.
def count_the(text):
    return text.count("the")


def task2():
    print(count_the("the other theme is there"))
    print("aaaa".count("aa"))     # 2, not 3


# Task 3: replace with a count (worksheet question 9) - a new string comes back
def replace_first_three(text):
    return text.replace("|", "we", 3)


def task3():
    print(replace_first_three("a|b|c|d|e"))


# Task 4: normalize with lower() before checking "in" (worksheet question 13)
def has_yes(text):
    return "yes" in text.lower()


def task4():
    print(has_yes("Maybe YES maybe no"))
    print(has_yes("no way"))


# If time: find with a start position - the "." must come after the "@"
def looks_like_email(address):
    at = address.find("@")
    if at == -1:
        return False
    return address.find(".", at + 1) != -1


def task5():
    print(looks_like_email("dana@school.org"))
    print(looks_like_email("dana@school"))
    print(looks_like_email("dana.school"))


warmup()
# task1()
# task2()
# task3()
# task4()
# task5()
