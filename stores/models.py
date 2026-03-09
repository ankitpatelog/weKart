from django.db import models
from category.models import Category 
from django.urls import reverse
from django.contrib import admin

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)  
    modified_date = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_date']
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self.product_name
    
# nwo make the variation model so admin can add the variations btw color and size
    
# choices 
# djanog always uses tupel inside tuple so to iterate and show the vallues inside the admin panel
variaton_category_variatioin = (
    ('color','color'),
    ('size','size'),
)

# we are making the variation manager class when the frontend ,we want to show the color and size of each product then from color method inside the class we get all the 
# values of particular color and if active or not and  show into the frontend using the method when we call it

class VariationManager(models.Manager):
    def colors(self):
        return super(self,VariationManager).filter(variation_category = 'color', is_active="True")

    def size(self):
        return super(self,VariationManager).filter(variaton_category = 'size', is_active="True")

    
class Variation(models.Model):
    product             = models.ForeignKey(Products,on_delete=models.CASCADE)
    variation_category  = models.CharField(max_length=100,choices=variaton_category_variatioin)
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
    