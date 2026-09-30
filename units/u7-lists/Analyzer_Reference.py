# Unit 7.5 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


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


# Task 2 (project - the checkpoint): "AI Experiment Analyzer"
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


warmup()
# task1()
# experiment_analyzer()
