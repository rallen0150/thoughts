# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0010_auto_20170515_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='random_url',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
