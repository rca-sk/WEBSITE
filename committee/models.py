from django.db import models
from datetime import datetime
from phone_field import PhoneField

# Create your models here.

class Executive_committee_member(models.Model):
    title           = models.CharField(max_length=50)
    name            = models.CharField(max_length=50)
    introduction    = models.CharField(max_length=100, blank=True)
    phone           = PhoneField(blank=True, help_text = 'contact phone number')
    email           = models.EmailField(blank=True)
    is_published    = models.BooleanField(default=True)
    picture         = models.ImageField(upload_to='photos/mayors/', blank=True)

    def __str__(self):
        return self.name



class Mayor(models.Model):
    title           = models.CharField(max_length=50)
    name            = models.CharField(max_length=50)
    introduction    = models.CharField(max_length=100, blank=True)
    phone           = PhoneField(blank=True, help_text = 'contact phone number')
    email           = models.EmailField(blank=True)
    is_published    = models.BooleanField(default=True)
    picture         = models.ImageField(upload_to='photos/mayors/', blank=True)

    def __str__(self):
        return self.name


