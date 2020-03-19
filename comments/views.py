from django.contrib import messages
from django.shortcuts import redirect, reverse, render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, View

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from posts import models as post_models
from . import models as comment_models
from . import forms
from core import mixins


class CommentListView(View):

    """ Comment List View """

    def get(self, request):
        return render(request, "comments/comment_list.html", {"user_obj": request.user})


class CreateCommentView(mixins.LoggedInOnlyMixin, SuccessMessageMixin, View):

    """ Create Comment View """

    def post(self, request, post):
        if request.method == "POST":
            comment = request.POST
            form = forms.CreateCommentForm(request.POST)
            post = post_models.Post.objects.get(pk=post)
            if not post:
                return redirect(reverse("core:home"))
            if form.is_valid():
                comment = form.save()
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))


class EditCommentView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    """ Edit Comment View """

    model = comment_models.Comment
    template_name = "comments/comment_edit.html"
    fields = [
        "comment",
    ]
    success_message = "댓글이 수정되었습니다!"

    # Comment Author가 아니면 접근할 수 없도록 Mixin
    def test_func(self):
        comment = comment_models.Comment.objects.get(pk=self.kwargs.get("pk"))
        return self.request.user == comment.user

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return redirect("core:home")

    def get_success_url(self, **kwargs):
        comment = comment_models.Comment.objects.get(pk=self.kwargs.get("pk"))
        return reverse_lazy("posts:detail", kwargs={"pk": comment.post.pk})


class DeleteCommentView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    """ Delete Comment View """

    model = comment_models.Comment
    template_name = "comments/comment_delete.html"
    success_message = "댓글이 삭제되었습니다."

    # Comment Author가 아니면 접근할 수 없도록 Mixin
    def test_func(self):
        comment = comment_models.Comment.objects.get(pk=self.kwargs.get("pk"))
        return self.request.user == comment.user

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return redirect("core:home")

    def get_success_url(self, **kwargs):
        comment = comment_models.Comment.objects.get(pk=self.kwargs.get("pk"))
        return reverse_lazy("posts:detail", kwargs={"pk": comment.post.pk})
