from django.urls import path

from .views import register, login, logout, dashboard

app_name = 'accounts'

urlpatterns = [
  path('login', login, name='login'),
  path('register', register, name='register'),
  path('logout', logout, name='logout'),
  path('dashboard', dashboard, name='dashboard')
]
