from django.shortcuts import render
from django.views.generic import ListView
from django.conf.urls import url,include
from .views import shodsearch

urlpatterns = [
	url(r'^$',shodsearch, name='Shodan'),
	url(r'^accounts/', include('registration.backends.default.urls')),
]