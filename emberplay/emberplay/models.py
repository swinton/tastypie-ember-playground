from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()

    def __unicode__(self):
        return self.text
