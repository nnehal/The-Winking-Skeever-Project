from django import forms
from .models import PDFDocument

class PDFDocumentForm(forms.modelform):
    class Meta:
        model = PDFDocument
        fields = ("description", "pdf_file")