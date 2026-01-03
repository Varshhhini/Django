from django.urls import path
from .views import enroll_course,my_courses

urlpatterns = [
    path('<int:course_id>/', enroll_course, name='enroll'),
    path('my_courses/', my_courses, name='my_courses'),
]
