# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Nutrient(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey('NutrientGroup', null=True, blank=True)

    def __str__(self):
        return self.name

class NutrientGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    majorNGroup = models.ForeignKey('NutrientGroup', null=True, blank=True)
    servingSize = models.IntegerField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    kilojouls = models.IntegerField(null=True, blank=True)
    servingUnit = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class FoodNutrient(models.Model):
    food = models.ForeignKey('Food', null=True, blank=True)
    nutrient = models.ForeignKey('Nutrient', null=True, blank=True)
    quantity = models.FloatField()
    quantityUnit = models.CharField(max_length=5)

    def __str__(self):
        return "{}'s {}".format(self.food, self.nutrient)
