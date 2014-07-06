from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.home_view', name="vista_inicio"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^deportes/','deportes_view',name='vista_deprotes'),
)
