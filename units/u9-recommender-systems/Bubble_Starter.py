# Warm-up: out of these 5 recommendations, 3 are about "space" - the result should be 3, not 2.
# Predict, run, then fix the comparison.

def count_related(feed, topic):
    count = 0
    for card in feed:
        if card != topic:
            count += 1
    return count


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))


# Task 1: write simulate_feed_round(topic, other_topics, round_number) - a toy model of a feed with
# 5 cards. The user keeps watching "topic", so the feed gets more of it every round:
#   related = round_number + 1, but never more than 4 (one slot always stays for something else)
# The feed is a list of 5 topics: first `related` copies of topic, then the remaining slots filled
# from other_topics, one after the other (other_topics[0], other_topics[1], ... and back to the start).
# Test with other_topics = ["cooking", "sports", "art"]:
#   round 0 -> ["space", "cooking", "sports", "art", "cooking"]
#   round 2 -> ["space", "space", "space", "cooking", "sports"]
#   round 6 -> ["space", "space", "space", "space", "cooking"]


# Task 2: write run_bubble_experiment(topic, other_topics, rounds) - for every round build the feed,
# print "Round N - related: K of 5" and collect K. Return the list of all the K values.
# Test with rounds = 5: the list is [1, 2, 3, 4, 4].


# Task 3 (if time): write count_different(feed) - how many DIFFERENT topics are in the feed
# (hint: keep a list of the topics you have already seen). Print it for every round of Task 2:
# the variety of the feed goes down while the related count goes up.
# Test: count_different(["space", "space", "cooking", "space", "cooking"]) -> 2.
