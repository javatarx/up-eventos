from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','web.views.home_view',name="vista_inicio"),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

)
