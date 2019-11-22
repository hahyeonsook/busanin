from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "businessman",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("businessman",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "businessman",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
