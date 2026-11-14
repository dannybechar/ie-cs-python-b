# Warm-up: train and test share the image "img2" - this must be reported as a leak (True).
# Predict, run, then fix the check (hint: comparing two whole lists for equality is not the same as
# checking whether any single item appears in both).

def has_leak(train_ids, test_ids):
    return train_ids == test_ids


train_ids = ["img1", "img2", "img3"]
test_ids = ["img2", "img9"]
print(has_leak(train_ids, test_ids))


# Task 1: write describe_trial(true_label, predicted, confidence) - it RETURNS one line of text:
# "<true_label> -> <predicted> (confidence <confidence>) - correct"   or   "... - WRONG"
# depending on whether predicted matches true_label. Test it on ("fist", "fist", 0.91) and on
# ("ok", "fist", 0.55). Then use it on two real trials from your Teachable Machine experiment
# (confidence is a fraction here: 91% is written 0.91).


# Task 2: write count_correct(true_labels, predicted_labels) - how many positions match between the
# two lists (assume they are the same length). Test it on
# true_labels      = ["fist", "ok", "fist", "ok", "ok"]
# predicted_labels = ["fist", "ok", "ok",   "ok", "ok"]


# If time (homework): write best_label(labels, scores) - it returns the label with the highest score.
# Test it on labels = ["fist", "ok"], scores = [0.62, 0.38], and think: what does the model say about
# a picture of a peace sign, a hand that belongs to neither category?
