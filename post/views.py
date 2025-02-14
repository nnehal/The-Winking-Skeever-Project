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
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully posted!!")
    else:
        form = PDFDocumentForm()

    return render(request, "post/post_pdf.html", {'form': form})
    