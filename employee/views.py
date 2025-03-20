from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from post.models import UploadDocument
import csv
from django.core.files import File

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('page-index')
    else:
        form = UserRegisterForm()

    return render(request, 'employee/register.html', {"form": form})

@login_required
def profile(request):
    target = UploadDocument.objects.last().File
    name = request.user.username
    schedule = []
    # reading csv file
    with target.open(mode='r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            for i in range(len(row)):
                if(name == row[i].strip().title()):
                    shift = row[0]
                    match(i):
                        case 1:
                            schedule.append(shift + " Monday")
                        case 2:
                            schedule.append(shift + " Tuesday")
                        case 3:
                            schedule.append(shift + " Wednesday")
                        case 4:
                            schedule.append(shift + " Thursday")
                        case 5:
                            schedule.append(shift + " Friday")
                        case 6:
                            schedule.append(shift + " Saturday")
                        case 7:
                            schedule.append(shift + " Sunday")
                        case _:
                            print("Go HOME!!\n")

    return render(request, "employee/profile.html", {"schedule": schedule})