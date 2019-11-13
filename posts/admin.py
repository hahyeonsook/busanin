from django.contrib import admin
from . import models


class PostPhotoInline(admin.TabularInline):

    """ Post Photo Inline Definition """

    model = models.Photo


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """ Post Admin Definition """

    list_display = (
        "user",
        "name",
        "businesses",
    )

    list_filter = (
        "user",
        "businesses",
    )

    search_fields = (
        "^user__username",
        "name",
        "businesses",
    )

    inlines = [
        PostPhotoInline,
    ]


@admin.register(models.Photo)
class PostPhotoAdmin(admin.ModelAdmin):

    """ Post Photo Admin Definition """

    pass
