from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd 

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/database', methods=['POST','GET'])
# def dataset():
#     pass

@app.route('/visualization', methods=['POST','GET'])
def visual():
    return render_template('plot.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'tenure': [input['Tenure']],
            'InternetService': [input['Internetservice']],
            'OnlineSecurity': [input['Onlinesecurity']],
            'OnlineBackup': [input['Onlinebackup']],
            'DeviceProtection': [input['Deviceprotection']],
            'TechSupport': [input['Techsupport']],
            'StreamingTV': [input['Streamingtv']],
            'StreamingMovies': [input['Streamingmovies']],
            'Contract': [input['contract']],
            'PaymentMethod': [input['Paymentmethod']]
        })

        prediksi = model.predict_proba(df_to_predict)[:,1]

        if prediksi > 0.472842:
            quality = 'Churn'
        else:
            quality = 'Not Churn'
        
        return render_template('result.html', data=input, pred=quality)

if __name__ == '__main__':
    
    filename = 'rf_final.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)