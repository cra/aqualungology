# coding: utf-8

from django import forms

from content.models import Film

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name',
                'reason', 'genre',
                'company', 'length')


class AddMediaEntryForm(forms.Form):
    full_name = forms.CharField(label=u"Stuff", required=True,)
    comment = forms.CharField(u'comment',)
    time = forms.CharField(label=u"Время")
