# coding: utf-8
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import date_based

from content.models import Article, ID
from content.feeds import LatestEntriesFeed

import views


articles_info = {
    'queryset': Article.objects.all(),
    'date_field': 'date_published',
    'extra_context': {"body_class": "blog"}
}

urlpatterns = (
    url(r'^$', 'content.views.index', name='index'),
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
    url(r'^articles/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        date_based.object_detail,
        dict(articles_info,
            slug_field='slug',
            template_name='article_details.html',
            extra_context={"COMMENTS_ENABLED": True},
            allow_future=True,),
        name='blag-article-detail'),
)
