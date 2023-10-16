from django.views.generic import ListView, DetailView


from .models import Product

class ProductListView(ListView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_list.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    return context


class ProductDetailView(DetailView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_detail.html'
