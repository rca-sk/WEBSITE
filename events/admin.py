from django.contrib import admin
from .models import Event




class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'time', 'posted_by', 'send_to_committee', 'send_to_all_members')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'send_to_committee', 'send_to_all_members', 'posted_by')
    list_editable = ('is_published',)
    search_fields = ('title', 'summary', 'detail', 'posted_by')
    list_per_page = 20




# Register your models here.
admin.site.register(Event, EventAdmin)