from django import forms
from .models import UploadDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = UploadDocument
        fields = ["Description", "File"]