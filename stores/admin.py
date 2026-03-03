from django.contrib import admin
from . models import Products

# Register your models here.

class ProductManager(admin.ModelAdmin):
    list_display = ('product_name','slug','price' ,'stock' , 'is_available','category')
    
    prepopulated_fields = {'slug': ('product_name',)} 

admin.site.register(Products,ProductManager)
