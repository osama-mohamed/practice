import requests

endpoint = 'https://httpbin.org/anything'
res = requests.get(endpoint, json={'query': 'Hello OSAMA'})
print(res.json())
print(res.status_code)