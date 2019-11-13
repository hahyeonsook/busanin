from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Post
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "posts"


class PostDetail(DetailView):

    """ PostDetail Definition """

    model = models.Post
