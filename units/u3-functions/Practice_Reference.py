# Unit 3.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: the arguments were in the wrong order. Correct call: price_after_discount(200, 20) -> 160.0
def price_after_discount(price, percent):
    discount = price * percent / 100
    return price - discount


print(price_after_discount(200, 20))


# Task 1 (worksheet 4.2, exercise 7)
def three_averages(g1, g2, g3):
    avg = (g1 + g2 + g3) / 3
    return avg


def task1():
    res = three_averages(80, 90, 100)
    print("The average is:", res)


# Task 2 (worksheet 4.2, exercise 8): the first rule that matches decides
def calculate_shipping(price, is_express):
    if price >= 200:
        shipping = 0
    elif is_express:
        shipping = 30
    else:
        shipping = 15
    return price + shipping


def task2():
    print("Total 1:", calculate_shipping(150, True))
    print("Total 2:", calculate_shipping(250, True))
    print("Total 3:", calculate_shipping(100, False))


# Task 3 (deck 4.1, find_max): a variable that holds the best value so far
def find_max(a, b, c):
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


def task3():
    max_number = find_max(7, 15, 9)
    print("The biggest number is:", max_number)


# Task 4 (deck 4.1, final_grade): an early return
def final_grade(grade, bonus):
    total = grade + bonus
    if total > 100:
        return 100
    return total


def task4():
    result = final_grade(95, 10)
    print("Final grade:", result)
    print("Final grade:", final_grade(70, 10))


# Task 5 (exam question 4.4, question 1): digit loops. The Ministry code uses int(number / 10) and
# "%d" formatting; here // and a comma in print do the same job with what the class has learned.
def secret1(number):
    while number > 0:
        print(number % 10)
        number = number // 10


def secret2(number):
    counter = 0
    while number > 0:
        number = number // 10
        counter = counter + 1
    print(counter)


def secret3(number):
    total = 0
    while number > 0:
        total = total + number % 10
        number = number // 10
    print("The digit sum is:", total)
    return total


def secret4(number):
    result = 1
    while number > 1:
        result = result * (number % 10)
        number = number // 10
    print("The digit product is:", result)


def task5():
    secret1(12345)  # 5 4 3 2 1, one per line
    secret2(12345)  # 5
    secret3(1024)   # The digit sum is: 7
    secret4(1024)   # The digit product is: 0 (the loop stops at 1, but 4 * 2 * 0 is already 0)


# Task 6 (exam question 4.4, question 2): a "special" number - the last digit is more than half the digit sum
def special_number():
    num = int(input("Please enter a number: "))
    total = 0
    digit = num % 10
    while num != 0:
        total = total + num % 10
        num = num // 10
    if digit > total / 2:
        print("Number is special")
    else:
        print("Number is not special")


# Task 7 (exam question 4.4, question 3): a perfect number - equals the sum of its divisors (not itself)
def perfect_number():
    num = int(input("Please enter a number: "))
    total = 0
    x = 1
    while x < num:
        if num % x == 0:
            total = total + x
        x = x + 1
    if total == num:
        print("Perfect number")
    else:
        print("Not perfect number")


# Task 8 (worksheet 4.5, exercise 6, part a): two early returns
def calculate_gift(years, monthly):
    if monthly <= 1200:
        return 0
    if years < 8:
        return years * 50
    else:
        return years * 100


def task8():
    print(calculate_gift(5, 1500))   # 250
    print(calculate_gift(10, 1500))  # 1000
    print(calculate_gift(10, 1000))  # 0


# If time (worksheet 4.5, exercise 6, parts b and c): the main program for 10 customers
def gifts_for_ten():
    count = 0
    total = 0
    for i in range(10):
        years = int(input("Years of membership: "))
        monthly = int(input("Monthly purchases: "))
        voucher = calculate_gift(years, monthly)
        if voucher > 0:
            count += 1
            total += voucher
    print("Customers who received a voucher:", count)
    print("Total vouchers:", total, "shekels")


# If time (exam question 4.4, question 4): positions of a digit in a 9-digit ID, right to left
def find_location():
    id_number = int(input("Please enter ID number: "))
    digit = int(input("Please enter a digit: "))
    found = False
    for index in range(1, 10):
        if id_number % 10 == digit:
            print(index)
            found = True
        id_number = id_number // 10
    if found == False:
        print(-1)


# task1()
# task2()
# task3()
# task4()
# task5()
# special_number()
# perfect_number()
# task8()
# gifts_for_ten()
# find_location()
