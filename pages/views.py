from django.shortcuts import render

from announcements.models import Announcement
from events.models import Event

def index(request):
    recent_announcements = Announcement.objects.order_by('-time').filter(is_published=True)[:3]
    recent_events        = Event.objects.order_by('-time').filter(is_published=True)[:3]
    context = {
        'recent_announcements' : recent_announcements,
        'recent_events'        : recent_events
    }
    return render(request, 'index.html', context)