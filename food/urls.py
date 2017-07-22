from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'food'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<meal_id>[0-9]+)/addFood$', views.addFood, name='addFood'),
    url(r'^animal/add/$', views.AnimalCreate.as_view(), name='animal-add'),
    url(r'^animal/(?P<pk>[0-9]+)/$', views.AnimalUpdate.as_view(), name='animal-detail'),
]
