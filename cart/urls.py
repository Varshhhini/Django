from django.urls import path
from .views import add_to_cart, cart_view

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:course_id>/', add_to_cart, name='add_to_cart'),
]
