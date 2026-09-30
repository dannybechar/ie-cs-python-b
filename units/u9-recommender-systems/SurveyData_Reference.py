# Unit 9.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: 0 is the agreed code for "don't know this item", never "disliked".
def describe_rating(value):
    if value == 0:
        return "don't know"
    elif value == 1:
        return "disliked"
    elif value == 2:
        return "neutral"
    elif value == 3:
        return "liked"


# Task 1: every value must be one of the four agreed codes
def validate_ratings(row):
    for value in row:
        if value not in (0, 1, 2, 3):
            return False
    return True


def task1():
    print(validate_ratings([3, 1, 0, 3]))
    print(validate_ratings([3, 1, 5, 3]))


# Task 2: "known" means anything the user rated above 0
def count_known(ratings):
    count = 0
    for value in ratings:
        if value != 0:
            count += 1
    return count


def task2():
    print(count_known([3, 1, 0, 3, 2]))


print(describe_rating(0))
# task1()
# task2()
