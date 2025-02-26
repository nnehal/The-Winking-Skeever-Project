from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm

# Create your views here.

def index(request):
    return render(request, "post/index.html")

def schedule(request):
    return render(request, "post/schedule.html")

def post_schedule(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("page-index")
    else:
        form = DocumentForm()

    return render(request, "post/post_document.html", {'form': form})
    