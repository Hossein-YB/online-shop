from django.urls import path
from .views import cart_detail_view, add_to_cart_view, remove_from_cart_view, clear_cart_view

app_name = 'cart'


urlpatterns = [
    path('', cart_detail_view, name="cart_detail"),
    path('add/<int:product_id>/', add_to_cart_view, name="add_to_cart"),
    path('remove/<int:product_id>/', remove_from_cart_view, name="remove_from_cart"),
    path('clear/', clear_cart_view, name="clear_cart"),
]
