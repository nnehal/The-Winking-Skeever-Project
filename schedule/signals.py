from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UploadDocument
import pandas as pd

def convert_file():
    uploaded_file = UploadDocument.objects.last().File

    df = pd.read_excel(uploaded_file)
    df.to_html("static/posted_sched.html")
    df.to_csv("static/schedule.csv", index=False, encoding="utf-8")

@receiver(post_save, sender=UploadDocument)
def create_profile(sender, instance, created, **kwargs):
    if created:
        convert_file()