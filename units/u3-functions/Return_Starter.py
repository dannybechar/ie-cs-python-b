# Warm-up: run this. The function should give back three times the number, but it prints None. Add one word to fix it.


def triple(num):
    num * 3


result = triple(7)
print(result)


# Task 1: three snippets from the worksheet (see the lab brief). Predict the output on paper first, then run.
def calculate_box(length, width):
    area = length * width
    print("Area is:", area)


def sum_prices(item1, item2, item3):
    return item1 + item2 + item3


def check_pass(grade):
    if grade >= 60:
        return "Pass"
        print("Congratulations!")
    return "Fail"


# calculate_box(4, 5)
# total = sum_prices(25, 40)        # predict: what happens? Run it, read the error, then fix the call.
# print("Total price:", total)
# result = check_pass(85)
# print("Result:", result)


# Task 2: write rectangle_perimeter(length, width) - it RETURNS the perimeter, it does not print.
# Call it with 6 and 3, save the result in res and print "Perimeter:", res.


# Task 3: change this function so it returns the pay instead of printing it.
# Then save the result in a variable called total and print it.
def calculate_pay(hours, wage):
    pay = hours * wage
    print("Total pay:", pay)


# Task 4: write get_cheaper(price1, price2) - it returns the lower of the two prices.
# Call it with 80 and 55 and print "Cheaper price is:", cheap.


# If time: write average_grade(grade1, grade2) that returns the average,
# then use the returned value in an if/else that prints "Passed" (60 or more) or "Failed".
