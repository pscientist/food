# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
# import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Nutrient(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey('NutrientGroup', null=True, blank=True)

class NutrientGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


