# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0005_remove_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='public',
        ),
    ]
