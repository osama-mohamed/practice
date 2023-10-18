from django.views.generic import ListView, DetailView


from .models import Product, DigitalProduct



class ProductTemplateMixin(object):
  title = None
  template_name = 'products/product_list.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['title'] = self.title
    return context

class DigitalProductListView(ProductTemplateMixin, ListView):
  model = DigitalProduct
  title = 'Digital Products'


class ProductListView(ProductTemplateMixin, ListView):
  model = Product
  title = 'Products'


class ProductDetailView(DetailView):
  # queryset = Product.objects.all()
  model = Product
  template_name = 'products/product_detail.html'
