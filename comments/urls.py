from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("<int:pk>/edit/", views.EditCommentView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeleteCommentView.as_view(), name="delete"),
    path("create/<int:post>/", views.create_comment, name="create"),
]
