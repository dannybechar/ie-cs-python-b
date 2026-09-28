# Unit 9.2 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.

import csv


# Warm-up, fixed: 0 means "don't know" - it must never count as a shared preference.
# Skip any position where either rating is 0.
def fixed_similarity(first, second):
    matches = 0
    for index in range(len(first)):
        if first[index] != 0 and second[index] != 0 and first[index] == second[index]:
            matches += 1
    return matches


# Task 1: read a ratings CSV into three parallel structures
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
            aliases.append(row[0])
            ratings.append([int(value) for value in row[1:]])
    return item_names, aliases, ratings


def task1():
    items, users, all_ratings = load_ratings("ratings.csv")
    print(items)
    print(users)
    print(all_ratings)


# Task 2: matches AND common, in one pass
def similarity_score(first, second):
    if len(first) != len(second):
        raise ValueError("Rating lists must have the same length")

    matches = 0
    common = 0

    for index in range(len(first)):
        if first[index] != 0 and second[index] != 0:
            common += 1
            if first[index] == second[index]:
                matches += 1

    return matches, common


def task2():
    print(similarity_score([3, 1, 0, 3, 2], [3, 1, 3, 2, 2]))
    assert similarity_score([3, 1], [3, 1]) == (2, 2)
    assert similarity_score([0, 1], [0, 1]) == (1, 1)
    assert similarity_score([0, 0], [3, 2]) == (0, 0)
    assert similarity_score([3, 1], [1, 3]) == (0, 2)
    print("all asserts passed")


# Task 3: a rate, guarded against division by zero
def similarity_rate(first, second):
    matches, common = similarity_score(first, second)
    if common == 0:
        return 0.0
    return matches / common


def task3():
    print(similarity_rate([3, 1, 0], [3, 1, 2]))
    maya = [3, 0, 2, 1, 3, 0]
    ron = [3, 2, 2, 0, 1, 3]
    print(similarity_score(maya, ron))
    print(round(similarity_rate(maya, ron), 2))


print(fixed_similarity([0, 1, 3], [0, 1, 2]))
# task1()
# task2()
# task3()
