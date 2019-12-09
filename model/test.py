# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:32:11 2019

@author: Project-C
"""


import csv
import random
def loadDataset(name):
    data = []
    with open(name, newline='') as f:
        reader = csv.reader(f)
        reader = list(reader)
    data = reader.copy()
    return data

data = loadDataset("datatest.csv")

y_all = [i[0] for i in data]
x_all = [i[1:] for i in data]

import pickle
bssid_token = pickle.load(open("BSSID_pleno", 'rb'))

bssid_token = {"c4:a3:66:ba:07:be" : 0, "98:de:d0:ed:3f:24" : 1,
               "fc:ec:da:47:11:17":2, "fc:ec:da:47:15:3b": 3}
x_true = []
for j in range(len(x_all)):
    x_temp = [0 for i in range(len(bssid_token))]
    for i in range(0,len(x_all[j]),2):
        if x_all[j][i] in bssid_token.keys():
            x_temp[bssid_token[x_all[j][i]]] = x_all[j][i+1]
    x_true.append(x_temp)
            

model = pickle.load(open("model_forest_pleno", 'rb'))

y_pred = model.predict(x_true)
y_test = y_all

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
