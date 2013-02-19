# coding: utf-8

from datetime import datetime

from annoying.decorators import render_to
from django.shortcuts import redirect, get_object_or_404
from django.forms.formsets import formset_factory

from content.models import Film, Article
from content.forms import AddFilmForm, AddMediaEntryForm

def get_articles_by_year_dict():
    all_articles = Article.objects.filter(is_published=True)
    years = [a.date_published.year for a in all_articles]

    articles = dict()
    for year in set(years):
        articles[year] = all_articles.filter(date_published__year=year).order_by('date_published')

    return articles


@render_to('index.html')
def index(request):
    article = Article.objects.filter(is_published=True).latest('date_published')
    return {'article' : article,
            'articles': get_articles_by_year_dict(),}


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
    return {'articles': get_articles_by_year_dict() }


@render_to('about.html')
def about(request):
    return {'body_class': 'index'}


@render_to('contact.html')
def contacts(request):
    return {'body_class': 'contacts'}


@render_to('contact.html')
def projects(request):
    return {'body_class': 'contacts'}


@render_to('testjs.html')
def testjs(request):
    AddMediaEntryFormSet = formset_factory(AddMediaEntryForm, extra=2, can_delete=True)
    import json
    import re
    film = Film.objects.get(pk=1)
    test_json = film.name

    if request.method == "POST":
        addmedia_formset = AddMediaEntryFormSet(request.POST, prefix='mediaentry')
        if addmedia_formset.is_valid():

            store_val =  filter(
                lambda x: 'DELETE' in x and x['DELETE'] == False, 
                addmedia_formset.cleaned_data
            )

            film.name = json.dumps(store_val, ensure_ascii=False)
            film.save()
            return redirect('testjs')

    else:
        addmedia_formset = AddMediaEntryFormSet(
                prefix="mediaentry", 
                initial=json.loads(test_json))

    return {"media_formset": addmedia_formset}
