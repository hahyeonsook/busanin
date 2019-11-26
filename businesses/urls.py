from django.urls import path
from . import views

app_name = "businesses"

urlpatterns = [
    path("", views.BusinessListView.as_view(), name="list"),
    path("create/", views.CreateBusinessView.as_view(), name="create"),
    path("<int:pk>/", views.BusinessDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditBusinessView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.BusinessPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add/", views.AddPhotoView.as_view(), name="add-photos",),
    path(
        "<int:business_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photos",
    ),
    path(
        "<int:business_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photos",
    ),
    path("<int:pk>/delete/", views.DeleteBusinessView.as_view(), name="delete"),
]

