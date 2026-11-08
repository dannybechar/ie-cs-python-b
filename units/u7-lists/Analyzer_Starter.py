# Warm-up: 81 IS in the list, at index 0. Predict, run, then fix the way the result is checked.

def linear_search(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


scores = [81, 24, 67, 91]
if linear_search(scores, 81):
    print("Found")
else:
    print("Not found")


# Task 1: write linear_search_sorted(values, target) - like linear_search, but stops early:
# on a SORTED list, once values[index] is no longer less than target, there is no point
# continuing. Test on [10, 20, 35, 50, 80] with target 35 (present) and target 40 (absent).
# Then run [10, 20, 35, 50, 80].index(35) and [10, 20, 35, 50, 80].index(40) - what is the
# difference between the built-in index() and your search when the value is missing?


# Task 2: "A new phone number" - a phone company gives every new customer a number.
# prefixes = ["050", "052", "053", "054"]; a number looks like "052-8819853"
# (the prefix, a dash, and 7 random digits: random.choice for the prefix, random.randint for
# the digits, str() to turn them into text).
# a) write random_number(prefixes) - returns one random number.
# b) write is_special(number, special) - True when number is in the special list, or when the digit
#    "5" appears more than once in its 7 digits, or when its 7 digits are a rising or falling run
#    (hint: "1234567" in "0123456789"). Special numbers are not given to customers.
# c) write new_phone_number(taken, special) - returns a number that is not in taken and not special.
# d) build a list of 10 different numbers with a loop, and print it.


# Task 3 (project - "AI Experiment Analyzer"): a program that reads similarity scores from
# input() until -1 is entered (the sentinel - not stored), keeping only scores from 0 to 100;
# then prints the original list, a sorted COPY of it, the average, minimum and maximum; then
# reads a threshold and prints how many scores are at or above it; then reads a target score and
# prints its position in the sorted list (using linear_search_sorted).
# Every part is a small function that you tested alone first.
