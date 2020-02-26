from django.contrib import admin
from .models import CommunityMember

class CommunityMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'phone', 'email', 'id_or_passport', 'location_in_Korea', 'education_level', 'major_or_field_of_work', 'institution', 'graduation_year', 'activity', 'other_information')
    list_display_links = ('id', 'first_name', 'last_name')
    list_editable = ()
    search_fields = ('id', 'first_name', 'last_name', 'birth_date', 'phone', 'email', 'id_or_passport','location_in_Korea','education_level','major_or_field_of_work', 'institution', 'graduation_year', 'activity', 'other_information')
    list_per_page = 30



# Register your models here.
admin.site.register(CommunityMember, CommunityMemberAdmin)
