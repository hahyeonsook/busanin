from django.http import Http404
from django.views.generic import DetailView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms


class BusinessDetailView(DetailView):

    """ BusinessDetail Definition """

    model = models.Business


class EditBusinessView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Business
    template_name = "businesses/business_update.html"
    fields = [
        "name",
        "description",
        "address",
        "open_time",
        "close_time",
        "phone",
    ]
    success_url = reverse_lazy("core:home")

    def get_object(self, queryset=None):
        business = super().get_object(queryset=queryset)
        if business.businessman.pk != self.request.user.pk:
            raise Http404()
        return business


class BusinessPhotosView(user_mixins.LoggedInOnlyView, DetailView):
    model = models.Business
    template_name = "businesses/business_photos.html"

    def get_object(self, queryset=None):
        business = super().get_object(queryset=queryset)
        if business.businessman.pk != self.request.user.pk:
            raise Http404()
        return business


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    model = models.Photo
    template_name = "businesses/photo_create.html"
    fields = (
        "caption",
        "file",
    )
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        photo = form.save(self)
        pk = self.kwargs.get("pk")
        photo.business = models.Business.objects.get(pk=pk)
        photo.save()

        business = photo.business
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("businesses:photos", kwargs={"pk": business.pk}))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "businesses/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        business_pk = self.kwargs.get("business_pk")
        return reverse("businesses:photos", kwargs={"pk": business_pk})


@login_required
def delete_photo(request, business_pk, photo_pk):
    user = request.user
    try:
        business = models.Business.objects.get(pk=business_pk)
        if business.businessman.pk != user.pk:
            messages.error(request, "Can't delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("businesses:photos", kwargs={"pk": business_pk}))
    except models.Business.DoesNotExist:
        return redirect(reverse("core:home"))


class DeleteBusinessView(DeleteView):

    model = models.Business
    template_name = "businesses/business_delete.html"
    success_url = reverse_lazy("core:home")


class CreateBusinessView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateBusinessForm
    template_name = "businesses/business_create.html"

    def form_valid(self, form):
        business = form.save()
        business.businessman = self.request.user
        business.save()
        form.save_m2m()
        messages.success(self.request, "Businesses Uploaded")
        return redirect(reverse("businesses:photos", kwargs={"pk": business.pk}))

