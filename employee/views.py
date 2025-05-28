from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from schedule.models import UploadDocument
import csv

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

def get_schedule_by_name(csv_file, name):
    schedule = {}
    # reading csv file
    with csv_file.open(mode='r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            for i in range(len(row)):
                if(name == row[i].strip().title()):
                    shift = row[0]
                    match(i):
                        case 1:
                            schedule.update({"Monday": shift})
                        case 2:
                            schedule.update({"Tuesday": shift})
                        case 3:
                            schedule.update({"Wednesday": shift})
                        case 4:
                            schedule.update({"Thursday": shift})
                        case 5:
                            schedule.update({"Friday": shift})
                        case 6:
                            schedule.update({"Saturday": shift})
                        case 7:
                            schedule.update({"Sunday": shift})
                        case _:
                            print("Go HOME!!\n")

    return schedule

@login_required
def profile(request):
    target = UploadDocument.objects.last().File
    name = request.user.username
    schedule = get_schedule_by_name(target, name)

    return render(request, "employee/profile.html", {"schedule": schedule})