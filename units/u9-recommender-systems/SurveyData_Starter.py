# Warm-up: a rating of 0 means "don't know this item" - not "didn't like it". Predict, run, then fix.

def describe_rating(value):
    if value == 0:
        return "not liked"
    elif value == 1:
        return "disliked"
    elif value == 2:
        return "neutral"
    elif value == 3:
        return "liked"


print(describe_rating(0))


# Task 1: write validate_ratings(row) - returns True if every value in the list row is one of
# 0, 1, 2, 3, otherwise False. Test on [3, 1, 0, 3] (valid) and on [3, 1, 5, 3] (invalid).


# Task 2: write count_known(ratings) - how many values in the list are NOT 0 (the user knows
# that many items). Test on [3, 1, 0, 3, 2].
