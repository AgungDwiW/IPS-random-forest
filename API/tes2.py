#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:17:27 2019

@author: temperantia
"""
import requests
import json
data = {"c4:a3:66:ba:07:be":"-89",
            "98:de:d0:ed:3f:24":"-86",
            "4c:5e:0c:9d:fb:ff":"-90",
            "fc:ec:da:47:11:17":"-76",
            "04:18:d6:ad:04:71":"-79",
            "64:70:02:3f:4e:59":"-88",
            "fc:ec:da:47:15:3b":"-60",
            "fc:ec:da:47:0d:7f":"-80"}
data = json.dumps(data)
req = requests.post("http://127.0.0.1:5000/api", json=data)
