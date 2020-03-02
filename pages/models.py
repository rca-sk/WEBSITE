from django.db import models
from datetime import datetime
# Create your models here.


class About(models.Model):
    chairman_name       = models.CharField(max_length=200)
    paragraph1          = models.TextField(blank=True)
    paragraph2          = models.TextField(blank=True)
    paragraph3          = models.TextField(blank=True)
    paragraph4          = models.TextField(blank=True)
    paragraph5          = models.TextField(blank=True)
    paragraph6          = models.TextField(blank=True)
    paragraph7          = models.TextField(blank=True)
    time                = models.DateTimeField(default = datetime.now, blank=True)
    chairman_picture    = models.ImageField(upload_to='photos/about/%Y/%m/%d/', blank=True)
    chairman_signature  = models.ImageField(upload_to='photos/about/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.chairman_name