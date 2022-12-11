from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import AddToCart
from .cart import Cart
from products.models import Products


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCart(initial={
            'inplace': True,
            'quantity': item['quantity']
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)
    form = AddToCart(request.POST)

    if form.is_valid():
        cleandata = form.cleaned_data
        quantity = cleandata['quantity']
        cart.add(product, quantity, replace_quantity=cleandata['inplace'])

    return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')



