from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Cart

@login_required(login_url='login')
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Cart.objects.get_or_create(user=request.user, course=course)
    return redirect('cart')

@login_required(login_url='login')
def cart_view(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'items': items})
