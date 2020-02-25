from django.shortcuts import render
from .models import Announcement
# Create your views here.

def index(request):
    announcements = Announcement.objects.order_by('-time').filter(is_published=True)
    context = {
        'announcements' : announcements
    }
    return render(request, 'announcements.html', context)



def announcement(request, announcement_id):
    announcement = Announcement.objects.filter(id=announcement_id)
    context = {
        'announcement' : announcement[0]
    }
    return render(request, 'announcement.html', context)