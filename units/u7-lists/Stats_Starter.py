# Warm-up: this should find the largest of [-5, -2, -9]. Predict, run, then fix the starting value.

def find_maximum(values):
    largest = 0
    for value in values:
        if value > largest:
            largest = value
    return largest


print(find_maximum([-5, -2, -9]))


# Task 1: write count_above(values, threshold) and count_in_range(values, low, high)
# (low and high are both included). Test on [81, 24, 67, 91].


# Task 2: write find_minimum(values) - returns None for an empty list, otherwise the smallest
# value, initialized from the list's own first element (not from 0). Test on [81, 24, 67, 91]
# and on [].


# Task 3: write build_report(values) - returns "No data" for an empty list; otherwise a string
# with the count, the average (rounded to 1 decimal place), the minimum and the maximum, each on
# its own line. Test on [81, 24, 67, 91].
