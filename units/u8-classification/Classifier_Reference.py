# Unit 8.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: normalize case before comparing, the same way classify_fruit's own source does.
def classify_fruit(color, shape, hardness):
    color = color.lower()
    shape = shape.lower()
    hardness = hardness.lower()

    if color == "yellow" and shape == "long":
        return "banana"
    elif color == "red" and shape == "round":
        return "apple"
    elif shape == "long" and hardness == "soft":
        return "banana"
    else:
        return "unknown"


# Task 1: a weather-based rule-based classifier
def classify_activity(temperature, raining, strong_wind):
    if raining or strong_wind:
        return "indoor"
    elif 18 <= temperature <= 30:
        return "outdoor"
    else:
        return "indoor"


def task1():
    # Edge cases (for discussion): a sunny but very humid day (humidity isn't a feature here);
    # light drizzle a runner may not mind (raining is treated as all-or-nothing).
    print(classify_activity(25, False, False))
    print(classify_activity(25, True, False))
    print(classify_activity(35, False, False))


# Task 2: trace, then confirm
def classify_level(score, attempts):
    if score >= 80 and attempts <= 3:
        return "advanced"
    elif score >= 50:
        return "intermediate"
    else:
        return "beginner"


def task2():
    for score, attempts in [(90, 2), (90, 6), (55, 8), (40, 1)]:
        print(classify_level(score, attempts))


print(classify_fruit("Yellow", "Long", "Soft"))
# task1()
# task2()
