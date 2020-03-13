import os
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates Unknown"

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username="unknown")
        except User.DoesNotExist:
            admin = None
        if not admin:
            password = os.environ.get("DJANGO_SECRET")
            User.objects.create("unknown", "qu3230@gmail.com", password)
            self.stdout.write(self.style.SUCCESS(f"Unknown created!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Unknown exists!"))
