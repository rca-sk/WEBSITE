from django.db import models
from datetime import datetime
# Create your models here.

class Carrier_announcement(models.Model):
    title               = models.CharField(max_length=200)
    summary             = models.CharField(max_length=300)
    paragraph1          = models.TextField(blank=True)
    paragraph2          = models.TextField(blank=True)
    paragraph3          = models.TextField(blank=True)
    paragraph4          = models.TextField(blank=True)
    paragraph5          = models.TextField(blank=True)
    time                = models.DateTimeField(default = datetime.now, blank=True)
    posted_by           = models.CharField(max_length=100)
    is_published        = models.BooleanField(default=True)
    picture1            = models.ImageField(upload_to='photos/carrier/%Y/%m/%d/', blank=True)
    picture2            = models.ImageField(upload_to='photos/carrier/%Y/%m/%d/', blank=True)
    file1               = models.FileField(upload_to='files/carrier/%Y/%m/%d/', blank=True)
    file2               = models.FileField(upload_to='files/carrier/%Y/%m/%d/', blank=True)
    file3               = models.FileField(upload_to='files/carrier/%Y/%m/%d/', blank=True)
    file4               = models.FileField(upload_to='files/carrier/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.title
