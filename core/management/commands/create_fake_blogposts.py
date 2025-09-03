from django.core.management.base import BaseCommand
from faker import Faker
import random

from core.models import BlogPost, Author


class Command(BaseCommand):
    help = "Create fake BlogPost objects"

    def handle(self, *args, **options: dict) -> None:
        pass

    def add_arguments(self, parser) -> None:
        pass

    def _get_random_author(self) -> Author | None:
        """
        Helper method that will return a random Author object from the database.

        This will help link the BlogPost to an Author.
        """
        authors = list(Author.objects.all())
        return random.choice(authors) if authors else None
