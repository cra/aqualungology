# coding: utf-8
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import date_based

from content.models import Article, ID
from content.feeds import LatestEntriesFeed

import views


urlpatterns = (
    url(r'^films/put/$',
        'content.views.upload',
        {'media_type': "film"},
        name='create-media'),
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),
    url(r'^articles/$',
        'content.views.articles',
        name='articles'),
    url(r'^about/$',
        'content.views.about',
        name='about'),
    url(r'^id/$',
        'django.views.generic.list_detail.object_list', 
        { 
            'queryset': ID.objects.filter(is_valid=True),
            'template_name': 'id.html'
        },
        name='id'),
    url(r'^projects/$',
        'content.views.projects',
        name='projects'),

    url(r'^(?P<slug>[-\w]+)/$',
        'content.views.article_details',
        name='blag-article-detail'),
)
