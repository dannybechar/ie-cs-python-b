# Warm-up: this counts a shared "0" (both people don't know the item) as a point. It should not.
# The expected answer for the test below is 2. Predict, run, then fix it.

def count_same(first, second):
    same = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            same += 1
    return same


print(count_same("00XVV", "V0XXV"))


# The survey data (Task 4 shows how the lists are made from the Forms file).
item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
answers = ["XV0XX", "0VV0X", "V0XXV", "00XVV"]


# Task 1: write show_comparison(first, second) - for every item print its name, the two answers and
# the word "point" (if it is a point) or "-" (if not). Test: show_comparison("00XVV", "V0XXV") prints
#   sushi 0 V -
#   beet 0 0 -
#   dal X X point
#   pasta V X -
#   pizza V V point


# Task 2: write print_scores(target_index) - for every participant EXCEPT the target print the alias
# and the number of points shared with the target. Test: print_scores(3) prints
#   user_01 0
#   user_02 0
#   user_03 2


# Task 3: write best_score(target_index) - the highest number of points between the target and
# any other participant. Test: best_score(3) -> 2.


# Task 4 (if time): the teacher runs CsvToLists_Teacher.py on the class survey and gives you three
# lines (item_names, aliases, answers). Paste them above, replace the sample data, and run Task 2.
