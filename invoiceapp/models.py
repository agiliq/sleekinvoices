from django.db import models
from django.contrib.auth.models import Permission, User

class Company_credentials(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    email = models.EmailField(default='')
    company_name = models.CharField(max_length=150)
    company_address = models.CharField(max_length=500)
    country = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=30)
    website_url = models.URLField(max_length=100)

    def __str__(self):
        return self.company_name

class Client(models.Model):
    user = models.ForeignKey(User,default=1)
    organisation_name = models.CharField(max_length=50)
    email = models.EmailField(default='')
    country = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=30)
    client_address = models.CharField(max_length=500)
    def __str__(self):
        return self.organisation_name

class Invoice(models.Model):
    user = models.ForeignKey(User,default=1)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,default="")
    raise_for = models.CharField(max_length=200)
    raised_by = models.CharField(max_length=50,default='')
    email_to = models.EmailField(default='xyz@yahoo.com')
    description_of_items = models.CharField(max_length=150)
    currency = models.CharField(max_length=10)
    cost = models.IntegerField(default=100)
    quantity = models.IntegerField(default=1)
    date_created = models.DateField(auto_now=False,auto_now_add=True)
    message =  models.TextField(max_length=500,default='Hey! Attatched along is your Invoice')

    def __str__(self):
        return self.raise_for

