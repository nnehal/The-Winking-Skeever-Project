from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.contrib.auth import get_user_model
from .models import UploadDocument

def index(request):
    return render(request, "schedule/index.html")

def display_schedule(request):
    schedule_file = UploadDocument.objects.last
    context = {
        "file":schedule_file
        }
    return render(request, "schedule/schedule.html", context)


def post_schedule(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # check file extension
            form.save()
            return redirect("page-schedule")
    else:
        form = DocumentForm()
    

    return render(request, "schedule/post_document.html", {'form': form})