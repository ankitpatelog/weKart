from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True)
    description =  models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories' , blank=True)
    
    class Meta:
        verbose_name = 'category' # the default name inside the admin model
        verbose_name_plural = 'categories' # new model assigned name in admin panel
    
    
    # create URL using: reverse create url using url pattern name and the fields you passed inside the reverse
    # products_by_category + slug      
    def get_url(self):
        return reverse('products_by_category',args = [self.slug])#each category has own its slug so use this to make the link and used by href in the store.html 
    
    def __str__(self):
        return self.category_name
        

