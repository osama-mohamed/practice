import requests

endpoint = 'http://localhost:8000/api/products/create/'

data = {
  'title': 'product title',
  'price': 19.99,
}
res = requests.post(endpoint, json=data)
print(res.json())