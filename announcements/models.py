from django.db import models
from datetime import datetime
from django.core.mail import send_mail

from committee.models import Executive_committee_member, Mayor
from database.models import CommunityMember

class Announcement(models.Model):
    title               = models.CharField(max_length=200)
    summary             = models.CharField(max_length=300)
    detail              = models.TextField(blank=True)
    time                = models.DateTimeField(default = datetime.now, blank=True)
    posted_by           = models.CharField(max_length=100)
    is_published        = models.BooleanField(default=True)
    picture1            = models.ImageField(upload_to='photos/announcements/%Y/%m/%d/', blank=True)
    picture2            = models.ImageField(upload_to='photos/announcements/%Y/%m/%d/', blank=True)



    def __str__(self):
        return self.title
