# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

LANGUAGES = [
    ('en', 'English')
]
DEFAULT_LANGUAGE = 0

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Eastern'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
STATIC_URL = "/site_media/static/"
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "site_media", "media"),
]
ADMIN_MEDIA_PREFIX = "/site_media/static/admin/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media')
MEDIA_URL = '/site_media/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^890^26o#5_f_#bR%cm)u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.csrf',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'emailkit',
    'uni_form',
    'captcha'
)

try:
    from local_settings import *
    if DEBUG:
        if DJANGO_DEBUG_TOOLBAR:
            MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
            INSTALLED_APPS += ('debug_toolbar',)
            
except ImportError:
    print 'No local_settings! You need to create one. Look at local_settings.py.tmpl'

