from django.views.generic import View, ListView
from django.views.decorators.http import require_http_methods
from django.shortcuts import render


@require_http_methods(['GET']) # only allow GET requests
def product_list_view(request):
  return render(request, 'temp', {})


class ProductHomeView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'temp', {})
  
  def post(self, request, *args, **kwargs):
    return render(request, 'temp', {})

class ProductListView(ListView):
  # model = Product
  queryset = Product.objects.all()
  template_name = 'temp'

ProductListView.as_view()
