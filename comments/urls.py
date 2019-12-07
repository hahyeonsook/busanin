from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("list/", views.CommentListView.as_view(), name="list"),
    path("<int:pk>/edit/", views.EditCommentView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeleteCommentView.as_view(), name="delete"),
    path("create/<int:post>/", views.CreateCommentView.as_view(), name="create"),
]
