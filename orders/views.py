from django.shortcuts import render, redirect
from .forms import OrderForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from cart.cart import Cart
from .models import OrderProduct


@login_required
def order_detail_view(request):

    cart = Cart(request)
    order_form = OrderForms()

    if request.method == "POST":
        if len(cart) == 0:
            messages.warning(request,_("Your cart is empty"))
            return redirect('product_list')

        order_form = OrderForms(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderProduct.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()
            messages.success(request, _("successfully Pay"))

    else:
        order_form = OrderForms()

    return render(request, 'orders/order_detail.html', context={'order_form': order_form})
