from django.shortcuts import render
import json
import requests

from .forms import UrlForm

API_KEY = 'AIzaSyBQt54uGw2lsD22LLgyiiHnL9M9IjB8BIg'
URL = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(API_KEY)


def home(request):
    form = UrlForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        url = form.cleaned_data.get('url')
        long_url = {'longUrl': url}
        headers = {'content-type': 'application/json'}
        response = requests.post(URL, data=json.dumps(long_url), headers=headers).json()
        context = {
            'url': response,
            'form': form,
        }
        return render(request, 'index.html', context)
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
