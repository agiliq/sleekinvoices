from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from base.models import UUIDModel, TimeStampedUUIDModel

class company(TimeStampedUUIDModel, models.Model):
	company_name = models.CharField(_('Company Name'), max_length=255, unique = True)
	street_address = models.CharField(_('Street Address'), max_length=255, unique = True)
	city = models.CharField(_('City'), max_length=255, unique = True)
	state = models.CharField(_('State'), max_length=255, unique = True)
	zip_code = models.CharField(_('Zip Code'), max_length=255, unique = True)
	country = models.CharField(_('Country'), max_length=255, unique = True)
	def __str__(self):
		return '{}'.format(self.company_name)


