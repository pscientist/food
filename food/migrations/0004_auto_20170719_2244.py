# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20170719_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
