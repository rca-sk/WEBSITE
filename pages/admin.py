from django.contrib import admin
from .models import About
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'chairman_name', 'time')
    list_display_links = ('id', 'chairman_name')


admin.site.register(About, AboutAdmin)