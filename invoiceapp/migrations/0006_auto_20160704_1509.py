# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0005_auto_20160704_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raise_invoice',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]