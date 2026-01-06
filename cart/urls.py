from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:course_id>/', remove_from_cart, name='remove_from_cart'),
]
