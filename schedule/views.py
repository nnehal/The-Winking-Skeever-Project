from django.shortcuts import render
from post.models import UploadDocument


# Create your views here.
def display_schedule(request):
    pdf = UploadDocument.objects.last()
    context = {
        'pdf':pdf
        }
    return render(request, 'schedule/schedule.html', context)