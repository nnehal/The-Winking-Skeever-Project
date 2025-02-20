from django.shortcuts import render
from post.models import PDFDocument


# Create your views here.
def display_schedule(request):
    p = PDFDocument.objects.all()
    context = {
        'photo':p
        }
    return render(request, 'schedule/schedule.html', context)