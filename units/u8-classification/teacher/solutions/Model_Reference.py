# Lessons 19.0–19.1 - reference for the teacher.
#
# STAND-IN MODEL: classify_image() returns fixed answers for seven made-up image names (no TensorFlow,
# no exported model, no photos) so this file can be verified with plain Python 3.14.
# The real model is the Ministry's code in Ministry_Model_Code.py - it needs a live run in Thonny/Colab
# with TensorFlow and a model exported from Teachable Machine. Set USE_REAL_MODEL = True for that run.
# One task per function; run ONE task at a time by removing the # from its call at the bottom.

USE_REAL_MODEL = False


def load_labels(labels_path):
    labels = []
    with open(labels_path, "r") as file:
        for line in file:
            labels.append(line.strip())
    return labels


# Warm-up, fixed: a line of labels.txt is "<number> <name>", so the label is "1 ok", never "ok".
# Keep only the part after the first space. (find returns -1 when there is no space, so a bare name stays whole.)
def clean_label(text):
    return text[text.find(" ") + 1:]


if USE_REAL_MODEL:
    from Ministry_Model_Code import classify_image
else:
    def classify_image(image_path):
        # Returns a list: [label as written in labels.txt, confidence from 0 to 1]
        labels = load_labels("labels_standin.txt")
        names = ["test_1_ok.png", "test_2_fist.png", "test_3_fist_dark.png", "test_4_ok_drawing.png",
                 "test_5_ok_side.png", "test_6_fist_blurry.png", "test_7_ok_far.png"]
        answers = [1, 0, 0, 0, 1, 0, 1]
        confidences = [0.99, 0.97, 0.91, 0.73, 0.88, 0.62, 0.80]
        for i in range(len(names)):
            if names[i] == image_path:
                return [labels[answers[i]], confidences[i]]
        return [labels[0], 0.5]


def warm_up():
    result = classify_image("test_1_ok.png")
    label = clean_label(result[0])
    print("label:", label)
    if label == "ok":
        print("Gesture recognized: OK - opening the door")
    else:
        print("Not an OK sign - the door stays closed")


# Task 1: a one-line report
def report(image_path):
    result = classify_image(image_path)
    label = clean_label(result[0])
    percent = round(result[1] * 100)
    print(image_path + " -> " + label + " (" + str(percent) + "%)")


def task1():
    report("test_1_ok.png")
    report("test_4_ok_drawing.png")


# Task 2: act only when the model is confident enough (deck 19.1: "for example above 85%")
def decide(label, confidence):
    if confidence >= 0.85:
        return "ACT: " + label
    else:
        return "NOT SURE: ask for another photo"


def task2():
    print(decide("ok", 0.99))
    print(decide("fist", 0.73))


# Task 3: accuracy over a whole test set = successes / attempts (lessons 18.0–18.1)
def calculate_accuracy(successes, attempts):
    if attempts == 0:
        return 0
    return successes / attempts * 100


def evaluate(test_images, true_labels):
    successes = 0
    for i in range(len(test_images)):
        result = classify_image(test_images[i])
        label = clean_label(result[0])
        if label == true_labels[i]:
            print(test_images[i], "-> correct")
            successes += 1
        else:
            print(test_images[i], "-> WRONG (model said " + label + ")")
    return calculate_accuracy(successes, len(test_images))


def task3():
    test_images = ["test_1_ok.png", "test_2_fist.png", "test_3_fist_dark.png", "test_4_ok_drawing.png",
                   "test_5_ok_side.png", "test_6_fist_blurry.png", "test_7_ok_far.png"]
    true_labels = ["ok", "fist", "fist", "ok", "ok", "fist", "ok"]
    accuracy = evaluate(test_images, true_labels)
    print("Accuracy:", round(accuracy, 1), "%")


# Extension: combine the two ideas - how many images would the program ACT on, and were those right?
def task_if_time():
    test_images = ["test_1_ok.png", "test_2_fist.png", "test_3_fist_dark.png", "test_4_ok_drawing.png",
                   "test_5_ok_side.png", "test_6_fist_blurry.png", "test_7_ok_far.png"]
    true_labels = ["ok", "fist", "fist", "ok", "ok", "fist", "ok"]
    acted = 0
    acted_right = 0
    for i in range(len(test_images)):
        result = classify_image(test_images[i])
        label = clean_label(result[0])
        if decide(label, result[1]).startswith("ACT"):
            acted += 1
            if label == true_labels[i]:
                acted_right += 1
    print("acted on", acted, "of", len(test_images), "images;", acted_right, "were right")


warm_up()
# task1()
# task2()
# task3()
# task_if_time()
