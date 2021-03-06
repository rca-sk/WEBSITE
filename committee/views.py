from django.shortcuts import render
from .models import Executive_committee_member, Mayor


def index(request):
    executives  = Executive_committee_member.objects.filter(is_published=True).order_by('id')
    mayors      = Mayor.objects.filter(is_published=True).order_by('id')

    context = {
        'executives' : executives,
        'mayors': mayors
    }
    return render(request, 'committee.html', context)