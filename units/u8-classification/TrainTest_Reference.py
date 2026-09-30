# Unit 8.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: check whether any single test id also appears in train - not whether the two
# whole lists are identical.
def has_leak(train_ids, test_ids):
    for test_id in test_ids:
        if test_id in train_ids:
            return True
    return False


# Task 1: one readable line per trial
def describe_trial(true_label, predicted, confidence):
    if predicted == true_label:
        result = "correct"
    else:
        result = "WRONG"
    return true_label + " -> " + predicted + " (confidence " + str(confidence) + ") - " + result


def task1():
    print(describe_trial("fist", "fist", 0.91))
    print(describe_trial("ok", "fist", 0.55))


# Task 2: count matching positions
def count_correct(true_labels, predicted_labels):
    correct = 0
    for index in range(len(true_labels)):
        if true_labels[index] == predicted_labels[index]:
            correct += 1
    return correct


def task2():
    true_labels = ["fist", "ok", "fist", "ok", "ok"]
    predicted_labels = ["fist", "ok", "ok", "ok", "ok"]
    print(count_correct(true_labels, predicted_labels))


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))
test_ids_clean = ["img7", "img9"]
print(has_leak(train_ids, test_ids_clean))
# task1()
# task2()
