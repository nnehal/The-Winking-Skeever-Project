from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


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
            return redirect("page-schedule")
    else:
        form = DocumentForm()
    

    return render(request, "schedule/post_document.html", {'form': form})

def send_schedule(requests):
    Users = get_user_model()
    email_list = [user.email for user in Users.objects.all() if user.email]

    send_mail(
        "Test django email",
        "here is a message",
        "hello@gmai.com",
        email_list,
        fail_silently=False
    )