from django.contrib import admin
from .models import Products, Comments


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']

    def __str__(self):
        return self.title


@admin.register(Comments)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'star', 'body', 'active']

    def __str__(self):
        return self.body

