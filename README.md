# Fraud Detection Using Machine Learning

A machine learning project that analyzes financial transaction data and predicts potentially fraudulent transactions using Logistic Regression. The project includes exploratory data analysis, model training, evaluation, and an interactive web application built using Streamlit.

**Live Application:** [Add your Streamlit URL here]

## Project Overview

Financial transaction fraud is a significant challenge for digital payment systems. This project explores transaction patterns and develops a machine learning model to distinguish between legitimate and potentially fraudulent transactions.

The dataset contains approximately 6.36 million transactions, including 8,213 fraudulent records, representing around 0.13% of all transactions.

The project focuses on handling this class imbalance, preprocessing transaction data, training a classification model, and making predictions through a web interface.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Logistic Regression
- Streamlit
- Joblib
- Jupyter Notebook

## Key Features

- Exploratory data analysis of financial transactions
- Visualization of transaction amounts and fraud patterns
- Identification of class imbalance
- Numerical feature scaling using StandardScaler
- Categorical feature encoding using OneHotEncoder
- Logistic Regression with balanced class weights
- Model evaluation using classification reports and confusion matrices
- Interactive Streamlit interface for entering transaction details
- Prediction of potentially fraudulent transactions

## Machine Learning Workflow

1. **Data Exploration:** Examined transaction types, transaction amounts, fraud labels, missing values, and balance changes.
2. **Data Visualization:** Created distribution plots, box plots, and a correlation heatmap to understand transaction patterns.
3. **Data Preprocessing:** Prepared numerical and categorical features using a Scikit-learn ColumnTransformer.
4. **Model Training:** Split the dataset into 70% training and 30% testing data and trained a Logistic Regression classifier.
5. **Handling Class Imbalance:** Used balanced class weights to address the large difference between fraudulent and legitimate transactions.
6. **Model Evaluation:** Evaluated predictions using precision, recall, F1-score, and a confusion matrix.
7. **Deployment:** Saved the trained model using Joblib and integrated it into a Streamlit web application.

## Dataset

The project uses a financial transaction dataset containing approximately 6.36 million records.

The dataset includes transaction type, transaction amount, sender and receiver balances, and fraud indicators.

**Dataset source:** [Insert original dataset download link]

The dataset is not included directly in this repository because of its size.

## Running the Project Locally

1. Clone the GitHub repository.
2. Open the project folder in VS Code or another Python development environment.
3. Install the packages listed in `requirements.txt`.
4. Ensure the trained model file is present.
5. Start the Streamlit application using `streamlit run fraud_detection.py`.

## Model Evaluation

The model is evaluated using a classification report and confusion matrix.

Because fraudulent transactions represent only a small percentage of the dataset, recall, precision, and F1-score are particularly important when evaluating performance.

**Final model results:**

- Accuracy: [Add your measured accuracy]
- Fraud-class Precision: [Add your result]
- Fraud-class Recall: [Add your result]
- Fraud-class F1-score: [Add your result]

## Limitations and Future Improvements

- Compare Logistic Regression against Random Forest and XGBoost.
- Explore alternative approaches for handling imbalanced data.
- Improve fraud-class precision while maintaining strong recall.
- Add prediction confidence scores and more detailed explanations.
- Experiment with model hyperparameter tuning.
- Improve the Streamlit user interface.

## Project Purpose

This project was developed to gain hands-on experience in machine learning, data preprocessing, classification, model evaluation, and deploying Python applications.

The application is an educational demonstration and is not intended to make real financial fraud decisions.

## Acknowledgments

Project developed as a learning exercise following a fraud detection machine learning tutorial, with additional documentation and deployment work.

**Tutorial:** [Add the YouTube tutorial link]

**Author:** [Your name]

**GitHub:** [Your GitHub profile link]
