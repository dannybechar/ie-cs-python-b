# Unit 1.3 - reference solutions for the teacher.
# One function per task (define -> call, from Python A).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: without a new input inside the loop, age never changes and the condition stays True
def ask_age():
    age = int(input("Age: "))
    while age < 0:
        print("Invalid age")
        age = int(input("Age: "))
    print("Accepted:", age)


# Task 1: invalid means below 0 OR above 120
def valid_age():
    age = int(input("Age: "))
    while age < 0 or age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    print("Accepted:", age)


# Task 2: go on while there are tries left AND the code is not found yet
def locker():
    secret = 4321
    attempts = 0
    success = False
    while attempts < 3 and not success:
        guess = int(input("Code: "))
        attempts = attempts + 1
        if guess == secret:
            success = True
    if success:
        print("Access granted. Attempts:", attempts)
    else:
        print("Access blocked")


# Task 3 (unit checkpoint): a known number of rounds -> for; the goal is checked once, after the loop
def points_goal():
    points = 0
    for round_num in range(1, 4):
        print("Round", round_num)
        earned = int(input("Points: "))
        points = points + earned
        print("Total so far:", points)
    if points >= 10:
        print("Goal reached")
    else:
        print("Keep going")


# If time: the loop ends when the guess is right; if / else inside the loop gives a hint
def guess_number():
    secret = 7
    tries = 1
    guess = int(input("Guess 1-10: "))
    while guess != secret:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
        tries = tries + 1
        guess = int(input("Guess 1-10: "))
    print("Correct in", tries, "tries")


# ask_age()
# valid_age()
locker()
# points_goal()
# guess_number()
