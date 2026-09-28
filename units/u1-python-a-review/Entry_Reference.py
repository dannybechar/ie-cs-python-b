# Unit 1.1 - reference solutions for the teacher.
# One function per task (define -> call, from Python A).
# Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: input() always returns text, so the age must be converted with int()
def ticket_price():
    age = int(input("Age: "))
    tickets = int(input("Tickets: "))
    if age < 12:
        price = 8
    else:
        price = 12
    print("Total:", tickets * price)


# Task 1: "yes" is text, so it needs quotes;
# the age must be 13 or more AND 15 or less - with or, every age passes
def fix_the_gate():
    age = int(input("Age: "))
    permission = input("Permission (yes/no): ")
    if age >= 13 and age <= 15:
        if permission == "yes":
            print("Access granted")


# Task 2: three cases, exactly one message - if / elif / else
def entry_check():
    age = int(input("Age: "))
    permission = input("Permission (yes/no): ")
    if age >= 13 and age <= 15 and permission == "yes":
        print("Access granted")
    elif age < 13 or age > 15:
        print("Age out of range")
    else:
        print("Permission required")


# Task 3: check the input first, then the levels from the top down
def score_level():
    score = int(input("Score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Good")
    else:
        print("Keep practicing")


# If time: not turns True into False
def club_open():
    day = int(input("Day (1-7): "))
    is_holiday = input("Holiday (yes/no): ") == "yes"
    if day >= 1 and day <= 5 and not is_holiday:
        print("The club is open")
    else:
        print("The club is closed")


# ticket_price()
# fix_the_gate()
entry_check()
# score_level()
# club_open()
