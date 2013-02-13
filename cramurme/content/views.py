# coding: utf-8

from datetime import datetime

from annoying.decorators import render_to
from django.shortcuts import redirect, get_object_or_404

from content.models import Film, Article
from content.forms import AddFilmForm


@render_to('index.html')
def index(request):
    article = Article.objects.filter(is_published=True).latest('date_published')
    all_articles = Article.objects.all()
    return {'article' : article,
            'all_articles': all_articles,}


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
    ctx = dict()

    all_articles = Article.objects.all()
    #years = sorted([a.date_published.year for a in all_articles])
    years = [a.date_published.year for a in all_articles]

    ctx['articles'] = dict()
    for year in set(years):
        ctx['articles'][year] = all_articles.filter(date_published__year=year).order_by('date_published')

    return ctx


@render_to('about.html')
def about(request):
    return {'body_class': 'index'}


@render_to('contact.html')
def contacts(request):
    return {'body_class': 'contacts'}


@render_to('contact.html')
def projects(request):
    return {'body_class': 'contacts'}
