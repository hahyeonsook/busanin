from django.urls import path

from . import views

app_name = "conversations"


urlpatterns = [
    path("list/", views.ConversationListView.as_view(), name="list"),
    path("go/<int:a_pk>/<int:b_pk>/", views.GoConversationView.as_view(), name="go"),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
]
