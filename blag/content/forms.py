# coding: utf-8

from django import forms

from content.models import Film

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name',
                'reason', 'genre',
                'company', 'length')

