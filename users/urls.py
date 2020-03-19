from django.urls import path
from conversations import views as conv_views
from . import views

app_name = "users"

urlpatterns = [
    path("leave/", views.SignOutView.as_view(), name="leave"),
    path("leave/kakao/", views.kakao_leave, name="kakao-leave"),
    path(
        "leave/kakao/callback/", views.kakao_leave_callback, name="kakao-leave-callback"
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github/", views.github_login, name="github-login"),
    path("login/github/callback/", views.github_callback, name="github-callback"),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path(
        "login/kakao/callback/", views.kakao_login_callback, name="kakao-login-callback"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "verify/<str:key>/",
        views.CompleteVerificationView.as_view(),
        name="complete-verification",
    ),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]
