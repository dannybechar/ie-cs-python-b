# Warm-up: out of these 5 recommendations, 3 are about "space" - the result should be 3, not 2.
# Predict, run, then fix the comparison.

def count_related(recommendations, topic):
    count = 0
    for rec in recommendations:
        if rec != topic:
            count += 1
    return count


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))


# Task 1: write simulate_feed_round(current_topic, other_topics, round_number) - models the card
# rule from the lesson: returns a list of 3 recommendations - TWO copies of current_topic, and ONE
# "other" topic picked deterministically as other_topics[round_number % len(other_topics)].
# Test with current_topic="space", other_topics=["cooking", "sports", "art"], round_number=0, then 1.


# Task 2: write run_bubble_experiment(start_topic, other_topics, rounds) - for round_number in
# range(rounds): build that round's recommendations with simulate_feed_round, print the round
# number and count_related(recommendations, start_topic), and return a list of all those counts.
# Test with start_topic="space", other_topics=["cooking", "sports", "art"], rounds=5, and check
# that the related-count stays high (never below 2 out of 3) every round.
