from flask import Blueprint
from flask import render_template
from flask import request
from os import remove
from werkzeug import secure_filename
from flask import Flask, redirect, url_for
import pickle
import json

"""
predictor
"""
bssid_token = pickle.load(open("BSSID_pleno", 'rb'))
model = pickle.load(open("model_forest_pleno", 'rb'))

def predict(test):
    test = json.loads(test)
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
    pred = model.predict([cleaned])
    #except:
    #    err = {"error": "error - cant predict"}
    #    return json.dumps(err)
        
    ret = {"predicted": pred[0]}
    return ret

"""
controller
"""
WebApp = Blueprint("controller",__name__)

@WebApp.route('/api', methods=['POST'])
def index():
    return predict(request.get_json())
    #return str(bc.predict())

@WebApp.route('/test', methods=['POST'])
def test():
    print(request.get_json())
    return request.get_json()
