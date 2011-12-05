# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from emailkit.views import contact_us

urlpatterns = patterns('',
    url(r'^$', contact_us, name='emailkit_contact_us'),
)
