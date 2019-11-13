from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class BusinessPhotoInline(admin.TabularInline):

    """ Photo Inline Define """

    model = models.Photo


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):

    """ Business Admin Definition """

    list_display = (
        "name",
        "address",
        "businessman",
        "phone",
    )

    list_filter = (
        "name",
        "address",
        "businessman",
    )

    search_fields = (
        "^businessman__username",
        "address",
    )

    inlines = [
        BusinessPhotoInline,
    ]


@admin.register(models.Photo)
class BusinessPhotoAdmin(admin.ModelAdmin):

    """ Business Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
