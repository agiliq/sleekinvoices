from django.db import models
from django.contrib.auth.models import Permission, User

class company_credentials(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    company_address = models.CharField(max_length=500)
    country = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=30)
    website_url = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
