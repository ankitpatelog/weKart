from django.shortcuts import render
from . models import Cart,CartItem
from stores.models import Products
from django.shortcuts import redirect

# Create your views here.

# func for getting the current card_id 

def get_cart_id(request):
    cart = request.session.session_key # take out hte session for the particular request
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request,product_id):
    # fucntion of this function
    # this add_cart add the porduct into the available cart or new cart 
    
    product = Products.objects.get(id=product_id)
    
    # get the current cart form session or make the new one if not available
    try:
        cart = Cart.objects.get(cart_id = get_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = get_cart_id(request)
        )
        cart.save()
        
        # now at this point we have the product and cart ,now add them into cart
        
    try:
    #   now get the clicked product and increment its quantity by 1
        cart_item = CartItem.objects.get(product = product,cart = cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        # if the product is adding for the first time then makethe quantity by 1
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    
    # print(cart_item.product)
    # print(cart_item.cart.cart_id)
    return redirect('cart')
        
def cart(request):
    # get sessioin token which is the cart_id 
    cart_id = request.session.session_key
    
    total = 0
    quantitty = 0
    
    try:
        cart = Cart.objects.get(cart_id = cart_id)
        cart_item = CartItem.objects.filter(cart=cart,is_active = True)
        
        for item in cart_item:
            total += (item.product.price * item.quantity)
            quantitty += item.quantity    
         
    except Cart.DoesNotExist:
        cart = None
    
    context = {
        'cart' : cart,
        'total' : total,
        'quantitty' : quantitty
    }
    return render(request,'store/cart.html',context)