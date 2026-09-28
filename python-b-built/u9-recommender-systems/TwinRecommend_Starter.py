# Warm-up: this compares a user to itself, which will always look like a perfect match.
# Predict, run, then fix it (hint: skip the target's own index).

def similarity_score(first, second):
    matches = 0
    common = 0
    for index in range(len(first)):
        if first[index] != 0 and second[index] != 0:
            common += 1
            if first[index] == second[index]:
                matches += 1
    return matches, common


def find_digital_twin(target_index, all_ratings, minimum_common=2):
    best_index = None
    best_key = (-1.0, -1)

    for candidate_index in range(len(all_ratings)):
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


ratings = [
    [3, 1, 0, 3, 0],
    [3, 1, 3, 2, 3],
    [1, 3, 2, 1, 0],
    [3, 2, 2, 3, 0],
]
print(find_digital_twin(0, ratings))


# Task 1: write recommend_item(target_ratings, twin_ratings, item_names, liked_threshold=3) - finds
# the item the target rated 0 (doesn't know) where the twin's rating is >= liked_threshold and
# highest among such items; returns (item_name, twin_rating), or None if there is no such item.


# Task 2 (project - the checkpoint): write main() that: loads items/aliases/all_ratings from
# "ratings.csv" (Unit 9.2), finds target_index = 0's digital twin (minimum_common=2), and - if a
# twin was found - recommends an item and prints target alias, twin alias, similarity rate, shared
# ratings, and the recommendation (or a clear message if none was found). If no twin was found at
# all, print a clear message and stop.
