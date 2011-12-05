from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import static

urlpatterns = patterns('',
    url(r'^contact-us/$', include('emailkit.urls')),
    url(r'^captcha/', include('captcha.urls')),
    # https://docs.djangoproject.com/en/1.3/howto/static-files/#serving-other-directories
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
