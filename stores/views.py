from django.shortcuts import render
from category.models import Category
from stores.models import Products
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def store(request, category_slug=None):

    # filter products by category if slug exists
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category, is_available=True)
    else:
        products = Products.objects.filter(is_available=True)

    # product count
    product_count = products.count()

    # pagination
    paginator = Paginator(products, 6)   # 6 products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    # get all categories for sidebar/menu
    categories = Category.objects.all()

    context = {
        "categories_all": categories,
        "products": paged_products,
        "product_count": product_count,
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

def search(request):

    products = None
    product_count = 0

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')

        if keyword:
            products = Products.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword)
            )

            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store.html', context)