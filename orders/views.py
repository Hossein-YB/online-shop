import requests
from django.shortcuts import render
from .forms import OrderForms
from django.contrib.auth.decorators import login_required


@login_required
def order_detail_view(request):

    if request.method == "POST":

        order_form = OrderForms(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

    else:
        order_form = OrderForms()

    return render(request, 'orders/order_detail.html', context={'order_form': order_form})
