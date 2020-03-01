from django.contrib import admin
from .models import Carrier_announcement




class CarrierAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'time', 'posted_by')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'posted_by')
    list_editable = ('is_published',)
    search_fields = ('title', 'summary', 'time', 'posted_by', 'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4', 'paragraph5')
    list_per_page = 50



# Register your models here.
admin.site.register(Carrier_announcement, CarrierAnnouncementAdmin)