from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PDFDocumentForm

# Create your views here.

def index(request):
    return render(request, "post/index.html")

def schedule(request):
    return render(request, "post/schedule.html")

def post_schedule(request):
    if request.method == "POST":
        form = PDFDocumentForm(request.POST, request.FILES)
        form.save()
        return ("Upload Success")
    else:
        form = PDFDocumentForm()

    return render(request, "index.html", {'forms': form})
    