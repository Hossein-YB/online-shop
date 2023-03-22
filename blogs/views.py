
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_GET
from .models import BlogCategories, Post
from .forms import FormSearch


def blog_404(request):
    return render(request, 'blogs/blog_404.html')


class BlogView(generic.ListView):
    model = Post
    paginate_by = 20
    context_object_name = 'posts'
    template_name = 'blogs/home_blog.html'


@require_GET
def get_user_search(request):
    form_search = FormSearch(request.GET, )

    if form_search.is_valid():
        search_word = request.GET.get('title')

        posts = Post.searchst_with_word(search_word)
        for i in posts:
            print(i)
        return render(request, template_name="blogs/blog_post_list.html", context={
            'posts': posts,
            'search_word': search_word,
        })
    else:
        return reverse('blog:not_find_page')


class PostListView(generic.ListView):
    pass


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, template_name="blogs/blog-post-detail.html", context={'post': post})
