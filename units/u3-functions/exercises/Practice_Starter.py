# Warm-up: the price after a 20 percent discount of 200 should be 160.0. Run it, see what is wrong, and fix ONE line.


def price_after_discount(price, percent):
    discount = price * percent / 100
    return price - discount


print(price_after_discount(20, 200))


# Task 1: write three_averages(g1, g2, g3) - returns the average. Call it with 80, 90, 100 and print the result.


# Task 2: write calculate_shipping(price, is_express) - returns price + shipping.
# 200 or more: free shipping; else express (True): 30; else 15. Test (150, True), (250, True), (100, False).


# Task 3: write find_max(a, b, c) - returns the biggest of three numbers. Start by assuming a is the biggest.


# Task 4: write final_grade(grade, bonus) - returns grade + bonus, but never more than 100.


# Task 5 (exam question): predict the output of each call on paper BEFORE you run anything.
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


# secret1(12345)
# secret2(12345)
# secret3(1024)
# secret4(1024)


# Task 6 (exam question): special_number() - see the lab brief for the code with blanks.


# Task 7 (exam question): perfect_number() - see the lab brief for the code with blanks.


# Task 8: write calculate_gift(years, monthly) - see the lab brief. It returns the gift amount, or 0.
# If time: the main program for 10 customers, and find_location() - see the lab brief.
