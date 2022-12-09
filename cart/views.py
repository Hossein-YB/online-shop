from django.shortcuts import render, get_object_or_404, redirect
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
