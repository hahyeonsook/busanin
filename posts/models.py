from django.db import models
from core import models as core_models

# from businesses import models as business_models


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80, blank=True)
    file = models.ImageField()
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Post(core_models.TimeStampedModel):

    """ Post Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField(default="")
    businesses = models.ForeignKey(
        "businesses.Business", related_name="posts", on_delete=models.PROTECT, null=True
    )
    user = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
