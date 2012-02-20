# coding: utf-8

from annoying.decorators import render_to
from django.shortcuts import redirect

from content.models import Film, Article
from content.forms import AddFilmForm


@render_to('index.html')
def index(request):
    return {}


@render_to('upload.html')
def upload(request, media_type):
    form = AddFilmForm()
    #if 'films' in media_type:

    return {'form': form}


@render_to('articles.html')
def articles(request):
    return {'articles': Article.objects.all()}


@render_to('articles.html')
def blag_article_details(request, year, month, day, slug):
    #if 'films' in media_type:
    print year, month, day, slug
    return {}
