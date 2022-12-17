from django.contrib import admin
from .models import Order, OrderProduct
from jalali_date.admin import ModelAdminJalaliMixin


class InlineOrderAdmin(admin.TabularInline):
    model = OrderProduct
    fields = ['order', 'product', 'price', 'quantity']
    extra = 10


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Order
    list_display = ['user', 'is_paid', 'first_name', 'address', ]
    # fields = ['*']
    inlines = [
        InlineOrderAdmin,
    ]

    def __str__(self):
        return self.user


@admin.register(OrderProduct)
class OrderProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']

    def __str__(self):
        return self.order
