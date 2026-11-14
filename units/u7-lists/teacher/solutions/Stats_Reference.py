# Lessons 13.2, 14.0–14.2 - reference for the teacher.
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


# Ministry 14.0 #12 avg_stud: l1 holds the grades of all students one after another, l2 says how many grades each has.
# The bug of the official solution (begin += 1 + i) is fixed here
def avg_stud(l1, l2):
    result = []
    begin = 0
    for count in l2:
        part = l1[begin:begin + count]
        result.append(round(sum(part) / count, 2))
        begin += count      # NOT begin += 1 + count (the Ministry 14.0 p. 23 solution skips a grade per student)
    return result



# Task 3, step (a) (Ministry 13.2 #6): read a flat menu: name, price, name, price ...
def read_menu(count):
    menu = []
    for turn in range(count):
        name = input("Dish name: ")
        price = int(input("Price: "))
        menu.append(name)
        menu.append(price)
    return menu


# Task 3, step (d) (Ministry 12.6 Q6): the clothes of Odelia - one flat list name, price, name, price ...
# (the Ministry's sample list has broken quotes and some prices as text; here the prices are numbers)
def clothes_by_index(buy):
    total = 0
    for index in range(len(buy)):
        if index % 2 == 1:
            total += buy[index]
    return round(total, 2)


def clothes_by_value(buy):
    total = 0
    for item in buy:
        if type(item) != str:
            total += item
    return round(total, 2)


def clothes_names(buy):
    for index in range(0, len(buy), 2):
        print(buy[index])


# Task 3, step (e) (Ministry 13.2 #5): names are full names "First Last" with one space between them
def names_report(full_names):
    with_el = 0
    long_names = 0
    same_letter = 0
    for full_name in full_names:
        if "el" in full_name.lower():
            with_el += 1
        if len(full_name) > 7:
            long_names += 1
        parts = full_name.split()
        if parts[0][0].lower() == parts[1][0].lower():
            same_letter += 1
    print("Names with el:", with_el)
    print("Names longer than 7:", long_names)
    print("Same first letter:", same_letter)


# Task 6 (Ministry 14.2): choose two of Q1, Q4, Q6, Q7
def half_zero_one(size):
    result = []
    for index in range(size):
        if index < size // 2:
            result.append(0)
        else:
            result.append(1)
    return result


def is_ascending(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def is_strictly_ascending(values):
    for index in range(len(values) - 1):
        if values[index] >= values[index + 1]:
            return False
    return True


def same_items_loop(first, second):
    if len(first) != len(second):
        return False
    for index in range(len(first)):
        if first[index] != second[index]:
            return False
    return True


def same_items(first, second):
    return first == second


def best_grades(grade_a, grade_b):
    grade_c = []
    for index in range(len(grade_a)):
        if grade_a[index] > grade_b[index]:
            grade_c.append(grade_a[index])
        else:
            grade_c.append(grade_b[index])
    return grade_c


def pass_fail(numbers):
    passed = []
    failed = []
    for number in numbers:
        if number > 55:
            passed.append(number)
        else:
            failed.append(number)
    print("pass:", passed)
    print("fail:", failed)


# Challenge menu - Ministry 14.5: how many words in a sentence (split is required, count is forbidden)
def count_words(text):
    return len(text.split())


# Challenge menu - Ministry 12.1 p. 40: bug severities
def can_release(bugs):
    kinds = ["Highly Critical", "Critical", "Major", "Medium", "Minor"]
    for kind in kinds:
        print(kind + ":", bugs.count(kind))
    return (bugs.count("Highly Critical") == 0 and bugs.count("Critical") == 0
            and bugs.count("Major") <= 1 and bugs.count("Medium") <= 5 and bugs.count("Minor") <= 10)


# Challenge menu - Ministry 14.0 #11: delete the items whose POSITION is divisible by 3 (positions 0, 3, 6 ...)
def remove_place_num(values):
    result = []
    for index in range(len(values)):
        if index % 3 != 0:
            result.append(values[index])
    return result


def remove_place_num_in_place(values):
    # deleting in place is safe when the loop walks from the END: the positions still to visit do not move
    for index in range(len(values) - 1, -1, -1):
        if index % 3 == 0:
            values.pop(index)


# Challenge menu - Ministry 14.0 #13: the "magic list" is NOT a list of lists, it only compares three slices
def magic(my_list):
    if len(my_list) == 0 or len(my_list) % 3 != 0:
        return False
    size = len(my_list) // 3
    first = my_list[:size]
    second = my_list[size:size * 2]
    third = my_list[size * 2:]
    return first == second and second == third


# Stretch - Ministry 14.0 pp. 4-11 (strings and split only; no nested loops, no lists of lists)
def robber(text):
    vowels = "aeiou "
    robber_text = ""
    for item in text:
        if item in vowels:
            robber_text = robber_text + item
        else:
            robber_text = robber_text + item + "o" + item
    return robber_text


def valid_ip(ip_text):
    parts = ip_text.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():          # the Ministry's version crashes on "a.b.c.d" (int() on text)
            return False
        if int(part) > 255:
            return False
    return True


def encrypt(text):
    text = text.replace("E", "&").replace("e", "&")
    text = text.replace("T", "@").replace("t", "@")
    text = text.replace("A", "%").replace("a", "%")
    return text


if __name__ == "__main__":
    print(find_maximum([-5, -2, -9]))
    # grades_report([95, 72, 88, 100, 45, 78, 96, 56])
    # presents_report([200, 150, 300, 50, 100, 250, 500, 120, 80, 350])
    # print(count_in_range([81, 24, 67, 91], 60, 90))
    # print_most_expensive(["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18])
    # print(student_averages([100, 77, 85, 98, 100], [95, 83, 77, 90, 100], [76, 87, 84, 93, 100]))
    # print(magic([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]), remove_place_num([0, 1, 2, 3, 4, 5, 6]))
    # print(evens_first([5, 2, 8, 1, 4]), discount_20([100, 50]))
    # print(avg_stud([80, 35, 90, 85, 55, 75, 60, 80, 90], [3, 2, 4]))
