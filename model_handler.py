from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model("dish_model.h5", compile=False)

class_names = ["Pho", "Goi cuon", "Banh mi", "Banh xeo", "Com tam"]

def predict_dish(image_path):
    img = image.load_img(image_path, target_size=(300, 300, 3))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)
    print(f"Predicted dish: {class_names[class_idx]}")
    return class_names[class_idx]
