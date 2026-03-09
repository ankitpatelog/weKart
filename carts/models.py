from django.db import models
from accounts.models import Accounts
from stores.models import Products,Variation

# from accounts.models import Accounts

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        total_price = self.quantity * self.product.price
        return total_price
    
    def inc_product(self):
        prev_quantity = self.quantity
        # update the db with the +1 value from the prev_quantity
        self.quantity = prev_quantity + 1
        self.save()
        
    def dec_product(self):
        prev_quantity = self.quantity
        # update the db with the +1 value from the prev_quantity
        self.quantity = prev_quantity -1
        self.save()
    
    
    def __str__(self):
        return self.product.product_name
    
    # we will store the cart id in sessions int he browser and get the cart id from it and fetcj the cart items form it 
    
    
    