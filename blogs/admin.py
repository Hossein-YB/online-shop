from django.contrib import admin
from .models import Post, BlogCategories, CategorySearchHistory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'user', 'datetime_modified', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(BlogCategories)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'count_search', 'user', 'datetime_modified', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(CategorySearchHistory)
class CategorySearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'category']

