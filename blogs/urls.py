from django.urls import path
from .views import BlogView, get_user_search, post_detail_view, blog_404, category_post_view

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name="home_blog"),
    path('search/', get_user_search, name="search_in_blog"),
    path('category/<int:category_id>/', category_post_view, name="blog_post_list"),
    path('post/<int:post_id>/', post_detail_view, name="post_detail"),
    path('blognotfind/', blog_404, name="not_find_page"),
]
