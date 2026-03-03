from django.shortcuts import render
from stores.models import Products 

def home(request):
    prodcuts = Products.objects.filter(is_available=True)
    
    context = {
        'products' : prodcuts
    }
    
    return render(request,'home.html',context)