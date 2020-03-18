from django.db import models
from core.models import TimeStampedModel
from users import models as users_model


class Comment(TimeStampedModel):

    """ Comment Model Definition """

    comment = models.TextField()
    user = models.ForeignKey(
        "users.User",
        related_name="comments",
        on_delete=models.SET(users_model.set_FkUser),
    )
    post = models.ForeignKey(
        "posts.Post", related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.post.name} - {self.comment} by {self.user.username}"
