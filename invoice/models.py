from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from users.models import User
from django.utils.translation import ugettext_lazy as _
from base.models import UUIDModel, TimeStampedUUIDModel

# Create your models here.


class invoice(TimeStampedUUIDModel, models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vendor')
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client')
	
	class Meta:
		unique_together = (('sender', 'receiver'),)
