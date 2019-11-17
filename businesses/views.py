from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class BusinessList(ListView):

    """ BusinessList Definition """

    model = models.Business
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "businesses"


class BusinessDetail(DetailView):

    """ BusinessDetail Definition """

    model = models.Business
