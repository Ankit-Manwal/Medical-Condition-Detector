# Medical-Condition-Detector

Medical-Condition-Detector is a Streamlit-based web application designed to diagnose medical conditions based on user inputs. It covers three main areas: general conditions, diabetes, and skin diseases. The application uses different machine learning models tailored to each category, ensuring accurate and reliable predictions.

## Features

- **General Conditions Diagnosis**: Symptom-based diagnosis across 41 classes.
- **Diabetes Prediction**: Predicts the likelihood of diabetes based on user input.
- **Skin Disease Classification**: Identifies skin diseases from images, covering six distinct classes.

## Datasets

- **General Conditions**: [Disease Symptom Description Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data)
- **Diabetes**: [Diabetes Data Set](https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data)
- **Skin Diseases**: [Skin Diseases Image Dataset 1](https://www.kaggle.com/datasets/ismailpromus/skin-diseases-image-dataset) and [Skin Diseases Image Dataset 2](https://www.kaggle.com/datasets/ascanipek/skin-diseases)

## Models and Accuracy

- **General Conditions**: Artificial Neural Network (ANN)
  - Accuracy: Almost 100% (ideal conditions with all symptoms input, but its reliability is based on input symptoms and their description in real-world environment)
- **Diabetes**: Random Forest Classifier
  - Accuracy: 83%
- **Skin Diseases**: Convolutional Neural Network (CNN)
  - Classes: 
    - Akne
    - Basal Cell Carcinoma (BCC)
    - Melanocytic Nevi (NV)
    - Melanoma
    - Pigment
    - Seborrheic Keratoses and other Benign Tumors
  - Accuracy: 82%

## Installation

Clone the repository, navigate to the project directory, install the required packages, and run the Streamlit application:
```bash
git clone https://github.com/Ankit-Manwal/Medical-Condition-Detector.git
cd Medical-Condition-Detector
pip install -r requirements.txt
streamlit run streamlit_app/front.py
```

## Contact

For any questions or inquiries, please contact ankitmanwal2081@gmail.com.
