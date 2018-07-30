from django.shortcuts import render

from .models import Product

# Create your views here. 
def product_detail_view(request):
    qs = Product.objects.get(id=1)
    # context = {
    #     'title': qs.title,
    #     'description': qs.description,
    #     'price': qs.price,
    #     'id': qs.id,
    #     'summary': qs.summary,
    #     'featured': qs.featured
    # }
    context = {
        'object': qs
    }
    # return render(request, 'product/detail.html', context)
    return render(request, 'products/product_detail.html', context)