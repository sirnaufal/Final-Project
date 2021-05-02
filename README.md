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

Informasi Fitur:

    customerID: identitas tiap customer (categorical)
    gender : jenis kelamin customer (categorical: 'Male', 'Female')
    SeniorCitizen : apakah customer termasuk muda atau tua (numeric: 0, 1)
    Partner : apakah customer memiliki pasangan atau tidak (categorical: 'Yes', 'No')
    Dependents: apakah customer memiliki tanggungan atau tidak (categorical: 'Yes', 'No')
    tenure: lama waktu dalam bulan customer berlangganan (numeric)
    PhoneService: apakah customer menggunakan layanan telepon atau tidak (categorical: 'Yes', 'No')
    MultipleLines: apakah customer menggunakan multiple lines atau tidak (categorical: 'Yes', 'No', 'No phone service')
    InternetService: apakah customer menggunakan layanan internet atau tidak (categorical: 'DSL', 'Fiber optic', 'No')
    OnlineSecurity: apakah customer menggunakan layanan online security atau tidak (categorical: 'Yes', 'No', 'No internet service')
    OnlineBackup: apakah customer menggunakan layanan online backup atau tidak (categorical: 'Yes', 'No', 'No internet service')
    DeviceProtection: apakah customer menggunakan layanan device protection atau tidak (categorical: 'Yes', 'No', 'No internet service')
    TechSupport: apakah customer menggunakan layanan tech support atau tidak (categorical: 'Yes', 'No', 'No internet service')
    StreamingTV: apakah customer menggunakan layanan streaming tv atau tidak (categorical: 'Yes', 'No', 'No internet service')
    StreamingMovies: apakah customer menggunakan layanan streaming movie atau tidak (categorical: 'Yes', 'No', 'No internet service')
    Contract: kontrak berlangganan customer (categorical: 'Month-to-month', 'One year', 'Two year')
    PaperlessBilling: apakah customer menggunakan paperless billing atau tidak (categorical: 'Yes', 'No')
    PaymentMethod: metode pembayaran yang digunakan oleh customer (categorical: 'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)')
    MonthlyCharges: tagihan per bulan dari customer (numeric)
    TotalCharges: tagihan total dari customer (numeric)
    
Informasi target:

    Churn: apakah customer akan melakukan churn atau tidak (categorical: 'Yes', 'No')
    
Tahapan Pengerjaan:
1. Melakukan Data Cleaning dan Preprocessing
2. Membuat visualisasi dataset
3. Mencari Model Machine Learning yang paling baik
4. Membuat dashboard menggunakan model machine learning yang sudah dipilih agar user bisa menginput data customernya dan melakukan prediksi

Model akhir yang digunakan adalah Random Forest Classifier
---
HOME PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/home.png)

VISUALIZATION PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/visual.png)

PREDICTION PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/predict.png)

RESULT PAGE
![](https://github.com/sirnaufal/Final-Project/blob/main/image/result.png)
