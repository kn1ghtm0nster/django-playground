from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Author


class Command(BaseCommand):
    help = "Create fake Author objects"

    def handle(self, *args, **options: dict) -> None:
        current_authors = Author.objects.count()
        count = options['count']

        # Check for the delete flag
        if options['delete']:
            Author.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(
                "All existing Author objects have been deleted."))
            return

        if current_authors > 0:
            self.stdout.write(self.style.WARNING(
                f"There are currently {current_authors} authors in the database. Are you sure you want to create more?"))

            user_input = input("Clear existing data? (y/n)\n")

            if user_input.lower() in ['y', 'yes']:
                Author.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    "All existing Author objects have been deleted."))
            elif user_input.lower() in ['n', 'no']:
                self.stdout.write(self.style.WARNING(
                    "No changes made to existing Author objects."))
            else:
                self.stdout.write(self.style.ERROR(
                    "Invalid input. No changes made to existing Author objects."))

        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            "Creating fake Author objects..."
        ))

        for _ in range(count):
            Author.objects.create(
                name=fake.name(),
                bio=fake.text(max_nb_chars=200),
                website=fake.url(),
                email=fake.email(),
            )

        self.stdout.write(self.style.SUCCESS(
            f"Successfully created {count} fake Author objects."
        ))

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of fake authors to create'
        )

        # This flag is to DELETE ALL existing Author objects. USE CAREFULLY!
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all existing Author objects before creating new ones'
        )
