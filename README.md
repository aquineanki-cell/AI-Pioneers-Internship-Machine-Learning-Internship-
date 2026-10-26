# AI-Pioneers-Internship-Machine-Learning-Internship-


💳 Credit Card Fraud Detection - ML Capstone Project

Author: Aquine Roshan Pais

Program: AI Pioneers Machine Learning Internship (4-Week Capstone)

📑 Project Overview

This repository contains an end-to-end Machine Learning pipeline designed to detect fraudulent credit card transactions. The project tackles the real-world challenge of analyzing highly imbalanced financial data, balancing the need to maximize fraud detection while minimizing false alarms for innocent customers. The final deliverable is a production-ready Random Forest model deployed as a local Web API using Flask.

🚀 Weekly Milestones

Week 1: Data Preprocessing & EDA

Data Cleaning: Handled missing values and removed duplicates from a 10,000-record dataset.

Feature Scaling: Normalized financial metrics (e.g., transaction amounts, trust scores) to ensure fair algorithm evaluation.

Imbalance Identification: Identified extreme target skewness, setting the stage for advanced modeling techniques.

Week 2: Supervised Learning & The "Accuracy Trap"

Model Selection: Evaluated Logistic Regression vs. Random Forest algorithms.

The SMOTE Effect: Applied Synthetic Minority Over-sampling Technique (SMOTE) to address class imbalance.

Insight: Demonstrated the Precision-Recall Trade-off. While SMOTE boosted recall to 77%, it caused an 84% false alarm rate (Precision = 16%). The baseline Random Forest was chosen as the superior model for achieving a flawless 100% precision with zero false alarms.

Week 3: Unsupervised Learning & Advanced Evaluation

Dimensionality Reduction: Utilized PCA to compress data into 2D for visual mapping.

Clustering: Applied K-Means to discover 3 hidden behavioral customer segments without using predefined labels.

Hyperparameter Tuning: Used GridSearchCV to find the optimal Random Forest parameters.

Validation: Achieved an exceptional 5-Fold Cross-Validation score of 0.995 and a near-perfect ROC-AUC score of 0.994.

Week 4: API Deployment

Serialization: Exported the trained model's mathematical decision trees using joblib (fraud_model.pkl).

Web Server: Engineered a backend web application using Flask (app.py) with a /predict endpoint.

Client Testing: Developed a client-side testing script (test_api.py) using the requests library to transmit simulated JSON transaction payloads and receive real-time "Safe" or "Fraud" predictions.

🛠️ Tech Stack

Language: Python 3

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-Learn, Imbalanced-Learn (SMOTE)

Data Visualization: Matplotlib, Seaborn

Deployment: Flask, Joblib, Requests

📁 Repository Structure

cleaned_credit_card_fraud_10k.csv - The preprocessed dataset.

Week1_to_3_Notebooks.ipynb - Jupyter notebooks containing EDA, modeling, clustering, and evaluation code.

fraud_model.pkl - The serialized Random Forest model.

app.py - The Flask web server script.

test_api.py - The client script to test API predictions.

visualizations/ - Saved PNG outputs (Confusion Matrices, K-Means Clusters, ROC Curve).

💻 How to Run the Project Locally

1. Install Dependencies
Ensure you have Python installed, then install the required libraries:

pip install pandas scikit-learn flask requests


2. Start the Flask Server
Run the app.py file to start the local web server. Keep this terminal open.

python app.py


You should see a message indicating the server is running on http://127.0.0.1:5000.

3. Test the API
Open a second terminal window and run the testing script to send a simulated transaction to the server:

python test_api.py


The terminal will output the model's live prediction: {'prediction': 'Warning: Fraudulent Transaction Detected!'} or Safe.
