from django.db import models
from phone_field import PhoneField

# Create your models here.

class CommunityMember(models.Model):
    first_name              = models.CharField(max_length=50)
    last_name               = models.CharField(max_length=50)
    birth_date              = models.DateField(blank=True)
    phone                   = PhoneField(blank=True)
    email                   = models.EmailField(blank=True)
    id_or_passport          = models.CharField(max_length=50,blank=True)
    location_in_Korea       = models.CharField(max_length=100, blank=True)
    institution             = models.CharField(max_length=100,blank=True)
    education_level         = models.CharField(max_length=50, blank=True)
    major_or_field_of_work  = models.CharField(max_length=100, blank=True)
    graduation_year         = models.DateField(blank=True)
    activity                = models.CharField(max_length=50, blank=True)
    other_information       = models.TextField(blank=True)

    
    def __str__(self):
        return self.first_name