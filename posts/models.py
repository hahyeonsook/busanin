from django.db import models
from core import models as core_models

# from businesses import models as business_models


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80, blank=True)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Post(core_models.TimeStampedModel):

    """ Post Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField(default="")
    businesses = models.ManyToManyField(
        "businesses.Business", related_name="posts", blank=True
    )
    user = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    def count_comments(self):
        comment = self.comments.all().count()
        return comment

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
