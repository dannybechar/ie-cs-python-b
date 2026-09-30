# Warm-up: all three predictions are actually correct - this should print 100.0. Predict, run, then
# fix it (hint: a real labels.txt line can carry a trailing space or newline).

def calculate_accuracy(actual, predicted):
    if len(actual) == 0 or len(actual) != len(predicted):
        return 0
    correct = 0
    for index in range(len(actual)):
        if actual[index] == predicted[index]:
            correct += 1
    return correct / len(actual) * 100


actual_labels = ["fist", "ok", "fist"]
predicted_labels = ["fist", "ok ", "fist"]   # a trailing space, as read from a real labels.txt line
print(calculate_accuracy(actual_labels, predicted_labels))


# Task 1: confirm the fix on the full official example:
actual_full = ["fist", "ok", "fist", "ok", "ok", "fist", "ok"]
predicted_full = ["fist", "ok", "ok", "ok", "ok", "fist", "ok"]
# print(round(calculate_accuracy(actual_full, predicted_full), 1))  # expect about 85.7


# CLASSROOM MODE: classify_image() below does not load a real Teachable Machine model - it is a
# stand-in (no TensorFlow/Keras/model files needed) so this file runs with plain Python. Before
# class, swap MOCK_MODE to False and fill in the real loading code (see the reference file).

MOCK_MODE = True


def classify_image(image_path):
    pass  # complete this: in classroom mode, guess the label from the file name (see Task 2)


# Task 2 (project - the checkpoint): complete classify_image() so that in classroom mode it looks
# at image_path (lowercased): if it contains "fist", return ("fist", 0.9); if it contains "ok",
# return ("ok", 0.9); otherwise return ("unknown", 0.5). Then write predict_test_set(test_images,
# actual_labels) that calls classify_image on each path, prints the path/prediction/confidence,
# collects the predicted labels into a list, and finally prints the overall accuracy against
# actual_labels using calculate_accuracy.
