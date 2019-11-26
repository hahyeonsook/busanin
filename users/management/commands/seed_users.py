import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users do u want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(
            User,
            number,
            {
                "bio": lambda x: seeder.faker.text(),
                "is_staff": False,
                "is_superuser": False,
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            user = User.objects.get(pk=pk)
            user.avatar = f"user_photos/{random.randint(1, 20)}.webp"

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
