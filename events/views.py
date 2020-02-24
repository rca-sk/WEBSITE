from django.shortcuts import render
from .models import Event
# Create your views here.

def index(request):
    events = Event.objects.all()

    context = {
        'events': events
    }
    return render(request, 'events.html', context)



def event(request, event_id):
    event = Event.objects.filter(id=event_id)
    context = {
        'event':event[0]
    }
    return render(request, 'event.html', context)