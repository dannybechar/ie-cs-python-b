# Unit 3.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up: the body used "student", but the parameter is named "name"
def show_result(name, stars):
    print(name, "has", stars, "stars")


# Task 1: two parameters, three calls with different arguments
def show_mission(student, mission):
    print(student, "will complete", mission)


def task1():
    show_mission("Dana", "maze")
    show_mission("Omar", "quiz")
    show_mission("Noa", "debugging")


# Task 2: three parameters, in a fixed order
def show_card(student, level, points):
    print("Student:", student)
    print("Level:", level)
    print("Points:", points)


def task2():
    show_card("Maya", "easy", 10)
    show_card("Ali", "hard", 30)


# Task 3: same behavior as the three print lines, now with one function
def show_level(level, points):
    print("Level", level, "needs", points, "points")


def task3():
    show_level(1, 10)
    show_level(2, 20)
    show_level(3, 35)


show_result("Maya", 4)
# task1()
# task2()
# task3()
