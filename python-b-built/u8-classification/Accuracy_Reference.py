# Unit 8.4 - reference for the teacher.
# CLASSROOM MODE: classify_image() calls a stand-in, not a real Keras model, so this file runs with
# plain Python and needs no downloaded model or files. Before class, swap MOCK_MODE to False and
# fill in the real loading code below - then test it live in Thonny with an exported model.
# One task per block; run ONE task at a time by removing the # from its call at the bottom.

MOCK_MODE = True


# Warm-up, fixed: strip every label before comparing - trailing spaces or newlines from a real
# labels.txt file are a documented, common cause of "wrong" accuracy.
def calculate_accuracy(actual, predicted):
    if len(actual) == 0 or len(actual) != len(predicted):
        return 0
    correct = 0
    for index in range(len(actual)):
        if actual[index].strip() == predicted[index].strip():
            correct += 1
    return correct / len(actual) * 100


# Task 2: classify_image, completed
def classify_image(image_path):
    if MOCK_MODE:
        lower_path = image_path.lower()
        if "fist" in lower_path:
            return "fist", 0.9
        elif "ok" in lower_path:
            return "ok", 0.9
        else:
            return "unknown", 0.5

    # Real model (needs `pip install tensorflow keras pillow numpy`, an exported keras_Model.h5
    # and labels.txt from Teachable Machine, both loaded ONCE, outside this function):
    #
    # from keras.models import load_model
    # from PIL import Image, ImageOps
    # import numpy as np
    # model = load_model("keras_Model.h5", compile=False)
    # with open("labels.txt", "r", encoding="utf-8") as f:
    #     class_names = f.readlines()
    #
    # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # image = Image.open(image_path).convert("RGB")
    # image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    # normalized = (np.asarray(image).astype(np.float32) / 127.5) - 1
    # data[0] = normalized
    # prediction = model.predict(data, verbose=0)
    # index = int(np.argmax(prediction))
    # class_name = class_names[index].strip().split(" ", 1)[-1]
    # return class_name, float(prediction[0][index])
    raise NotImplementedError("Fill in the real model above and set MOCK_MODE = False.")


def predict_test_set(test_images, actual_labels):
    predicted_labels = []
    for image_path in test_images:
        label, confidence = classify_image(image_path)
        predicted_labels.append(label)
        print(image_path)
        print("Prediction:", label)
        print("Confidence:", round(confidence, 3))

    accuracy = calculate_accuracy(actual_labels, predicted_labels)
    print("Accuracy:", round(accuracy, 1), "%")


def checkpoint():
    test_images = [
        "test_images/fist_1.jpg",
        "test_images/ok_1.jpg",
        "test_images/fist_dark.jpg",
        "test_images/ok_side.jpg",
    ]
    actual_labels = ["fist", "ok", "fist", "ok"]
    predict_test_set(test_images, actual_labels)


actual_labels = ["fist", "ok", "fist"]
predicted_labels = ["fist", "ok ", "fist"]
print(calculate_accuracy(actual_labels, predicted_labels))

actual_full = ["fist", "ok", "fist", "ok", "ok", "fist", "ok"]
predicted_full = ["fist", "ok", "ok", "ok", "ok", "fist", "ok"]
print(round(calculate_accuracy(actual_full, predicted_full), 1))
# checkpoint()
