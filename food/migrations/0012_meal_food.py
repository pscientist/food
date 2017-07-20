# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20170720_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='food',
            field=models.ManyToManyField(through='food.MealFood', to='food.Food'),
        ),
    ]
