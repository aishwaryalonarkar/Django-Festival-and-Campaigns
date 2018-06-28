# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.conf.urls import include,url
from . import models
from . import admin
from django.conf import settings
from . import views

app_name = 'festivalapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main$', views.main, name='main'),
    url(r'^flist/$', views.flist,name='flist'),
 	url(r'^flist/finfo/(?P<fest_id>\d+)/$', views.finfo,name='finfo'),
 	url(r'^(?P<pk>[a-z]+)/fsearched/$', views.fsearched,name='fsearched'),
 	url(r'^fest_campaign/(?P<pk>[0-9]+)$',views.fest_campaign,name='fest_campaign'),
    url(r'^elist/$', views.elist,name='elist'),
 	url(r'^elist/einfo/(?P<pk>\d+)/$', views.einfo,name='einfo'),
    #url(r'^IndexView/$', views.IndexView,name='index'),
]