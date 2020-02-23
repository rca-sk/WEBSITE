from django.contrib import admin
from .models import Executive_committee_member
from .models import Mayor




class Executive_committee_memberAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

class MayorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

# Register your models here.
admin.site.register(Executive_committee_member, Executive_committee_memberAdmin)
admin.site.register(Mayor, MayorAdmin)
