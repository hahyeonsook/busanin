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


