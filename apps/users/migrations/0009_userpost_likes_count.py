# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20171019_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]