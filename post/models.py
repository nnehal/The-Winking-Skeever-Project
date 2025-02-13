from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)

    # change pdf file location
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

