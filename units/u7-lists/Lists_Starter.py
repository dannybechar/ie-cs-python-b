# Warm-up: this should change the second score to 75. Predict, run, then fix one symbol.

scores = [60, 70, 80]
scores[1] == 75
print(scores)


# Task 1: write ai_report(scores) - prints: how many scores, the first score, the last score,
# and whether 100 is among them. Test on [81, 24, 67, 91].


# Task 2: write update_score(scores, index, new_value) - if index is a valid position in scores,
# update it and return True; otherwise print "Invalid index" and return False. Test on [60, 70, 80]
# with index 1 (valid) and with index 5 (invalid).


# Task 3: write slice_report(values) - prints, each on its own line with a label: the whole list,
# the first five items, the items from index 2 up to (not including) 5, every third item
# starting at index 2, and the list reversed. Test on [25, 20, 21, 24, 21, 24, 21, 16, 23].


# Task 4 (if time): write combine(first, second) - returns a NEW list with the items of both
# lists (use +); print the new list and its length, and show that first and second did not change.
# Then print list("cat") and explain what list() did.
