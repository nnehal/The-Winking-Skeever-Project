from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="page-index"),
    path("schedule/", views.schedule, name="page-schedule")
]