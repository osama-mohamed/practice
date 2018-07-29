from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    context = {
        'my_text': 'this a test text',
        'my_number': 123,
        'my_list': [123, 456, 789]
    }
    return render(request, 'about.html', context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
