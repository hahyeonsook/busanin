from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyMixin(UserPassesTestMixin):

    """ 사용자가 Email User가 아닐 때 보여주는 View로 제한하는 Mixin"""

    def test_func(self):
        return not self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return redirect("core:home")


class LoggedOutOnlyMixin(UserPassesTestMixin):

    """ 사용자가 Log out 상태일 때 보여주는 View로 제한하는 Mixin"""

    def test_func(self):
        return not self.request.user.is_authenticated

    # 유저가 로그인을 한 상태면 볼 수 없다.
    def handle_no_permission(self):
        messages.error(self.request, "접근 권한이 없습니다.")
        return redirect("core:home")


class LoggedInOnlyMixin(LoginRequiredMixin):

    """ 사용자가 Log in 상태가 아닐 때, log in으로 넘겨주는 View로 만드는 Mixin """

    login_url = reverse_lazy("users:login")


class NotFormSuceesMessageMixin:

    """ Form이 아닌 GET하는 View들에서 SuccessMessage를 추가해주는 View로 만드는 Mixin """

    success_message = ""

    def get(self, request, *args, **kwargs):

        if self.success_message:
            messages.success(self.request, self.success_message)

        return super().get(request, *args, **kwargs)

