from django.contrib import admin
from django.utils.html import mark_safe
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
        'created',
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

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
