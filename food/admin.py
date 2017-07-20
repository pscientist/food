# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import NutrientGroup
from .models import Nutrient
from .models import Food
from .models import Animal
from .models import AnimalNutrient
from .models import FoodNutrient
from .models import MealFood
from .models import Meal

admin.site.register(NutrientGroup)
admin.site.register(Nutrient)
admin.site.register(Food)
admin.site.register(Animal)
admin.site.register(FoodNutrient)
admin.site.register(AnimalNutrient)
admin.site.register(MealFood)
admin.site.register(Meal)



