# Warm-up: remove_even should delete every even number, so the list should end as [1].
# Predict the printed list, run it, then explain on paper what the loop skipped.

def remove_even(values):
    for item in values:
        if item % 2 == 0:
            values.remove(item)


numbers = [2, 4, 6, 8, 1]
remove_even(numbers)
print(numbers)


# Task 1: write sum_by_index(values) (a loop over range(len(values))) and sum_by_value(values)
# (a loop directly over the list). Both return the total. Inside each loop also print item, to see
# what item holds. Test on [51, 84, 72, 13, 29] - both must give 249.


# Task 2: write calculate_average(values) - returns the average; for an empty list returns 0.
# Test on [25.1, 20.0, 21.5, 24.0, 21.4, 24.5, 21.5, 16.0, 23.3] and on [].


# Task 3: write read_prices(count) - reads count prices with input() (use float), adds each
# to a list, and returns the list. Then, outside the function, print the list and the total
# (use sum_by_value). Run it with count 5 and the prices 400, 350, 100, 250, 70.


# Task 4: write without_even(values) - returns a NEW list without the even numbers (the
# original must not change). Then write sorted_copy(values) - returns a sorted copy while the
# original keeps its order. Test both on [5, 2, 8, 1, 4].
