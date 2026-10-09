# Unit 1 test - reference solutions for the teacher (not for students).
# Questions 1-3 are trace questions; the code is shown in the test itself.


def q1(age, member):
    if age < 10:
        print("Child")
    elif age < 18 and member == "yes":
        print("Teen member")
    elif age < 18:
        print("Teen")
    else:
        print("Adult")


def q2():
    total = 0
    count = 0
    for i in range(2, 12, 3):
        total = total + i
        if i > 6:
            count = count + 1
    print("Total:", total, "Big:", count)


def q3():
    x = 20
    steps = 0
    while x > 3:
        x = x - 6
        steps = steps + 1
    print(x, steps)


def q4_fixed():
    n = 1
    while n <= 5:
        print(n)
        n = n + 1
    print("Done")


# Question 6
def ticket():
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    elif age < 6:
        print("Free")
    elif age <= 17:
        print("Student: 20")
    else:
        print("Regular: 40")


# Question 7
def grades():
    total = 0
    excellent = 0
    for i in range(6):
        grade = int(input("Grade: "))
        total = total + grade
        if grade >= 90:
            excellent = excellent + 1
    print("Average:", total / 6)
    print("Grades >= 90:", excellent)


# Question 8
def savings():
    total = 0
    deposits = 0
    while total < 100 and deposits < 5:
        amount = int(input("Deposit: "))
        total = total + amount
        deposits = deposits + 1
    if total >= 100:
        print("Goal reached after", deposits, "deposits")
    else:
        print("Goal not reached. Total:", total)
