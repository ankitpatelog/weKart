from django.contrib import admin
from stores.models import Products,Variation


# Register your models here.

# product admin panel 
class ProductManager(admin.ModelAdmin):
    list_display = ('product_name','slug','price' ,'stock' , 'is_available','category')
    
    prepopulated_fields = {'slug': ('product_name',)} 

admin.site.register(Products,ProductManager)

# variation admin panel 
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    
admin.site.register(Variation,VariationAdmin)
