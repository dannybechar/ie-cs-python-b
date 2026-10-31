# Unit 3.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: counter = counter + 1 inside a function makes counter LOCAL (it is assigned there),
# and then the right-hand side reads a local that has no value yet. global tells Python: use the outside one.
counter = 0


def do_step():
    global counter
    counter = counter + 1
    print("Step done!")


do_step()
print("Counter:", counter)


# Task 1 (worksheet 4.5, exercises 1 and 3): local or global
app_name = "Math Quiz"


def show_greeting(user_name):
    welcome_msg = "Hello " + user_name
    print(welcome_msg)
    print("Welcome to " + app_name)


score = 50


def update_score():
    score = 100  # a NEW local variable; the global score is untouched
    print("Inside function:", score)


def task1():
    show_greeting("Dana")
    update_score()
    print("Outside function:", score)  # 50
    # print(welcome_msg) -> NameError: welcome_msg is local to show_greeting


# Task 2 (deck 4.3, practice 2): a global that a function changes
total_points = 0


def add_bonus(bonus):
    global total_points
    total_points = total_points + bonus


def task2():
    add_bonus(10)
    add_bonus(10)
    print(total_points)  # 20


# Task 3 (worksheet 4.6, question 1): a function that uses other functions. The Ministry version builds the
# message with an f-string (taught in Unit 4); here the function returns a short word and the main program prints.
def parking_a():
    return 20


def parking_b(hours):
    if hours <= 3:
        return 5
    elif hours <= 4:
        return 15
    else:
        return 30


def compare_parking(hours):
    price_a = parking_a()
    price_b = parking_b(hours)
    if price_a < price_b:
        return "Parking A is cheaper"
    elif price_b < price_a:
        return "Parking B is cheaper"
    else:
        return "Same price"


def task3():
    print("2 hours:", compare_parking(2))
    print("4 hours:", compare_parking(4))
    print("10 hours:", compare_parking(10))
    print("24 hours:", compare_parking(24))


# Task 4 (worksheet 4.6, question 2): one return per branch, -1 when nothing matches
def how_many_legs(animal):
    if animal == "spider":
        return 8
    elif animal == "ant":
        return 6
    elif animal == "dog" or animal == "cat":
        return 4
    elif animal == "chicken":
        return 2
    else:
        return -1


def task4():
    animal = input("Enter name of an animal: ")
    print(how_many_legs(animal))


# Checkpoint (worksheet 4.6, question 4, adapted): two global variables with roles - a sum and a counter.
# The Ministry version returns two values at once (sumOfDonations, numberOfHighDonors); returning two values
# is not taught yet, so the function changes the globals instead.
sum_of_donations = 0
number_of_high_donors = 0


def add_donation(donation):
    global sum_of_donations
    global number_of_high_donors
    sum_of_donations += donation
    if donation > 100:
        number_of_high_donors += 1
        print("Thank you, the certificate is on the way")


def checkpoint():
    number_of_donors = int(input("Enter number of donors: "))
    for i in range(number_of_donors):
        donation = int(input("Enter donation: "))
        add_donation(donation)
    print("Total donations:", sum_of_donations)
    print("Number of donations above 100 nis:", number_of_high_donors)


# If time: worksheet 4.5 exercise 4
coins = 10


def add_coins(new_coins):
    global coins
    coins = coins + new_coins


# If time: deck 4.3, "weight of a number" - the product of the digits of a two-digit number
def weight_of_number(number):
    d1 = number % 10
    d2 = number // 10
    return d1 * d2


def task_if_time():
    add_coins(5)
    print("Total coins:", coins)  # 15
    a = weight_of_number(75)
    b = weight_of_number(12)
    print(a, b)  # 35 2
    if a > b:
        print(75)
    else:
        print(12)


# task1()
# task2()
# task3()
# task4()
# checkpoint()
# task_if_time()
