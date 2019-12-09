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
    cleaned = [0 for i in range(len(bssid_token))]
    for i in bssid_token:
        cleaned[bssid_token[i]] = int(test[i])
    if len(cleaned) != len(bssid_token):
        err = {"error": "error - some AP no found"}
        return json.dumps(err)
    #try:
    print ([cleaned])
    pred = model.predict([cleaned])
    #except:
    #    err = {"error": "error - cant predict"}
    #    return json.dumps(err)
        
    ret = {"predicted": pred[0]}
    return ret
app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/api', methods=['POST'])
def predictApi():
    return predict(request.get_json())
    #return str(bc.predict())


@app.route('/test', methods=['POST'])
def test():
    print(request.get_json())
    return str(request.get_json())


if __name__ == '__main__':

    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=5000,host='0.0.0.0')
    