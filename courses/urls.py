from django.urls import path
from .views import (
    CourseView,
    CourseListView
    # my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    # path('', CourseView.as_view(template_name='contact.html'), name='courses_list'),
    # path('', my_fbv, name='courses_list'),
    

    # path('create/', <create_view>, name='courses_create'),
    path('<int:id>/', CourseView.as_view(), name='courses_detail'),
    # path('<int:id>/update/', <update_view>, name='courses_update'),
    # path('<int:id>/delete/', <delete_view>, name='courses_delete'),
]