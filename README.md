# Purwadhika Data Science and Machine Learning Final Project - Predict Customer Churn

Nama : Muhammad Naufal Luthfi

Deskripsi Final Project
--- 
Sebuah perusahaan telco sedang mendapat masalah yaitu banyak dari customernya yang churn. Oleh karenanya, perusahaan tersebut ingin mencari cara untuk menyelesaikan masalah tersebut dengan menggunakan algoritma machine learning.
Final Project ini bertujuan untuk memprediksi apakah customer perusahaan telco tersebut akan melakukan churn atau tidak.

Goal Final Project
--- 
Membuat model machine learning yang dapat memprediksi minimal 80 persen customer yang akan churn.

Dataset yang digunakan
--- 
Dataset: Telecom-Customer_Churn

Source : [kaggle](https://www.kaggle.com/lampubhutia/telecomcustomer-churn)

![](https://github.com/sirnaufal/Final-Project/blob/main/image/kaggle.png)

Dataset yang digunakan berasal dari kaggle yang diambil dari IBM Sample Dataset. Masing-masing baris pada dataset mewakili setiap customer dan masing-masing kolom pada dataset berisi informasi tertentu dari tiap customer. Berikut merupakan penjelasan dari tiap kolom pada dataset.

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
