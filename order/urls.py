from django.urls import path
from .views import order_detail_view

app_name = 'order'

urlpatterns = [
    path('', order_detail_view, name='order_detail')
]

