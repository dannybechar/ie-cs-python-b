# Unit 3.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: the function computed num * 3 but never returned it, so Python returns None.
def triple(num):
    return num * 3


result = triple(7)
print(result)


# Task 1: trace and find the error (worksheet 4.2, exercises 1-3)
def calculate_box(length, width):
    area = length * width
    print("Area is:", area)


def sum_prices(item1, item2, item3):
    return item1 + item2 + item3


def check_pass(grade):
    if grade >= 60:
        return "Pass"
        print("Congratulations!")  # never runs: return stops the function
    return "Fail"


def task1():
    calculate_box(4, 5)
    # sum_prices(25, 40) -> TypeError: three parameters, only two arguments. Fix: send three.
    total = sum_prices(25, 40, 30)
    print("Total price:", total)
    result = check_pass(85)
    print("Result:", result)


# Task 2: return the perimeter (worksheet 4.2, exercise 4)
def rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter


def task2():
    res = rectangle_perimeter(6, 3)
    print("Perimeter:", res)


# Task 3: from print to return (worksheet 4.2, exercise 5)
def calculate_pay(hours, wage):
    pay = hours * wage
    return pay


def task3():
    total = calculate_pay(8, 50)
    print("Total pay:", total)


# Task 4: two possible returns (worksheet 4.2, exercise 6)
def get_cheaper(price1, price2):
    if price1 < price2:
        return price1
    else:
        return price2


def task4():
    cheap = get_cheaper(80, 55)
    print("Cheaper price is:", cheap)


# If time: use the returned value in an if
def average_grade(grade1, grade2):
    return (grade1 + grade2) / 2


def task_if_time():
    avg = average_grade(55, 65)
    if avg >= 60:
        print("Passed")
    else:
        print("Failed")


# task1()
# task2()
# task3()
# task4()
# task_if_time()
