# Lessons 19.0–19.1 - the REAL model code (Ministry deck 19.1, pp. 15-24), for a live run with TensorFlow.
#
# NOT verified here: it needs TensorFlow, Pillow, NumPy and a model exported from Teachable Machine
# ("Tensorflow" -> "Savedmodel" -> converted_savedmodel.zip, extracted: a folder model.savedmodel and labels.txt).
# The Ministry treats this code as a black box: the students edit ONLY the three paths below.
# Differences from the Ministry deck (19.1 pp. 15-24), each with its reason:
#  1. The three paths are at the TOP of the file; the deck has them inside main(). Reason: classify_image()
#     (our addition, used by the lab functions) shares them, so the students still edit the paths in ONE place.
#     Tell the class: "the deck shows them inside main(); here they are above it - same three lines".
#  2. The deck's typo `__name__ _= "__main__"` is fixed.
#  3. Comments are in English; the two print messages are in Hebrew, as in the deck.
#  4. The model is loaded once per run: main() loads it itself (as in the deck); classify_image() loads it the
#     first time it is called and then keeps it (the first draft of this file loaded it twice at import).
#  5. The classify_image() block at the bottom is OUR addition (it returns the same label and confidence
#     that main() prints, as a list [label, confidence]).

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
    print("הקטגוריה אליה התמונה שייכת לפי המודל:", predicted_label)
    print("רמת הביטחון של המודל:", round(confidence, 2))


# ---- OUR ADDITION: the same steps as main(), packaged so the lab functions can call it ----
loaded = []   # filled on the first call: [model, labels]


def classify_image(image_path):
    # Returns a list: [label as written in labels.txt, confidence from 0 to 1]
    if len(loaded) == 0:
        loaded.append(tf.keras.layers.TFSMLayer(model_path, call_endpoint="serving_default"))
        loaded.append(load_labels(labels_path))
    model = loaded[0]
    labels = loaded[1]
    image = preprocess_image(image_path, (224, 224))
    predictions = model(image)
    predictions_tensor = list(predictions.values())[0]
    predicted_class_idx = tf.argmax(predictions_tensor[0]).numpy()
    return [labels[predicted_class_idx], float(predictions_tensor[0][predicted_class_idx].numpy())]


if __name__ == "__main__":
    main()
