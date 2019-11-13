from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """ Post Admin Definition """

    pass


@admin.register(models.Photo)
class PostPhotoAdmin(admin.ModelAdmin):

    """ Post Photo Admin Definition """

    pass
