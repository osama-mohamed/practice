from django.urls import path
from .views import (
  CreateHotelAPIView,
  ListHotelAPIView,
  DetailHotelAPIView,
  UpdateHotelAPIView,
  DeleteHotelAPIView,
  ListHotelSearchAPIView,
)

app_name = 'hotels_api'

urlpatterns = [
  path("<int:pk>/", DetailHotelAPIView.as_view(), name="detail"),
  path('', ListHotelAPIView.as_view(), name='all'),
  path('search/', ListHotelSearchAPIView.as_view(), name='search'),
  path("create/", CreateHotelAPIView.as_view(), name="create"),
  path("update/<int:pk>/", UpdateHotelAPIView.as_view(), name="update"),
  path("delete/<int:pk>/", DeleteHotelAPIView.as_view(), name="delete"),
]