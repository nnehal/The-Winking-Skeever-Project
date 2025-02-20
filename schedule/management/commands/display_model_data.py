from django.core.management.base import BaseCommand
from post.models import PDFDocument

class Command(BaseCommand):
    help = "Displays data from the model"

    def handle(self, *args, **options):
        for obj in PDFDocument.objects.all():
            self.stdout.write(str(obj.__dict__))