from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'announcements.html')



def announcement(request):
    return render(request, 'announcements.html')