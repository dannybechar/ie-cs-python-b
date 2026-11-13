# Lessons 16.0–16.2 - reference for the teacher.
# One task per function; run ONE task at a time by removing the # from its call at the bottom.
# Everything here is plain rule-based code: no AI, no model - a person wrote every rule.


# Warm-up, fixed: the year 1860 itself matched neither "< 1860" nor "> 1860", so "The Urchin" was lost.
# Either ">= 1860" or a plain "else" closes the gap.
def classify_paintings():
    years = [1889, 1519, 1860, 1893]
    paintings = ["Starry Night", "Mona Lisa", "The Urchin", "The Scream"]
    classic = []
    modern = []
    for i in range(len(paintings)):
        if years[i] < 1860:
            classic.append(paintings[i])
        else:
            modern.append(paintings[i])
    print("classic:", classic)
    print("modern:", modern)


# Task 1: a playlist classifier, one feature (the year)
def task1_songs(split_year):
    years = [2008, 2022, 2015, 1999, 2017, 2026]
    songs = ["Halo", "As It Was", "Shape of You", "All Star", "Believer", "Michelle"]
    nostalgia = []
    hits = []
    for i in range(len(songs)):
        if years[i] < split_year:
            nostalgia.append(songs[i])
        else:
            hits.append(songs[i])
    print("nostalgia:", nostalgia)
    print("hits:", hits)


# Task 2: another feature, the same pattern
def task2_length():
    lengths = [180, 240, 150, 310, 200, 199]
    songs = ["Halo", "As It Was", "Shape of You", "All Star", "Believer", "Michelle"]
    short_songs = []
    long_songs = []
    for i in range(len(songs)):
        if lengths[i] < 200:
            short_songs.append(songs[i])
        else:
            long_songs.append(songs[i])
    print("short:", short_songs)
    print("long:", long_songs)


# Task 3 (paper): good features = relevant AND distinguishing.
#   color: good but not enough alone; softness: useful (but a rotten apple is soft, an unripe banana is hard);
#   country of origin, purchase date, price per kilo: NOT good - both fruits share them, or they describe the
#   shop and not the fruit.


# Task 4: the Ministry's classify_fruit (deck 16.1, solution 16.2.0)
def classify_fruit(softness, color):
    if softness < 2 and color in ["red", "green", "yellow"]:
        return "apple"
    elif softness > 2 and color in ["yellow", "green"]:
        return "banana"
    else:
        return "unknown fruit"


def task4_fruit():
    print(classify_fruit(1, "green"))     # apple
    print(classify_fruit(4, "yellow"))    # banana
    print(classify_fruit(3, "purple"))    # unknown fruit
    # Edge cases: an unripe banana is hard and green - the rule says apple (wrong).
    print(classify_fruit(1, "green"))     # apple, but it is an unripe banana
    # Softness exactly 2 matches neither "< 2" nor "> 2": the same kind of gap as the Louvre bug.
    print(classify_fruit(2, "yellow"))    # unknown fruit


# Task 5 (think): "speed > 120 = happy" fails for a fast rock song with sad words, or a slow, happy lullaby.
# A year is one dry number; a mood is many things at once (scale, words, instruments, tempo).


# If time, the Ministry's "advanced features" (worksheet 16.2): classify vehicles, animals or geometric shapes by features.
# One sample answer (a vehicle classifier with parallel lists; any similar student program is fine):
def task_if_time_vehicles():
    names = ["bicycle", "car", "motorcycle", "scooter", "bus"]
    wheels = [2, 4, 2, 2, 6]
    engine = [False, True, True, True, True]
    pedal_powered = []
    motor_two_wheels = []
    motor_other = []
    for i in range(len(names)):
        if not engine[i]:
            pedal_powered.append(names[i])
        elif wheels[i] == 2:
            motor_two_wheels.append(names[i])
        else:
            motor_other.append(names[i])
    print("no engine:", pedal_powered)
    print("engine, two wheels:", motor_two_wheels)
    print("engine, other:", motor_other)
    # Edge cases: a three-wheeled tuk-tuk goes to "other"; an electric bicycle has an engine AND pedals.


# Also if time: a weather classifier (our own addition, not in the Ministry worksheet). Rain or strong wind: indoor; otherwise 18 to 30 degrees: outdoor, else indoor.
def classify_activity(temperature, raining, strong_wind):
    if raining or strong_wind:
        return "indoor"
    elif 18 <= temperature <= 30:
        return "outdoor"
    else:
        return "indoor"


def task_if_time():
    print(classify_activity(25, False, False))   # outdoor
    print(classify_activity(25, True, False))    # indoor
    print(classify_activity(35, False, False))   # indoor
    # Edge cases: a humid day (humidity is not a feature); light drizzle (raining is all-or-nothing).


# ---- Teacher demos for the first 45 minutes (not student tasks) ----

# Demo A (deck 16.1, "Artistic classification"): the Louvre task with NO painting from exactly 1860.
def demo_louvre():
    years = [1889, 1519, 1906, 1893]
    paintings = ["Starry Night", "Mona Lisa", "Water Lilies", "The Scream"]
    classic = []
    modern = []
    for i in range(len(paintings)):
        if years[i] < 1860:
            classic.append(paintings[i])
        elif years[i] > 1860:
            modern.append(paintings[i])
    print("classic:", classic)
    print("modern:", modern)


# Demo B (deck 16.1, two features and a separating line): cats and dogs by ear stand-up (1-5) and eye darkness (1-5).
# One feature alone cannot separate them; the line  ears + eyes = 6  can.
def classify_pet(ears, eyes):
    if ears + eyes > 6:
        return "cat"
    else:
        return "dog"


def demo_line():
    cat_ears = [5, 4, 2]
    cat_eyes = [3, 4, 5]
    dog_ears = [5, 2, 1, 3]
    dog_eyes = [1, 3, 4, 2]
    print("one feature - ears:  cats", cat_ears, "dogs", dog_ears)
    print("one feature - eyes:  cats", cat_eyes, "dogs", dog_eyes)
    for i in range(len(cat_ears)):
        print("cat", cat_ears[i], cat_eyes[i], "->", classify_pet(cat_ears[i], cat_eyes[i]))
    for i in range(len(dog_ears)):
        print("dog", dog_ears[i], dog_eyes[i], "->", classify_pet(dog_ears[i], dog_eyes[i]))


classify_paintings()
# task1_songs(2015)
# task1_songs(2020)
# task2_length()
# task4_fruit()
# task_if_time()
# task_if_time_vehicles()
# demo_louvre()
# demo_line()
