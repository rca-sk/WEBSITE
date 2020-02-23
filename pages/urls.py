from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('committee', views.committee, name='committee'),
    path('announcements', views.announcements, name='announcements'),
    path('events', views.events, name='events'),  
]