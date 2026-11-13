# Lessons 21.1–21.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.

item_names = ["sushi", "beet", "dal", "pasta", "pizza"]
aliases = ["user_01", "user_02", "user_03", "user_04"]
answers = ["XV0XX", "0VV0X", "V0XXV", "00XVV"]


def count_same(first, second):
    same = 0
    for index in range(len(first)):
        if first[index] == second[index] and first[index] != "0":
            same += 1
    return same


# Warm-up, fixed: skip the target's own index (no continue: the class has not learned it), so nobody is their own twin.
# best_score starts at 0, so somebody with 0 points is never a twin; on a tie the first one stays.
def find_twin(target_index):
    best_index = None
    best_score = 0
    for index in range(len(answers)):
        if index != target_index:
            score = count_same(answers[target_index], answers[index])
            if score > best_score:
                best_score = score
                best_index = index
    return best_index


# Task 1: an item the twin liked and the target does not know
def recommend_item(target_answers, twin_answers):
    for index in range(len(target_answers)):
        if target_answers[index] == "0" and twin_answers[index] == "V":
            return item_names[index]
    return None


def task1():
    print(recommend_item("00XVV", "V0XXV"))
    print(recommend_item("V0XXV", "V0XXV"))


# Task 2 (the project - the checkpoint)
def main():
    target_index = len(aliases) - 1
    twin_index = find_twin(target_index)
    if twin_index is None:
        print("No twin found.")
        return
    print("Target:", aliases[target_index])
    print("Twin:", aliases[twin_index])
    print("Points:", count_same(answers[target_index], answers[twin_index]))
    recommendation = recommend_item(answers[target_index], answers[twin_index])
    if recommendation is None:
        print("Nothing new to recommend.")
    else:
        print("Recommendation:", recommendation)


# Task 3 (if time): every recommended item in one string
def recommend_all(target_answers, twin_answers):
    result = ""
    for index in range(len(target_answers)):
        if target_answers[index] == "0" and twin_answers[index] == "V":
            if result != "":
                result += ", "
            result += item_names[index]
    return result


def task3():
    print(recommend_all("0000X", "VV0VX"))
    print(recommend_all("V0XXV", "V0XXV") == "")


# The edge cases of the lab (teacher check). They replace the global lists, so run them last.
def run_edge_cases():
    global answers, aliases
    # 1. nobody shares an answer -> no twin
    answers = ["0000V", "XXXX0", "00000"]
    aliases = ["a", "b", "c"]
    print("no twin:", find_twin(2), find_twin(0))
    # 2. the twin has nothing new to offer
    print("nothing new:", recommend_item("V0XXV", "V0XXV"))
    # 3. the target already knows everything
    print("knows all:", recommend_item("VXVXV", "VXXXV"))
    # 4. a tie -> the first one stays
    answers = ["VVXXX", "VVXXX", "VV000"]
    aliases = ["a", "b", "c"]
    print("tie:", find_twin(2))
    # 5. a shared "0" is not a point
    print("zero is no point:", count_same("0V", "0X"))


print(find_twin(3))
# task1()
# main()
# task3()
# run_edge_cases()
