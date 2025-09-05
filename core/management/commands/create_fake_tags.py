from django.core.management.base import BaseCommand
from faker import Faker
import random

from core.models import BlogPost, Tag


class Command(BaseCommand):
    help = "Create fake Tag objects"

    def handle(self, *args, **options: dict) -> None:
        tag_count = Tag.objects.count()
        count = options['count']

        # Check for the delete flag
        if options['delete']:
            Tag.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(
                "All existing Tag objects have been deleted."))
            return

        if tag_count > 0:
            self.stdout.write(self.style.WARNING(
                f"There are currently {tag_count} tags. Are you sure you want to create more?"
            ))

            user_input = input("Clear existing data? (y/n)\n")

            if user_input.lower() in ['y', 'yes']:
                Tag.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    "All existing Tag objects have been deleted."))
            elif user_input.lower() in ['n', 'no']:
                self.stdout.write(self.style.NOTICE(
                    "No changes made to existing Tag objects."))
            else:
                self.stdout.write(self.style.ERROR(
                    "Invalid input. No changes made to existing Tag objects."))

        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            "Creating fake Tag objects..."
        ))

        for _ in range(count):
            post = self._get_random_blogpost()
            tag = Tag.objects.create(
                name=fake.word().capitalize(),
            )
            tag.posts.add(post)

        self.stdout.write(self.style.SUCCESS(
            f"Successfully created {count} fake Tag objects."
        ))

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of fake Tag objects to create.'
        )

        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all existing Tag objects before creating new ones.'
        )

    def _get_random_blogpost(self) -> BlogPost:
        bloposts = list(BlogPost.objects.all())
        return random.choice(bloposts)
