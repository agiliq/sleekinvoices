# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-24 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('country', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=30)),
                ('client_address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company_credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
                ('company_name', models.CharField(max_length=150)),
                ('company_address', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=30)),
                ('website_url', models.URLField(max_length=100)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Raise_invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raise_for', models.CharField(max_length=200)),
                ('email_to', models.EmailField(default='xyz@yahoo.com', max_length=254)),
                ('description_of_items', models.CharField(max_length=150)),
                ('currency', models.CharField(max_length=10)),
                ('cost', models.IntegerField(default=100)),
                ('quantity', models.IntegerField(default=1)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('message', models.TextField(default='Hey! Attatched along is your Invoice', max_length=500)),
                ('client', models.ForeignKey(default='ABC Infosolutions', on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.Client')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
