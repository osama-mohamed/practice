import requests

endpoint = 'http://localhost:8000/api/products/'
res = requests.get(endpoint)
print(res.json())