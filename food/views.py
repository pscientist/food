# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Meal, Nutrient, Food, MealFood, Animal
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'meals_list'

    def get_queryset(self):
        return Meal.objects.all()

    def get_context_data(self):
        d = {'a' : 'a'}
        return d

class DetailView(generic.DetailView):
    model = Nutrient
    template_name = 'food/detail.html'


class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'description']

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['name', 'description']



def addFood(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    food_list = Food.objects.all()
    try:
        selected_food = Food.objects.get(pk=request.POST['food'])
        logger.info(request.POST['food'])

    except (KeyError, Food.DoesNotExist):
        pass
    else:
        mf = MealFood()
        mf.food = selected_food
        mf.meal = meal
        mf.save()

    return render(request, 'food/addFood.html', {'meal' : meal, 'food_list' : food_list})

