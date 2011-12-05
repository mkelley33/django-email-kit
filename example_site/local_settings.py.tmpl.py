# -*- coding: utf-8 -*-
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# django-debug-toolbar settings
INTERNAL_IPS = ('127.0.0.1',)
DJANGO_DEBUG_TOOLBAR = False

ADMINS = (
    ('Michaux Kelley', 'mkelley@thinkbliss.com'),
)

MANAGERS = ADMINS
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': { 'autocommit': True },
    },

}

# You should modify these values to your liking.
CAPTCHA_LETTER_ROTATION = (-32, 29)
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_arcs',)
CAPTCHA_LENGTH = 4
CAPTCHA_DICTIONARY_MAX_LENGTH = 100
CAPTCHA_TIMEOUT = 5

# The values in the brackets below MUST be replaced.
# The new values shouldn't include the brackets.
EMAIL_HOST = '<your-smtp-email-host>'
EMAIL_HOST_USER = '<your-email-host-user>'
EMAIL_HOST_PASSWORD = '<your-host-password>'
# You may need to change the EMAIL_PORT, but the following is ok for
# gmail addresses.
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '<a-prefix-youd-like-to-see-in-subject-line>'
# Secured sending; Change to false if not needed.
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '<the-default-email-sender-address>'
