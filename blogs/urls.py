from django.urls import path
from .views import BlogView, get_user_search, PostDetailView, PostListView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name="home_blog"),
    path('search/', get_user_search, name="search_in_blog"),
    path('posts/<int:pk>/', PostListView.as_view(), name="blog_post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('blognotfind/', PostDetailView.as_view(), name="not_find_page"),
]
