from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

from django.core.mail import send_mail


from committee.models import Executive_committee_member, Mayor
from database.models import CommunityMember

class Email(models.Model):
    email_subject       = models.CharField(max_length=200)
    email_body          = models.TextField()
    time                = models.DateTimeField(default=datetime.now)
    send_to_committee   = models.BooleanField(default=False)
    send_to_all_members = models.BooleanField(default=False)
    custom_recipients   = models.BooleanField(default=False)
    recipients_list     = ArrayField(models.CharField(max_length=100, blank=True))


    def __str__(self):
        return self.email_subject

    def save(self, *args, **kwargs):
        super(Email, self).save(*args, **kwargs)

        if self.send_to_committee:
            executives = [person.email for person in Executive_committee_member.objects.all()]
            mayors = [mayor.email for mayor in Mayor.objects.all()]
            recipients = executives + mayors
            send_mail(
                self.email_subject,
                self.email_body,
                'rcaskcommittee@gmail.com',
                recipients,
                fail_silently = True
            )
        if self.send_to_all_members:
            recipients = [member.email for member in CommunityMember.objects.all()]
            send_mail(
                self.email_subject,
                self.email_body,
                'rcaskcommittee@gmail.com',
                recipients,
                fail_silently=True
            )
        
        if self.custom_recipients:
            send_mail(
                self.email_subject,
                self.email_body,
                'rcaskcommittee@gmail.com',
                self.recipients_list,
                fail_silently = True
            )



