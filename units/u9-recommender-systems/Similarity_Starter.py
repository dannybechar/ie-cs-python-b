# Warm-up: this counts a shared "don't know" (0 and 0) as a match, which it should not be.
# Predict, run, then fix it.

def broken_similarity(first, second):
    matches = 0
    for index in range(len(first)):
        if first[index] == second[index]:
            matches += 1
    return matches


print(broken_similarity([0, 1, 3], [0, 1, 2]))


# Task 1: complete load_ratings(filename) - reads a CSV file shaped like ratings.csv (a header row
# "alias,item1,item2,..." then one row per user) and returns (item_names, aliases, ratings): the
# item names from the header, a list of aliases, and a list of rating lists (each value an int).
import csv


def load_ratings(filename):
    aliases = []
    ratings = []
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        item_names = header[1:]
        for row in reader:
            if not row:
                continue
            # complete: append the alias and the row's ratings (as integers) to the right lists
    return item_names, aliases, ratings


# Task 2: write similarity_score(first, second) - returns (matches, common): common counts
# positions where NEITHER rating is 0; matches counts, among those, how many are equal.
# Test: similarity_score([3, 1, 0, 3, 2], [3, 1, 3, 2, 2]) should be (3, 4).


# Task 3: write similarity_rate(first, second) - matches / common from similarity_score, or 0.0
# if common is 0. Test: similarity_rate([3, 1, 0], [3, 1, 2]) should be 1.0.
