from django.shortcuts import redirect, get_object_or_404,render
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Enrollment

@login_required(login_url='login')
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('course_list')


@login_required(login_url='login')
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'my_courses.html', {'enrollments': enrollments})