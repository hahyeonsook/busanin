from django.urls import path
from posts import views as posts_views
from . import views

app_name = "core"

urlpatterns = [
    path("", posts_views.HomeView.as_view(), name="home"),
    path("search/", views.SearchView.as_view(), name="search"),
]

