from django.shortcuts import render, redirect
from .models import UploadDocument
from .forms import DocumentForm
import pandas as pd

def index(request):
    return render(request, "schedule/index.html")

def display_schedule(request):
    # schedule_file = "static/posted_sched.html"

    # context = {
    #     "file":schedule_file
    #     }
    return render(request, "schedule/schedule.html")


def post_schedule(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # check file extension
            form.save()
            return redirect("page-index")
    else:
        form = DocumentForm()
    

    return render(request, "schedule/post_document.html", {'form': form})

