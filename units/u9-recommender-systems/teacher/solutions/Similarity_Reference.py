# Lesson 21.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: a point needs the SAME answer AND an answer that is not "0".
# ("0" and "0" is not a shared opinion - nobody knows the item.)
def count_same(first, second):
    same = 0
    for index in range(len(first)):
        if first[index] == second[index] and first[index] != "0":
            same += 1
    return same


# The survey data = the Ministry's example table (ratings.csv): sushi, beet, dal, pasta, pizza.
item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
answers = ["XV0XX", "0VV0X", "V0XXV", "00XVV"]


# Task 1: the trace table, printed
def show_comparison(first, second):
    for index in range(len(first)):
        if first[index] == second[index] and first[index] != "0":
            mark = "point"
        else:
            mark = "-"
        print(item_names[index], first[index], second[index], mark)


def task1():
    show_comparison("00XVV", "V0XXV")


# Task 2: the points of the target with everybody else
def print_scores(target_index):
    for index in range(len(answers)):
        if index != target_index:
            print(aliases[index], count_same(answers[target_index], answers[index]))


def task2():
    print_scores(3)


# Task 3: the maximum pattern - keep the highest score seen so far
def best_score(target_index):
    best = 0
    for index in range(len(answers)):
        if index != target_index:
            score = count_same(answers[target_index], answers[index])
            if score > best:
                best = score
    return best


def task3():
    print(best_score(3))
    print(best_score(0))


print(count_same("00XVV", "V0XXV"))
# task1()
# task2()
# task3()
