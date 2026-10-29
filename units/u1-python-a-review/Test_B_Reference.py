# Unit 1 test, Form B (retest) - reference solutions for the teacher (not for students).
# Questions 1-3 are trace questions; the code is shown in the test itself.


def q1(temp, rain):
    if temp < 10:
        print("Cold")
    elif temp < 25 and rain == "yes":
        print("Umbrella")
    elif temp < 25:
        print("Nice")
    else:
        print("Hot")


def q2():
    total = 0
    count = 0
    for i in range(1, 14, 4):
        total = total + i
        if i > 8:
            count = count + 1
    print("Total:", total, "Count:", count)


def q3():
    x = 25
    steps = 0
    while x > 4:
        x = x - 7
        steps = steps + 1
    print(x, steps)


def q4_fixed():
    # the faults: stop 8 -> 9, step 2 removed, print("Done") moved out of the loop
    for n in range(1, 9):
        print(n)
    print("Done")


def q4b_fixed(height):
    if height >= 120 and height <= 190:
        print("Ride allowed")
    else:
        print("Ride not allowed")


# Question 5
def q5a():
    for i in range(4, 21, 4):
        print(i)


def q5b():
    for i in range(30, 9, -5):
        print(i)


# Question 6
def score_message():
    score = int(input("Score: "))
    if score < 0 or score > 100:
        print("Invalid")
    elif score < 55:
        print("Fail")
    elif score <= 84:
        print("Pass")
    else:
        print("Excellent")


# Question 7
def runs():
    total = 0
    long_runs = 0
    for i in range(5):
        km = int(input("Km: "))
        total = total + km
        if km >= 10:
            long_runs = long_runs + 1
    print("Average:", total / 5)
    print("Runs >= 10:", long_runs)


# Question 8
def reading():
    total = 0
    days = 0
    while total < 200 and days < 6:
        pages = int(input("Pages: "))
        total = total + pages
        days = days + 1
    if total >= 200:
        print("Finished after", days, "days")
    else:
        print("Not finished. Pages:", total)


if __name__ == "__main__":
    import builtins

    def run(fn, answers):
        it = iter(answers)
        builtins.input = lambda prompt="": str(next(it))
        print(f"--- {fn.__name__} {answers}")
        fn()

    for t, r in [(5, "no"), (20, "yes"), (20, "no"), (25, "yes"), (9, "yes"), (10, "yes"), (24, "no")]:
        print(t, r, end=" -> "); q1(t, r)
    q2(); q3(); q4_fixed()
    for h in (100, 119, 120, 190, 191, 150):
        print(h, end=" -> "); q4b_fixed(h)
    q5a(); q5b()
    for s in (-5, -1, 0, 54, 55, 84, 85, 100, 101):
        run(score_message, [s])
    run(runs, [5, 12, 10, 8, 15])
    run(runs, [1, 2, 3, 4, 5])
    run(reading, [120, 90])
    run(reading, [20, 20, 20, 20, 20, 20])
    run(reading, [80, 70, 60])
    run(reading, [200])
    run(reading, [30, 30, 30, 30, 30, 50])
