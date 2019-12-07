from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView, View
from posts import models as post_models
from users import models as user_models
from . import models as comment_models
from . import forms


class CommentListView(View):
    def get(self, request):
        return render(request, "comments/comment_list.html", {'user_obj': request.user})


class CreateCommentView(View):
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

