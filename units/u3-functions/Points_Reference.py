# Unit 3.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: the function computes price - discount but never returns it, so the function
# returns None (Python's default) and "None" is what final_price holds and prints.
def discounted(price, percent):
    discount = price * percent / 100
    return price - discount


# Task 1: a returning function with no print inside it
def is_even(number):
    return number % 2 == 0


def task1():
    print(is_even(14))
    print(is_even(9))


# Task 2: the returned value used directly in an if
def passed(score):
    return score >= 60


def task2():
    if passed(72):
        print("Continue")
    else:
        print("Try again")


# Task 3 (checkpoint): three small functions, bottom-up
def calculate_points(level, tasks):
    return level * tasks * 10


def passed_checkpoint(points):
    return points >= 100


def show_result(name, points, success):
    print(name, points, success)


def task3():
    points = calculate_points(2, 6)
    success = passed_checkpoint(points)
    show_result("Maya", points, success)
    # boundary case: exactly 100 points
    points_b = calculate_points(2, 5)
    show_result("Ali", points_b, passed_checkpoint(points_b))
    # a case that does not pass
    points_c = calculate_points(1, 3)
    show_result("Noa", points_c, passed_checkpoint(points_c))


final_price = discounted(80, 25)
print(final_price)
# task1()
# task2()
# task3()
