# Warm-up: train and test share the image "img2" - this should be reported as a leak. Predict, run,
# then fix the check (hint: comparing two whole lists for equality is not the same as checking overlap).

def has_leak(train_ids, test_ids):
    return train_ids == test_ids


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))


# Task 1: write describe_trial(true_label, predicted, confidence) - returns one line of text:
# "<true_label> -> <predicted> (confidence <confidence>) - correct" or "... - WRONG" depending on
# whether predicted matches true_label. Test on ("fist", "fist", 0.91) and on ("ok", "fist", 0.55).


# Task 2: write count_correct(true_labels, predicted_labels) - how many positions match between
# the two lists (assume they're the same length). Test on
# true_labels     = ["fist", "ok", "fist", "ok", "ok"]
# predicted_labels = ["fist", "ok", "ok",   "ok", "ok"]
