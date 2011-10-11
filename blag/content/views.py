# coding: utf-8

from annoying.decorators import render_to
from django.shortcuts import redirect

@render_to('index.html')
def index(request):
    return {}
