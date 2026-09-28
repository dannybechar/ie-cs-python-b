# Unit 7.4 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: if every value is negative, 0 is never beaten. Start from the list's own
# first element, so the candidate is always a real value from the data.
def find_maximum(values):
    if len(values) == 0:
        return None
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


# Task 1: a counter that grows only when the condition holds
def count_above(values, threshold):
    count = 0
    for value in values:
        if value >= threshold:
            count += 1
    return count


def count_in_range(values, low, high):
    count = 0
    for value in values:
        if low <= value <= high:
            count += 1
    return count


def task1():
    scores = [81, 24, 67, 91]
    print(count_above(scores, 70))
    print(count_in_range(scores, 60, 90))


# Task 2: the same fix as the warm-up, mirrored for the minimum
def find_minimum(values):
    if len(values) == 0:
        return None
    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
    return smallest


def task2():
    print(find_minimum([81, 24, 67, 91]))
    print(find_minimum([]))


# Task 3: a small report, built from the functions above
def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def calculate_average(values):
    if len(values) == 0:
        return 0
    return calculate_total(values) / len(values)


def build_report(values):
    if len(values) == 0:
        return "No data"
    report = "RESULT REPORT\n"
    report += "Count: " + str(len(values)) + "\n"
    report += "Average: " + str(round(calculate_average(values), 1)) + "\n"
    report += "Minimum: " + str(find_minimum(values)) + "\n"
    report += "Maximum: " + str(find_maximum(values))
    return report


print(find_maximum([-5, -2, -9]))
# task1()
# task2()
# print(build_report([81, 24, 67, 91]))
