from django.urls import path
from .views import HomePageView, AboutUSPage
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('aboutus/', AboutUSPage.as_view(), name="about_us"),
]
