from django.urls import path

from .views import contact

app_name = 'contacts'

urlpatterns = [
  path('contact', contact, name='contact')
]
