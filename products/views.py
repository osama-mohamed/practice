from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class HomeListView(ListView):
    queryset = Product.objects.all().order_by('-id')
    template_name = 'home.html'
