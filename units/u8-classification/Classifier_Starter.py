# Warm-up: this should print "banana". Predict, run, then fix it (hint: check the letter case).

def classify_fruit(color, shape, hardness):
    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"


print(classify_fruit("Yellow", "Long", "Soft"))


# Task 1: write classify_activity(temperature, raining, strong_wind) - a rule-based classifier that
# returns "indoor" or "outdoor". Rain or strong wind means indoor; otherwise a temperature between
# 18 and 30 (inclusive) means outdoor, anything else indoor. Then find TWO edge cases where the
# classifier's decision feels wrong or incomplete, and name the missing feature each time.


# Task 2: trace classify_level(score, attempts) BEFORE running it, for each pair below, then check.
def classify_level(score, attempts):
    if score >= 80 and attempts <= 3:
        return "advanced"
    elif score >= 50:
        return "intermediate"
    else:
        return "beginner"


# (90, 2), (90, 6), (55, 8), (40, 1)
