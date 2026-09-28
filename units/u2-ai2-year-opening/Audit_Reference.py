# Unit 2.2 - reference for the teacher.
# This code counts a dataset - it is not a machine-learning model.
# One function per task. Run ONE task at a time: remove the # from one call at the bottom.


# Warm-up: a group is under-represented when its share is SMALL - the comparison must be <
def kettle_audit():
    traditional = 45
    electric = 5
    total = traditional + electric
    electric_share = electric / total * 100
    print("Electric kettles:", electric_share, "%")
    if electric_share < 20:
        print("Under-represented")
    else:
        print("Balanced")


# Task 1: one share per group; a counter remembers whether any warning was printed
def car_data_audit():
    day = int(input("Day images: "))
    night = int(input("Night images: "))
    rain = int(input("Rain images: "))
    total = day + night + rain
    day_share = day / total * 100
    night_share = night / total * 100
    rain_share = rain / total * 100
    print("Day:", day_share, "%")
    print("Night:", night_share, "%")
    print("Rain:", rain_share, "%")
    warnings = 0
    if day_share < 20:
        print("Warning: day is under-represented")
        warnings = warnings + 1
    if night_share < 20:
        print("Warning: night is under-represented")
        warnings = warnings + 1
    if rain_share < 20:
        print("Warning: rain is under-represented")
        warnings = warnings + 1
    if warnings == 0:
        print("Every group is at least 20%")


# kettle_audit()
car_data_audit()
