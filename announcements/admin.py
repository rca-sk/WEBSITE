from django.contrib import admin
from .models import Announcement




class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'time', 'posted_by')
    list_display_links = ('id', 'title')
    list_filter = ('is_published','posted_by')
    list_editable = ('is_published',)
    search_fields = ('title', 'detail', 'time', 'posted_by')
    list_per_page = 50



# Register your models here.
admin.site.register(Announcement, AnnouncementAdmin)
