# Unit 7.5 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
import random


def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


# Warm-up, fixed: index 0 is a valid, successful result, but Python treats 0 as False in an
# "if". Compare explicitly to -1 instead of using the returned value as a yes/no flag.
def warmup():
    scores = [81, 24, 67, 91]
    position = linear_search(scores, 81)
    if position != -1:
        print("Found at", position)
    else:
        print("Not found")


# Task 1: early stop on a sorted list
def linear_search_sorted(values, target):
    index = 0
    while index < len(values) and values[index] < target:
        index += 1
    if index < len(values) and values[index] == target:
        return index
    return -1


def task1():
    values = [10, 20, 35, 50, 80]
    print(linear_search_sorted(values, 35))
    print(linear_search_sorted(values, 40))



# Task 1, third part (Ministry 14.4 Q10): the position of a result in a SORTED ranking - the index if it is equal to one
# of the results, otherwise the index of the first result that is larger (the early stop). If nothing is larger,
# the position is len(best): the result would be last.
def position_in_ranking(best, result):
    for index in range(len(best)):
        if best[index] >= result:
            return index
    return len(best)


def ranking_demo():
    best = [10, 20, 35, 50, 80]
    print(position_in_ranking(best, 35))
    print(position_in_ranking(best, 40))
    print(position_in_ranking(best, 5))
    print(position_in_ranking(best, 99))


# Task 1, second part: the built-in index() raises an error when the value is missing
def index_demo():
    values = [10, 20, 35, 50, 80]
    print(values.index(35))
    print(values.index(40))


# Task 2: a new phone number
def random_number(prefixes):
    prefix = random.choice(prefixes)
    return prefix + "-" + str(random.randint(1000000, 9999999))


def is_special(number, special):
    digits = number[4:]
    if number in special:
        return True
    if digits.count("5") > 1:
        return True
    if digits in "0123456789" or digits in "9876543210":
        return True
    return False


def new_phone_number(taken, special):
    prefixes = ["050", "052", "053", "054"]
    number = random_number(prefixes)
    while number in taken or is_special(number, special):
        number = random_number(prefixes)
    return number


def task2():
    special = ["050-5555555", "050-1234777"]
    taken = []
    for turn in range(10):
        taken.append(new_phone_number(taken, special))
    print(taken)


# Exam bank (Ministry 14.4, choose one): Q3 shift right, Q4 find the bug, Q8 permutation, Q9 improvement
def shift_right(values):
    last = values.pop()
    values.insert(0, last)


# Q4: strictly ascending. The official snippet is an image that is not in the delivered text, so this buggy version is
# OURS (two typical mistakes: the loop runs one step too far, and equal neighbours are accepted). The fixed version follows.
def strictly_ascending_bug(values):
    for index in range(len(values)):
        if values[index] > values[index + 1]:
            return False
    return True


def strictly_ascending(values):
    for index in range(len(values) - 1):
        if values[index] >= values[index + 1]:
            return False
    return True


def is_permutation(values):
    for number in range(1, len(values) + 1):
        if values.count(number) != 1:
            return False
    return True


def improved(times):
    for index in range(1, len(times)):
        if times[index] >= times[index - 1]:
            return False
    return True


def exam_demo():
    numbers = [1, 2, 3, 4]
    shift_right(numbers)
    print(numbers)
    print(strictly_ascending([1, 2, 3]), strictly_ascending([1, 1, 2]), strictly_ascending([]))
    print(is_permutation([2, 4, 5, 1, 3]), is_permutation([2, 4, 4, 1, 3]), is_permutation([1, 2, 4]))
    print(improved([14.2, 13.9, 13.5]), improved([14.2, 14.2, 13.5]))


# Task 3 (project - the checkpoint): "AI Experiment Analyzer"
def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def calculate_average(values):
    if len(values) == 0:
        return 0
    return calculate_total(values) / len(values)


def find_minimum(values):
    if len(values) == 0:
        return None
    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
    return smallest


def find_maximum(values):
    if len(values) == 0:
        return None
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


def count_above(values, threshold):
    count = 0
    for value in values:
        if value >= threshold:
            count += 1
    return count


def read_scores():
    values = []
    score = int(input("Score from 0 to 100, or -1: "))
    while score != -1:
        if 0 <= score <= 100:
            values.append(score)
        else:
            print("Invalid score")
        score = int(input("Score from 0 to 100, or -1: "))
    return values


def experiment_analyzer():
    scores = read_scores()

    if len(scores) == 0:
        print("No valid scores")
        return

    ordered = scores.copy()
    ordered.sort()

    print("Original:", scores)
    print("Ordered:", ordered)
    print("Average:", round(calculate_average(scores), 1))
    print("Minimum:", find_minimum(scores))
    print("Maximum:", find_maximum(scores))

    threshold = int(input("Threshold: "))
    print("At or above threshold:", count_above(scores, threshold))

    target = int(input("Score to search for: "))
    position = linear_search_sorted(ordered, target)
    print("Position in ordered list:", position)


if __name__ == "__main__":
    warmup()
    # task1()
    # ranking_demo()
    # exam_demo()
    # index_demo()
    # task2()
    # experiment_analyzer()
