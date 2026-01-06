from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Cart

@login_required(login_url='login')
def add_to_cart(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        course=course
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required(login_url='login')
def cart_view(request):
    items = Cart.objects.filter(user=request.user)

    total = 0
    for item in items:
        total += item.course.price * item.quantity

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


@login_required(login_url='login')
def remove_from_cart(request, course_id):
    item = get_object_or_404(
        Cart,
        user=request.user,
        course_id=course_id
    )
    item.delete()
    return redirect('cart')
