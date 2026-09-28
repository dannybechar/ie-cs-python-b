# Unit 1.2 - reference solutions for the teacher.
# One function per task (define -> call, from Python A).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: total = score replaces the total; total = total + score adds to it
def sum_five():
    total = 0
    for day in range(1, 6):
        score = int(input("Score: "))
        total = total + score
    print("Total:", total)


# Task 1a: a negative step counts down; stop 0 is not included, so 1 is the last value
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Go!")


# Task 1b: start 2, step 2; stop 21 so that 20 is included
def evens():
    for n in range(2, 21, 2):
        print(n)


# Task 2: the counter changes only when the condition is True; the total changes every round
def trace_me():
    total = 0
    high = 0
    for i in range(3):
        score = int(input("Score: "))
        total = total + score
        if score >= 80:
            high = high + 1
    print("Total:", total, "High:", high)


# Task 3: set up the total and the counter before the loop, divide after it
def five_scores():
    total = 0
    above = 0
    for i in range(5):
        score = int(input("Score: "))
        total = total + score
        if score >= 80:
            above = above + 1
    average = total / 5
    print("Average:", average)
    print("Scores >= 80:", above)


# If time: % gives the remainder - 0 means "divides exactly"
def sevens():
    count = 0
    for n in range(1, 101):
        if n % 7 == 0:
            count = count + 1
    print("Numbers that divide by 7:", count)


# sum_five()
# countdown()
# evens()
# trace_me()
five_scores()
# sevens()
