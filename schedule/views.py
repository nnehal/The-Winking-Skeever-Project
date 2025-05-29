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

def convert_file():
    uploaded_file = UploadDocument.objects.last().File

    df = pd.read_excel(uploaded_file)
    df.to_html("static/posted_sched.html")
    df.to_csv("static/schedule.csv", index=False, encoding="utf-8")

def post_schedule(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # check file extension
            form.save()
            return redirect("page-index")
    else:
        form = DocumentForm()
    
    convert_file()

    return render(request, "schedule/post_document.html", {'form': form})

