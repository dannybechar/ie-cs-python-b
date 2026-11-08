# Unit 7.4 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: start from a REAL value of the list, never from 0
def find_maximum(values):
    if len(values) == 0:
        return None
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


def find_minimum(values):
    if len(values) == 0:
        return None
    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
    return smallest


def calculate_average(values):
    if len(values) == 0:
        return 0
    total = 0
    for value in values:
        total += value
    return total / len(values)


# Task 1: average, filters, a message
def grades_report(grades):
    if len(grades) == 0:
        print("No grades")
        return
    average = calculate_average(grades)
    above = []
    low = []
    for grade in grades:
        if grade > average:
            above.append(grade)
        if grade <= 60:
            low.append(grade)
    print("Average:", average)
    print("Above average:", above)
    print("60 or less:", low)
    if average > 90:
        print("Excellent!")


# Task 2: a total, an average, a counter that grows only when its condition holds
def presents_report(presents):
    total = 0
    for present in presents:
        total += present
    average = total / len(presents)
    count = 0
    for present in presents:
        if present > average:
            count += 1
    print("Total:", total)
    print("Average:", average)
    print("Above average:", count)


def count_in_range(values, low, high):
    count = 0
    for value in values:
        if low <= value <= high:
            count += 1
    return count


# Task 3: one flat list - names at even positions, prices at odd positions
def print_most_expensive(menu):
    best_price = menu[1]
    best_name = menu[0]
    for index in range(len(menu)):
        if index % 2 == 1 and menu[index] > best_price:
            best_price = menu[index]
            best_name = menu[index - 1]
    print("Most expensive:", best_name, best_price)


def average_price(menu):
    total = 0
    for index in range(len(menu)):
        if index % 2 == 1:
            total += menu[index]
    return total / (len(menu) // 2)


def names_above_average(menu):
    average = average_price(menu)
    names = []
    for index in range(len(menu)):
        if index % 2 == 1 and menu[index] > average:
            names.append(menu[index - 1])
    return names


def menu_shortcut(menu):
    print(menu[0::2])
    print(menu[1::2])


# Task 4: parallel lists - the same position in every list belongs to the same student
def student_averages(math, comp, physics):
    averages = []
    for index in range(len(math)):
        average = (math[index] + comp[index] + physics[index]) / 3
        averages.append(round(average, 2))
    return averages


# Task 5 (if time)
def evens_first(values):
    evens = []
    odds = []
    for value in values:
        if value % 2 == 0:
            evens.append(value)
        else:
            odds.append(value)
    return evens + odds


def discount_20(prices):
    result = []
    for price in prices:
        result.append(price * 0.8)
    return result


# the bug (begin += 1 + count skips one grade per student), fixed
def group_averages(grades, counts):
    result = []
    begin = 0
    for count in counts:
        part = grades[begin:begin + count]
        result.append(round(sum(part) / count, 2))
        begin += count
    return result


if __name__ == "__main__":
    print(find_maximum([-5, -2, -9]))
    # grades_report([95, 72, 88, 100, 45, 78, 96, 56])
    # presents_report([200, 150, 300, 50, 100, 250, 500, 120, 80, 350])
    # print(count_in_range([81, 24, 67, 91], 60, 90))
    # print_most_expensive(["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18])
    # print(student_averages([100, 77, 85, 98, 100], [95, 83, 77, 90, 100], [76, 87, 84, 93, 100]))
    # print(evens_first([5, 2, 8, 1, 4]), discount_20([100, 50]))
    # print(group_averages([80, 35, 90, 85, 55, 75, 60, 80, 90], [3, 2, 4]))
