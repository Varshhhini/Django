from django.urls import path
from .views import course_list, course_detail

urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:id>/', course_detail, name='course_detail'),
]
