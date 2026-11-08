# Unit 8.4 - the REAL model code (Ministry deck 19.1, pp. 15-24), for a live run with TensorFlow.
#
# NOT verified here: it needs TensorFlow, Pillow, NumPy and a model exported from Teachable Machine
# ("Tensorflow" -> "Savedmodel" -> converted_savedmodel.zip, extracted: a folder model.savedmodel and labels.txt).
# The Ministry treats this code as a black box: the students edit ONLY the three paths below.
# Changes from the Ministry deck: the three paths moved to the top (so classify_image can share them),
# the deck's typo `__name__ _= "__main__"` fixed, English comments, and the classify_image() block at the
# bottom is OUR addition (it returns the same label and confidence that main() prints).

import tensorflow as tf
import numpy as np
from PIL import Image

# ---- EDIT ONLY THESE THREE LINES (paths on your computer) ----
model_path = "model.savedmodel"   # the model folder, extracted from converted_savedmodel.zip
labels_path = "labels.txt"        # the categories file, from the same zip
image_path = "test_image.png"     # the image you want to test
# ---------------------------------------------------------------


# Load the category names from the text file
def load_labels(labels_path):
    with open(labels_path, "r") as file:
        labels = [line.strip() for line in file]
    return labels


# Prepare the input image
def preprocess_image(image_path, target_size):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size)          # resize the image to the model's input size
    img_array = np.array(img) / 255.0      # normalize pixel values to [0, 1]
    return np.expand_dims(img_array, axis=0)


# Main function
def main():
    # Load the model using TFSMLayer
    model = tf.keras.layers.TFSMLayer(model_path, call_endpoint="serving_default")
    labels = load_labels(labels_path)

    # Process the test image
    input_shape = (224, 224)
    image = preprocess_image(image_path, input_shape)
    predictions = model(image)

    # Extract the information from the model's answer
    predictions_tensor = list(predictions.values())[0]   # automatically get the model's output tensor

    # Get the category the model decided the image belongs to
    predicted_class_idx = tf.argmax(predictions_tensor[0]).numpy()   # the class with the highest confidence
    predicted_label = labels[predicted_class_idx]
    confidence = predictions_tensor[0][predicted_class_idx].numpy()

    # Show the results
    print("The category of the image according to the model:", predicted_label)
    print("The model's confidence level:", round(confidence, 2))


# ---- OUR ADDITION: the same steps as main(), packaged so the lab functions can call it ----
model = tf.keras.layers.TFSMLayer(model_path, call_endpoint="serving_default")
labels = load_labels(labels_path)


def classify_image(image_path):
    # Returns a list: [label as written in labels.txt, confidence from 0 to 1]
    image = preprocess_image(image_path, (224, 224))
    predictions = model(image)
    predictions_tensor = list(predictions.values())[0]
    predicted_class_idx = tf.argmax(predictions_tensor[0]).numpy()
    return [labels[predicted_class_idx], float(predictions_tensor[0][predicted_class_idx].numpy())]


if __name__ == "__main__":
    main()
