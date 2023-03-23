from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.views.decorators.http import require_GET
from django.utils.translation import gettext as _
from .models import Post
from .forms import FormSearch


def blog_404(request):
    text = _("Oops! The searched article was not found")
    posts = Post.get_top_post(4)
    return render(request, template_name='blogs/blog_404.html', context={
        'posts': posts,
        'text': text
    })


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
        posts = Post.search_post_with_word(search_word)
        return render(request, template_name="blogs/blog_post_list.html", context={
            'posts': posts,
            'search_word': search_word,
        })
    else:
        return reverse('blog:not_find_page')


def category_post_view(request, category_id):
    posts = Post.get_by_category(category_id)
    if posts:
        return render(request, template_name="blogs/blog_post_list.html", context={
            'posts': posts
        })
    else:
        return redirect("blog:not_find_page")


def post_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, template_name="blogs/blog-post-detail.html", context={'post': post})
    except Post.DoesNotExist:
        return redirect("blog:not_find_page")
