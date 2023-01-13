from django.shortcuts import render, redirect
from orders.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
@login_required(login_url='login')
def add_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
        cart_id =_cart_id(request))
        cart.save(),
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item =CartItem.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart_detail')
@login_required(login_url='login')
def cart_detail(request):
    total=0
    counter=0
    cart_items=None
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items =  CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    context = {
    'cart_items': cart_items,
    'total':total,
    'counter': counter
    }

    return render(request,'cart.html', context)
