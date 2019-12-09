#!flask/bin/python
import os
from flask import Flask
from flask import request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import json

# creating and saving some model
"""
predictor
"""
bssid_token = pickle.load(open("BSSID_pleno", 'rb'))
model = pickle.load(open("model_forest_pleno", 'rb'))

def predict(test):
    """
    test = {"c4:a3:66:ba:07:be":"-89",
            "98:de:d0:ed:3f:24":"-86",
            "4c:5e:0c:9d:fb:ff":"-90",
            "fc:ec:da:47:11:17":"-76",
            "04:18:d6:ad:04:71":"-79",
            "64:70:02:3f:4e:59":"-88",
            "fc:ec:da:47:15:3b":"-60",
            "fc:ec:da:47:0d:7f":"-80"}
    """
    print(test)
    cleaned = [0 for i in range(len(bssid_token))]
    for i in bssid_token:
        cleaned[bssid_token[i]] = int(test[i])
    if len(cleaned) != len(bssid_token):
        return "error"
    try:
        print ([cleaned])
        model.n_jobs = 1
        pred = model.predict([cleaned])
    except:
        return "error"
        
    return str(pred[0])
app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/api', methods=['POST'])
def predictApi():
    PostData = request.form.get('PostData')
    jsons = json.loads(PostData)
    return predict(jsons)
    #return str(bc.predict())


@app.route('/test', methods=['POST'])
def test():
    PostData = request.form.get('PostData')
    jsons = json.loads(PostData)
    return str(jsons)


if __name__ == '__main__':

    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')
    