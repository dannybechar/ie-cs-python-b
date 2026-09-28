# Unit 7.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: removing while iterating shifts later items into skipped positions.
# Build a NEW list of what to keep instead of mutating the one being looped over.
def warmup():
    values = [2, 4, 6, 8, 10]
    kept = []
    for value in values:
        if value % 2 != 0:
            kept.append(value)
    print(kept)


# Task 1: copy before sorting, so the original order survives
def get_sorted_copy(values):
    ordered = values.copy()
    ordered.sort()
    return ordered


def task1():
    scores = [72, 95, 61]
    print(get_sorted_copy(scores))
    print(scores)


# Task 2: the accumulation pattern - init, loop, update, use after the loop
def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def calculate_average(values):
    if len(values) == 0:
        return 0
    return calculate_total(values) / len(values)


def task2():
    scores = [72, 84, 65]
    print(calculate_total(scores))
    print(calculate_average(scores))


warmup()
# task1()
# task2()
