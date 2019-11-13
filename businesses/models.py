from django.db import models
from phone_field import PhoneField
from core import models as core_models


class Photo(core_models.TimeStampedModel):

    """ Business Photo Model Definition """

    caption = models.CharField(max_length=80, blank=True)
    file = models.ImageField()
    Business = models.ForeignKey("Business", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Business(core_models.TimeStampedModel):

    """ Business Model Definition """

    name = models.CharField(max_length=80)
    description = models.TextField(default="")
    address = models.CharField(max_length=140)
    open_time = models.TimeField()
    close_time = models.TimeField()
    businessman = models.ForeignKey("users.User", on_delete=models.CASCADE)
    phone = PhoneField(blank=True)

    def __str__(self):
        return self.name
