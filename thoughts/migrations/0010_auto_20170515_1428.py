# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0009_auto_20170515_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='random_url',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
