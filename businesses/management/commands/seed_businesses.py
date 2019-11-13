import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from businesses import models as business_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many businesses"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many businesses do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        seeder.add_entity(
            business_models.Business,
            number,
            {
                "name": lambda x: seeder.faker.sentence(),
                "description": lambda x: seeder.faker.text(),
                "address": lambda x: seeder.faker.address(),
                "businessman": lambda x: random.choice(all_users),
                "phone": lambda x: seeder.faker.phone_number(),
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            business = business_models.Business.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                business_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"business_photos/{random.randint(1, 33)}.webp",
                    business=business,
                )

        self.stdout.write(self.style.SUCCESS(f"{number} businesses created!"))

