from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from posts import models as post_models
from . import models as comment_models
from . import forms as comment_forms


def create_comment(request, post):
    if request.method == "POST":
        form = comment_forms.CreateCommentForm(request.POST)
        post = post_models.Post.objects.get(pk=post)
        if not post:
            return redirect(reverse("core:home"))
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))


class EditCommentView(UpdateView):

    model = comment_models.Comment
    template_name = "comments/comment_edit.html"
    fields = [
        "comment",
    ]
    success_url = reverse_lazy("core:home")


class DeleteCommentView(DeleteView):

    model = comment_models.Comment
    template_name = "comments/comment_delete.html"
    success_url = reverse_lazy("core:home")

