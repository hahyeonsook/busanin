from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username="ebadmin")
        except User.DoesNotExist:
            admin = None
        if not admin:
            User.objects.create_superuser("ebadmin", "qu3230@gmail.com", "123456")
            self.stdout.write(self.style.SUCCESS(f"Superuser created!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exist!"))
