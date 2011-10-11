# coding: utf-8

from django.db import models


class MediaEntry(models.Model):
    name = models.CharField(u'Название', max_length=200)
    reason = models.TextField(u'Причина добавления', max_length=400, default='')
    processed = models.BoolField(u'Усвоено')
    emotions = models.TextField(u'Впечатления', max_length=300, default='', default=False)

    class Meta:
        verbose_name = u'Ресурс'
        verbose_name_plural = u'Ресурсы'

    def process(self, emotions=None):
        self.processed = True
        if emotions:
            self.emotions = emotions


class Film(MediaEntry):
    FILM_GENRES = (
        ('U', 'Unspecified')
        ('O', 'Other'),
        ('D', 'Documentary'),
        ('S', 'Series'),
        ('P', 'Porn'),
        ('C', 'Comedy'),
    )

    length = models.IntegerField(u'Длительность в минутах', required=False)
    genre = models.CharField(max_length=1, choices=FILM_GENRES, required=False)
    company = models.CharField(u'Компания для просмотра', required=False)
