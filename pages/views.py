from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Post


def home_page_view(request):

    posts = Post.get_posts(4)
    return render(request, 'home.html', context={'posts': posts})


class AboutUSPage(TemplateView):
    template_name = 'pages/aboutus.html'

