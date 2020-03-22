from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("comments/", include("comments.urls", namespace="comments")),
    path("businesses/", include("businesses.urls", namespace="businesses")),
    path("users/", include("users.urls", namespace="users")),
    path("conversations/", include("conversations.urls", namespace="conversations")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
