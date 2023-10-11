from django.shortcuts import render, get_object_or_404


from .models import Product
# Create your views here.


def products_list_view(request):
  qs = Product.objects.all()
  context = {
    'object_list': qs
  }
  return render(request, 'products/list-view.html', context)


def product_detail_view(request, id):
  obj = get_object_or_404(Product, id=id)
  context = {
    'object': obj
  }
  return render(request, 'products/detail-view.html', context)

def product_detail_slug_view(request, slug):
  obj = get_object_or_404(Product, slug=slug)
  context = {
    'object': obj
  }
  return render(request, 'products/detail-view.html', context)