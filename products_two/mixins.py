class ProductTemplateMixin(object):
  title = 'Products'
  template_name = 'products/product_list.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['title'] = self.get_title()
    return context
  
  def get_title(self):
    return self.title