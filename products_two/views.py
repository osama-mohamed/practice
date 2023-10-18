from django.views.generic import ListView, DetailView


from .models import Product, DigitalProduct
from .mixins import ProductTemplateMixin


class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct

  def get_title(self):
    return 'Digital Products'


class ProductListView(ProductTemplateMixin, ListView):
  model = Product


class ProductDetailView(ProductTemplateMixin, DetailView):
  model = Product
  template_name = 'products/product_detail.html'

  def get_title(self):
    return self.get_object().title
