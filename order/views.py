from django.shortcuts import render


def order_detail_view(request):
    return render(request, 'order/order_detail.html', )