from django.db.models import Q
from django.shortcuts import render
from users import models as user_models
from . import models


def go_conversation(request, a_pk, b_pk):
    try:
        user_one = user_models.User.objects.get_or_none(pk=a_pk)
        user_two = user_models.User.objects.get(pk=b_pk)
    except user_models.DoesNotExist:
        user_one = None
        user_two = None

    if user_one is not None and user_two is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=user_one) & Q(participants=user_two)
        )
        print(conversation)
