from django import template
from blogs.models import BlogCategories
register = template.Library()


@register.filter
def categories(request):
    category_query = BlogCategories.get_top_category()
    return category_query




