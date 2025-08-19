from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Person


class Command(BaseCommand):
    help = "Create fake Person objects"

    def handle(self, *args, **options: dict) -> None:
        current_count = Person.objects.count()
        count = options['count']

        if current_count > 0:
            self.stdout.write(self.style.WARNING(
                f"WARNING: There are already {current_count} Person objects. Are you sure you want to create more?"
            ))

            user_input = input("Clear existing data? (y/n): \n")

            if user_input.lower() in ['y', 'yes']:
                Person.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    "All existing Person objects have been deleted."))
            elif user_input.lower() in ['n', 'no']:
                self.stdout.write(self.style.NOTICE(
                    "No changes made to existing Person objects."))
            else:
                self.stdout.write(self.style.ERROR(
                    "Invalid input. No changes made to existing Person objects."))

        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            "Creating fake Person objects..."
        ))

        for _ in range(count):
            Person.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=18, max=90),
                email=fake.email(),
            )

        self.stdout.write(self.style.SUCCESS(
            f"SUCCESS: Created {count} fake Person objects"
        ))

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of fake people to create'
        )
