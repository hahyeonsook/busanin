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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["form"] = comments_forms.CreateCommentForm()
        return self.render_to_response(context)

