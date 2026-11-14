# Lessons 19.0–19.1 - starter. Needs the file labels_standin.txt in the same folder (it looks like the labels.txt
# that Teachable Machine exports: one line per category, "<number> <name>").
#
# STAND-IN MODEL: the classify_image() below is NOT a real model. It returns fixed answers for seven
# made-up image names, so this file runs with plain Python (no TensorFlow, no exported model, no photos).
# With a real exported model, set USE_REAL_MODEL = True and put Ministry_Model_Code.py next to this file.

USE_REAL_MODEL = False


def load_labels(labels_path):
    labels = []
    with open(labels_path, "r") as file:
        for line in file:
            labels.append(line.strip())
    return labels


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


# Warm-up: the OK sign should open the door. Predict what prints, run, then find why it does not.
result = classify_image("test_1_ok.png")
label = result[0]
confidence = result[1]
print("label:", label)
if label == "ok":
    print("Gesture recognized: OK - opening the door")
else:
    print("Not an OK sign - the door stays closed")


# Task 1: write report(image_path) - it classifies the image and PRINTS one line:
# "<image_path> -> <label> (<confidence as a whole percent>%)"   for example   test_1_ok.png -> ok (99%)
# Run it on "test_1_ok.png" and "test_4_ok_drawing.png".


# Task 2: write decide(label, confidence) - it RETURNS a message:
#   confidence 0.85 or more:  "ACT: <label>"
#   below 0.85:               "NOT SURE: ask for another photo"
# Test it on ("ok", 0.99) and on ("fist", 0.73).


# Task 3: write calculate_accuracy(successes, attempts) (from lessons 18.0–18.1), and then
# evaluate(test_images, true_labels): classify every image, print one line per image saying
# "correct" or "WRONG", count the successes, and RETURN the accuracy in percent.
# test_images = ["test_1_ok.png", "test_2_fist.png", "test_3_fist_dark.png", "test_4_ok_drawing.png",
#                "test_5_ok_side.png", "test_6_fist_blurry.png", "test_7_ok_far.png"]
# true_labels = ["ok", "fist", "fist", "ok", "ok", "fist", "ok"]
# With your own model use your own image names (the 7 test images) and their true labels.
