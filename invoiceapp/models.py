from django.db import models
from django.contrib.auth.models import Permission, User

class Company_credentials(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    email = models.EmailField()
    company_name = models.CharField(max_length=150)
    company_address = models.CharField(max_length=500)
    country = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=30)
    website_url = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Raise_invoice(models.Model):
    raise_for = models.CharField(max_length=200)
    email_to = models.EmailField(default='xyz@yahoo.com')
    description_of_items = models.TextField(max_length=1000)
    currency = models.CharField(max_length=10)
    total_money = models.IntegerField(default=100)
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=False,auto_now_add=True)
    message =  models.TextField(max_length=1000,default='Hey! Attatched along is your Invoice')

    def __str__(self):
        return self.raise_to_company_name