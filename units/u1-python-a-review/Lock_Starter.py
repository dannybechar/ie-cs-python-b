# Warm-up: run it and type -2. Why does it never stop? Stop it (red Stop button), then add one line.


def ask_age():
    age = int(input("Age: "))
    while age < 0:
        print("Invalid age")
    print("Accepted:", age)


# Task 1: write valid_age() - ask again until the age is between 0 and 120.


# Task 2: write locker() - up to 3 tries to type the code 4321, then Access granted or Access blocked.


# Task 3 (unit checkpoint): write points_goal() - 3 rounds, add the points, then check the goal of 10.


ask_age()
# valid_age()
# locker()
# points_goal()
