# Unit 9.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: "0" is its own answer ("don't know"); anything else is NOT a valid answer.
def describe_answer(answer):
    if answer == "V":
        return "liked"
    elif answer == "X":
        return "disliked"
    elif answer == "0":
        return "don't know"
    else:
        return "invalid answer"


# Task 1: every character must be one of the three agreed capital letters / digit
def is_valid_answers(answers):
    for character in answers:
        if character != "V" and character != "X" and character != "0":
            return False
    return True


def task1():
    print(is_valid_answers("VX0XV"))
    print(is_valid_answers("VX0xV"))
    print(is_valid_answers("VX5XV"))


# Task 2: "known" means anything the person answered with V or X
def count_known(answers):
    count = 0
    for character in answers:
        if character != "0":
            count += 1
    return count


def task2():
    print(count_known("VX0XV"))


# Task 3 (if time): a broken row has the wrong number of answers
def has_all_answers(item_names, answers):
    return len(answers) == len(item_names)


def task3():
    item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
    print(has_all_answers(item_names, "VX0XV"))
    print(has_all_answers(item_names, "VX0X"))


print(describe_answer("0"))
print(describe_answer("v"))
# task1()
# task2()
# task3()
