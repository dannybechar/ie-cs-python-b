# Warm-up: this should remove every even number, leaving an empty list. Predict, run, then fix it
# (hint: changing a list's length while looping over it skips elements).

values = [2, 4, 6, 8, 10]
for value in values:
    if value % 2 == 0:
        values.remove(value)
print(values)


# Task 1: write get_sorted_copy(values) - returns a NEW sorted list, without changing the
# original. Test on [72, 95, 61] and confirm the original list is unchanged afterward.


# Task 2: write calculate_total(values) and calculate_average(values) (0 for an empty list).
# Test both on [72, 84, 65].
