from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.store,name = 'store'),
    path('category/<slug:category_slug>/',views.store,name= 'products_by_category'), # slug value is the category_slug
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name= 'product_detail'), #shows product page 
    path('search/', views.search, name='search'),
]