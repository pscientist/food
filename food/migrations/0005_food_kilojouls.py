# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20170719_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='kilojouls',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]