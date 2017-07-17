# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import NutrientGroup
from .models import Nutrient

admin.site.register(NutrientGroup)
admin.site.register(Nutrient)

