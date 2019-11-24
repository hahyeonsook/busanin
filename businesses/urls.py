from django.urls import path
from . import views

app_name = "businesses"

urlpatterns = [
    path("", views.BusinessList.as_view(), name="list"),
    path("update/", views.UpdateBusinessView.as_view(), name="update"),
    path("delete/", views.DeleteBusinessView.as_view(), name="delete"),
    path("<int:pk>/", views.BusinessDetail.as_view(), name="detail"),
]

