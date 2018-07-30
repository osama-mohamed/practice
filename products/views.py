from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here. 
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         # Product.objects.create(title=my_new_title)
#     context = {
        
#     }
#     return render(request, 'products/product_create.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    # qs = Product.objects.get(id=1)
    # context = {
    #     'title': qs.title,
    #     'description': qs.description,
    #     'price': qs.price,
    #     'id': qs.id,
    #     'summary': qs.summary,
    #     'featured': qs.featured
    # }
    context = {
        # 'object': qs
    }
    # return render(request, 'product/detail.html', context)
    return render(request, 'products/product_detail.html', context)