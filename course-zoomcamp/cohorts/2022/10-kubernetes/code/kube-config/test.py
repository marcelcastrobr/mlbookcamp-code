#/bin/python3
import requests

data = {
    #"url": "http://bit.ly/mlbookcamp-pants" # pants
    "url": "https://raw.githubusercontent.com/alexeygrigorev/clothing-dataset-small/master/test/dress/06a00c0f-5f9a-410d-a7da-3881a9df3a71.jpg" # dress
}

#url = "http://localhost:8500/2015-03-31/functions/function/invocations"
#url = "https://0a1v3fyo2m.execute-api.eu-west-1.amazonaws.com/test/predict"
#url = 'http://localhost:9696/predict'
url = 'http://a486906cbe40d47788f03bb9cf5454ed-1247452604.eu-west-1.elb.amazonaws.com/predict'

results = requests.post(url, json=data).json()

print(results)