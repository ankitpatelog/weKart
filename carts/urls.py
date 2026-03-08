from django.urls import path
from . import views
# Create your urls here.

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/',views.remove_cart,name='remove_cart'),
    path('remove_whole/<int:product_id>/',views.remove_whole,name='remove_whole'),
]
