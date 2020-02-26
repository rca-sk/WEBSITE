from django.db import models
from datetime import datetime
from django.core.mail import send_mail
# Create your models here.

from committee.models import Executive_committee_member, Mayor
from database.models import CommunityMember

class Announcement(models.Model):
    title               = models.CharField(max_length=200)
    summary             = models.CharField(max_length=300)
    detail              = models.TextField(blank=True)
    time                = models.DateTimeField(default = datetime.now, blank=True)
    posted_by           = models.CharField(max_length=100)
    is_published        = models.BooleanField(default=True)
    send_to_committee   = models.BooleanField(default=False)
    send_to_all_members = models.BooleanField(default=False)
    picture1            = models.ImageField(upload_to='photos/announcements/%Y/%m/%d/', blank=True)
    picture2            = models.ImageField(upload_to='photos/announcements/%Y/%m/%d/', blank=True)



    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        super(Announcement, self).save(*args, **kwargs)

        if self.send_to_committee:
            executives = [person.email for person in Executive_committee_member.objects.all()]
            mayors = [mayor.email for mayor in Mayor.objects.all()]
            recipients = executives + mayors
            send_mail(
                self.title,
                self.detail,
                'rcaskcommittee@gmail.com',
                recipients,
                fail_silently = False
            )
        if self.send_to_all_members:
            recipients = [member.email for member in CommunityMember.objects.all()]
            send_mail(
                self.title,
                self.detail,
                'rcaskcommittee@gmail.com',
                recipients,
                fail_silently=False
            )