# Warm-up: this should print the largest of the three numbers, -2. Predict, run, then fix one line.

def find_maximum(values):
    largest = 0
    for value in values:
        if value > largest:
            largest = value
    return largest


print(find_maximum([-5, -2, -9]))


# Task 1: write grades_report(grades) - prints the average, the list of grades above the average,
# the list of grades that are 60 or less, and - only if the average is above 90 - "Excellent!".
# Test on [95, 72, 88, 100, 45, 78, 96, 56] and on [95, 100, 92, 98] and on [].


# Task 2: write presents_report(presents) - prints the total, the average present, and how many
# presents are above the average. Test on [200, 150, 300, 50, 100, 250, 500, 120, 80, 350].
# Then write count_in_range(values, low, high) - counts values from low to high, both included.
# Test on [81, 24, 67, 91] with 60 and 90.


# Task 3: a menu is ONE flat list: name, price, name, price ...
# menu = ["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18]
# Names sit at even positions (0, 2, 4 ...) and prices at odd positions (1, 3, 5 ...).
# a) write print_most_expensive(menu) - prints the name and price of the most expensive dish.
# b) write average_price(menu) - returns the average price.
# c) write names_above_average(menu) - returns a list of the names that cost more than the average.
# Then try the shortcut: print menu[0::2] and menu[1::2] and explain what they are.


# Task 4: three lists hold the grades of the same 5 students, in the same order:
# math = [100, 77, 85, 98, 100]
# comp = [95, 83, 77, 90, 100]
# physics = [76, 87, 84, 93, 100]
# write student_averages(math, comp, physics) - returns a new list: the average of each student
# (round every average to 2 decimal places).


# Task 5 (if time - choose at least one):
# a) evens_first(values) - returns a NEW list: all the even numbers first, then the odd ones.
# b) discount_20(prices) - returns a NEW list of the prices after a 20% discount.
# c) Find the bug: the function below should return the average of each student. The grades of
#    all students are in one list; counts says how many grades each student has.
#    grades = [80, 35, 90, 85, 55, 75, 60, 80, 90]   counts = [3, 2, 4]   expected [68.33, 70.0, 76.25]

def group_averages(grades, counts):
    result = []
    begin = 0
    for count in counts:
        part = grades[begin:begin + count]
        result.append(sum(part) / count)
        begin += 1 + count
    return result
