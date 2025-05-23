from django.urls import path
from . import views

urlpatterns = [
    path("", views.display_schedule, name="page-schedule"),
    path("post/", views.post_schedule, name="page-postschedule")
]