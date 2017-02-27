from django.shortcuts import render
from django.views.generic import ListView

from django.conf.urls import url
from .views import LinkListView


urlpatterns = [
	url(r'^$',search, name='home.html'),
]