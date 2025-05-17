import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import joblib

# Class names for your categories
class_names = ["Pho", "Goi cuon", "Banh mi", "Banh xeo", "Com tam"]

# Load pretrained CNN model for embeddings (from your model.h5)
model = tf.keras.models.load_model("model.h5", compile=False)
embedding_model = tf.keras.models.Model(
    inputs=model.input,
    outputs=model.get_layer('out_relu').output
)

# Load trained fusion classifier
fusion_clf = joblib.load("fused_dish_classifier.pkl")

IMG_SIZE = (300, 300)


def get_embedding(image_path):
    img = keras_image.load_img(image_path, target_size=IMG_SIZE)
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    feature_map = embedding_model.predict(img_array, verbose=0)
    pooled = tf.keras.layers.GlobalAveragePooling2D()(
        tf.convert_to_tensor(feature_map))
    return pooled.numpy().flatten()


def get_color_histogram(image_path, bins_per_channel=8):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hist_features = []
    for i in range(3):
        hist = cv2.calcHist([img], [i], None, [bins_per_channel], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        hist_features.extend(hist)
    return np.array(hist_features)


def get_sift_feature_count(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, _ = sift.detectAndCompute(gray, None)
    return len(keypoints)


def get_fused_feature_vector(image_path):
    embedding = get_embedding(image_path)
    color_hist = get_color_histogram(image_path)
    sift_count = get_sift_feature_count(image_path)
    fused_vector = np.concatenate([embedding, color_hist, [sift_count]])
    return fused_vector


def predict_dish(image_path):
    # Fusion prediction
    fused_vector = get_fused_feature_vector(image_path).reshape(1, -1)
    class_idx = fusion_clf.predict(fused_vector)[0]
    pred_proba = fusion_clf.predict_proba(fused_vector)[0]

    pred_dict = dict(zip(class_names, pred_proba))
    print("Prediction probabilities:")
    for dish, prob in pred_dict.items():
        print(f"{dish}: {prob:.4f}")

    confidence = pred_proba[class_idx]
    print(
        f"Predicted dish: {class_names[class_idx]} (Confidence: {confidence:.2f})\n")

    # Show top-3 predictions
    top_indices = pred_proba.argsort()[-3:][::-1]
    for i in top_indices:
        print(f"{class_names[i]}: {pred_proba[i]:.4f}")

    return class_names[class_idx]