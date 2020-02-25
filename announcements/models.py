from django.db import models
from datetime import datetime
from django.core.mail import send_mail
# Create your models here.

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
            send_mail(
                self.title,
                self.detail,
                'rcaskcommittee@gmail.com',
                ['adriel.tech.email@gmail.com'],
                fail_silently = False
            )
        if self.send_to_all_members:
            send_mail(
                self.title,
                self.detail,
                'rcaskcommittee@gmail.com',
                ['adriel.tech.email@gmail.com', 'siradriel@gmail.com'],
                fail_silently=False
            )