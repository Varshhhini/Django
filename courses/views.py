from django.shortcuts import render, redirect
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {
        'courses': courses
    })


def course_detail(request, id):
    course = Course.objects.filter(id=id).first()

    if not course:
        return redirect('course_list')  

    return render(request, 'courses/course_detail.html', {
        'course': course
    })
