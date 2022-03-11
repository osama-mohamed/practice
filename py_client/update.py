import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
  'title': 'new product title',
  'price': 999.99,
}
res = requests.put(endpoint, json=data)
print(res.json())