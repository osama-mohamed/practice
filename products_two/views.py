from django.views.generic import ListView, DetailView


from .models import Product

class ProductListView(ListView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_detail.html'
