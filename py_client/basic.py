import requests

endpoint = 'http://localhost:8000/api/'
res = requests.post(endpoint, params={'abc': 123}, json={'title': 'Hello title', 'content': 'Hello content'})
print(res.json())