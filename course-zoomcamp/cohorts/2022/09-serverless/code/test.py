import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

#data = {'url': 'http://bit.ly/mlbookcamp-pants'}
data = {'url': 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'}
#data = {'url': 'https://commons.wikimedia.org/wiki/Dog#/media/File:Yellow_Labrador_Retriever_2.jpg'}

result = requests.post(url, json=data).json()
print(result)