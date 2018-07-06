from django.core.management.base import BaseCommand
from api.models import deleteCapsuleModels

class Command(BaseCommand):
    def handle(self, *args, **options):
        deleteCapsuleModels()
