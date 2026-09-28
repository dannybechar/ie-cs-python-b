# Warm-up: 81 IS in the list, at index 0. Predict, run, then fix the way the result is checked.

def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


scores = [81, 24, 67, 91]
if linear_search(scores, 81):
    print("Found")
else:
    print("Not found")


# Task 1: write linear_search_sorted(values, target) - like linear_search, but stops early:
# on a SORTED list, once values[index] is no longer less than target, there is no point
# continuing. Test on [10, 20, 35, 50, 80] with target 35 (present) and target 40 (absent).


# Task 2 (project - "AI Experiment Analyzer"): a program that reads similarity scores from
# input() until -1 is entered (the sentinel - not stored), keeping only scores from 0 to 100;
# then prints the original list, a sorted COPY of it, the average, minimum and maximum; then
# reads a threshold and prints how many scores are at or above it; then reads a target score and
# prints its position in the sorted list (using linear_search_sorted).
