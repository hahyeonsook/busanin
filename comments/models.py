from django.db import models
from core import models as core_models


class Comment(core_models.TimeStampedModel):

    """ Comment Model Definition """

    comment = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.name} - {self.comment}"
