# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0008_auto_20160707_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raise_invoice',
            old_name='total_money',
            new_name='cost',
        ),
    ]