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


@admin.register(models.Photo)
class BusinessPhotoAdmin(admin.ModelAdmin):

    """ Business Photo Admin Definition """

    list_display = ("__str__",)
