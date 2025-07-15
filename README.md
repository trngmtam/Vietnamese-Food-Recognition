# Vietnamese Food Detection & Calorie Calculation 

## Demo Video  

[Watch the demo video here](https://youtu.be/v1RyfsgLyPY)

---

## Contributors  
- Tran Thi Nhu Quynh ([Kyltetran](https://github.com/Kyltetran))
- Truong Ngoc Minh Tam   

---

## Introduction  

This project aims to develop an application for food detection and calorie calculation using computer vision techniques. The application takes an image of a dish, either uploaded from the computer or captured via webcam, and automatically identifies which Vietnamese dish it is. Once the dish is detected, the program retrieves the full list of ingredients, their respective weights, calorie values, and any notes from a prebuilt SQLite database.

Currently, the project supports five popular Vietnamese dishes:
- **Phở**  
- **Bánh xèo**  
- **Bánh mì**  
- **Cơm tấm**  
- **Gỏi cuốn**  

We built this project because it combines two areas we’re personally interested in: applying computer vision techniques alongside deep learning models for food detection and developing health-related applications focused on food and nutrition. We've often wondered about the calorie content of the dishes we eat daily but lacked an accurate and accessible way to calculate it — especially for local Vietnamese foods. This final project presented the perfect opportunity to turn that curiosity into a practical, working application.

---

## Method  

Our food classification approach evolved in several stages, integrating both classical computer vision techniques and deep learning strategies:

### 1. Traditional Feature-Based Methods  
- **Color Histograms (HSV color space)**: Captured color distribution of each dish image.
- **SIFT (Scale-Invariant Feature Transform)**: Extracted local keypoints and texture features.
- Result: Accuracy below 20%, proving handcrafted features alone were insufficient.

### 2. Custom CNN  
- Designed a Convolutional Neural Network trained from scratch.
- Training accuracy: ~80%
- Validation accuracy plateau: ~30% (overfitting issue)

### 3. Fine-Tuning Pretrained Models  
- **EfficientNetV2**:  
  - Training/Validation/Test accuracy: ~90%  
  - Poor generalization on real-time images (biased predictions)
  
- **MobileNetV2**:  
  - Training accuracy: ~60%  
  - Generalized better on real-time images  
  - Chosen as the feature extractor for the final model.

### 4. Fusion-Based Final Model  
To address the weaknesses of standalone methods:
- Extracted **deep embeddings** from fine-tuned MobileNetV2.
- Combined them with handcrafted features, including **Color Histograms** and **SIFT Descriptors**, forming a comprehensive representation of each image.
- Fused features used to train a **Random Forest classifier**.

This final fusion strategy effectively balanced high-level and low-level visual cues for robust, real-time predictions.

---

## Dataset

### 1. Food images
- **Source:** [Kaggle - Vietnamese Foods](https://www.kaggle.com/datasets/quandang/vietnamese-foods/data)
- Original dataset: 30 dishes  
- Selected for this project: 5 dishes (Phở, Cơm tấm, Bánh mì, Bánh xèo, Gỏi cuốn)
- Image count: ~1000 images per dish divided into `Train`, `Test`, and `Validate` folders
- Total images: 5000+
- Located in the `dataset2` folder.

### 2. Calories
- Located in the `calorie.db` file
- The ingredients and their corresponding calorie information for each dish are predefined and stored in the `calorie.db` dataset
---

## Results  

| Dish       | CNN Accuracy | Fusion Accuracy |
|------------|:-------------|:----------------|
| Phở        | 6.17%        | **93.21%**       |
| Bánh mì    | 24.53%       | **92.45%**       |
| Bánh xèo   | 42.55%       | **92.77%**       |
| Gỏi cuốn   | 1.16%        | **84.30%**       |
| Cơm tấm    | 53.97%       | **86.24%**       |

**Key Findings:**
- Handcrafted features alone were ineffective for this task.
- EfficientNetV2 achieved high accuracy (~90%), but it produced biased and inconsistent predictions when tested on real-world images.
- MobileNetV2 yielded a training accuracy (~60%), with high training loss (~6.0), and less stable convergence. However, it demonstrated better robustness and generalization to real-time images compared to EfficientNetV2
- Fusing CNN embeddings with color histograms and SIFT descriptors delivered the highest accuracy and reliability for real-time predictions.

---

## Source Code  

All Python files for building the full application and the Jupyter Notebook used for model training are included in this repository.

**Note:**  
The fine-tuned MobileNetV2 (`model.h5`) and the fusion model (`fusion_dish_classifier.pkl`) are large files (~2GB each) and could not be uploaded to GitHub. Instead, we’ve included the Jupyter Notebook (`train_model.ipynb`) containing the full training and saving code for these models.

---

## Conclusion  

We successfully developed a complete food detection and calorie calculation application. Starting with classical computer vision techniques like color histograms and SIFT, we encountered low accuracy rates. We then experimented with deep learning models including CNN, EfficientNetV2, and MobileNetV2. While these improved results, some models struggled with overfitting or biases.  

By combining a fine-tuned MobileNetV2 model with handcrafted features through a feature fusion strategy, we significantly improved prediction accuracy — achieving over 89% in real-time tests. This project helped us strengthen our understanding of computer vision, deep learning, and the practical value of integrating multiple techniques for robust, real-world applications.

---

## Acknowledgments  

- [Vietnamese Food Dataset on Kaggle](https://www.kaggle.com/datasets/quandang/vietnamese-foods/data)
- TensorFlow, Keras API Documentation  
- OpenCV Documentation  
- scikit-learn Documentation  

---
