from django.db import models

class UploadDocument(models.Model):
    Description = models.CharField(max_length=255, blank=True)
    File = models.FileField(upload_to="sched/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Description