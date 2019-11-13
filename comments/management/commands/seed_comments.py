import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from comments import models as comment_models
from users import models as user_models
from posts import models as post_models


class Command(BaseCommand):

    help = "This command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reviews do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        posts = post_models.Post.objects.all()
        seeder.add_entity(
            comment_models.Comment,
            number,
            {
                "comment": lambda x: seeder.faker.text(),
                "user": lambda x: random.choice(users),
                "post": lambda x: random.choice(posts),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} comments created!"))
