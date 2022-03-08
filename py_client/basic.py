import requests

endpoint = 'http://localhost:8000/api/'
res = requests.get(endpoint, params={'abc': 123}, json={'query': 'Hello OSAMA'})
# print(res.json())