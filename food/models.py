# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Nutrient(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey('NutrientGroup', null=True, blank=True)

class NutrientGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)



