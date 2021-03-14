from typing import Any, Union

from flask import Flask, render_template, request, jsonify, abort
import requests
import configparser
import pandas as pd
from numpy import ndarray
from pandas import DataFrame, Series
from pandas.core.arrays import ExtensionArray

df = pd.read_csv("C:/Users/ammar/Downloads/Projet7/df_train_low_memory.csv", skiprows=50, nrows=20)
df = df.iloc[:, 1:5]
df.columns = ["id", "sex", "age", "salary"]
df.set_index("id", inplace=True)
df_id = list(df.index)
print(df)

app = Flask(__name__)


@app.route('/')
def Home_page():
    return render_template("home.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # try to get prediction with model
    id_client = int(request.form["ID"])
    if id_client in df_id:
        try:
            predict_model = df.loc[id_client].sum()
     return render_template('predict.html', prediction=predict_model)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '404 Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
