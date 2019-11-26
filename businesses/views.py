from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from users import models as user_model
from . import models as business_model


class BusinessList(ListView):

    """ BusinessList Definition """

    model = business_model.Business
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "businesses"


class BusinessDetail(DetailView):

    """ BusinessDetail Definition """

    model = business_model.Business


class UpdateBusinessView(UpdateView):

    model = business_model.Business
    template_name = "businesses/business_update.html"
    fields = [
        "name",
        "description",
        "address",
        "open_time",
        "close_time",
        "phone",
    ]

    def get_object(self, queryset=None):
        return self.request


class DeleteBusinessView(DeleteView):

    model = business_model.Business
    template_name = "businesses/business_delete.html"
    success_url = reverse_lazy("businesses:list")

    def get_object(self, queryset=None):
        return self.request

class CreateBusinessView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateBusinessForm
    template_name = "businesses/business_create.html"

    def form_valid(self, form):
        business = form.save()
        business.businessman = self.request.user
        business.save()
        form.save_m2m()
        messages.success(self.request, "Businesses Uploaded")
        return redirect(reverse("businesses:detail", kwargs={"pk": business.pk}))

