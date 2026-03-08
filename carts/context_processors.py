from carts.models import Cart,CartItem
from .views import get_cart_id

def cart_count(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
          cart = Cart.objects.filter(cart_id = get_cart_id(request))
          if request.user.is_authenticated:
                cart_item = CartItem.objects.all().filter(user = request.user)
                for item in cart_item:
                    cart_count += item.quantity       
        except Cart.DoesNotExist:
            cart_count =0
    return dict(cart_count = cart_count)