from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from post.models import UploadDocument
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

@login_required
def profile(request):
    # csv file name
    filename = UploadDocument.objects.last().File.url

    # initializing the titles and rows list
    # fields = []
    # rows = []
    name = User.username
    schedule = []
    # reading csv file
    with open(filename) as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one

        for row in csvreader:
            for i in range(len(row)):
                if(name == row[i].strip().title()):
                    time = row[0]
                    match(i):
                        case 1:
                            schedule.append(time + " Monday")
                        case 2:
                            schedule.append(time + " Tuesday")
                        case 3:
                            schedule.append(time + " Wednesday")
                        case 4:
                            schedule.append(time + " Thursday")
                        case 5:
                            schedule.append(time + " Friday")
                        case 6:
                            schedule.append(time + " Saturday")
                        case 7:
                            schedule.append(time + " Sunday")
                        case _:
                            print("Go HOME!!\n")

            

    context = {
        "schedule": schedule
    }
    return render(request, "employee/profile.html", context)