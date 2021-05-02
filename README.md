# Purwadhika Data Science and Machine Learning Final Project - Predict Customer Churn

Name : Muhammad Naufal Luthfi

Final Project Description
--- 
Churn is a condition where a customer stops using a product or service. A telco company has a problem because many of its customers are churning out. Therefore, the company wanted to find a way to solve this problem using machine learning algorithms. 

Goal Final Project
--- 
Create a machine learning model that can predict at least 80 percent of customers who will churn and create a web application from a local host based on the model that has been selected to predict whether a customer will churn or not 

Dataset
--- 
Dataset: Telecom-Customer_Churn

Source : [kaggle](https://www.kaggle.com/lampubhutia/telecomcustomer-churn)

![](https://github.com/sirnaufal/Final-Project/blob/main/image/kaggle.png)

Dataset for this project comes from kaggle taken from the IBM Sample Dataset. Each row in the dataset represents each customer and each column in the dataset contains specific information from each customer.

Feature Information:

    customerID: customer identity number (categorical)
    gender : Whether the customer is a male or a female (categorical: 'Male', 'Female')
    SeniorCitizen : Whether the customer is a senior citizen or not (numeric: 0, 1)
    Partner : Whether the customer has a partner or not (categorical: 'Yes', 'No')
    Dependents: Whether the customer has dependents or not (categorical: 'Yes', 'No')
    tenure: Number of months the customer has stayed with the company (numeric)
    PhoneService: Whether the customer has a phone service or not (categorical: 'Yes', 'No')
    MultipleLines: Whether the customer has multiple lines or not (categorical: 'Yes', 'No', 'No phone service')
    InternetService: Customer’s internet service provider (categorical: 'DSL', 'Fiber optic', 'No')
    OnlineSecurity: Whether the customer has online security or not (categorical: 'Yes', 'No', 'No internet service')
    OnlineBackup: Whether the customer has online backup or not (categorical: 'Yes', 'No', 'No internet service')
    DeviceProtection: Whether the customer has device protection or not (categorical: 'Yes', 'No', 'No internet service')
    TechSupport: Whether the customer has tech support or not (categorical: 'Yes', 'No', 'No internet service')
    StreamingTV: Whether the customer has streaming TV or not (categorical: 'Yes', 'No', 'No internet service')
    StreamingMovies: Whether the customer has streaming movies or not (categorical: 'Yes', 'No', 'No internet service')
    Contract: The contract term of the customer (categorical: 'Month-to-month', 'One year', 'Two year')
    PaperlessBilling: Whether the customer has paperless billing or not (categorical: 'Yes', 'No')
    PaymentMethod: The customer’s payment method (categorical: 'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)')
    MonthlyCharges: The amount charged to the customer monthly (numeric)
    TotalCharges: The total amount charged to the customer (numeric)
    
Target Information:

    Churn: Whether the customer churned or not (categorical: 'Yes', 'No')
    
Final Project working step:
1. Data Cleaning dan Preprocessing
2. Data Visualization
3. Choose best model
4. create a web application from a local host based on the model that has been selected to predict whether a customer will churn or not

Final model is Random Forest Classifier
---
HOME PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/home.png)

VISUALIZATION PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/visual.png)

PREDICTION PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/predict.png)

RESULT PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/result.png)
