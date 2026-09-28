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


# Task 1: write check_variety(labels, counts, minimum) - for each category, if its count is below
# minimum, print a warning naming it; count how many warnings were printed; if there were none,
# print "Every category meets the minimum". Test on:
# labels = ["bright background", "dark background", "side light", "new user"]
# counts = [40, 5, 15, 3]
# minimum = 10


# Task 2: write count_covered(required, tested) - how many items of required also appear in
# tested (a simple checklist-coverage count). Test on
# required = ["background", "lighting", "user", "angle"]
# tested   = ["lighting", "angle"]
