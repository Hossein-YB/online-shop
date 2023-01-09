from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Blog


def home_page_view(request):
    blog_post = Blog.objects.order_by('-datetime_created')[:4]
    return render(request, 'home.html', {'blog': blog_post})


class AboutUSPage(TemplateView):
    template_name = 'pages/aboutus.html'

