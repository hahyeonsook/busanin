from django.views.generic import ListView, DetailView

from . import models
from comments import forms as comments_forms


class HomeView(ListView):

    """ HomeView 정의 """

    model = models.Post
    paginate_by = 12
    ordering = "created"
    paginate_orphans = 6
    context_object_name = "posts"


class PostDetail(DetailView):

    """ Post Detail View """

    model = models.Post

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        photos = self.object.photos.all().order_by("-created")

        context["form"] = comments_forms.CreateCommentForm()
        context["photos"] = photos
        return self.render_to_response(context)

