from django.urls import path
from .views import home_page_view, AboutUSPage

urlpatterns = [
    path('', home_page_view, name="home"),
    path('aboutus/', AboutUSPage.as_view(), name="about_us"),
]
