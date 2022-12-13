from django.contrib import admin
from .models import Products, Comments
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(ModelAdminJalaliMixin, admin.TabularInline):
    model = Comments
    fields = ['user', 'star', 'body', 'active', ]
    extra = 1
    

@admin.register(Products)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInline,
    ]

    def __str__(self):
        return self.title


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'star', 'body', 'active']

    def __str__(self):
        return self.body

