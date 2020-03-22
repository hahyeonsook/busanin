from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, FormView

from core import mixins
from . import models, forms


class BusinessDetailView(DetailView):

    """ Business Detail View """

    model = models.Business


class EditBusinessView(mixins.LoggedInOnlyMixin, UpdateView):

    """ Edit Business View """

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

    # Business Author가 아니면 접근할 수 없도록 LoggedInOnlyMixin Override
    def test_func(self):
        business = models.Business.objects.get(pk=self.kwargs.get("pk"))
        if self.request.user != business.user:
            return super().test_func(self)
        return True

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return super().handle_no_permission(self)

    def get_object(self, queryset=None):
        business = super().get_object(queryset=queryset)
        if business.businessman.pk != self.request.user.pk:
            raise Http404()
        return business

    def get_success_url(self, **kwargs):
        return reverse_lazy("businesses:detail", kwargs={"pk": self.kwargs.get("pk")})


class BusinessPhotosView(mixins.LoggedInOnlyMixin, DetailView):

    """ Business Photos Detail View """

    model = models.Business
    template_name = "businesses/business_photos.html"

    def get_object(self, queryset=None):
        business = super().get_object(queryset=queryset)
        if business.businessman.pk != self.request.user.pk:
            raise Http404()
        return business


class AddPhotoView(mixins.LoggedInOnlyMixin, SuccessMessageMixin, FormView):

    """ Add Photo View """

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


class EditPhotoView(mixins.LoggedInOnlyMixin, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "businesses/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "사진을 수정했습니다."
    fields = ("caption",)

    def get_success_url(self):
        business_pk = self.kwargs.get("business_pk")
        return reverse("businesses:photos", kwargs={"pk": business_pk})


class DeletePhotoView(mixins.LoggedInOnlyMixin, SuccessMessageMixin, DeleteView):

    """ Delete Photo View """

    model = models.Photo
    template_name = "businesses/business_delete.html"
    success_message = "사진이 삭제되었습니다."
    pk_url_kwarg = "photo_pk"

    # Business Author가 아니면 접근할 수 없도록 Mixin
    def test_func(self):
        business = models.Business.objects.get(pk=self.kwargs.get("business_pk"))
        if self.request.user != business.user:
            return super().test_func(self)
        return True

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return super().handle_no_permission(self)

    def get_success_url(self):
        business_pk = self.kwargs.get("business_pk")
        return reverse("businesses:photos", kwargs={"pk": business_pk})


class DeleteBusinessView(mixins.LoggedInOnlyMixin, UserPassesTestMixin, DeleteView):

    """ Delete Business View """

    model = models.Business
    template_name = "businesses/business_delete.html"
    success_url = reverse_lazy("core:home")

    # Business Author가 아니면 접근할 수 없도록 Mixin
    def test_func(self):
        business = models.Business.objects.get(pk=self.kwargs.get("pk"))
        if self.request.user != business.user:
            return super().test_func(self)
        return True

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return super().handle_no_permission(self)


class CreateBusinessView(mixins.LoggedInOnlyMixin, SuccessMessageMixin, FormView):

    form_class = forms.CreateBusinessForm
    template_name = "businesses/business_create.html"
    success_message = "사업체가 성공적으로 등록되었습니다!"

    # Businesman이 아니면 접근할 수 없도록 Mixin
    def test_func(self):
        if self.request.user.businessman:
            return super().test_func(self)
        return True

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return super().handle_no_permission(self)

    def form_valid(self, form):
        business = form.save()
        business.businessman = self.request.user
        business.save()
        form.save_m2m()
        messages.success(self.request, "Businesses Uploaded")
        return redirect(reverse("businesses:photos", kwargs={"pk": business.pk}))
