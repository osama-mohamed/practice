from django.shortcuts import render

from .forms import LocationForm


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
