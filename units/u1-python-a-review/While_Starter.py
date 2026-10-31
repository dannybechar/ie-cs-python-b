# Warm-up: run it and type -2. Why does it never stop? Stop it (red Stop button), then add one line.


def ask_age():
    age = int(input("Age: "))
    while age < 0:
        print("Invalid age")
    print("Accepted:", age)


# Task 1: write three_digit() - ask for a whole number again and again until it has exactly 3 digits (100-999). Then print End loop.


# Task 2: write three_evens() - read whole numbers until 3 EVEN numbers were typed. Keep a counter. Then print End loop.


# Task 3: write score_and_timer() - first count the score 0, 1, ... 10, then a timer 10, 9, ... 1 and Time is up!


# Task 4: four loops that never end. Do NOT run them yet: predict what each one does, then run ONE, stop it (red Stop button) and fix it.
# Check: 1. start value  2. condition can become False  3. update inside the loop  4. update goes the right way
def loop_a():
    count = 0
    while count < 3:
        n = int(input("Enter number: "))


def loop_b():
    n = 0
    while n < 10:
        print(n)
    print("End loop")


def loop_c():
    n = 0
    while n < 10:
        print(n)
        n = n - 1
    print("End loop")


def loop_d():
    n = 0
    while n > -1:
        print(n)
        n = n + 1
    print("End loop")


# Task 5: write for_to_while() - the same output as: for i in range(0, 5, 1): print(i)  - but with while.
# Then run compare_loops() and check your table.
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


# Task 6: write locker() - up to 3 tries to type the code 4321, then Access granted or Access blocked.


# Task 7 (together): exciting_number() - trace first, then run.
# An exciting number: the sum of its digits is at least 3 times the number of its digits.
# Plan: while num > 0 -> take the last digit (num % 10), add it to total, count it, cut it off (num // 10).


# Task 8 (unit checkpoint, alone): write cubes_sum() - add 1 + 8 + 27 + ... (the cubes) while the sum is below 100.


# If time: count_red() (beads, ask "yes"/"no" to continue) and twos() (2, 22, 222, 2222 ... while the number is below 10000).


ask_age()
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
