# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='short_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='direction',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
