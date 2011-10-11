# coding: utf-8
from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = (
    url(r'^$', 'content.views.index', name='index'),
)
