# Django wait for db

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # Wait for DB
    def handle(self, *args, **options):
        pass

