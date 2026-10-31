# Unit 5.1 - reference for the teacher.
# One task per function; run ONE at a time by removing the # from its call at the bottom.


# Warm-up, explained: the last valid index is len(word) - 1 (or -1). word[len(word)] is one past the end:
# IndexError: string index out of range
def warmup():
    word = "ROBOT"
    last_letter = word[len(word) - 1]
    print(last_letter)


# Task 1: predict-and-check (Ministry worksheet 7.2, questions 1-2)
def task1():
    text1 = "I like to play, "
    text2 = "piano"
    text3 = "guitar"
    print(text1 + text2)
    print(text1 + text3)
    print(text3 * 2)
    msg1 = "abc" + "d" * 3
    msg2 = "ef"
    msg3 = "7"
    print(msg1 + msg2)
    print(len(msg1))
    print(len(msg1 + msg2))
    print(msg3 * 2)
    print(len(msg3))


# Task 2: int() and str() (worksheet question 3) - "+" adds numbers, joins strings
def add_as_numbers(first, second):
    return int(first) + int(second)


def join_as_text(first, second):
    return first + second


def task2():
    print(add_as_numbers("12", "30"))
    print(join_as_text("12", "30"))


# Task 3: positive and negative indices on "PYTHON" (worksheet question 4)
def show_edges(st):
    print(st[0])
    print(st[-6])
    print(st[5])
    print(st[-1])
    print(st[2])
    print(st[-4])


def task3():
    show_edges("PYTHON")


# Task 4: a returning function
def first_and_last(word):
    return word[0] + word[-1]


def task4():
    print(first_and_last("ROBOT"))
    print(first_and_last("A"))


# If time
def stars_for(word):
    return "*" * len(word)


def task5():
    print(stars_for("hello"))



warmup()
# task1()
# task2()
# task3()
# task4()
# task5()
