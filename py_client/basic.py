import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/'
res = requests.get(endpoint, json={'query': 'Hello OSAMA'})
# print(res.json())
print(res.status_code)