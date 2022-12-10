from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import AddToCart
from .cart import Cart
from products.models import Products


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)
    form = AddToCart(request.POST)

    if form.is_valid():
        cleandata = form.cleaned_data
        quantity = cleandata['quantity']
        cart.add(product, quantity)

    return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, _('Your Cart is clen'))
    return redirect('cart:cart_detail')



