from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UploadDocument
from employee.models import Profile
from django.core.mail import send_mass_mail
import pandas as pd
import pathlib

def convert_file():
    uploaded_file = UploadDocument.objects.last().File

    df = pd.read_excel(uploaded_file)
    df.to_html("static/posted_sched.html")
    df.to_csv("static/schedule.csv", index=False, encoding="utf-8")

def get_schedule():
    return pathlib.Path(__file__).resolve().parent.parent / "static/schedule.csv"


def parse_csv(filename) -> tuple:
    df = pd.read_csv(filename)
    print(df)
    sleepInn = {}
    bwInn = {}

    for _date in df.columns[1:]:
        sleepInn [_date] = ("8am-4pm", df[_date][2]), ("4pm-12am", df[_date][3]), ("12am-8am", df[_date][4])
        bwInn [_date] = ("8am-4pm", df[_date][8]), ("4pm-12am", df[_date][10]), ("12am-8am", df[_date][11])

    return sleepInn, bwInn

def get_nested_value(dict_obj, keys) -> set:
    employee_names = set()

    for _date in keys:
        daily = dict_obj.get(_date, {})

        for per_shift in daily:
            shift, name = per_shift
            employee_names.add(name)
    return employee_names

def send_schedule():
    filename = get_schedule()
    si, bw = parse_csv(filename)

    keys = list(si.keys())
    
    emp_scheduled_si = get_nested_value(si, keys)
    emp_scheduled_bw = get_nested_value(bw, keys)

    emp_scheduled = emp_scheduled_si.union(emp_scheduled_bw)

    print(emp_scheduled)
    Users = Profile.objects.all()
    email_list = []
    messages = []
    for emp in emp_scheduled:
        for u in Users:
            if emp == u.user.last_name:
                email = {}
                email["subject"] = "This week's schedule!"
                email["message"] = str(u.latest_schedule)
                email["address"] = u.user.email
                email_list.append(email)

    from_email = "testdev729@gmail.com"
    for email_data in email_list:
        messages.append((email_data["subject"], email_data["message"], from_email, [email_data["address"]]))
    send_mass_mail(messages, fail_silently=False)



@receiver(post_save, sender=UploadDocument)
def create_profile(sender, instance, created, **kwargs):
    if created:
        convert_file()
        send_schedule()