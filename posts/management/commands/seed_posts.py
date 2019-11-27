import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from posts import models as post_models
from users import models as user_models
from businesses import models as business_models


class Command(BaseCommand):

    help = "This command creates many posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many posts do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        all_businesses = business_models.Business.objects.all()
        seeder.add_entity(
            post_models.Post,
            number,
            {
                "name": lambda x: seeder.faker.sentence(),
                "description": lambda x: seeder.faker.text(),
                "user": lambda x: random.choice(all_users),
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            post = post_models.Post.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                post_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"post_photos/{random.randint(1, 33)}.jpg",
                    post=post,
                )
                post_models.businesses = random.choice(all_businesses)

        self.stdout.write(self.style.SUCCESS(f"{number} posts created!"))

