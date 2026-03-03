from django.shortcuts import render
from category.models import Category
from stores.models import Products

# Create your views here.

def store(request):
    categories = Category.objects.all()
    prodcuts = Products.objects.filter(is_available=True)
    product_count = prodcuts.count()
    
    context = {
        "categories" : categories,
        'products' : prodcuts,
        'product_count' : product_count,
    }
    return render(request,'store.html',context)