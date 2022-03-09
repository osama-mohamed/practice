from django.http import JsonResponse
from products.models import Product
import json


def api_home(request, *args, **kwargs):
  # body = request.body
  # data = {}
  # try:
  #   data = json.loads(body)
  # except:
  #   pass
  # data['params'] = dict(request.GET)
  # data['headers'] = dict(request.headers)
  # data['content_type'] = request.content_type
  model_data = Product.objects.all().order_by('?').first()
  data = {}
  if model_data:
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
  return JsonResponse(data)