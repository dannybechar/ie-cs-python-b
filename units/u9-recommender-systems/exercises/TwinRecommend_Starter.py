# Warm-up: find_twin compares the target with EVERYONE, including itself - a person always shares
# every answer with itself. Expected twin of user_04 (index 3): user_03 (index 2). Predict, run, fix.

item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
answers = ["XV0XX", "0VV0X", "V0XXV", "00XVV"]


def count_same(first, second):
    same = 0
    for index in range(len(first)):
        if first[index] == second[index] and first[index] != "0":
            same += 1
    return same


def find_twin(target_index):
    best_index = None
    best_score = 0
    for index in range(len(answers)):
        score = count_same(answers[target_index], answers[index])
        if score > best_score:
            best_score = score
            best_index = index
    return best_index


print(find_twin(3))


# Task 1: write recommend_item(target_answers, twin_answers) - return the NAME of the first item the
# twin liked ("V") and the target does not know ("0"). If there is no such item, return None.
# Test: recommend_item("00XVV", "V0XXV") -> "sushi".


# Task 2 (the project - the checkpoint): write main() that
#   1. takes the last participant as the target: target_index = len(aliases) - 1
#   2. finds the twin; if there is no twin print "No twin found." and stop (return)
#   3. prints the target alias, the twin alias and their number of points
#   4. prints the recommendation, or "Nothing new to recommend." if there is none.
# Expected for the sample data:
#   Target: user_04
#   Twin: user_03
#   Points: 2
#   Recommendation: sushi


# Task 3 (if time): write recommend_all(target_answers, twin_answers) - ONE string with every
# recommended item name, separated by ", " (an empty string if there is none).
