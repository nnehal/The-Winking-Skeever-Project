from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.display_schedule, name="page-display_schedule")
]