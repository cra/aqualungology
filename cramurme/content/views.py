# coding: utf-8

from annoying.decorators import render_to
from django.shortcuts import redirect, get_object_or_404

from content.models import Film, Article
from content.forms import AddFilmForm


@render_to('index.html')
def index(request):
    article = Article.objects.filter(is_published=True).latest('date_published')
    return {'article' : article,
            'body_class': 'blog'}


@render_to('upload.html')
def upload(request, media_type):
    form = AddFilmForm()
    #if 'films' in media_type:

    return {'form': form}


@render_to('article_details.html')
def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return {'article': article}


@render_to('articles.html')
def articles(request):
    return {'articles': Article.objects.all(), 'body_class': 'blog'}


@render_to('about.html')
def about(request):
    return {'body_class': 'index'}


@render_to('contact.html')
def contacts(request):
    return {'body_class': 'contacts'}


@render_to('contact.html')
def projects(request):
    return {'body_class': 'contacts'}
