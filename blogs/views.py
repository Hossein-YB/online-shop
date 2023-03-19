from django.shortcuts import render
from django.views import generic
from .models import BlogCategories, Post
from .forms import FormSearch


def home_blog_view(request):
    category_query = BlogCategories.get_top_category()
    for i in category_query:
        print(i)
    return render(request, template_name="blogs/home_blog.html", context={
        'categories': category_query,
    })


def get_user_search(request):
    title = FormSearch(request.GET, )
    if title.is_valid():
        title = request.GET.get('title')
        posts = Post.search_in_titles(title)

    return render(request, template_name="blogs/blog_post_list.html", context={
        'posts': posts
    })



class PostListView(generic.ListView):
    pass

class PostDetailView(generic.DetailView):
    pass


