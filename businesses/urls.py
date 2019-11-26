from django.urls import path
from . import views

app_name = "businesses"

urlpatterns = [
    path("", views.BusinessListView.as_view(), name="list"),
    path("create/", views.CreateBusinessView.as_view(), name="create"),
    path("<int:pk>/photos/add/", views.AddPhotoView.as_view(), name="add-photos",),
]

