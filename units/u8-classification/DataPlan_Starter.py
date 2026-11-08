# Warm-up: 20 fist images out of 100 total should clearly be flagged as under-represented.
# Predict, run, then fix the condition.

def check_balance(fist_count, ok_count):
    total = fist_count + ok_count
    fist_share = fist_count / total * 100
    if fist_share > 50:
        print("fist is under-represented")
    else:
        print("Balanced enough")


check_balance(20, 80)


# Task 1: write calculate_accuracy(successes, attempts) - it RETURNS the accuracy as a percent:
# successes divided by attempts, times 100. If attempts is 0, return 0.
# Test it on the lesson example: 2 successes out of 4 attempts (expected 50.0), and on 6 out of 7.
# Then use it for your own model: how many of the 7 test images did it classify correctly?


# Task 2: write check_variety(labels, counts, minimum) - for each factor, if its count is below
# minimum, print a warning naming it; count how many warnings were printed; if there were none,
# print "Every factor meets the minimum". Test on:
# labels = ["bright background", "dark background", "side light", "new user"]
# counts = [40, 5, 15, 3]
# minimum = 10


# If time: write count_covered(required, tested) - how many items of required also appear in
# tested (a simple checklist-coverage count for your bias experiments). Test on
# required = ["background", "lighting", "user", "angle"]
# tested   = ["lighting", "angle"]
