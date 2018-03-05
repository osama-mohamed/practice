from django.shortcuts import render
import json
import requests

from .forms import LocationForm

URL = 'https://www.google.com/maps/embed/v1/directions?' \
      'key=AIzaSyDyahJ9vyi0ptBQCc8ZQXwo-PvUvEtJcR8' \
      '&origin=Oslo+Norway' \
      '&destination=Telemark+Norway'


def home(request):
    form = LocationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        first_location = form.cleaned_data.get('first_location')
        second_location = form.cleaned_data.get('second_location')
        context = {
            'form': form,
            'first_location': first_location,
            'second_location': second_location,
        }
        return render(request, 'index.html', context)
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
