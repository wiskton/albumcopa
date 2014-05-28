# -*- coding: utf-8 -*-
import sys

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'figurinhas.views.home', name='home'),
    url(r'^album/$', 'figurinhas.views.album', name='album'),
    url(r'^repetidas/$', 'figurinhas.views.repetidas', name='repetidas'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if len(sys.argv) >= 2 and sys.argv[1] in ('runserver', 'runserver_plus',):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)