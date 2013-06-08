# -*- coding: utf-8 -*-
# Django settings for aqualungology project.

import os.path

BASE_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = conf.SERVER_EMAIL
ADMINS = conf.ADMINS

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

DATABASES = conf.DATABASES
TIME_ZONE = conf.TIME_ZONE

LOGIN_URL = '/login/'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = conf.LANGUAGE_CODE

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
# Example: "/home/example.com/static/"
STATIC_ROOT = BASE_PATH+'/static/'

# URL to use when referring to static files located in STATIC_ROOT.
# Examples: "/static/", "http://static.example.com/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('img', os.path.join(STATIC_ROOT, 'img')),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = conf.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
#    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
#    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'aqualungology.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

ALLOWED_HOSTS = '*'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Override the server-derived value of SCRIPT_NAME
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''
