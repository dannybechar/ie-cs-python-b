# Unit 8.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: a share far below 50% is the sign of under-representation, not above it.
# Flag either category if it drifts too far from an even 50/50 split.
def check_balance(fist_count, ok_count):
    total = fist_count + ok_count
    fist_share = fist_count / total * 100
    if fist_share < 40 or fist_share > 60:
        print("Categories are not balanced - fist is", round(fist_share, 1), "%")
    else:
        print("Balanced enough")


# Task 1: a warning per under-filled category
def check_variety(labels, counts, minimum):
    warnings = 0
    for index in range(len(labels)):
        if counts[index] < minimum:
            print("Warning:", labels[index], "has only", counts[index], "images")
            warnings += 1
    if warnings == 0:
        print("Every category meets the minimum")


def task1():
    labels = ["bright background", "dark background", "side light", "new user"]
    counts = [40, 5, 15, 3]
    check_variety(labels, counts, 10)


# Task 2: checklist coverage, using "in" over a list - the same pattern as Unit 7's search
def count_covered(required, tested):
    count = 0
    for item in required:
        if item in tested:
            count += 1
    return count


def task2():
    required = ["background", "lighting", "user", "angle"]
    tested = ["lighting", "angle"]
    print(count_covered(required, tested))


check_balance(20, 80)
check_balance(48, 52)
# task1()
# task2()
