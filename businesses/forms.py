from django import forms
from . import models


class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = (
            "name",
            "description",
            "address",
            "open_time",
            "close_time",
            "phone",
        )

    def save(self, *args, **kwargs):
        business = super().save(commit=False)
        return business


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)

        business = models.Business.objects.get(pk=pk)
        photo.business = business
        photo.save()
