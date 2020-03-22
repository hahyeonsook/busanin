import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand

from django_seed import Seed

from conversations import models as conversation_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many conversations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many conversation do u want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()

        seeder.add_entity(
            conversation_models.Message,
            number,
            {"participants": lambda x: random.choice(users)},
        )

        seeder = Seed.seeder()

        created_conversations = seeder.execute()
        created_clean = flatten(list(created_conversations.values()))
        for pk in created_clean:
            conversation = conversation_models.Conversation.objects.get(pk=pk)
            conversation.participants.set(random.choice(users))

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
