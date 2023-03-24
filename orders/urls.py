from django.urls import path
from .views import order_detail_view

urlpatterns = [
    path('', order_detail_view, name="order_detail")
]