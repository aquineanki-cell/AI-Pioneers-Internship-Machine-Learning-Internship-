# AI-Pioneers-Internship-Machine-Learning-Internship-


Credit Card Fraud Detection - AI Pioneers Capstone

Author: Aquine Roshan Pais

Program: AI Pioneers Machine Learning Internship (October 2026)

📌 Project Overview

This repository contains the end-to-end machine learning pipeline and deployment code for a Credit Card Fraud Detection system. Built over a 4-week internship at AI Pioneers, the project tackles the challenge of identifying financial fraud within a highly imbalanced dataset of 10,000 transactions.

The primary business objective was to maximize the detection of actual fraud while strictly minimizing false alarms that could disrupt the experience of legitimate customers.

🚀 Weekly Breakdown

Week 1: Data Preprocessing

Cleaning & Scaling: Removed noise/duplicates and normalized financial metrics to ensure fair algorithmic evaluation.

Class Imbalance: Identified the extreme skew in the target variable (is_fraud), setting the stage for specialized evaluation metrics and sampling techniques.

Week 2: Model Selection & The SMOTE Effect

The Accuracy Trap: Both Logistic Regression and Random Forest achieved 99% accuracy because they defaulted to predicting "normal" transactions.

Model Comparison: Logistic Regression missed actual fraud cases (low recall). Random Forest demonstrated flawless precision.

The SMOTE Trade-off: Applied Synthetic Minority Over-sampling Technique (SMOTE). While it successfully boosted recall to 77%, it drastically reduced precision to 16%, causing an 84% false alarm rate. We selected the baseline Random Forest as the superior, production-ready model.

Week 3: Unsupervised Learning & Advanced Evaluation

K-Means & PCA: Compressed the dataset using Principal Component Analysis (PCA) to 2 dimensions and applied K-Means clustering to discover 3 hidden behavioral customer segments.

Model Stability: Validated the Random Forest model using 5-Fold Cross-Validation, achieving an exceptional average stability score of 0.995.

ROC-AUC: Achieved a near-perfect ROC-AUC score of 0.994, confirming the model's outstanding mathematical ability to separate legitimate charges from fraud.

Week 4: API Deployment

Serialization: Extracted the trained Random Forest model from memory using joblib and saved it as fraud_model.pkl.

Flask Web API: Engineered a backend web application (app.py) with a /predict endpoint that processes JSON transaction payloads and returns real-time fraud alerts.

🛠️ Technologies Used

Python 3.x

Machine Learning: Scikit-Learn, Imbalanced-Learn (SMOTE)

Data Manipulation: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Deployment: Flask, Joblib, Requests

💻 How to Run the Application Locally

Clone the repository:

git clone https://github.com/yourusername/fraud-detection-capstone.git
cd fraud-detection-capstone


Start the Flask Server:
Open a terminal and run the main application file. Keep this terminal open.

python app.py


You should see a message indicating the server is running on http://127.0.0.1:5000.

Test the API:
Open a second, separate terminal and run the test script to simulate an incoming transaction.

python test_api.py


The console will print the model's real-time prediction (e.g., {'prediction': 'Warning: Fraudulent Transaction Detected!'}).

📊 Visualizations

Please refer to the images/ folder for high-resolution Confusion Matrices, ROC Curves, and PCA Cluster plots generated during the evaluation phases.
