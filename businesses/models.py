from django.db import models
from phone_field import PhoneField
from core import models as core_models


class Photo(core_models.TimeStampedModel):

    """ Business Photo Model Definition """

    caption = models.CharField(max_length=80, blank=True)
    file = models.ImageField(upload_to="business_photos")
    business = models.ForeignKey(
        "Business", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class Business(core_models.TimeStampedModel):

    """ Business Model Definition """

    name = models.CharField(max_length=80)
    description = models.TextField(default="")
    address = models.CharField(max_length=140)
    open_time = models.TimeField(blank=True)
    close_time = models.TimeField(blank=True)
    businessman = models.ForeignKey(
        "users.User", related_name="businesses", on_delete=models.CASCADE
    )
    phone = PhoneField(blank=True)

    def __str__(self):
        return self.name

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
