from django.urls import path
from django import views
# Create your urls here.

urlpatterns = [
    path('cart/',views.cart,name='cart')
]
