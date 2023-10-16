from django.views.generic import ListView, DetailView


from .models import Product, DigitalProduct



class DigitalProductListView(ListView):
  model = DigitalProduct
  template_name = 'products/product_list.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['title'] = 'Digital Downloads'
    return context # digitalproduct_list

class ProductListView(ListView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_list.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['title'] = 'Products'
    return context # product_list


class ProductDetailView(DetailView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_detail.html'
