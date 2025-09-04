from django.core.management.base import BaseCommand
from faker import Faker
import random

from core.models import BlogPost, Author


class Command(BaseCommand):
    help = "Create fake BlogPost objects"

    def handle(self, *args, **options: dict) -> None:
        current_blog_count = BlogPost.objects.count()
        count = options['count']

        # Check for the delete flag
        if options['delete']:
            BlogPost.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(
                "All existing BlogPost objects have been deleted."))
            return

        if current_blog_count > 0:
            self.stdout.write(self.style.WARNING(
                f"There are currently {current_blog_count} blog posts. Are you sure you want to create more?"
            ))

            user_input = input("Clear existing data? (y/n)\n")

            if user_input.lower() in ['y', 'yes']:
                BlogPost.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    "All existing BlogPost objects have been deleted."))
            elif user_input.lower() in ['n', 'no']:
                self.stdout.write(self.style.NOTICE(
                    "No changes made to existing BlogPost objects."))
            else:
                self.stdout.write(self.style.ERROR(
                    "Invalid input. No changes made to existing BlogPost objects."))

        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            "Creating fake BlogPost objects..."
        ))

        for _ in range(count):
            author = self._get_random_author()

            BlogPost.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=1000),
                author=author,
            )

        self.stdout.write(self.style.SUCCESS(
            f"Successfully created {count} fake BlogPost objects."
        ))

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of fake BlogPost objects to create'
        )

        # delete flag to clear existing data
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all existing BlogPost objects before creating new ones'
        )

    def _get_random_author(self) -> Author:
        """
        Helper method that will return a random Author object from the database.

        This will help link the BlogPost to an Author.
        """
        authors = list(Author.objects.all())
        return random.choice(authors)
