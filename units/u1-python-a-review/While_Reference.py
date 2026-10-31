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


# Task 1: read first (before the loop), ask again inside; invalid = below 100 OR above 999
def three_digit():
    num = int(input("Enter number: "))
    while num < 100 or num > 999:
        num = int(input("Enter number: "))
    print("End loop")


# Task 2: count is the loop variable - it counts the EVEN numbers, not the numbers typed
def three_evens():
    count = 0
    while count < 3:
        n = int(input("Enter number: "))
        if n % 2 == 0:
            count = count + 1
    print("End loop")


# Task 3: counting forward (score) and backward (timer)
def score_and_timer():
    score = 0
    while score <= 10:
        print("Score:", score)
        score += 1
    timer = 10
    while timer > 0:
        print("Timer:", timer)
        timer -= 1
    print("Time is up!")


# Task 4: each loop was missing something from the checklist
def loop_a():
    count = 0
    while count < 3:
        n = int(input("Enter number: "))
        count += 1  # fix: update the variable the condition checks


def loop_b():
    n = 0
    while n < 10:
        print(n)
        n += 1  # fix: there was no update at all
    print("End loop")


def loop_c():
    n = 0
    while n < 10:
        print(n)
        n += 1  # fix: n - 1 moved AWAY from 10
    print("End loop")


def loop_d():
    n = 0
    while n < 10:  # fix: n > -1 is always True when n only grows
        print(n)
        n += 1
    print("End loop")


# Task 5: start value, condition (the stop value is never included), update
def for_to_while():
    i = 0
    while i < 5:
        print(i)
        i += 1


# compare_loops(): A, B and C all print 0 2 4 6 8 and Done!
def compare_loops():
    print("A")
    n = 0
    while n < 10:
        print(n)
        n += 2
    print("Done!")
    print("B")
    for item in range(10):
        if item % 2 == 0:
            print(item)
    print("Done!")
    print("C")
    for item in range(0, 10, 2):
        print(item)
    print("Done!")


# Task 6: go on while there are tries left AND the code is not found yet
def locker():
    secret = 4321
    attempts = 0
    success = False
    while attempts < 3 and not success:
        guess = int(input("Code: "))
        attempts += 1
        if guess == secret:
            success = True
    if success:
        print("Access granted. Attempts:", attempts)
    else:
        print("Access blocked")


# Task 7: the "exciting number" exam task (Python A exam). Works for positive whole numbers.
def exciting_number():
    num = int(input("Enter a positive number: "))
    total = 0
    digits = 0
    while num > 0:
        digit = num % 10
        total += digit
        digits += 1
        num = num // 10
    if total >= 3 * digits:
        print("Exciting number")
    else:
        print("Not an exciting number")


# Task 8 (checkpoint): the stop condition is on the SUM, so we do not know the number of terms in advance
def cubes_sum():
    i = 1
    total = 0
    while total < 100:
        total += i * i * i
        print("Sum so far:", total)
        i += 1
    print("Stopped at", total, "after", i - 1, "terms")


# If time: the "yes" answer is the sentinel that keeps the loop going
def count_red():
    red = 0
    ans = "yes"
    while ans == "yes":
        color = input("Please enter a color: ")
        if color == "red":
            red += 1
        ans = input("Do you want to continue? yes/no ")
    print("The number of red beads is:", red)


# If time: 2, 22, 222, ... - the next term is the previous one times 10 plus 2
def twos():
    term = 2
    while term < 10000:
        print(term)
        term = term * 10 + 2


# ask_age()
# three_digit()
# three_evens()
# score_and_timer()
# loop_a()
# loop_b()
# loop_c()
# loop_d()
# for_to_while()
# compare_loops()
# locker()
# exciting_number()
# cubes_sum()
# count_red()
# twos()
