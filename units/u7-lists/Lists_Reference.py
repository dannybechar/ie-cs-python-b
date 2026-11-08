# Unit 7.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: == compares (and throws the result away); = assigns
def warmup():
    scores = [60, 70, 80]
    scores[1] = 75
    print(scores)


# Task 1: length, first, last, membership
def ai_report(scores):
    print("Number of tests:", len(scores))
    print("First score:", scores[0])
    print("Last score:", scores[-1])
    print("Contains perfect score:", 100 in scores)


# Task 2: bounds-checked update
def update_score(scores, index, new_value):
    if 0 <= index < len(scores):
        scores[index] = new_value
        return True
    print("Invalid index")
    return False


def task2():
    scores = [60, 70, 80]
    print(update_score(scores, 1, 75), scores)
    print(update_score(scores, 5, 99), scores)


# Task 3: slicing [start:stop:step] - the stop index is not included
def slice_report(values):
    print("All:", values)
    print("First five:", values[:5])
    print("From index 2 up to 5:", values[2:5])
    print("Every third, from index 2:", values[2::3])
    print("Reversed:", values[::-1])


# Task 4 (if time): + builds a new list, the originals stay as they were; list() splits text
def combine(first, second):
    return first + second


def task4():
    morning = [81, 24]
    evening = [67, 91]
    both = combine(morning, evening)
    print(both, len(both))
    print(morning, evening)
    print(list("cat"))
    print(list())


if __name__ == "__main__":
    warmup()
    # ai_report([81, 24, 67, 91])
    # task2()
    # slice_report([25, 20, 21, 24, 21, 24, 21, 16, 23])
    # task4()
