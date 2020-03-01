from django.shortcuts import render
from .models import Carrier_announcement
# Create your views here.

def index(request):
    carrier_announcements = Carrier_announcement.objects.order_by('-time').filter(is_published=True)
    context = {
        'carrier_announcements' : carrier_announcements
    }
    return render(request, 'carrier.html', context)



def carrier_announcement(request, carrier_announcement_id):
    carrier_announcement = Carrier_announcement.objects.filter(id=carrier_announcement_id)
    context = {
        'carrier_announcement' : carrier_announcement[0]
    }
    return render(request, 'carrier_announcement.html', context)