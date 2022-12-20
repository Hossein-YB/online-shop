from django.shortcuts import render


def order_detail_view(request):
    return render(request, 'orders/order_detail.html')

