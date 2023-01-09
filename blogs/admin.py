from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['title', 'user', 'datetime_modified', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

