# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-26 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raise_invoice',
            name='client',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.Client'),
        ),
    ]