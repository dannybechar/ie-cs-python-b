# Unit 7.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: == compares (and throws the result away); = assigns
def warmup():
    scores = [60, 70, 80]
    scores[1] = 75
    print(scores)


# Task 1: length, first, last, membership
def ai_report(scores):
    print("Number of tests:", len(scores))
    print("First score:", scores[0])
    print("Last score:", scores[-1])
    print("Contains perfect score:", 100 in scores)


# Task 2: bounds-checked update
def update_score(scores, index, new_value):
    if 0 <= index < len(scores):
        scores[index] = new_value
        return True
    print("Invalid index")
    return False


def task2():
    scores = [60, 70, 80]
    print(update_score(scores, 1, 75), scores)
    print(update_score(scores, 5, 99), scores)


warmup()
# ai_report([81, 24, 67, 91])
# task2()
