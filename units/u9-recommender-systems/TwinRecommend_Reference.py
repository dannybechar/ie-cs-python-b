# Unit 9.3 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.

import csv


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


# Warm-up, fixed: skip the target's own index with continue, so a user is never its own twin.
def find_digital_twin(target_index, all_ratings, minimum_common=2):
    best_index = None
    best_key = (-1.0, -1)

    for candidate_index in range(len(all_ratings)):
        if candidate_index == target_index:
            continue

        matches, common = similarity_score(
            all_ratings[target_index],
            all_ratings[candidate_index]
        )
        if common < minimum_common:
            continue

        rate = matches / common
        candidate_key = (rate, common)
        if candidate_key > best_key:
            best_key = candidate_key
            best_index = candidate_index

    return best_index, best_key


# Task 1: recommend the twin's best-loved item the target doesn't know
def recommend_item(target_ratings, twin_ratings, item_names, liked_threshold=3):
    best_item_index = None
    best_rating = -1

    for index in range(len(item_names)):
        target_does_not_know = target_ratings[index] == 0
        twin_likes_item = twin_ratings[index] >= liked_threshold

        if target_does_not_know and twin_likes_item:
            if twin_ratings[index] > best_rating:
                best_rating = twin_ratings[index]
                best_item_index = index

    if best_item_index is None:
        return None
    return item_names[best_item_index], best_rating


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


# Task 2 (project - the checkpoint)
def main():
    item_names, aliases, all_ratings = load_ratings("ratings.csv")

    target_index = 0
    twin_index, twin_score = find_digital_twin(target_index, all_ratings, minimum_common=2)

    if twin_index is None:
        print("Not enough shared ratings to find a digital twin.")
        return

    recommendation = recommend_item(
        all_ratings[target_index],
        all_ratings[twin_index],
        item_names
    )

    print("Target:", aliases[target_index])
    print("Digital twin:", aliases[twin_index])
    print("Similarity rate:", round(twin_score[0], 2))
    print("Shared ratings:", twin_score[1])

    if recommendation is None:
        print("No suitable recommendation was found.")
    else:
        item_name, twin_rating = recommendation
        print("Recommended item:", item_name)
        print("Twin rating:", twin_rating)


ratings = [
    [3, 1, 0, 3, 0],
    [3, 1, 3, 2, 3],
    [1, 3, 2, 1, 0],
    [3, 2, 2, 3, 0],
]
print(find_digital_twin(0, ratings))
# main()
