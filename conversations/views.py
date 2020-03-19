from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from users import models as user_models
from core import mixins
from . import models


class GoConversationView(mixins.LoginRequiredMixin, View):

    """ Conversation detail or create 하는 View """

    def get(self, request, *args, **kwargs):
        """ 
        다른 User와 Conversation을 할 때, 생성되지 않았으면 자동으로 생성
        or 생성되어 있는 Conversation을 return 함
        """
        user_one = user_models.User.objects.get_or_none(pk=self.kwargs["a_pk"])
        user_two = user_models.User.objects.get_or_none(pk=self.kwargs["b_pk"])

        if user_one is not None and user_two is not None:
            try:
                conversation = models.Conversation.objects.get(
                    Q(participants=user_one) & Q(participants=user_two)
                )
            except models.Conversation.DoesNotExist:
                conversation = models.Conversation.objects.create()
                conversation.participants.add(user_one, user_two)
            return redirect(
                reverse("conversations:detail", kwargs={"pk": conversation.pk})
            )


class ConversationDetailView(View):

    """ 두 사용자 사이의 Conversation Detail View """

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            conversation = models.Conversation.objects.get(pk=pk)
        except models.Conversation.DoesNotExist:
            conversation = None
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        try:
            conversation = models.Conversation.objects.get(pk=pk)
        except models.Conversation.DoesNotExist:
            conversation = None
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))


class ConversationListView(View):

    """ Conversation List View """

    def get(self, *args, **kwargs):
        return render(
            self.request,
            "conversations/conversation_list.html",
            {"user_obj": self.request.user},
        )
