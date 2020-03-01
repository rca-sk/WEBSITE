from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='carrier'),
    path('<int:carrier_announcement_id>', views.carrier_announcement, name='carrier_announcement')
]