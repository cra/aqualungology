# uwsgi.py for use with a django project
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'blag.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
