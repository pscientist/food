# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Nutrient, NutrientGroup


class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'nutrients_list'
    def get_queryset(self):
        return Nutrient.objects.all()

class DetailView(generic.DetailView):
    model = Nutrient
    template_name = 'food/detail.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didnt select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
