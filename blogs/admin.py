from django.contrib import admin
from .models import Blog, BlogCategories


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['title', 'user', 'datetime_modified', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(BlogCategories)
class Blog(admin.ModelAdmin):
    list_display = ['name', 'user', 'datetime_modified', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

