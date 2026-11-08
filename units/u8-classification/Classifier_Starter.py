# Warm-up: four paintings must be sorted into "classic" (before 1860) and "modern" (1860 and later).
# Predict how many paintings the two lists will hold, run, then find the bug and fix it.

def classify_paintings():
    years = [1889, 1519, 1860, 1893]
    paintings = ["Starry Night", "Mona Lisa", "The Urchin", "The Scream"]
    classic = []
    modern = []
    for i in range(len(paintings)):
        if years[i] < 1860:
            classic.append(paintings[i])
        elif years[i] > 1860:
            modern.append(paintings[i])
    print("classic:", classic)
    print("modern:", modern)


classify_paintings()


# Task 1: a playlist classifier. Songs released before the split year go to the "nostalgia" list,
# the others to the "hits" list. Use two parallel lists (songs, years), two empty lists and a loop.
# Run it with the split year 2015, then change the split year and run again.
# years = [2008, 2022, 2015, 1999, 2017, 2026]
# songs = ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F"]


# Task 2: classify the same songs by a different feature - song length in seconds
# (short: under 200 seconds, long: 200 or more). You need a new parallel list of lengths.
# lengths = [180, 240, 150, 310, 200, 199]


# Task 3 (on paper, no code): see the lab brief - choose two good features for apple vs banana.


# Task 4: write classify_fruit(softness, color). softness is 1 (hard) to 5 (soft), color is a string.
#   apple:  softness < 2 and the color is "red", "green" or "yellow"
#   banana: softness > 2 and the color is "yellow" or "green"
#   anything else: "unknown fruit"
# Call it three times and print the results for: (1, "green"), (4, "yellow"), (3, "purple").
# Then call it for an unripe banana: (1, "green"). Was the computer right? And what happens for (2, "yellow")?


# Task 5 (think, no code): a rule says "song speed above 120 = happy song, otherwise sad song".
# Write one song or style where this rule fails, and explain why a feature like "mood" is hard to define with if/else.
