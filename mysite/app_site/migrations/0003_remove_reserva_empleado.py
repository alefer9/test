# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0002_auto_20171105_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='empleado',
        ),
    ]