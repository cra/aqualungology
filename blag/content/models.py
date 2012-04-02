# coding: utf-8

from django.db import models

class Article(models.Model):
    slug = models.SlugField(max_length=200, unique_for_date='date_published')
    title = models.CharField(u'титле', max_length=250)
    content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True, db_index=True)
    # TODO save rendered content in model to speed up loading

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return ('blag-article-detail', (), { 'year': self.date_published.strftime('%Y'),
                                             'month': self.date_published.strftime('%b').lower(),
                                             'day': self.date_published.strftime('%d'),
                                             'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)


class MediaEntry(models.Model):
    name = models.CharField(u'Название', max_length=200)
    reason = models.TextField(u'Причина добавления', max_length=400, default='')
    processed = models.BooleanField(u'Усвоено')
    emotions = models.TextField(u'Впечатления', max_length=300, default='')

    class Meta:
        verbose_name = u'Ресурс'
        verbose_name_plural = u'Ресурсы'

    def process(self, emotions=None):
        self.processed = True
        if emotions:
            self.emotions = emotions


class Film(MediaEntry):
    FILM_GENRES = (
        ('U', 'Unspecified'),
        ('O', 'Other'),
        ('D', 'Documentary'),
        ('S', 'Series'),
        ('P', 'Porn'),
        ('C', 'Comedy'),
    )

    length = models.CharField(u'Длительность в минутах', max_length=20)
    genre = models.CharField(u'Жанр', max_length=1, choices=FILM_GENRES, blank=True)
    company = models.CharField(u'Компания для просмотра', max_length=100, blank=True)

