from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    Description = models.CharField(max_length=255, blank=True)
    # change pdf file location
    PDF = models.FileField(upload_to='pdf/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Description