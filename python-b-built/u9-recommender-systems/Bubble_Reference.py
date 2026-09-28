# Unit 9.4 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: count matches (==), not mismatches (!=).
def count_related(recommendations, topic):
    count = 0
    for rec in recommendations:
        if rec == topic:
            count += 1
    return count


# Task 1: one round of the card rule - 2 copies of the current topic, 1 "other" (deterministic,
# not random, so the simulation is reproducible)
def simulate_feed_round(current_topic, other_topics, round_number):
    other = other_topics[round_number % len(other_topics)]
    return [current_topic, current_topic, other]


def task1():
    print(simulate_feed_round("space", ["cooking", "sports", "art"], 0))
    print(simulate_feed_round("space", ["cooking", "sports", "art"], 1))


# Task 2: repeat the round, tracking how "related" the feed stays
def run_bubble_experiment(start_topic, other_topics, rounds):
    related_counts = []
    for round_number in range(rounds):
        recommendations = simulate_feed_round(start_topic, other_topics, round_number)
        related = count_related(recommendations, start_topic)
        print("Round", round_number, "- related:", related, "of", len(recommendations))
        related_counts.append(related)
    return related_counts


def task2():
    counts = run_bubble_experiment("space", ["cooking", "sports", "art"], 5)
    print(counts)
    print("Every round at least 2 of 3 related:", all(c >= 2 for c in counts))


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))
# task1()
# task2()
