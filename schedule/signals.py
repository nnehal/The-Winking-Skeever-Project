from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UploadDocument
import pandas as pd
from django.contrib.auth import get_user_model
from employee.models import Profile
from django.core.mail import send_mass_mail
import csv
import pathlib

def convert_file():
    uploaded_file = UploadDocument.objects.last().File

    df = pd.read_excel(uploaded_file)
    df.to_html("static/posted_sched.html")
    df.to_csv("static/schedule.csv", index=False, encoding="utf-8")


def parse_csv(filename) -> dict:
    sleepInn = {}
    bwInn = {}

    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

        for i in range(1,8):
            date_ = rows[0][i]
            sleepInn [date_] = {"8am-4pm": rows[3][i], "4pm-12am": rows[4][i], "12am-8am": rows[5][i]}
            bwInn[date_] = {"8am-4pm": rows[9][i], "4pm-12am": rows[11][i], "12am-8am": rows[12][i]}
            
    weekly_schedule = [sleepInn, bwInn]

    return sleepInn, bwInn

def get_nested_value(dict_obj, keys, default=None) -> set:
    current = dict_obj
    val = set()

    for key in keys:
        more_dict = current.get(key, default)
        val.add(more_dict.get("8am-4pm"))
        val.add(more_dict.get("4pm-12am"))
        val.add(more_dict.get("12am-8am"))
    
    return val

def send_schedule():
    filename = pathlib.Path(__file__).resolve().parent.parent / "static/schedule.csv"
    si, bw = parse_csv(filename)

    keys = list(si.keys())
    
    emp_scheduled_si = get_nested_value(si, keys)
    emp_scheduled_bw = get_nested_value(bw, keys)

    emp_scheduled = emp_scheduled_si.union(emp_scheduled_bw)

    Users = Profile.objects.all()
    email_list = []
    messages = []
    for emp in emp_scheduled:
        print(emp)
        for u in Users:
            if emp == u.user.last_name:
                email = {}
                email["subject"] = "This week's schedule!"
                email["message"] = str(u.latest_schedule)
                email["address"] = u.user.email
                email_list.append(email)

    # add sender email
    from_email = "testdev729@gmail.com"
    for email_data in email_list:
        print(email_data["address"])
        messages.append((email_data["subject"], email_data["message"], from_email, [email_data["address"]]))
    print(messages)
    send_mass_mail(messages, fail_silently=False)
    # print(messages)



@receiver(post_save, sender=UploadDocument)
def create_profile(sender, instance, created, **kwargs):
    if created:
        convert_file()
        send_schedule()