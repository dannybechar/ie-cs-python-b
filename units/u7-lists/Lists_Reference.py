# Unit 7.1 - reference for the teacher.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.


# Warm-up, fixed: == compares (and throws the result away); = assigns
def warmup():
    scores = [60, 70, 80]
    scores[1] = 75
    print(scores)


# Predict table (Ministry 9.4 Q1-Q3 in our version; the answers are in the lesson notes).
# Run it AFTER the students wrote their predictions.
def predict_table():
    data = [4, 5, 6, "Yael", "Ester", 7, 8]
    print(data[1])
    print(data[-3])
    data[2] = "Amir"
    print(data)
    print(len(data))
    data = [4, 5, "Amir", "Yael", "Adi", 12, 988, 20, "20", 97]
    print(data[::2])
    print(data[::-1])
    print(data[2:7:2])
    print(data[-8:-3])
    print(data[1:])
    print(data[-4:-1])
    my_list = [4] * 3
    print(my_list)
    print(data[:2] + my_list)


# The Ministry 9.1 pp. 4-9 demo list: mixed types, index table, slices, + of three lists
def official_demo():
    everything = [24.56, "Itamar", 340, -7]
    print(everything, len(everything))
    my_list = [24.56, "Itamar", 340, -7, "Yael"]
    print(my_list[0], my_list[1], my_list[-1], my_list[-2])
    print(my_list[1:3])
    print(my_list[-4:-1])
    print(my_list[1:])
    print(my_list[2:])
    list1 = ["A", "B", "C", "D", "E"]
    list2 = ["F", "G", "H", "I", "J"]
    print(list1 + list2 + ["K", "L"])
    print(list1, list2)


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
    # predict_table()
    # official_demo()
    # ai_report([81, 24, 67, 91])
    # task2()
    # slice_report([25, 20, 21, 24, 21, 24, 21, 16, 23])
    # task4()
