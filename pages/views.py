from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Post
from products.models import Products


def home_page_view(request):
    products = Products.objects.all().order_by("-datetime_created")[:8]
    posts = Post.get_posts(4)
    return render(request, 'home.html', context={'posts': posts, 'products': products})


class AboutUSPage(TemplateView):
    template_name = 'pages/aboutus.html'

