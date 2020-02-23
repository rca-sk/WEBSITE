from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'event.html')



def event(request):
    return render(request, 'events.html')