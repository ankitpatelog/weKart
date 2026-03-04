from django.shortcuts import render
from category.models import Category
from stores.models import Products
from django.shortcuts import render,get_object_or_404

# Create your views here.

def store(request, category_slug=None):

    if category_slug != None:
        # show products according to category slug
        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
        categories = Category.objects.all()
        products = Products.objects.filter(is_available=True)
        product_count = products.count()

    categories = Category.objects.all()
    
    context = {
        "categories_all": categories,
        "products": products,
        "product_count": product_count,
    }

    return render(request, "store.html", context)


def product_detail(request , category_slug,product_slug):
    return render(request,'store/product_detail.html')