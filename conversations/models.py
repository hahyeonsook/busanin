from django.db import models
from core.models import TimeStampedModel
from users import models as users_model


class Conversation(TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"

    def get_participants(self):
        users = {}
        for user in self.participants.all():
            users[f"user.pk"] = user
        return users


class Message(TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation",
        related_name="messages",
        on_delete=models.SET(users_model.set_FkUser),
    )

    def __str__(self):
        return f"{self.message}"
