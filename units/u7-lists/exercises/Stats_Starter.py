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


# Task 3 (Ministry 13.2 #5): the names are full names, "First Last" with one space, e.g. "Dana Dikla".
# Write names_report(full_names) - prints: how many names contain the letters "el" (Elinor, Batel, Israel -
# ignore capital letters), how many names are longer than 7 characters (the space counts), and how many
# names have a first name and a last name that start with the same letter (Dana Dikla, Carmi Cohen).
# Test on a list of 10 names of your own.


# Task 4: a menu is ONE flat list: name, price, name, price ...
# menu = ["milk", 15, "bread", 10, "cornflakes", 20, "eggs", 18]
# Names sit at even positions (0, 2, 4 ...) and prices at odd positions (1, 3, 5 ...).
# a) write read_menu(count) - reads count dishes (a name, then a price) with input() into one flat list and returns it.
# b) write print_most_expensive(menu) - prints the name and price of the most expensive dish.
# c) write average_price(menu) - returns the average price.
# d) write names_above_average(menu) - returns a list of the names that cost more than the average.
# e) Odelia's clothes: buy = ["yellow shirt", 61.5, "red shirt", 73.99, "blue shirt", 60.0, "long shirt", 33.3, "orange shirt", 45.5]
#    print the total by index, the total by value (hint: type(item) != str), and the item names only.
# Then try the shortcut: print menu[0::2] and menu[1::2] and explain what they are.


# Task 5: three lists hold the grades of the same 5 students, in the same order:
# math = [100, 77, 85, 98, 100]
# comp = [95, 83, 77, 90, 100]
# physics = [76, 87, 84, 93, 100]
# write student_averages(math, comp, physics) - returns a new list: the average of each student
# (round every average to 2 decimal places).


# Task 6 (Ministry 14.2 - choose two):
# Q1: half_zero_one(size) - size is even; returns a list of that size, first half 0, second half 1 (8 -> [0, 0, 0, 0, 1, 1, 1, 1]).
# Q4: is_ascending(values) - True when every value is not smaller than the one before it ([11, 22, 33, 44] yes, [11, 22, 77, 44] no).
# Q6: best_grades(grade_a, grade_b) - two lists of grades of the same students; returns a new list with the higher grade of each student.
# Q7: pass_fail(numbers) - print the list of grades above 55 and the list of the other grades.
# (Q2 and Q3 of 14.2 are the "above the average" pattern you already wrote in Task 2.)


# Challenge menu (choose what you like):
# a) 14.0 #8 evens_first(values) - returns a NEW list: all the even numbers first, then the odd ones.
# b) 14.0 #9 discount_20(prices) - returns a NEW list of the prices after a 20% discount.
# c) 14.0 #11 remove_place_num(values) - returns a NEW list without the items whose POSITION is divisible by 3 (positions 0, 3, 6 ...).
# d) 14.0 #13 magic(my_list) - True when the list is not empty, its length divides by 3, and its three equal parts are the same:
#    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] is magic. (No list of lists is needed - three slices do it.)
# e) 14.5 count_words(text) - how many words are in a sentence? You must use split; you may not use count.
# f) 12.1 p. 40 can_release(bugs) - bugs is a list of kinds ("Highly Critical", "Critical", "Major", "Medium", "Minor").
#    Print how many of each kind; the software may be released with no Critical and no Highly Critical, at most 1 Major, 5 Medium and 10 Minor.
# g) 14.0 #12 FIND THE BUG: the function below should return the average of each student. The grades of
#    all students are in one list; l2 says how many grades each student has.
#    l1 = [80, 35, 90, 85, 55, 75, 60, 80, 90]   l2 = [3, 2, 4]   expected [68.33, 70.0, 76.25]

def avg_stud(l1, l2):
    result = []
    begin = 0
    for count in l2:
        part = l1[begin:begin + count]
        result.append(sum(part) / count)
        begin += 1 + count
    return result


# Stretch for fast students (Ministry 14.0 pp. 4-11, strings only):
# h) robber(text) - Robber language: every letter that is not a vowel (a e i o u) is doubled with an "o" between: "cat" -> "cocatot", "have fun" -> "hohavove fofunon". The space stays.
# i) valid_ip(ip_text) - True for "192.168.0.17": four parts separated by dots, each a whole number from 0 to 255.
# j) encrypt(text) - every E becomes &, every T becomes @, every A becomes % (capital and small): "THE PARTY IS TODAY AT MIDNIGHT" -> "@H& P%R@Y IS @OD%Y %@ MIDNIGH@"
