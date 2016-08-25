from django.conf.urls import patterns, include, url
from django.contrib import admin

from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),
    )

if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))
