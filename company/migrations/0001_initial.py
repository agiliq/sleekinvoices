# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=255, unique=True, verbose_name='Company Name')),
                ('street_address', models.CharField(max_length=255, unique=True, verbose_name='Street Address')),
                ('city', models.CharField(max_length=255, unique=True, verbose_name='City')),
                ('state', models.CharField(max_length=255, unique=True, verbose_name='State')),
                ('zip_code', models.CharField(max_length=255, unique=True, verbose_name='Zip Code')),
                ('country', models.CharField(max_length=255, unique=True, verbose_name='Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]