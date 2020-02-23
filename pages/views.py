from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def committee(request):
    return render(request, 'committee.html')


def announcements(request):
    return render(request, 'announcements.html')


def events(request):
    return render(request, 'events.html')