from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100,unique=True)
    description =  models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories' , blank=True)
    
    class Meta:
        verbose_name = 'category' # the default name inside the admin model
        verbose_name_plural = 'categories' # new model assigned name in admin panel
    
    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate if empty
            self.slug = slugify(self.category_name) 
        super().save(*args, **kwargs)
        
    # Source - https://stackoverflow.com/a/70705995
# Posted by Vkash Poudel
# Retrieved 2026-03-01, License - CC BY-SA 4.0

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, is_staff=True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return
