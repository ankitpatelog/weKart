from django.shortcuts import render
from category.models import Category
from stores.models import Products
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

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

        # pagination
        pagi_products = Products.objects.filter(is_available = True)
        paginator = Paginator(pagi_products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
    categories = Category.objects.all()
    

    context = {
        "categories_all": categories,
        "products": products,
        "product_count": product_count,
        "paged_products" : paged_products,
    }

    return render(request, "store.html", context)


def product_detail(request , category_slug,product_slug):
    # first get the single_product that matches the category slug with the prodcut slug
    try:
      single_product = get_object_or_404(Products,category__slug=category_slug , slug = product_slug) # means product ->category->slug that matches with the category-slug coming from the link and the slug of product matches  woth the product_slug comming from the product model slug
      print(single_product)
    except Exception as e:
        raise e
      
    context = {
        'single_product' : single_product,
    }
    return render(request, 'store/product_detail.html', context)