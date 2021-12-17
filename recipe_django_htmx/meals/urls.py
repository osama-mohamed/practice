from django.urls import path

from .views import (
  meal_queue_toggle_view,
)

app_name='meals'

urlpatterns = [
  path('meal-toggle/<int:recipe_id>/', meal_queue_toggle_view, name='meal-toggle'),
]
