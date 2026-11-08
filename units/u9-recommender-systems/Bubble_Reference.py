# Unit 9.4 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.
# The model is a TOY: the numbers (+1 related card per round, at most 4 of 5) are our own choice,
# not the real rule of any platform. It shows the direction of the effect, nothing more.


# Warm-up, fixed: count the cards that ARE the topic (==), not the ones that are not (!=).
def count_related(feed, topic):
    count = 0
    for card in feed:
        if card == topic:
            count += 1
    return count


# Task 1: one round of the toy feed (5 cards): more and more cards of the watched topic
def simulate_feed_round(topic, other_topics, round_number):
    related = round_number + 1
    if related > 4:
        related = 4
    feed = []
    for slot in range(5):
        if slot < related:
            feed.append(topic)
        else:
            feed.append(other_topics[(slot - related) % len(other_topics)])
    return feed


def task1():
    other_topics = ["cooking", "sports", "art"]
    print(simulate_feed_round("space", other_topics, 0))
    print(simulate_feed_round("space", other_topics, 2))
    print(simulate_feed_round("space", other_topics, 6))


# Task 2: repeat the round and follow how "related" the feed gets
def run_bubble_experiment(topic, other_topics, rounds):
    related_counts = []
    for round_number in range(rounds):
        feed = simulate_feed_round(topic, other_topics, round_number)
        related = count_related(feed, topic)
        print("Round", round_number, "- related:", related, "of", len(feed))
        related_counts.append(related)
    return related_counts


def task2():
    print(run_bubble_experiment("space", ["cooking", "sports", "art"], 5))


# Task 3 (if time): how many different topics are left in the feed?
def count_different(feed):
    seen = []
    for card in feed:
        if card not in seen:
            seen.append(card)
    return len(seen)


def task3():
    other_topics = ["cooking", "sports", "art"]
    print(count_different(["space", "space", "cooking", "space", "cooking"]))
    for round_number in range(5):
        feed = simulate_feed_round("space", other_topics, round_number)
        print("Round", round_number, "- different topics:", count_different(feed))


print(count_related(["space", "space", "cooking", "space", "sports"], "space"))
# task1()
# task2()
# task3()
