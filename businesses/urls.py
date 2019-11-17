from django.urls import path
from . import views

app_name = "businesses"

urlpatterns = [
    path("", views.BusinessList.as_view(), name="home"),
    path("<int:pk>", views.BusinessDetail.as_view(), name="detail"),
]

