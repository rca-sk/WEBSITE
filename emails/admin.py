from django.contrib import admin
from .models import Email
# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id','time','email_subject','send_to_committee','send_to_all_members','custom_recipients')
    list_display_links = ('email_subject',)
    list_filter = ('send_to_committee','send_to_all_members','custom_recipients',)
    search_fields = ('email_subject', 'email_body')


admin.site.register(Email, EmailAdmin)